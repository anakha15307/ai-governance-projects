# Chapter 15: Metrics and Reporting

**Purpose:** Prove the program works — to leadership, to auditors, and to
yourself. Governance that can't be measured can't be managed or funded.

**When to use it:** Monthly (operational metrics for the risk review),
quarterly (program KPIs for the governance committee and board).

## Program KPIs

| KPI | What it tells you | Target (illustrative) |
|---|---|---|
| Inventory coverage | % of known AI uses registered with owner + tier | 100% of known; survey annually for unknown |
| Intake triage SLA | % of intakes tiered within 5 business days | ≥ 95% |
| Assessment backlog | Tier 3–4 assessments past due | 0 |
| Control-test pass rate | % of key controls passing effectiveness tests | ≥ 90% |
| Reviewer catch rate | Measured human-oversight effectiveness (Ch. 7–8) | ≥ 90% where applicable |
| Incident count by severity | SEV-1–4 per quarter, with trend | Track trend; investigate spikes |
| Mean time to contain (incidents) | Response speed | Decreasing trend |
| Training completion | % complete by role | 100% for high-risk roles |
| Remediation closure | % of findings closed by due date | ≥ 90% |
| Policy exception aging | Exceptions past review date | 0 |

Pick the 6–8 that fit your program's maturity; a 30-metric dashboard is
unread. Every KPI needs a definition, a data source, and an owner — metrics
without provenance are decoration.

## The board one-pager

Leadership gets one page, quarterly — use
[`templates/board-one-pager.md`](../templates/board-one-pager.md). Structure:

1. **Program health at a glance** — 4–6 KPIs with trend arrows.
2. **Material risks** — top 3 residual risks in plain language, what we're
   doing about each.
3. **Decisions needed** — tier-4 approvals, policy changes, funding.
4. **Incidents** — what happened, what changed (no jargon).

The test: a board member who reads only this page should be able to ask two
intelligent questions. If they can't, the page failed.

## Procedure

1. Coordinator collects metrics monthly from the register, monitoring
   plans, training records, and incident log.
2. Analyst sanity-checks: do the numbers match reality? (A 100% control-test
   pass rate with no failures ever recorded is suspicious, not excellent.)
3. Program owner reviews and writes the narrative — metrics need
   interpretation, not just presentation.
4. Committee/board receives the one-pager; decisions and questions recorded
   in minutes.

## Worked mini-example (illustrative)

*Meridian Logistics*, Q3 board one-pager: inventory coverage 100% (14 uses);
triage SLA 100%; one SEV-2 (Relay refund incident — contained in 2 hours,
14 customers corrected); reviewer catch rate 91%; training completion 96%
(4 support agents overdue — flagged). Material risks: (1) vendor silent
changes — mitigated by new contract clause at renewal; (2) HR resume
screener tiered Tier 3, assessment in progress. Decisions needed: approve
Tier-3 assessment scope for the screener; fund quarterly red-teaming.
Two questions from the board — exactly as designed.

## Common pitfalls

- **Vanity metrics.** "AI uses governed: 47" without tier distribution or
  risk context says nothing.
- **Metrics nobody acts on.** If a KPI misses target three quarters running
  with no consequence, delete it or fix the program.
- **Reporting activity instead of outcomes.** "12 assessments completed"
  is activity; "residual high risks reduced from 8 to 3" is an outcome.
- **Surprising the board.** Bad news in the one-pager should never be the
  first time leadership hears it.

## Templates

- [`templates/board-one-pager.md`](../templates/board-one-pager.md)

## Repo tooling

- [`governance-dashboard/`](../../governance-dashboard/) — risk register
  dashboard for the stakeholder-facing reporting layer.
