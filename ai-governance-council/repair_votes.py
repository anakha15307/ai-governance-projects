#!/usr/bin/env python3
"""Repair failed council votes.

Re-runs only the votes that failed in the original run (tier is None),
using the exact same prompts the runner used. Repaired votes are marked
with "repaired": true and the original error is preserved. Council verdicts
already recorded are NEVER changed by this script; repairs only complete
the per-seat record for analysis.
"""
import copy
import json
import sys
import time

sys.path.insert(0, "/home/hatch/workspace/ai-governance-council")
from run_council import (SEATS, SYSTEM_R1, R1_TEMPLATE, R2_TEMPLATE, call_seat)

BASE = "/home/hatch/workspace/ai-governance-council"
SEAT_BY_ID = {s["id"]: s for s in SEATS}


def main():
    with open(f"{BASE}/results.json") as f:
        results = json.load(f)
    with open(f"{BASE}/cases.json") as f:
        cases = {c["id"]: c for c in json.load(f)}

    # Snapshot originals so round-2 repair prompts match the original run exactly
    original_rounds = {c["id"]: copy.deepcopy(c["rounds"]) for c in results["cases"]}

    def save():
        with open(f"{BASE}/results.json", "w") as f:
            json.dump(results, f, indent=2)

    repaired = 0
    still_failed = []
    for c in results["cases"]:
        case = cases[c["id"]]
        orig = original_rounds[c["id"]]
        for rnd in ("round1", "round2"):
            if rnd not in c["rounds"]:
                continue
            for seat in SEATS:
                sid = seat["id"]
                vote = c["rounds"][rnd].get(sid, {})
                if vote.get("tier"):
                    continue  # only repair failures
                print(f"Repairing {c['id']} {rnd} {sid} ...", flush=True)
                if rnd == "round1":
                    prompt = R1_TEMPLATE.format(title=case["title"],
                                                description=case["description"])
                    new_vote = call_seat(seat, prompt, SYSTEM_R1)
                else:
                    own = orig["round1"][sid]
                    peers = "\n".join(
                        f"- {s['id']} ({s['label']}): {orig['round1'][s['id']]['tier']} "
                        f"(confidence {orig['round1'][s['id']].get('confidence')}): "
                        f"{orig['round1'][s['id']]['justification']}"
                        for s in SEATS if s["id"] != sid)
                    prompt = R2_TEMPLATE.format(
                        seat=f"{sid} ({seat['label']})",
                        title=case["title"], description=case["description"],
                        own_tier=own["tier"], own_conf=own.get("confidence"),
                        own_just=own["justification"], peers=peers)
                    new_vote = call_seat(seat, prompt, "", max_tokens=800)
                new_vote["repaired"] = True
                new_vote["original_error"] = vote.get("justification", "")
                c["rounds"][rnd][sid] = new_vote
                if new_vote.get("tier"):
                    repaired += 1
                    print(f"  -> repaired: {new_vote['tier']} "
                          f"(conf {new_vote.get('confidence')})", flush=True)
                else:
                    still_failed.append((c["id"], rnd, sid))
                    print("  -> still failing", flush=True)
                save()
                time.sleep(seat["pace"])

    print(f"\nRepaired {repaired} votes; still failing: {still_failed}")


if __name__ == "__main__":
    main()
