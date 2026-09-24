#!/usr/bin/env python3
"""AI use-case intake triage CLI.

Scores a new AI use case against the triage rubric (see triage-rubric.md),
assigns a review track, and appends the result to registry.json.

Standard library only. No network, no API keys.

Usage:
    python3 triage.py                       # interactive prompts
    python3 triage.py --demo                # triage an illustrative sample use case
    python3 triage.py --registry registry.json   # use a different registry file
"""

from __future__ import annotations

import argparse
import datetime
import json
import sys
from pathlib import Path

DIMENSIONS = [
    ("personal_data_involvement", "D1 personal data involvement", [
        "No personal data",
        "Internal business data only",
        "Customer / employee personal data",
        "Sensitive, special-category, or minors' data",
    ]),
    ("decision_impact_oversight", "D2 decision impact & oversight", [
        "Informational output only",
        "Advisory output, human decides",
        "Automated recommendation with human override",
        "Autonomous decision affecting people",
    ]),
    ("external_exposure", "D3 external exposure", [
        "Internal, non-public",
        "Limited internal pilot",
        "Customer-facing",
        "Public-facing or safety-adjacent",
    ]),
    ("data_handling_vendor", "D4 data handling & vendor posture", [
        "Internal systems only",
        "Approved vendor / tool",
        "New vendor or public model API",
        "Unmanaged / consumer tool",
    ]),
    ("regulatory_sensitivity", "D5 regulatory sensitivity", [
        "General productivity",
        "Regulated-adjacent domain",
        "Employment, education, finance, legal",
        "EU AI Act Annex III-type high-risk use",
    ]),
]

# (min_score, track_label, sla_business_days, description)
TRACKS = [
    (12, "D — Critical", 2, "Executive + legal review; deployment hold until cleared."),
    (8, "C — Elevated", 3, "Full risk assessment required; committee review."),
    (4, "B — Standard", 5, "Governance analyst review; light documentation."),
    (0, "A — Minimal", 10, "Notify-only; log in registry; no formal review."),
]

AUTO_TRACK_D_FLAGS = [
    "Prohibited-use indicators (e.g., social scoring, real-time remote biometric identification)",
    "Minors' data with automated decision-making",
    "Unapproved tool already in production (shadow AI)",
]


def assign_track(scores: dict[str, int], auto_critical: bool) -> tuple[str, int, str]:
    if auto_critical:
        return "D — Critical", 2, "Automatic Track D trigger applied (score-independent)."
    total = sum(scores.values())
    for min_score, label, sla, desc in TRACKS:
        if total >= min_score:
            return label, sla, desc
    raise AssertionError("unreachable")  # pragma: no cover


def prompt_scores() -> tuple[dict[str, int], dict[str, str]]:
    print("\nScore each dimension 0-3 (see triage-rubric.md). Press Enter to accept 0.\n")
    scores: dict[str, int] = {}
    rationales: dict[str, str] = {}
    for key, title, options in DIMENSIONS:
        print(f"{title}:")
        for i, opt in enumerate(options):
            print(f"  {i} = {opt}")
        while True:
            raw = input("Score [0-3]: ").strip() or "0"
            if raw in {"0", "1", "2", "3"}:
                scores[key] = int(raw)
                break
            print("  Enter 0, 1, 2, or 3.")
        rationale = input("One-line rationale (optional): ").strip()
        rationales[key] = rationale or options[scores[key]]
        print()
    return scores, rationales


def prompt_flags() -> bool:
    print("Automatic Track D triggers (answer y/n):")
    for flag in AUTO_TRACK_D_FLAGS:
        if input(f"  {flag}? [y/N] ").strip().lower() == "y":
            return True
    return False


def load_registry(path: Path) -> list:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise SystemExit(f"error: {path} does not contain a JSON array")
    return data


def next_id(entries: list) -> str:
    nums = [int(e["id"].split("-")[1]) for e in entries
            if isinstance(e.get("id"), str) and e["id"].startswith("UC-")
            and e["id"].split("-")[1].isdigit()]
    return f"UC-{max(nums, default=0) + 1:04d}"


def triage(entry_meta: dict, scores: dict[str, int], rationales: dict[str, str],
           auto_critical: bool, registry: list) -> dict:
    total = sum(scores.values())
    track, sla_days, track_desc = assign_track(scores, auto_critical)
    today = datetime.date.today()
    entry = {
        "id": next_id(registry),
        "name": entry_meta.get("name", ""),
        "description": entry_meta.get("description", ""),
        "requestor": entry_meta.get("requestor", ""),
        "business_owner": entry_meta.get("business_owner", ""),
        "stage": entry_meta.get("stage", ""),
        "scores": scores,
        "score_rationale": [f"{k}={v}: {rationales.get(k, '')}"
                            for k, v in scores.items()],
        "total_score": total,
        "review_track": track,
        "status": "triaged",
        "created_at": today.isoformat(),
        "sla_due": (today + datetime.timedelta(days=sla_days)).isoformat(),
        "notes": entry_meta.get("notes", ""),
    }
    return entry


def main() -> int:
    ap = argparse.ArgumentParser(description="Triage a new AI use case into the registry.")
    ap.add_argument("--registry", default="registry.json",
                    help="Path to the registry JSON file (default: registry.json)")
    ap.add_argument("--demo", action="store_true",
                    help="Triage an illustrative sample use case (no prompts)")
    args = ap.parse_args()

    registry_path = Path(args.registry)
    registry = load_registry(registry_path)

    if args.demo:
        meta = {
            "name": "Illustrative demo: HR policy Q&A chatbot",
            "description": "Internal chatbot answering employee questions about HR policies using an approved enterprise LLM.",
            "requestor": "Illustrative requestor — People team",
            "business_owner": "Illustrative owner — CHRO",
            "stage": "idea",
            "notes": "Illustrative sample entry added by --demo.",
        }
        scores = {
            "personal_data_involvement": 1,
            "decision_impact_oversight": 1,
            "external_exposure": 0,
            "data_handling_vendor": 1,
            "regulatory_sensitivity": 1,
        }
        rationales = {k: "demo default" for k in scores}
        auto_critical = False
    else:
        print("=== AI use-case intake triage ===\n")
        meta = {
            "name": input("Use-case name: ").strip(),
            "description": input("One-line description: ").strip(),
            "requestor": input("Requestor: ").strip(),
            "business_owner": input("Business owner: ").strip(),
            "stage": input("Stage (idea / pilot / production): ").strip() or "idea",
            "notes": input("Notes (optional): ").strip(),
        }
        scores, rationales = prompt_scores()
        auto_critical = prompt_flags()

    entry = triage(meta, scores, rationales, auto_critical, registry)
    registry.append(entry)
    with registry_path.open("w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)
        f.write("\n")

    total = entry["total_score"]
    print("\n--- Triage result ---")
    print(f"ID:            {entry['id']}")
    print(f"Name:          {entry['name']}")
    print(f"Total score:   {total} / 15")
    print(f"Review track:  {entry['review_track']}")
    print(f"SLA due:       {entry['sla_due']}")
    print(f"Appended to:   {registry_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
