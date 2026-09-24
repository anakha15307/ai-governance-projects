#!/usr/bin/env bash
# Classify every example system card and print a summary table + reports.
set -euo pipefail
cd "$(dirname "$0")"
python3 classify.py --demo
