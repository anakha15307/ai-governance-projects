# Policy Violation Monitor

A supervisor-style oversight layer for LLM application outputs, the kind of
control that sits between a model and the user in any deployed AI system.
Every output is screened against a set of policy rules; high-severity
violations are auto-blocked, medium-severity ones are escalated to a human
reviewer, and everything is written to an append-only audit trail.

This is project 4 of a 6-project AI governance portfolio.

## Architecture

```
                 +------------------+
  LLM app output |  policies.py     |   deterministic rule checks
  (model/tool) -> |  evaluate()     |-> triggered rules + evidence
                 +------------------+
                          |
                 +------------------+
                 |  monitor.py      |   severity -> action routing
                 |  (supervisor)    |     high   -> auto-block
                 +------------------+     medium -> escalate to queue
                   |            |         low    -> log-and-pass
                   v            v
          audit.log.jsonl   review_queue.json
          (append-only)     (pending human decisions)
                                   |
                          +------------------+
                          |  review.py       |   human-in-the-loop
                          |  list / decide   |   decisions -> audit log
                          +------------------+
```

**Why a supervisor, not just filters?** Production oversight is rarely
"block or allow". The escalation path is the point: ambiguous cases go to a
human, the human's decision is recorded in the same audit trail, and the
system degrades gracefully (retry, cost caps) instead of failing silently.

## Quick start

Requires Python 3.12, standard library only. No network, no API keys.

```bash
cd ~/workspace/ai-governance-projects/policy-violation-monitor

# 1. Run the monitor over the demo fixture stream
python monitor.py --demo

# 2. Inspect the human review queue
python review.py list

# 3. Record a decision (appends to the audit log)
python review.py decide out-005 approve --note "Quoted text from a webpage, not a live injection"
python review.py decide out-014 reject --note "Clear injection phrasing in output"

# 4. Watch the cost cap work
python monitor.py --demo --max-cost 40
```

## Policy rule format

Rules live in `policies.py` as dicts in the `POLICIES` list:

```python
{
    "id": "EX-001",                                   # stable identifier
    "name": "Short human-readable name",              # shown in summaries
    "severity": "high",                               # high | medium | low
    "description": "What this guards against and why",
    "check": callable,                                # text -> list of evidence strings
}
```

The `check` function returns a list of evidence strings (matched substrings,
annotated hits); an empty list means "no violation". Current rules:

| ID      | Name                              | Severity |
|---------|-----------------------------------|----------|
| PII-001 | PII leakage: email addresses      | high     |
| PII-002 | PII leakage: phone numbers        | high     |
| PII-003 | PII leakage: ID-like numbers      | high     |
| SEC-001 | Secrets leakage: API keys/tokens  | high     |
| INJ-001 | Prompt-injection in output text   | medium   |
| DIS-001 | Disallowed content markers        | high     |

To add a rule, append a dict with the same shape, `evaluate()` picks it up
automatically. Severity drives the action: **high → auto-block**,
**medium → escalate for human review**, **low → log-and-pass**.

## Mapping to real oversight workflows

| This project | Production equivalent |
|---|---|
| Severity-based routing | Tiered response playbooks (block / review / allow) |
| `review_queue.json` + `review.py decide` | Human-in-the-loop review queues (e.g. Trust & Safety ops) |
| `audit.log.jsonl` (append-only) | Immutable audit trails required by EU AI Act / NIST AI RMF logging guidance |
| Retry with backoff | Resilient pipeline design: transient failures shouldn't drop oversight |
| Cost cap with graceful abort | Budget guardrails on monitoring itself; skipped items are logged, never silent |
| Deterministic regex rules | First line of defense before heavier model-based classifiers; auditable and explainable |

## Files

- `policies.py`, policy rule definitions and `evaluate()`
- `monitor.py`, supervisor CLI (`--demo`), retry, cost cap, audit logging
- `review.py`, human review CLI (`list`, `decide`)
- `fixtures/outputs.jsonl`, 20 simulated outputs (clean + planted violations)
- `audit.log.jsonl`, created on first run; append-only decision log
- `review_queue.json`, created on first run; pending/decided escalations

## Example output

```
$ python monitor.py --demo
Monitoring 20 outputs (cost cap: 1000, max retries: 3)

  [passed]    out-001: clean
  [passed]    out-002: clean
  [passed]    out-003: clean
  [BLOCKED]   out-004: PII-001
  [ESCALATED] out-005: INJ-001
  ...
  [retry] out-019: simulated flaky tool output (attempt 1/3, backoff 0.10s)
  [passed]    out-019: clean

====================================================
RUN SUMMARY
====================================================
  Outputs processed : 20/20
  Violations by policy:
    DIS-001  2
    INJ-001  2
    PII-001  2
    PII-002  2
    PII-003  1
    SEC-001  2
  Actions taken     : blocked=8, escalated=2, passed=10
  Retries used      : 1
  Cost consumed     : 80/1000
  Escalations pending review: 2
  Audit log         : .../audit.log.jsonl
```

## Limitations (by design)

- Detection is regex/heuristic: real deployments layer model-based
  classifiers on top. Deterministic rules are the auditable baseline.
- The disallowed-content rule uses a deliberately narrow keyword set; it
  demonstrates the mechanism, not a production blocklist.
- The reviewer identity is a placeholder (`human-reviewer`); wire it to real
  auth in production.
