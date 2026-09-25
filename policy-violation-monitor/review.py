"""Human-in-the-loop review tool for escalated outputs.

Usage:
  python review.py list
  python review.py decide <output_id> approve|reject --note "..."

`list` shows escalations with status 'pending'.
`decide` records the reviewer's decision as a new entry in the audit log
and marks the item decided in review_queue.json. Nothing is deleted - 
the queue is an append-friendly record of what humans did.
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_AUDIT = os.path.join(BASE_DIR, "audit.log.jsonl")
DEFAULT_QUEUE = os.path.join(BASE_DIR, "review_queue.json")


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def load_queue(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_queue(path, queue):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(queue, f, indent=2)
    os.replace(tmp, path)


def cmd_list(args):
    queue = load_queue(args.queue)
    pending = [q for q in queue if q["status"] == "pending"]
    decided = [q for q in queue if q["status"] != "pending"]

    print(f"Pending escalations: {len(pending)}")
    for q in pending:
        fired = ", ".join(
            f"{t['policy_id']}({t['severity']})" for t in q["triggered"])
        print(f"\n  {q['output_id']}  queued {q['queued_at']}")
        print(f"    triggered: {fired}")
        text = q["text"]
        print(f"    text: {text[:160]}{'...' if len(text) > 160 else ''}")

    if decided:
        print(f"\nAlready decided: {len(decided)}")
        for q in decided:
            d = q.get("decision", {})
            print(f"  {q['output_id']}: {d.get('verdict')} "
                  f"by {d.get('reviewer')} - {d.get('note', '')}")


def cmd_decide(args):
    queue = load_queue(args.queue)
    match = next((q for q in queue if q["output_id"] == args.output_id), None)
    if match is None:
        print(f"error: no queued item with id '{args.output_id}'", file=sys.stderr)
        sys.exit(1)
    if match["status"] != "pending":
        print(f"error: '{args.output_id}' is already decided "
              f"({match['decision'].get('verdict')})", file=sys.stderr)
        sys.exit(1)

    decision = {
        "verdict": args.verdict,
        "reviewer": "human-reviewer",   # in production: authenticated user id
        "note": args.note or "",
        "decided_at": now_iso(),
    }
    match["status"] = "decided"
    match["decision"] = decision
    save_queue(args.queue, queue)

    # Append the decision to the same audit trail the monitor writes.
    audit_entry = {
        "ts": decision["decided_at"],
        "output_id": match["output_id"],
        "source": "review",
        "triggered": match["triggered"],
        "severity": match["severity"],
        "action": f"review-{args.verdict}",
        "note": decision["note"],
    }
    with open(args.audit, "a", encoding="utf-8") as f:
        f.write(json.dumps(audit_entry) + "\n")

    print(f"{args.output_id}: recorded verdict '{args.verdict}'")


def main():
    parser = argparse.ArgumentParser(description="Human review tool")
    parser.add_argument("--queue", default=DEFAULT_QUEUE)
    parser.add_argument("--audit", default=DEFAULT_AUDIT)
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("list", help="show queued escalations")

    p_decide = sub.add_parser("decide", help="record a review decision")
    p_decide.add_argument("output_id")
    p_decide.add_argument("verdict", choices=["approve", "reject"])
    p_decide.add_argument("--note", default="", help="reviewer rationale")

    args = parser.parse_args()
    if args.command == "list":
        cmd_list(args)
    else:
        cmd_decide(args)


if __name__ == "__main__":
    main()
