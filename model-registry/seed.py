#!/usr/bin/env python3
"""Demo: seed the model registry with example models, datasets, and an
approval workflow, then print the registry table and build the HTML report.

What it does:
  1. Registers 4 datasets (with sources and licenses).
  2. Registers 3 models and links their dataset lineage:
     - cv-screener 1.2 (High-Risk) trained on two datasets -> submitted -> approved
     - support-chatbot 2.0 (Limited) fine-tuned on one dataset -> submitted -> approved
     - fraud-detector 0.9 (High-Risk) trained on one dataset -> submitted -> rejected
  3. Prints the registry table.
  4. Generates lineage-report.html via report.py.

Usage:
  python seed.py            # seed only if the registry is empty
  python seed.py --reset    # wipe existing data first, then seed

Exit status is 0 on success (including the already-seeded case).
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
STORE_PATH = BASE_DIR / "data" / "registry.json"


def run(*cli_args: str) -> None:
    """Run `python registry.py <cli_args>`, forwarding its output."""
    result = subprocess.run(
        [sys.executable, str(BASE_DIR / "registry.py"), *cli_args],
        capture_output=True, text=True,
    )
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)
    if result.returncode != 0:
        sys.exit(f"demo failed at: registry.py {' '.join(cli_args)}")


def seed() -> None:
    print("== datasets ==")
    run("register-dataset", "--name", "resume-corpus", "--version", "2024.1",
        "--source", "Internal applicant portal exports",
        "--license", "Proprietary — internal use only")
    run("register-dataset", "--name", "labeled-resumes", "--version", "2024.3",
        "--source", "Third-party annotation vendor",
        "--license", "Commercial — DPA in place")
    run("register-dataset", "--name", "support-tickets", "--version", "2025.1",
        "--source", "Zendesk export",
        "--license", "Proprietary — internal use only")
    run("register-dataset", "--name", "transaction-logs", "--version", "2025.2",
        "--source", "Core banking data warehouse",
        "--license", "Regulated — PCI-DSS scope")

    print("\n== model 1: high-risk CV screener (approve path) ==")
    run("register-model", "--name", "cv-screener", "--version", "1.2",
        "--owner", "Talent Platform",
        "--intended-use", "Screen CVs and rank applicants for initial recruiter review",
        "--risk-tier", "High-Risk")
    run("link", "--model", "cv-screener", "--version", "1.2",
        "--dataset", "resume-corpus", "--dataset-version", "2024.1",
        "--relation", "trained-on")
    run("link", "--model", "cv-screener", "--version", "1.2",
        "--dataset", "labeled-resumes", "--dataset-version", "2024.3",
        "--relation", "fine-tuned-on")
    run("submit", "--model", "cv-screener", "--version", "1.2",
        "--note", "Ready for governance review ahead of Q4 hiring pilot.")
    run("approve", "--model", "cv-screener", "--version", "1.2",
        "--reviewer", "M. Okafor",
        "--note", "Bias audit passed (audit-2026-004); human-in-the-loop retained.")

    print("\n== model 2: limited-risk chatbot (approve path) ==")
    run("register-model", "--name", "support-chatbot", "--version", "2.0",
        "--owner", "Customer Experience",
        "--intended-use", "Draft replies to tier-1 support tickets for agent approval",
        "--risk-tier", "Limited")
    run("link", "--model", "support-chatbot", "--version", "2.0",
        "--dataset", "support-tickets", "--dataset-version", "2025.1",
        "--relation", "fine-tuned-on")
    run("submit", "--model", "support-chatbot", "--version", "2.0")
    run("approve", "--model", "support-chatbot", "--version", "2.0",
        "--reviewer", "J. Lindqvist",
        "--note", "Disclosure banner enabled per transparency duty.")

    print("\n== model 3: high-risk fraud detector (reject path) ==")
    run("register-model", "--name", "fraud-detector", "--version", "0.9",
        "--owner", "Risk Engineering",
        "--intended-use", "Flag suspicious transactions for manual review",
        "--risk-tier", "High-Risk")
    run("link", "--model", "fraud-detector", "--version", "0.9",
        "--dataset", "transaction-logs", "--dataset-version", "2025.2",
        "--relation", "trained-on")
    run("submit", "--model", "fraud-detector", "--version", "0.9")
    run("reject", "--model", "fraud-detector", "--version", "0.9",
        "--reviewer", "M. Okafor",
        "--note", "False-positive rate 11% exceeds 5% tolerance; resubmit with threshold tuning.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Seed the registry with demo data.")
    parser.add_argument("--reset", action="store_true",
                        help="wipe existing registry data before seeding")
    args = parser.parse_args()

    if args.reset and STORE_PATH.exists():
        STORE_PATH.unlink()
        print("reset: removed existing registry data")

    if STORE_PATH.exists():
        print(f"registry already contains data ({STORE_PATH}).")
        print("Run with --reset to wipe and re-seed, or `python registry.py list` to inspect.")
        return

    seed()

    print("\n== registry table ==")
    run("list")

    print("\n== lineage report ==")
    result = subprocess.run(
        [sys.executable, str(BASE_DIR / "report.py")],
        capture_output=True, text=True,
    )
    print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)
    if result.returncode != 0:
        sys.exit("demo failed while generating the report")

    print("\nDone. Open lineage-report.html to see the governance report.")


if __name__ == "__main__":
    main()
