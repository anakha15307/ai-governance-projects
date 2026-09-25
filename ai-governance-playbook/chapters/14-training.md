# Chapter 14: Training

**Purpose:** Make sure each role knows what it needs to know, executives
can govern, builders can build safely, users can use AI without creating
incidents.

**When to use it:** At program launch (baseline for all roles), on role
change, after material incidents or policy changes, and annually as a
refresher.

## Procedure

### 1. Train by role, not by topic

One generic "AI training" teaches nobody anything. Minimum role tracks:

| Role | Must know | Format |
|---|---|---|
| Executives / board | What AI risk is, their accountability, how to read program metrics (Ch. 15) | 60-min briefing, annually |
| Use-case owners | Intake process, tiering, their control obligations, incident declaration | 90-min workshop at intake + annual refresher |
| Developers / data scientists | Secure AI development basics, eval design (Ch. 8), documentation standards (Ch. 16) | 2-hour technical session, annually |
| Business users | Acceptable-use policy (Ch. 6), data-handling rules, how to report concerns | 45-min module at onboarding + annual |
| Procurement / legal | Vendor assessment requirements (Ch. 12), contract terms, DPA basics | 90-min session, annually |
| Human reviewers | Their specific oversight duties, escalation paths, automation-bias awareness (Ch. 7) | Role-specific briefing before go-live + quarterly calibration |

### 2. Make it stick

- **Scenario-based:** "A customer pastes their password into the chatbot, 
  what do you do?" beats 40 slides on data classification.
- **Test it:** short quizzes with a pass threshold; track completion as a
  program KPI (Chapter 15). Training nobody verifies is a checkbox.
- **Refresh on trigger:** after an incident, the post-incident review
  (Chapter 11) feeds directly into updated training content.

### 3. Track and report

Completion rates by role, quiz scores, overdue counts, reported in the
program metrics (Chapter 15). Chronic non-completion in a high-risk area is
a governance finding, not an HR problem.

## Worked mini-example (illustrative)

*Meridian Logistics* rolls out training alongside the Relay deployment.
Support agents (human reviewers) get a 45-minute briefing: their approval
duties, the escalation path, and a live exercise, five drafts, two with
planted errors, reviewed together to calibrate what "careful review" looks
like. Result: agents flag that the review UI buries the policy-amount field
, a Chapter 7 interface fix that testing alone hadn't surfaced. Training
doubles as a control-design feedback loop.

## Common pitfalls

- **One-size-fits-all modules.** Executives don't need prompt-engineering
  tips; developers don't need board-reporting templates.
- **Annual click-through.** If the only measure is completion, the only
  outcome is completion.
- **Training after the incident it would have prevented.** Sequence it with
  deployment, not after.
- **No calibration for reviewers.** Human oversight degrades without
  periodic re-calibration (Chapter 7).

## Templates

- [`templates/training-plan.md`](../templates/training-plan.md)
