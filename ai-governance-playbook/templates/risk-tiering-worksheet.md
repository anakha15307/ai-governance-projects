# Risk Tiering Worksheet

Score **inherent risk** (before controls) per Playbook Chapter 3.
Use-case ID: [ORG-UC-NNN]. Name: [Name]
Analyst: [Name]. Date: [YYYY-MM-DD]

## Scores (1-3 per dimension)

| Dimension | Score | Rationale (one line each) |
|---|---|---|
| Impact on people | [1/2/3] | [Rationale] |
| Reversibility | [1/2/3] | [Rationale] |
| Autonomy | [1/2/3] | [Rationale] |
| Data sensitivity | [1/2/3] | [Rationale] |
| Regulatory exposure | [1/2/3] | [Rationale] |
| **Total** | **[5-15]** | |

**Scoring guide:** Impact, 1 convenience, 2 financial/employment/access
consequences, 3 health/safety/liberty/large-scale exclusion. Reversibility, 
1 easily undone, 2 undoable with effort/appeal, 3 irreversible. Autonomy, 
1 human decides, 2 human reviews before action, 3 AI acts without meaningful
review. Data, 1 public/internal non-personal, 2 personal non-sensitive,
3 sensitive personal data. Regulatory, 1 none, 2 guidance/enforcement
interest, 3 explicit statutory obligations.

## Tier assignment

| Total | Tier |
|---|---|
| 5-6 | Tier 1: Minimal |
| 7-9 | Tier 2: Limited |
| 10-12 | Tier 3: High |
| 13-15 | Tier 4: Critical |

- Tier assigned: [1 / 2 / 3 / 4]
- Override applied? [No / Yes: up one tier]
  - Override rationale: [Regulator-named use type / vulnerable population / novel context, explain]

## Proportionate requirements triggered

- [ ] Assessment depth: [None / Light / Full]
- [ ] Testing required: [None / Control-effectiveness / Full eval + red-team]
- [ ] Deployment authority: [Owner / Program owner / Committee / Committee + sponsor]
- [ ] Monitoring: [Standard policies / Monitoring plan / Monitoring plan + continuous]
- [ ] Review interval: [Annual / Annual / Semi-annual / Quarterly]

Analyst signature: [Name] Date: [YYYY-MM-DD]
Reviewer (Tier 3-4): [Name] Date: [YYYY-MM-DD]
