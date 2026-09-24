#!/usr/bin/env python3
"""Scaffold a new monthly regulatory brief from the template.

Standard library only.

Usage:
    python3 new_brief.py                 # scaffold for the current month
    python3 new_brief.py 2026 10         # scaffold for October 2026
"""

from __future__ import annotations

import argparse
import datetime
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEMPLATE = HERE / "monthly-brief-template.md"
BRIEFS = HERE / "briefs"


def main() -> int:
    ap = argparse.ArgumentParser(description="Scaffold a new monthly regulatory brief.")
    ap.add_argument("year", nargs="?", type=int, default=None)
    ap.add_argument("month", nargs="?", type=int, default=None)
    args = ap.parse_args()

    today = datetime.date.today()
    year = args.year or today.year
    month = args.month or today.month
    try:
        first = datetime.date(year, month, 1)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if not TEMPLATE.exists():
        print(f"error: template not found: {TEMPLATE}", file=sys.stderr)
        return 1

    month_name = first.strftime("%B")
    filename = f"{year:04d}-{month:02d}-{month_name.lower()}.md"
    dest = BRIEFS / filename
    if dest.exists():
        print(f"error: {dest} already exists", file=sys.stderr)
        return 1

    text = TEMPLATE.read_text(encoding="utf-8")
    text = text.replace("{{MONTH YEAR}}", f"{month_name} {year}")
    text = text.replace("{{DATE}}", today.isoformat())
    text = text.replace("{{AUTHOR}}", "AI Governance Analyst")

    # Link to the most recent previous brief, if any.
    prev = sorted(BRIEFS.glob("*.md"))
    prev_link = f"./{prev[-1].name}" if prev else "(none yet)"
    text = text.replace("{{PREV_LINK}}", prev_link)

    BRIEFS.mkdir(exist_ok=True)
    dest.write_text(text, encoding="utf-8")
    print(f"scaffolded {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
