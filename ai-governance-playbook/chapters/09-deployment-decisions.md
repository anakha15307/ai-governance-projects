# Chapter 9: Deployment Decisions

**Purpose:** Make go / conditional-go / no-go decisions explicitly, by the
right authority, with the rationale recorded — so "who approved this?" always
has an answer.

**When to use it:** Before any Tier 2+ deployment or material change;
re-decide when conditions of a conditional-go are met or breached.

## The three outcomes

- **Go:** residual risks within tolerance, controls implemented and tested,
  monitoring plan active. Deploy.
- **Conditional-go:** deploy *only* when the listed conditions are met —
  specific controls, a time-boxed re-test, a usage limit. Conditions have
  owners and dates. If conditions aren't met by the date, the decision lapses
  to no-go automatically.
- **No-go:** residual risk exceeds tolerance, or required evidence doesn't
  exist. Record what would change the decision — a no-go without a path
  forward is just a veto.

## Procedure

### 1. Route to the right decision authority

| Tier | Decides | Form |
|---|---|---|
| Tier 2 | Program owner (on analyst recommendation) | Decision record |
| Tier 3 | Governance committee | Decision record + meeting minutes |
| Tier 4 | Governance committee + executive sponsor sign-off | Decision record + minutes + sponsor signature |

The analyst recommends; the authority decides. The analyst's job is to make
the residual risk unmistakably clear, not to make the decision for them.

### 2. Complete the decision record

Use [`templates/deployment-decision-record.md`](../templates/deployment-decision-record.md):
use case, tier, assessment reference, residual risks, controls required,
conditions (for conditional-go), monitoring plan reference, decision,
rationale, dissent (record disagreement — see Chapter 1, step 5), signatures,
review date.

### 3. Enforce conditional-go conditions

The coordinator tracks each condition to its date. Missed condition =
automatic lapse to no-go until re-decided. Conditions that nobody tracks are
suggestions.

### 4. Set the review date

Every go decision carries a next-review date (by tier: Tier 2 annual,
Tier 3 semi-annual, Tier 4 quarterly). Deployment approval is a lease, not
a deed.

## Worked mini-example (illustrative)

*Meridian Logistics*, **ML-UC-007**: the analyst recommends conditional-go —
residual risks R-1–R-3 are medium-low with controls R-1a through R-3b, but
the reviewer catch rate is unmeasured and the redaction ordering bug is
unfixed. The program owner approves **conditional-go** with conditions:
(1) redaction fix verified by re-test within 14 days (owner: engineering
lead); (2) 60-day sampling shows ≥ 90% agent catch rate (owner: support
operations lead); (3) deployment limited to the support queue — no
proactive outreach. Review date: 90 days. At day 60, sampling shows 91% —
conditions met, decision converts to go, recorded in the register.

## Common pitfalls

- **Verbal approvals.** If it isn't written, it didn't happen — and the
  audit will notice.
- **Conditional-go without expiry.** Conditions drift; the lapse rule is the
  enforcement mechanism.
- **Decision shopping.** Owner disagrees with the analyst and finds a
  friendlier forum. The charter's disagreement path (Chapter 1) exists for
  this.
- **No dissent recorded.** Unanimous minutes for a contested decision signal
  a broken process, not harmony.

## Templates

- [`templates/deployment-decision-record.md`](../templates/deployment-decision-record.md)
