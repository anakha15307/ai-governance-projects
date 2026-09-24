#!/bin/bash
# Runs the demo for each of the six AI governance projects.
set -u
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

echo "=== 01 eu-ai-act-risk-classifier ==="
(cd eu-ai-act-risk-classifier && python3 classify.py --demo)
echo
echo "=== 02 bias-audit-suite ==="
(cd bias-audit-suite && python3 audit.py --demo)
echo
echo "=== 03 red-team-harness ==="
(cd red-team-harness && python3 run.py --demo)
echo
echo "=== 04 policy-violation-monitor ==="
(cd policy-violation-monitor && python3 monitor.py --demo)
echo
echo "=== 05 model-registry ==="
(cd model-registry && python3 seed.py --reset)
echo
echo "=== 06 governance-dashboard ==="
(cd governance-dashboard && python3 build.py && echo "dashboard.html generated")
