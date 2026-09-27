#!/usr/bin/env python3
"""Analyze council experiment results.

Reads results.json (including repaired votes) and prints the metrics used
in FINDINGS.md: council vs individual accuracy, agreement, vote changes,
confidence behavior, and failure accounting.
"""
import json
import math
from itertools import combinations

BASE = "/home/hatch/workspace/ai-governance-council"


def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    m = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (max(0, (c - m) / d), min(1, (c + m) / d))


def main():
    with open(f"{BASE}/results.json") as f:
        results = json.load(f)
    seats = results["seats"]
    cases = results["cases"]
    n = len(cases)

    print("=== Council verdicts ===")
    for c in cases:
        mark = "OK  " if c["council_verdict"] == c["ground_truth"] else "MISS"
        print(f"{mark} {c['id']}: council={c['council_verdict']} truth={c['ground_truth']}")
    ck = sum(1 for c in cases if c["council_verdict"] == c["ground_truth"])
    lo, hi = wilson(ck, n)
    print(f"council accuracy: {ck}/{n} = {ck/n:.3f} (95% CI {lo:.3f}-{hi:.3f})")

    print("\n=== Per-seat round-1 accuracy ===")
    for s in seats:
        sid = s["id"]
        as_run = sum(1 for c in cases
                     if c["rounds"]["round1"][sid].get("tier") == c["ground_truth"])
        done = [(c["rounds"]["round1"][sid], c) for c in cases
                if c["rounds"]["round1"][sid].get("tier")]
        rep = sum(1 for v, c in done if v["tier"] == c["ground_truth"])
        lo, hi = wilson(rep, len(done))
        rep_n = sum(1 for v, _ in done if v.get("repaired"))
        print(f"{sid} ({s['label']}): as-run {as_run}/{n}; "
              f"with repairs {rep}/{len(done)} = {rep/len(done):.3f} "
              f"(95% CI {lo:.3f}-{hi:.3f}; {rep_n} repaired)")

    print("\n=== Pairwise round-1 agreement (completed votes only) ===")
    for a, b in combinations([s["id"] for s in seats], 2):
        pairs = [(c["rounds"]["round1"][a]["tier"], c["rounds"]["round1"][b]["tier"])
                 for c in cases
                 if c["rounds"]["round1"][a].get("tier") and c["rounds"]["round1"][b].get("tier")]
        agree = sum(1 for x, y in pairs if x == y)
        print(f"{a} vs {b}: {agree}/{len(pairs)} agree")

    print("\n=== Round-2 vote changes ===")
    changed = 0
    for c in cases:
        if "round2" not in c["rounds"] or not c["rounds"]["round2"]:
            continue
        for s in seats:
            v = c["rounds"]["round2"][s["id"]]
            if v.get("changed_vote") is True:
                changed += 1
                print(f"  {c['id']} {s['id']}: "
                      f"{c['rounds']['round1'][s['id']].get('tier')} -> {v['tier']}")
    print(f"total changed votes: {changed}")

    print("\n=== Confidence (round-1 completed votes) ===")
    correct, wrong = [], []
    for c in cases:
        for s in seats:
            v = c["rounds"]["round1"][s["id"]]
            if v.get("tier") and isinstance(v.get("confidence"), (int, float)):
                (correct if v["tier"] == c["ground_truth"] else wrong).append(v["confidence"])
    def mean(xs):
        return sum(xs) / len(xs) if xs else float("nan")
    print(f"mean confidence when correct: {mean(correct):.3f} (n={len(correct)})")
    print(f"mean confidence when wrong:   {mean(wrong):.3f} (n={len(wrong)})")

    print("\n=== Failures (original run; repairs marked separately) ===")
    for s in seats:
        sid = s["id"]
        for rnd in ("round1", "round2"):
            fails = [c["id"] for c in cases
                     if rnd in c["rounds"] and c["rounds"][rnd].get(sid, {}).get("original_error")]
            if fails:
                print(f"{sid} {rnd}: {len(fails)} failed ({', '.join(fails)})")


if __name__ == "__main__":
    main()
