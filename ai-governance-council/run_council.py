#!/usr/bin/env python3
"""LLM Governance Council experiment.

Three model seats (Gemini via Google AI Studio, gpt-oss via Groq, Ling via
OpenRouter) independently classify synthetic AI use cases under the EU AI Act,
then deliberate on disagreements. Results are compared against ground truth
and against each single seat's accuracy.
"""
import json
import re
import subprocess
import sys
import time
from collections import Counter

BASE = "/home/hatch/workspace"
SEATS = [
    {"id": "seat-a", "label": "Gemini 3.8 Flash", "provider": "google-ai-studio",
     "model": "gemini-3.8-flash", "pace": 5},
    {"id": "seat-b", "label": "gpt-oss 120B", "provider": "groq",
     "model": "openai/gpt-oss-120b", "pace": 3},
    {"id": "seat-c", "label": "Ling 3.0 Flash", "provider": "openrouter",
     "model": "inclusionai/ling-3.0-flash-sante:free", "pace": 4},
]

SYSTEM_R1 = (
    "You are an AI governance analyst classifying AI systems under the EU AI Act. "
    "Respond with ONLY a JSON object, no markdown fences, no extra text. Keys: "
    "tier (exactly one of: Unacceptable, High-Risk, Limited Risk, Minimal Risk), "
    "confidence (0.0 to 1.0), justification (one or two sentences), "
    "key_factors (list of short strings)."
)

R1_TEMPLATE = (
    "Classify this AI use case under the EU AI Act risk tiers "
    "(Unacceptable, High-Risk, Limited Risk, Minimal Risk).\n\n"
    "Title: {title}\nDescription: {description}"
)

R2_TEMPLATE = (
    "You are {seat}, one of three AI governance analysts on a council classifying "
    "AI systems under the EU AI Act.\n\nUse case: {title}\nDescription: {description}\n\n"
    "In round 1 you voted: {own_tier} (confidence {own_conf}): {own_just}\n"
    "Your peers voted:\n{peers}\n\n"
    "Reconsider in light of their reasoning. You may keep or change your vote. "
    "Respond with ONLY a JSON object, no markdown fences, no extra text. Keys: "
    "tier (exactly one of: Unacceptable, High-Risk, Limited Risk, Minimal Risk), "
    "confidence (0.0 to 1.0), justification (one or two sentences), "
    "changed_vote (true or false)."
)


TIER_MAP = {
    "unacceptable": "Unacceptable",
    "high-risk": "High-Risk", "high risk": "High-Risk",
    "limited risk": "Limited Risk",
    "minimal risk": "Minimal Risk",
}


def normalize_vote(vote):
    """Normalize tier casing and coerce confidence to a float when possible."""
    tier = str(vote.get("tier", "")).strip().lower()
    if tier not in TIER_MAP:
        raise ValueError(f"bad tier value: {vote.get('tier')!r}")
    vote["tier"] = TIER_MAP[tier]
    try:
        vote["confidence"] = float(vote.get("confidence"))
    except (TypeError, ValueError):
        vote["confidence"] = None
    return vote


def extract_json(text):
    """Pull the first {...} block out of model output and parse it."""
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end <= start:
        raise ValueError("no JSON object found")
    return json.loads(text[start:end + 1])


def call_seat(seat, prompt, system, max_tokens=800, retries=4):
    cli = f"{BASE}/skills/{seat['provider']}/bin/chat.py"
    last_error = "unknown error"
    for attempt in range(retries):
        try:
            proc = subprocess.run(
                [sys.executable, cli, "--model", seat["model"],
                 "--prompt", prompt, "--system", system,
                 "--temperature", "0.2", "--max-tokens", str(max_tokens)],
                capture_output=True, text=True, timeout=180)
            if proc.returncode != 0:
                raise RuntimeError(proc.stderr.strip()[:300])
            vote = normalize_vote(extract_json(proc.stdout))
            vote["raw"] = proc.stdout.strip()[:2000]
            return vote
        except Exception as e:
            last_error = str(e)
            wait = 6 * (attempt + 1)
            print(f"  [{seat['id']}] attempt {attempt + 1} failed: {last_error[:120]} "
                  f"(retry in {wait}s)", flush=True)
            time.sleep(wait)
    return {"tier": None, "confidence": None, "justification": f"FAILED: {last_error[:200]}",
            "key_factors": [], "raw": "", "error": True}


