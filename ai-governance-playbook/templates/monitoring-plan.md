# Monitoring Plan

Per Playbook Chapter 10. Write before deployment; activate at go-decision.

Use-case ID: [ORG-UC-NNN]. Name: [Name]. Tier: [1/2/3/4]
Owner: [Use-case owner]. Analyst: [Name]. Effective: [YYYY-MM-DD]

## 1. What is monitored

| Layer | Signal | Method | Frequency | Owner |
|---|---|---|---|---|
| Output quality | [e.g., sampled reply accuracy] | [e.g., human review of 20/week] | [Weekly] | [Name] |
| Behavioral drift | [e.g., jailbreak attempt rate, failure-mode counts] | [e.g., log analysis] | [Weekly] | [Name] |
| Context drift | [e.g., policy/product changes affecting correctness] | [e.g., change log review] | [Monthly] | [Name] |

## 2. Alert thresholds

| Signal | Threshold | Alert goes to | SLA |
|---|---|---|---|
| [e.g., weekly sample pass rate] | [e.g., < 95%] | [Support lead + analyst] | [1 business day] |
| [e.g., critical failure: PII leak, wrong payment] | [Any occurrence] | [Program owner] | [4 hours] |

## 3. Review triggers (out-of-cycle review required)

- [ ] Model, prompt, or configuration change
- [ ] Vendor update or silent behavior change
- [ ] Data source change
- [ ] Incident or near-miss
- [ ] Complaint spike (define: [e.g., > 5 related complaints/week])
- [ ] Regulatory change affecting this use case
- [ ] Expansion to new users, geographies, or purposes

## 4. Escalation path

- Flagged item → [Name/role] within [SLA]
- No response within [SLA] → [default: hold/deny action for high-stakes uses]
- Escalation contact: [Name, channel]

## 5. Reporting

- Findings to monthly risk review: [Yes, coordinator includes]
- Metrics tracked: [sample pass rate, incident count, catch rate, open remediations…]

## 6. Plan review

- This plan reviewed: [date], next review: [YYYY-MM-DD, per tier interval]
