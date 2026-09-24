# Chapter 4: Risk Assessment

**Purpose:** Produce a rigorous, evidence-based risk assessment of a use case
that ends in a defensible risk rating and concrete control requirements.

**When to use it:** For Tier 2 (light version) and Tier 3–4 (full version)
use cases; re-assess on material change or at the tier's review interval.

## Procedure

### 1. Gather evidence — with discipline

Every fact in the assessment is tagged as one of three types. Never mix them:

- **Vendor / builder claim** — what the supplier or team *says* ("our model
  is 99% accurate"). Treated as unverified until tested or corroborated.
- **Analyst observation** — what you *saw* in testing, logs, docs, or
  interviews ("in 40 sampled tickets, 3 drafts contained wrong refund
  amounts").
- **Analyst recommendation** — what *should* happen ("require agent
  confirmation for amounts over $500"). Clearly separated from findings.

This three-way split is the single highest-value habit in this playbook. It
prevents vendor marketing from becoming your risk rating.

### 2. Build the risk register for the use case

For each risk: describe the failure mode concretely (not "AI risk" —
"chatbot drafts a refund the customer isn't owed, agent approves without
reading"), then score:

- **Likelihood** (1–5): how often would this occur per unit of operation,
  given current controls?
- **Impact** (1–5): if it occurs, how bad — financial, reputational, legal,
  harm to people?
- **Risk score = Likelihood × Impact** (1–25). Then assess **residual risk**
  after proposed controls.

Risk matrix: 1–4 low, 5–9 medium, 10–15 high, 16–25 critical. Residual risk
above the tier's tolerance (define it: e.g., no residual risk > 9 for Tier 2)
blocks deployment until mitigated.

### 3. Let the register drive the tests

Each risk rated medium or above gets at least one evaluation scenario
(Chapter 8). If a risk can't be turned into a test, it's probably not
concrete enough — rewrite it until it is.

### 4. Write the assessment

Structure: scope (from Chapter 2) → evidence summary (claims vs.
observations) → risk register with scores → control requirements (from
Chapter 5's library) → residual risk → recommendation
(go / conditional-go / no-go with rationale). Use
[`templates/risk-assessment.md`](../templates/risk-assessment.md).

### 5. Review and sign

Tier 2: peer review by another analyst. Tier 3: program owner review.
Tier 4: independent reviewer + governance committee. The reviewer checks
evidence tagging, scoring consistency, and whether recommendations actually
address the risks — not prose quality.

## Worked mini-example (illustrative)

*Meridian Logistics*, **ML-UC-007** (Relay chatbot, Tier 2). Excerpt from the
risk register:

| # | Failure mode | L | I | Score | Controls | Residual |
|---|---|---|---|---|---|---|
| R-1 | Draft states a refund policy that doesn't exist; agent approves without reading | 3 | 3 | 9 | R-1a: agent must open policy link for refund drafts (preventive); R-1b: weekly sampling of refund replies (detective) | 4 |
| R-2 | Draft includes another customer's personal data from retrieved context | 2 | 4 | 8 | R-2a: retrieval scoped to current ticket only (preventive); R-2b: PII pattern scan before send (detective) | 4 |
| R-3 | Customer pastes credentials into chat; stored in logs | 3 | 2 | 6 | R-3a: input warning banner (preventive); R-3b: log redaction job (corrective) | 3 |

*Evidence discipline in practice:* vendor claim — "Relay never hallucinates
policy"; analyst observation — "in 40 sampled drafts, 3 misstated the
72-hour refund window"; recommendation — "treat policy statements as
unverified until R-1a/R-1b operate for 60 days." Recommendation:
**conditional-go** — deploy with R-1a through R-3b implemented and a 60-day
control-effectiveness check (Chapter 8).

## Common pitfalls

- **Vendor claims laundered into findings.** "The vendor states…" is not
  evidence of anything except that the vendor states it.
- **Risks written as topics.** "Data privacy" is not a risk; "draft leaks
  another customer's address" is.
- **Likelihood scored on vibes.** Anchor it: incidents per 1,000 operations,
  or a stated basis ("no observed occurrence in 3 months of logs, but no
  monitoring either → 3, not 1").
- **Assessment without a decision.** Every assessment ends in go /
  conditional-go / no-go. Analysis that recommends nothing is trivia.

## Templates

- [`templates/risk-assessment.md`](../templates/risk-assessment.md)

## Repo tooling

- [`llm-eval-case-study/`](../../llm-eval-case-study/) — worked example of
  turning evaluation evidence into risk decisions.
- [`edtech-risk-assessment/`](../../edtech-risk-assessment/) — full assessment
  with NIST AI RMF mapping.
- [`khanmigo-risk-assessment/`](../../khanmigo-risk-assessment/) — third-party
  assessment using public sources only.
