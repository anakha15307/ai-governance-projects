# Chapter 5: Controls Library

**Purpose:** A reusable catalog of controls, organized by NIST AI RMF
function, so assessments assign real controls instead of inventing
recommendations from scratch.

**When to use it:** During risk assessment (Chapter 4) to select controls;
during control-effectiveness testing (Chapter 8); during audits (Chapter 16).

## How the library is organized

Each control has: **ID**, name, **type**, preventive (P), detective (D), or
corrective (C): the **tiers** it applies to, and a one-line description.
Preventive stops the failure; detective finds it; corrective fixes it after.
Every medium+ risk should have at least one control of each type where
feasible: a risk with only preventive controls is one bypass away from
realization.

## The catalog

### GOVERN: culture, roles, and accountability

| ID | Control | Type | Tiers | Description |
|---|---|---|---|---|
| G-1 | Named use-case owner | P | 1-4 | Every use case has one accountable human; no owner, no deployment |
| G-2 | Deployment approval record | P | 2-4 | Go/conditional-go/no-go recorded before launch (Ch. 9) |
| G-3 | Policy exception process | P | 1-4 | Documented path to request, approve, and time-limit exceptions |
| G-4 | Workforce AI training | P | 1-4 | Role-based training completed before access (Ch. 14) |
| G-5 | Third-party AI inventory clause | D | 2-4 | Procurement flags AI components to governance before purchase |

### MAP: context, categorization, and risk framing

| ID | Control | Type | Tiers | Description |
|---|---|---|---|---|
| M-1 | Use-case scoping record | P | 2-4 | Written scope, boundaries, assumptions before assessment (Ch. 2) |
| M-2 | Risk tiering worksheet | P | 1-4 | Tier assigned and recorded at intake (Ch. 3) |
| M-3 | Stakeholder & impact analysis | P | 3-4 | Who is affected, how, and what recourse they have |
| M-4 | Data lineage record | D | 2-4 | Sources, transformations, and retention for training/inference data |

### MEASURE: testing, evaluation, and monitoring

| ID | Control | Type | Tiers | Description |
|---|---|---|---|---|
| E-1 | Pre-deployment evaluation set | P | 3-4 | Scenario tests derived from the risk register (Ch. 8) |
| E-2 | Red-team exercise | P | 3-4 | Adversarial testing of abuse/jailbreak paths (Ch. 8) |
| E-3 | Control-effectiveness test | D | 2-4 | Periodic test that each key control actually works (Ch. 8) |
| E-4 | Output monitoring & sampling | D | 2-4 | Human review of sampled outputs on a schedule (Ch. 10) |
| E-5 | Drift / performance tracking | D | 3-4 | Metrics tracked over time with alert thresholds (Ch. 10) |
| E-6 | Bias / fairness evaluation | D | 3-4 | Disaggregated performance checks where people are affected |

### MANAGE: risk response, oversight, and improvement

| ID | Control | Type | Tiers | Description |
|---|---|---|---|---|
| R-1 | Human approval gate | P | 2-4 | Defined human decision point before high-stakes action (Ch. 7) |
| R-2 | Escalation path | C | 2-4 | Named humans and SLAs for flagged cases (Ch. 7) |
| R-3 | Incident runbook | C | 2-4 | Severity levels and response steps published and drilled (Ch. 11) |
| R-4 | Model/data change management | P | 3-4 | Re-tier and re-test on material change (Ch. 10) |
| R-5 | Decommissioning procedure | C | 2-4 | Data deletion, user notice, and record retention on retirement |
| R-6 | Residual-risk acceptance | P | 3-4 | Named approver signs residual risk above tolerance (Ch. 9) |

## Procedure: selecting controls

1. For each risk in the register, pick controls that address it, aim for
   P+D+C coverage on high risks.
2. Check the tier minimums: the table's tier column is the floor, not the
   ceiling.
3. Assign a **control owner** and an **effectiveness test** (Chapter 8) to
   every selected control. A control with no owner and no test is a wish.
4. Record selections in the risk assessment (Chapter 4 template).

## Worked mini-example (illustrative)

*Meridian Logistics*, **ML-UC-007** risk R-1 (draft states a nonexistent
refund policy): controls selected - **R-1** human approval gate, scoped so
refund drafts require the agent to open the policy page (P); **E-4** weekly
sampling of 20 refund replies (D); **R-3** incident runbook entry for
"customer acted on wrong policy info" (C). Owner: support operations lead.
Effectiveness test: monthly, plant 5 incorrect-policy drafts, measure agent
catch rate; target ≥ 90%.

## Common pitfalls

- **Controls copied from a framework without tailoring.** "We do NIST AI RMF"
  is not a control. Each control needs an owner, a procedure, and a test.
- **All preventive, no detective.** Prevention fails silently; detection is
  how you find out.
- **Library treated as maximum.** The catalog is the floor. Novel risks need
  novel controls.
- **Orphaned controls.** Selected in the assessment, never assigned, never
  tested, quietly dead within a quarter.

## Templates

- [`templates/control-test-plan.md`](../templates/control-test-plan.md)
