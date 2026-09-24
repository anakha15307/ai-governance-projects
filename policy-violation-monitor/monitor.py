"""Supervisor-style policy violation monitor.

Reads a stream of LLM application outputs, evaluates each against the
policy rules in policies.py, and takes an action based on severity:

  high   -> auto-block        (stop the output from reaching the user)
  medium -> escalate          (queue for human review)
  low    -> log-and-pass      (record, allow through)

Usage:
  python monitor.py --demo [--max-cost N] [--max-retries N]

The demo replays fixtures/outputs.jsonl. Every decision is appended to
audit.log.jsonl. Escalations are queued in review_queue.json for review.py.
"""

import argparse
import json
import os
import random
import sys
import time
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import policies  # noqa: E402

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_FIXTURES = os.path.join(BASE_DIR, "fixtures", "outputs.jsonl")
DEFAULT_AUDIT = os.path.join(BASE_DIR, "audit.log.jsonl")
DEFAULT_QUEUE = os.path.join(BASE_DIR, "review_queue.json")

# --- Simulated cost model (arbitrary units, offline-friendly) ---
COST_EVALUATE = 1    # running the policy suite against one output
COST_BLOCK = 5       # composing a block notice / takedown record
COST_ESCALATE = 10   # preparing a human-review packet


class TransientError(Exception):
    """A simulated flaky dependency (e.g. the tool/text source hiccups)."""


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def load_outputs(path):
    with open(path, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def load_queue(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_queue(path, queue):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(queue, f, indent=2)
    os.replace(tmp, path)


def append_audit(path, entry):
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")


def evaluate_with_retry(entry, max_retries, backoff_base=0.1):
    """Evaluate one output, retrying transient failures with backoff.

    Fixtures can mark "transient_error": true to simulate a flaky source
    that fails on the first attempt only.
    """
    attempts = 0
    while True:
        attempts += 1
        try:
            if entry.get("transient_error") and attempts == 1:
                # Deterministic in demo mode (random seeded in main); here
                # the fixture flag alone drives the failure.
                raise TransientError("simulated flaky tool output")
            triggered = policies.evaluate(entry["text"])
            return triggered, attempts - 1
        except TransientError as exc:
            if attempts > max_retries:
                raise
            sleep_s = backoff_base * (2 ** (attempts - 1))
            print(f"    [retry] {entry['id']}: {exc} "
                  f"(attempt {attempts}/{max_retries}, backoff {sleep_s:.2f}s)")
            time.sleep(sleep_s)


def decide_action(severity):
    if severity == "high":
        return "blocked"
    if severity == "medium":
        return "escalated"
    return "passed"


def run(fixtures_path, audit_path, queue_path, max_cost, max_retries):
    random.seed(42)  # reproducible demo runs
    outputs = load_outputs(fixtures_path)
    queue = load_queue(queue_path)

    total_cost = 0
    processed = 0
    aborted = False
    retries_used = 0
    violations_by_policy = {}
    actions_taken = {"blocked": 0, "escalated": 0, "passed": 0}

    print(f"Monitoring {len(outputs)} outputs "
          f"(cost cap: {max_cost}, max retries: {max_retries})\n")

    for entry in outputs:
        # Pre-charge the evaluation cost; abort gracefully if we'd exceed cap.
        if total_cost + COST_EVALUATE > max_cost:
            aborted = True
            append_audit(audit_path, {
                "ts": now_iso(), "output_id": entry["id"], "source": entry.get("source"),
                "triggered": [], "severity": "n/a", "action": "skipped",
                "note": "cost cap reached; output not evaluated",
            })
            print(f"  [cost-cap] {entry['id']}: skipped, budget exhausted")
            continue

        try:
            triggered, n_retries = evaluate_with_retry(entry, max_retries)
        except TransientError:
            append_audit(audit_path, {
                "ts": now_iso(), "output_id": entry["id"], "source": entry.get("source"),
                "triggered": [], "severity": "n/a", "action": "error",
                "note": f"transient failure persisted after {max_retries} retries",
            })
            print(f"  [error]    {entry['id']}: gave up after {max_retries} retries")
            continue

        retries_used += n_retries
        total_cost += COST_EVALUATE
        severity = policies.worst_severity(triggered)
        action = decide_action(severity)

        action_cost = {"blocked": COST_BLOCK, "escalated": COST_ESCALATE,
                       "passed": 0}[action]
        if total_cost + action_cost > max_cost:
            # Can't afford the action either: downgrade to a queued state and
            # record why, so nothing silently disappears.
            aborted = True
            append_audit(audit_path, {
                "ts": now_iso(), "output_id": entry["id"], "source": entry.get("source"),
                "triggered": [{"policy_id": p["id"], "severity": p["severity"],
                               "evidence_count": len(ev)} for p, ev in triggered],
                "severity": severity, "action": "deferred",
                "note": "cost cap reached; action deferred to next run",
            })
            print(f"  [cost-cap] {entry['id']}: action deferred, budget exhausted")
            continue

        total_cost += action_cost
        processed += 1
        actions_taken[action] += 1

        fired = []
        for policy, evidence in triggered:
            violations_by_policy[policy["id"]] = \
                violations_by_policy.get(policy["id"], 0) + 1
            fired.append({"policy_id": policy["id"],
                          "severity": policy["severity"],
                          "evidence_count": len(evidence)})

        append_audit(audit_path, {
            "ts": now_iso(),
            "output_id": entry["id"],
            "source": entry.get("source"),
            "triggered": fired,
            "severity": severity,
            "action": action,
            "note": "",
        })

        if action == "escalated":
            queue.append({
                "output_id": entry["id"],
                "text": entry["text"],
                "triggered": fired,
                "severity": severity,
                "queued_at": now_iso(),
                "status": "pending",
            })

        label = {"blocked": "[BLOCKED]  ", "escalated": "[ESCALATED]",
                 "passed": "[passed]   "}[action]
        detail = (", ".join(p["id"] for p, _ in triggered)
                  if triggered else "clean")
        print(f"  {label} {entry['id']}: {detail}")

    save_queue(queue_path, queue)

    pending = sum(1 for q in queue if q["status"] == "pending")

    print("\n" + "=" * 52)
    print("RUN SUMMARY")
    print("=" * 52)
    print(f"  Outputs processed : {processed}/{len(outputs)}")
    print(f"  Violations by policy:")
    if violations_by_policy:
        for pid in sorted(violations_by_policy):
            print(f"    {pid:8s} {violations_by_policy[pid]}")
    else:
        print("    (none)")
    print(f"  Actions taken     : blocked={actions_taken['blocked']}, "
          f"escalated={actions_taken['escalated']}, "
          f"passed={actions_taken['passed']}")
    print(f"  Retries used      : {retries_used}")
    print(f"  Cost consumed     : {total_cost}/{max_cost}")
    if aborted:
        print("  NOTE: cost cap hit — some outputs were skipped/deferred.")
    print(f"  Escalations pending review: {pending}")
    print(f"  Audit log         : {audit_path}")


def main():
    parser = argparse.ArgumentParser(description="Policy violation monitor")
    parser.add_argument("--demo", action="store_true",
                        help="replay fixtures/outputs.jsonl")
    parser.add_argument("--fixtures", default=DEFAULT_FIXTURES)
    parser.add_argument("--audit", default=DEFAULT_AUDIT)
    parser.add_argument("--queue", default=DEFAULT_QUEUE)
    parser.add_argument("--max-cost", type=int, default=1000,
                        help="cost cap per run (graceful abort when hit)")
    parser.add_argument("--max-retries", type=int, default=3,
                        help="retries for transient errors")
    args = parser.parse_args()

    if not args.demo:
        parser.error("--demo is required (only demo input source is implemented)")

    run(args.fixtures, args.audit, args.queue, args.max_cost, args.max_retries)


if __name__ == "__main__":
    main()
