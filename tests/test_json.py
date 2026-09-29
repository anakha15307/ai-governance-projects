"""Validate that JSON artifacts already committed to the repo parse as JSON.

These are static data files (datasets, example inputs, pre-generated
reports). This test only checks they are well-formed; it does not run
any demo.
"""

import json
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]

# (relative path, expected top-level JSON type)
JSON_FILES = [
    ("ai-governance-council/cases.json", list),
    ("ai-governance-council/results.json", dict),
    ("ai-use-case-intake/registry.json", list),
    ("bias-audit-suite/report.json", dict),
    ("governance-dashboard/data/risk_register.json", dict),
    ("laya-governance-experiments/results_bias.json", list),
    ("laya-governance-experiments/results_guardrail.json", list),
    ("model-registry/data/registry.json", dict),
    ("policy-violation-monitor/review_queue.json", list),
    ("red-team-harness/results.json", dict),
]

EXAMPLE_CARDS = sorted(
    (REPO_ROOT / "eu-ai-act-risk-classifier" / "examples").glob("*.json")
)


@pytest.mark.parametrize("relpath,expected_type", JSON_FILES)
def test_committed_json_parses(relpath, expected_type):
    path = REPO_ROOT / relpath
    assert path.is_file(), f"{relpath} is missing"
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(payload, expected_type), (
        f"{relpath} should be a {expected_type.__name__}, "
        f"got {type(payload).__name__}"
    )


def test_example_cards_parse():
    assert EXAMPLE_CARDS, "no example cards found"
    for card in EXAMPLE_CARDS:
        payload = json.loads(card.read_text(encoding="utf-8"))
        assert "name" in payload, f"{card.name} has no 'name' field"


def test_audit_log_lines_parse():
    log_path = REPO_ROOT / "policy-violation-monitor" / "audit.log.jsonl"
    assert log_path.is_file(), "audit.log.jsonl is missing"
    lines = [
        line
        for line in log_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    assert lines, "audit.log.jsonl has no entries"
    for line in lines:
        entry = json.loads(line)
        assert isinstance(entry, dict)