def main():
    with open(f"{BASE}/ai-governance-council/cases.json") as f:
        cases = json.load(f)

    results_path = f"{BASE}/ai-governance-council/results.json"
    try:
        with open(results_path) as f:
            results = json.load(f)
        done_ids = {c["id"] for c in results.get("cases", [])}
        print(f"Resuming: {len(done_ids)} cases already done, skipping them.", flush=True)
    except (FileNotFoundError, json.JSONDecodeError):
        results = {"seats": [{"id": s["id"], "label": s["label"], "model": s["model"]} for s in SEATS],
                   "cases": []}
        done_ids = set()
    # Refresh seat metadata in case the lineup changed between runs
    results["seats"] = [{"id": s["id"], "label": s["label"], "model": s["model"]} for s in SEATS]

    def save():
        with open(results_path, "w") as f:
            json.dump(results, f, indent=2)

    for case in cases:
        if case["id"] in done_ids:
            print(f"\n=== {case['id']}: {case['title']} (already done, skipping) ===", flush=True)
            continue
        print(f"\n=== {case['id']}: {case['title']} (truth: {case['ground_truth']}) ===", flush=True)
        rounds = {"round1": {}, "round2": {}}
        for seat in SEATS:
            prompt = R1_TEMPLATE.format(title=case["title"], description=case["description"])
            vote = call_seat(seat, prompt, SYSTEM_R1)
            rounds["round1"][seat["id"]] = vote
            print(f"  {seat['id']}: {vote['tier']} (conf {vote.get('confidence')})", flush=True)
            time.sleep(seat["pace"])

        r1_tiers = [v["tier"] for v in rounds["round1"].values()]
        if len(set(r1_tiers)) > 1:
            print("  -> disagreement, starting deliberation round", flush=True)
            for seat in SEATS:
                own = rounds["round1"][seat["id"]]
                peers = "\n".join(
                    f"- {s['id']} ({s['label']}): {rounds['round1'][s['id']]['tier']} "
                    f"(confidence {rounds['round1'][s['id']].get('confidence')}): "
                    f"{rounds['round1'][s['id']]['justification']}"
                    for s in SEATS if s["id"] != seat["id"])
                prompt = R2_TEMPLATE.format(
                    seat=f"{seat['id']} ({seat['label']})",
                    title=case["title"], description=case["description"],
                    own_tier=own["tier"], own_conf=own.get("confidence"),
                    own_just=own["justification"], peers=peers)
                vote = call_seat(seat, prompt, "", max_tokens=800)
                rounds["round2"][seat["id"]] = vote
                print(f"  {seat['id']} final: {vote['tier']} "
                      f"(changed: {vote.get('changed_vote')})", flush=True)
                time.sleep(seat["pace"])
            final_votes = rounds["round2"]
        else:
            final_votes = rounds["round1"]

        # Council verdict: majority vote, ties broken by mean confidence
        tiers = [v["tier"] for v in final_votes.values() if v["tier"]]
        counts = Counter(tiers)
        top = counts.most_common()
        if len(top) > 1 and top[0][1] == top[1][1]:
            tied = [t for t, c in top if c == top[0][1]]
            conf = {t: sum(v.get("confidence") or 0 for v in final_votes.values()
                           if v["tier"] == t) / max(1, sum(1 for v in final_votes.values() if v["tier"] == t))
                    for t in tied}
            verdict = max(tied, key=lambda t: conf[t])
        else:
            verdict = top[0][0] if top else None

        results["cases"].append({
            "id": case["id"], "title": case["title"],
            "ground_truth": case["ground_truth"],
            "ground_truth_basis": case["ground_truth_basis"],
            "rounds": rounds, "council_verdict": verdict,
            "unanimous_round1": len(set(r1_tiers)) == 1,
        })
        save()
        print(f"  saved {case['id']}", flush=True)

    print("\nSaved results.json")

    # Summary
    print("\n--- SUMMARY ---")
    for c in results["cases"]:
        ok = "OK " if c["council_verdict"] == c["ground_truth"] else "MISS"
        print(f"{ok} {c['id']}: council={c['council_verdict']} truth={c['ground_truth']}")
    for seat in SEATS:
        correct = sum(1 for c in results["cases"]
                      if c["rounds"]["round1"][seat["id"]]["tier"] == c["ground_truth"])
        print(f"{seat['id']} ({seat['label']}) round-1 accuracy: {correct}/{len(results['cases'])}")
    correct = sum(1 for c in results["cases"] if c["council_verdict"] == c["ground_truth"])
    print(f"council accuracy: {correct}/{len(results['cases'])}")


if __name__ == "__main__":
    main()
