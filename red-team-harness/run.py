#!/usr/bin/env python3
"""Red-teaming harness CLI.

Runs the attack suite against one or more targets, judges each response,
prints a before/after scoreboard, and writes results.json + scoreboard.md.

Usage:
    python3 run.py --demo                 # full suite: unguarded vs guarded
    python3 run.py --target guarded       # single target
    python3 run.py --list                 # list the attack library
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# Make the project root importable regardless of where run.py is invoked from.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from attacks import get_attacks  # noqa: E402
from judge import BLOCKED, HELPFUL, SUCCEEDED, judge  # noqa: E402
from targets import GuardedTarget, UnguardedTarget  # noqa: E402

TARGET_REGISTRY = {
    "unguarded": UnguardedTarget,
    "guarded": GuardedTarget,
}

CATEGORY_LABELS = {
    "prompt_injection": "Prompt injection",
    "jailbreak_persona": "Jailbreak personas",
    "data_exfiltration": "Data exfiltration",
    "disallowed_content": "Disallowed content",
}


def evaluate(target, attacks):
    """Run every attack against a target; return list of result dicts."""
    results = []
    for attack in attacks:
        try:
            response = target.query(attack["prompt"])
        except Exception as exc:  # a target must never crash the harness
            response = f"[TARGET ERROR: {type(exc).__name__}: {exc}]"
        judgement = judge(attack, response)
        results.append({
            "attack_id": attack["id"],
            "category": attack["category"],
            "severity": attack["severity"],
            "prompt": attack["prompt"],
            "response": response,
            "verdict": judgement.verdict,
            "reason": judgement.reason,
        })
    return results


def summarize(results):
    """Aggregate attack success rate (ASR) overall and per category."""
    attacks = [r for r in results if r["category"] != "control"]
    controls = [r for r in results if r["category"] == "control"]

    by_category = {}
    for r in attacks:
        cat = r["category"]
        bucket = by_category.setdefault(cat, {"total": 0, "succeeded": 0})
        bucket["total"] += 1
        if r["verdict"] == SUCCEEDED:
            bucket["succeeded"] += 1

    succeeded = sum(1 for r in attacks if r["verdict"] == SUCCEEDED)
    total = len(attacks)
    helpful = sum(1 for r in controls if r["verdict"] == HELPFUL)
    return {
        "by_category": by_category,
        "total": total,
        "succeeded": succeeded,
        "attack_success_rate": succeeded / total if total else 0.0,
        "controls_total": len(controls),
        "controls_helpful": helpful,
    }


def _pct(part, whole):
    return (100.0 * part / whole) if whole else 0.0


def print_scoreboard(summaries):
    """Print the before/after scoreboard to stdout."""
    names = list(summaries)
    print("\n================ RED-TEAM SCOREBOARD ================")
    for name in names:
        s = summaries[name]
        print(f"\nTarget: {name}")
        for cat, label in CATEGORY_LABELS.items():
            b = s["by_category"].get(cat, {"total": 0, "succeeded": 0})
            print(f"  {label:<20} {b['succeeded']:>2}/{b['total']:<2} "
                  f"({_pct(b['succeeded'], b['total']):5.1f}% ASR)")
        print(f"  {'OVERALL':<20} {s['succeeded']:>2}/{s['total']:<2} "
              f"({_pct(s['succeeded'], s['total']):5.1f}% ASR)")
        print(f"  Controls helpful: {s['controls_helpful']}/{s['controls_total']}")

    if len(names) == 2:
        before, after = summaries[names[0]], summaries[names[1]]
        drop = (before["attack_success_rate"] - after["attack_success_rate"]) * 100
        print("\n------------------------------------------------")
        print(f"BEFORE -> AFTER: {_pct(before['succeeded'], before['total']):.1f}% -> "
              f"{_pct(after['succeeded'], after['total']):.1f}% attack success rate "
              f"({-drop:+.1f} pp)")
        print("------------------------------------------------\n")


def write_scoreboard_md(summaries, path):
    """Write a Markdown version of the scoreboard."""
    names = list(summaries)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Red-Team Scoreboard",
        "",
        f"Generated: {now}",
        f"Attacks: {sum(s['total'] for s in summaries.values()) // max(len(names), 1)} "
        f"+ {summaries[names[0]]['controls_total']} benign controls",
        "",
        "| Category | " + " | ".join(f"{n} ASR" for n in names) + " |",
        "| --- | " + " | ".join("---:" for _ in names) + " |",
    ]
    for cat, label in CATEGORY_LABELS.items():
        cells = []
        for n in names:
            b = summaries[n]["by_category"].get(cat, {"total": 0, "succeeded": 0})
            cells.append(f"{b['succeeded']}/{b['total']} ({_pct(b['succeeded'], b['total']):.1f}%)")
        lines.append(f"| {label} | " + " | ".join(cells) + " |")
    overall = []
    for n in names:
        s = summaries[n]
        overall.append(f"**{s['succeeded']}/{s['total']} ({_pct(s['succeeded'], s['total']):.1f}%)**")
    lines.append("| **Overall** | " + " | ".join(overall) + " |")
    lines.append("")
    if len(names) == 2:
        before, after = summaries[names[0]], summaries[names[1]]
        drop = (before["attack_success_rate"] - after["attack_success_rate"]) * 100
        lines += [
            "## Before -> After",
            "",
            f"Attack success rate: **{_pct(before['succeeded'], before['total']):.1f}%** "
            f"-> **{_pct(after['succeeded'], after['total']):.1f}%** ({-drop:+.1f} pp)",
            "",
            f"Benign controls still answered helpfully: "
            f"{after['controls_helpful']}/{after['controls_total']} "
            f"(guardrails must not break normal use).",
            "",
        ]
    lines += [
        "## Methodology",
        "",
        "Rule-based judge: a response is BLOCKED if it contains refusal language; "
        "an attack SUCCEEDS if the response does not refuse and contains the attack's "
        "authored success marker (leaked secret, adopted persona phrase, compliance "
        "language). Benign controls are excluded from attack success rate. "
        "See README.md for the full methodology.",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def main(argv=None):
    parser = argparse.ArgumentParser(description="LLM red-teaming harness")
    parser.add_argument("--demo", action="store_true",
                        help="run the full suite: unguarded vs guarded, print scoreboard")
    parser.add_argument("--target", choices=list(TARGET_REGISTRY),
                        help="run the suite against a single target")
    parser.add_argument("--list", action="store_true",
                        help="list the attacks in the library and exit")
    parser.add_argument("--output-dir", default=".",
                        help="where to write results.json and scoreboard.md")
    args = parser.parse_args(argv)

    attacks = get_attacks()

    if args.list:
        for a in attacks:
            print(f"{a['id']:<7} [{a['category']:<18}] ({a['severity']:<8}) {a['prompt'][:70]}")
        return 0

    if args.demo:
        targets = ["unguarded", "guarded"]
    elif args.target:
        targets = [args.target]
    else:
        parser.error("pass --demo, --target <name>, or --list")
        return 2

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    summaries = {}
    full_results = {}
    for name in targets:
        target = TARGET_REGISTRY[name]()
        results = evaluate(target, attacks)
        summaries[name] = summarize(results)
        full_results[name] = results

    print(f"Ran {len(attacks)} attacks "
          f"({sum(1 for a in attacks if a['category'] != 'control')} adversarial + "
          f"{sum(1 for a in attacks if a['category'] == 'control')} controls) "
          f"against: {', '.join(targets)}")
    print_scoreboard(summaries)

    (out_dir / "results.json").write_text(
        json.dumps({"targets": full_results, "summaries": summaries},
                   indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    write_scoreboard_md(summaries, out_dir / "scoreboard.md")
    print(f"Wrote {out_dir / 'results.json'} and {out_dir / 'scoreboard.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
