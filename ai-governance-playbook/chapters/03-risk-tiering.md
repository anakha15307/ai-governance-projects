# Chapter 3: Risk Tiering

**Purpose:** Decide how much governance each use case gets, quickly,
consistently, and defensibly: so effort goes where risk is.

**When to use it:** At intake triage for every use case; re-tier when the use
case, data, or deployment context changes materially.

## Procedure

### 1. Score inherent risk (before controls)

Rate each dimension 1-3. Inherent means *as the use case is designed*,
ignoring any controls that may or may not exist yet.

| Dimension | 1 | 2 | 3 |
|---|---|---|---|
| Impact on people | Convenience / low stakes | Financial, employment, or access consequences | Health, safety, liberty, or large-scale exclusion |
| Reversibility | Easily undone by the affected person | Undoable with effort or appeal | Irreversible or effectively irreversible |
| Autonomy | Human decides; AI advises | Human reviews AI output before action | AI acts without meaningful human review |
| Data sensitivity | Public or internal non-personal | Personal data, non-sensitive | Sensitive personal data (health, biometrics, children, precise location) |
| Regulatory exposure | No sector-specific AI rules | Sector guidance or active enforcement interest | Explicit statutory obligations (e.g., EU AI Act high-risk use) |

Sum the five scores (range 5-15).

### 2. Assign the tier

| Score | Tier | Meaning | Governance weight |
|---|---|---|---|
| 5-6 | Tier 1: Minimal | Low risk | Intake + inventory entry; standard policies apply |
| 7-9 | Tier 2: Limited | Moderate risk | + light assessment, control checklist, annual review |
| 10-12 | Tier 3: High | Significant risk | + full assessment (Ch. 4), testing (Ch. 8), committee deployment decision (Ch. 9), monitoring plan (Ch. 10) |
| 13-15 | Tier 4: Critical | Severe / regulated risk | + everything in Tier 3 with independent review, continuous monitoring, board-level visibility |

### 3. Apply the override rule

The rubric is a starting point, not a verdict. Override up one tier when:
a regulator has named the use type, the use affects a vulnerable population,
or the deployment context is novel. Record the override and the reason, 
"analyst judgment" with no rationale is not auditable.

### 4. Set proportionate requirements

Each tier carries a defined minimum: which chapters apply, who decides
deployment, how often it's reviewed. Write this as a one-page table in your
program wiki so owners know what's expected before they submit intake.
(Tiers also drive control selection in Chapter 5 and test depth in
Chapter 8.)

## Worked mini-example (illustrative)

*Meridian Logistics*, use case **ML-UC-007** (Relay support chatbot, human
agent approves every draft before sending):

| Dimension | Score | Rationale |
|---|---|---|
| Impact on people | 2 | Wrong replies can cause financial harm (billing disputes) |
| Reversibility | 1 | Agent reviews before send; customer can appeal |
| Autonomy | 2 | Human-on-the-loop, not fully autonomous |
| Data sensitivity | 2 | Ticket text contains customer personal data |
| Regulatory exposure | 1 | No sector-specific AI statute applies |
| **Total** | **8** | **Tier 2: Limited** |

Requirements: light assessment, control checklist (human approval step,
data-handling rules), annual review. *Analyst note:* if Meridian later lets
Relay send replies without agent review, autonomy becomes 3 and the total
hits 9-10: re-tier to Tier 3 and require full assessment and testing
*before* the change ships. Tiering is a living decision, not a one-time label.

## Common pitfalls

- **Scoring residual risk instead of inherent.** Controls come later; tiering
  on "but we have a human review" bakes assumptions into the foundation.
- **Tier inflation.** Everything Tier 3 means nothing is Tier 3. The rubric
  exists to say no.
- **No re-tiering triggers.** Model change, new data, expanded deployment, 
  each should force a re-score.
- **Confusing the EU AI Act with this.** The Act's risk categories are legal
  classifications; these tiers are your internal governance effort levels.
  They inform each other but aren't the same thing (see Chapter 13).

## Templates

- [`templates/risk-tiering-worksheet.md`](../templates/risk-tiering-worksheet.md)

## Repo tooling

- [`eu-ai-act-risk-classifier/`](../../eu-ai-act-risk-classifier/). 
  EU AI Act tier classification to cross-check regulatory exposure.
