"""Smoke tests for the offline demo CLIs.

Each test copies a project folder into a temporary directory and runs its
demo there, so demo runs never write into the checked-in repo. Demos that
need network access, pip packages, or API credentials are marked skipped
instead of attempted.
"""

import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable
TIMEOUT = 120  # generous; most demos finish in seconds


def copy_project(name: str, tmp_path: Path) -> Path:
    """Copy a project dir to tmp so the demo can write files freely."""
    dest = tmp_path / name
    shutil.copytree(REPO_ROOT / name, dest)
    return dest


def run_demo(cwd: Path, script: str, args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(
        [PYTHON, script, *args],
        cwd=cwd,
        capture_output=True,
        text=True,
        timeout=TIMEOUT,
    )


def test_classify_demo(tmp_path):
    work = copy_project("eu-ai-act-risk-classifier", tmp_path)
    result = run_demo(work, "classify.py", ["--demo"])
    assert result.returncode == 0, result.stderr
    assert "EU AI ACT RISK CLASSIFIER" in result.stdout
    # the demo table covers all four tiers across the example cards
    for tier in ("Prohibited", "High-Risk", "Limited Risk", "Minimal Risk"):
        assert tier in result.stdout


def test_classify_single_card_json(tmp_path):
    work = copy_project("eu-ai-act-risk-classifier", tmp_path)
    result = run_demo(
        work,
        "classify.py",
        ["--card", "examples/spam_filter.json", "--json"],
    )
    assert result.returncode == 0, result.stderr
    payload = json.loads(result.stdout)
    assert payload["name"] == "MailGuard"
    assert payload["tier"] == "Minimal Risk"


def test_bias_audit_demo(tmp_path):
    work = copy_project("bias-audit-suite", tmp_path)
    result = run_demo(work, "audit.py", ["--demo"])
    assert result.returncode == 0, result.stderr
    report_path = work / "report.json"
    md_path = work / "report.md"
    assert report_path.is_file()
    assert md_path.is_file()
    report = json.loads(report_path.read_text(encoding="utf-8"))
    assert "models" in report and "results" in report
    assert set(report["models"]) == {"NeutralStub", "BiasedStub"}
    for model in report["models"]:
        assert "overall_severity" in report["results"][model]


def test_red_team_demo(tmp_path):
    work = copy_project("red-team-harness", tmp_path)
    result = run_demo(work, "run.py", ["--demo"])
    assert result.returncode == 0, result.stderr
    results_path = work / "results.json"
    scoreboard_path = work / "scoreboard.md"
    assert results_path.is_file()
    assert scoreboard_path.is_file()
    results = json.loads(results_path.read_text(encoding="utf-8"))
    assert isinstance(results, dict)
    assert {"targets", "summaries"} <= set(results)
    assert results["targets"], "results.json should cover at least one target"


def test_policy_monitor_demo(tmp_path):
    work = copy_project("policy-violation-monitor", tmp_path)
    # remove checked-in artifacts so the test proves the demo produced them
    for artifact in ("audit.log.jsonl", "review_queue.json"):
        (work / artifact).unlink(missing_ok=True)
    result = run_demo(work, "monitor.py", ["--demo"])
    assert result.returncode == 0, result.stderr
    audit_log = work / "audit.log.jsonl"
    queue_path = work / "review_queue.json"
    assert audit_log.is_file()
    assert queue_path.is_file()
    lines = [ln for ln in audit_log.read_text(encoding="utf-8").splitlines() if ln.strip()]
    assert lines, "audit.log.jsonl should have at least one decision logged"
    for line in lines:
        json.loads(line)
    queue = json.loads(queue_path.read_text(encoding="utf-8"))
    assert isinstance(queue, list)


def test_model_registry_seed(tmp_path):
    work = copy_project("model-registry", tmp_path)
    result = run_demo(work, "seed.py", ["--reset"])
    assert result.returncode == 0, result.stderr
    registry_path = work / "data" / "registry.json"
    assert registry_path.is_file()
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    assert registry, "seeded registry should not be empty"
    # the seed also generates a lineage report; a non-zero report run fails seed
    assert (work / "lineage-report.html").is_file()


def test_governance_dashboard_build(tmp_path):
    work = copy_project("governance-dashboard", tmp_path)
    (work / "dashboard.html").unlink(missing_ok=True)
    result = run_demo(work, "build.py", ["--demo"])
    assert result.returncode == 0, result.stderr
    dashboard = work / "dashboard.html"
    assert dashboard.is_file()
    content = dashboard.read_text(encoding="utf-8")
    assert len(content) > 1000
    assert "<html" in content.lower()


def test_triage_demo(tmp_path):
    work = copy_project("ai-use-case-intake", tmp_path)
    result = run_demo(work, "triage.py", ["--demo"])
    assert result.returncode == 0, result.stderr
    registry_path = work / "registry.json"
    assert registry_path.is_file()
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    assert isinstance(registry, list) and registry
    entry = registry[-1]
    assert "Illustrative demo" in entry["name"]
    assert "review_track" in entry
    assert "total_score" in entry


@pytest.mark.skip(reason="requires the laya pip package and numpy; not installed in CI")
def test_laya_analyze(tmp_path):
    work = copy_project("laya-governance-experiments", tmp_path)
    result = run_demo(work, "analyze.py", [])
    assert result.returncode == 0, result.stderr


@pytest.mark.skip(reason="requires provider API keys and CLI clients; not available in CI")
def test_council_run(tmp_path):
    work = copy_project("ai-governance-council", tmp_path)
    result = run_demo(work, "run_council.py", [])
    assert result.returncode == 0, result.stderr
