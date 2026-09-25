# Chapter 7: Human Oversight

**Purpose:** Decide where human judgment is mandatory, design the oversight
so it actually works, and define what happens when the human flags a problem.

**When to use it:** During assessment (Chapter 4) for every Tier 2+ use
case; re-validate whenever autonomy or stakes change.

## The three oversight models

- **Human-in-the-loop:** the AI cannot act without explicit human approval
  each time. Highest friction, strongest control. Use for irreversible or
  high-stakes actions.
- **Human-on-the-loop:** the AI acts (or prepares action) while a human
  supervises and can intervene: sampling, dashboards, alerts. Works only if
  the human has real authority and real attention.
- **Human-out-of-the-loop:** the AI acts autonomously; humans review
  aggregate performance afterward. Acceptable only for low-stakes, reversible
  actions with strong detective controls.

## Procedure

### 1. Choose the model by tier and stakes

Default mapping: Tier 4 → in-the-loop for consequential actions; Tier 3 →
in- or on-the-loop; Tier 2 → on-the-loop minimum for external outputs;
Tier 1 → out-of-the-loop acceptable. Deviations require written rationale.

### 2. Design against automation bias

Human oversight fails in predictable ways: reviewers rubber-stamp, attention
decays, and the interface hides what matters. Design requirements:

- The reviewer must see **what the AI is uncertain about** and **what
  changed** since last review: not just an "Approve" button.
- Review workload must be feasible: if a human must approve 500 items a day,
  you have theater, not oversight.
- Rotate reviewers and sample their decisions (Chapter 8, control E-4), 
  measure the catch rate, don't assume it.

### 3. Define the mandatory-human list

Write down the decisions AI may never make alone in your organization
(e.g., terminating employment, denying a customer claim above $X, sending
legal or safety communications). This list is policy (Chapter 6), enforced
by technical gates where possible.

### 4. Build the escalation path

For every supervised use case: what gets flagged, to whom, within what SLA,
and what happens if the human doesn't respond (default-deny for high stakes:
no response = no action). Record it in the assessment and the monitoring
plan.

## Worked mini-example (illustrative)

*Meridian Logistics*, **ML-UC-007**: Relay drafts replies; the agent reviews
and sends: human-**on**-the-loop for routine tickets, human-**in**-the-loop
for refunds over $500 (draft cannot send until the agent opens the policy
page and clicks explicit approval). The review UI shows the draft with
policy-amount fields highlighted and a one-line "why this draft" summary.
Escalation: any draft the agent flags goes to the support lead within 4
business hours; flagged drafts are excluded from training data. Monthly
sampling measures the agent catch rate on planted errors (target ≥ 90%), 
because the oversight claim is "agents catch bad drafts," and claims get
tested (Chapter 8).

## Common pitfalls

- **Oversight by job title.** "A human reviews it" means nothing without
  workload math, interface design, and measured catch rates.
- **Rubber-stamp interfaces.** If approving is one click and rejecting is
  five, you've designed the outcome.
- **No default on silence.** If the reviewer is out, does the system act or
  wait? Decide in advance.
- **Assuming oversight transfers liability.** A human clicking "approve"
  on something they couldn't reasonably evaluate is not meaningful oversight
, and won't look like it afterward.

## Templates

- Escalation paths: captured in [`templates/monitoring-plan.md`](../templates/monitoring-plan.md).

## Repo tooling

- [`policy-violation-monitor/`](../../policy-violation-monitor/), supervisor
  monitor implementing human-in-the-loop escalation.
