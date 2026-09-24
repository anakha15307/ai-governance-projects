# Vendor AI Assessment Checklist

> **Illustrative template.** Tailor to your procurement and risk policies;
> high-risk use cases may need deeper review (on-site audits, penetration
> test reports, model cards).
> Part of the [vendor AI assessment project](./README.md).

**How to use:** complete one copy per vendor/tool. Rate each item
Pass / Conditional / Fail / N-A, cite the evidence (document name, date),
and record remediation for anything not a clean Pass. The overall rating
follows the worst material finding.

---

## A. Vendor profile

| # | Item | Rating | Evidence |
|---|---|---|---|
| A1 | Vendor identity, ownership, and financial viability understood | | |
| A2 | Named security and privacy contacts available | | |
| A3 | Subprocessors disclosed; right to object to changes | | |

## B. Data practices

| # | Item | Rating | Evidence |
|---|---|---|---|
| B1 | Data processing agreement (DPA) executed with required terms | | |
| B2 | Customer data is **not** used to train vendor models by default (or opt-out confirmed in writing) | | |
| B3 | Data retention periods defined; deletion on termination confirmed | | |
| B4 | Data residency / cross-border transfer mechanism documented | | |
| B5 | Data minimization: vendor collects only what the service needs | | |

## C. Model and AI safety

| # | Item | Rating | Evidence |
|---|---|---|---|
| C1 | Model identity and version disclosed; change notification process exists | | |
| C2 | Evaluation results shared (accuracy, safety, or fairness — relevant to the use case) | | |
| C3 | Known limitations documented (model card or equivalent) | | |
| C4 | Content safety controls described (filters, refusal behavior) | | |
| C5 | Human-oversight hooks available where the use case needs them | | |

## D. Security

| # | Item | Rating | Evidence |
|---|---|---|---|
| D1 | Independent security attestation current (e.g., SOC 2 Type II, ISO 27001) | | |
| D2 | Encryption in transit and at rest; key management described | | |
| D3 | Access controls: SSO/SAML, MFA, role-based access, audit logging | | |
| D4 | Vulnerability disclosure / incident notification commitments with timelines | | |
| D5 | Penetration test summary available (for high-risk uses) | | |

## E. Compliance and legal

| # | Item | Rating | Evidence |
|---|---|---|---|
| E1 | Privacy compliance posture documented (GDPR/CCPA-relevant measures) | | |
| E2 | EU AI Act role allocation clear (provider vs. deployer obligations) | | |
| E3 | IP / output-ownership terms acceptable; indemnity reviewed by legal | | |
| E4 | Regulated-industry requirements addressed (if applicable) | | |

## F. Operational

| # | Item | Rating | Evidence |
|---|---|---|---|
| F1 | SLA and support model defined; uptime commitments | | |
| F2 | Exit plan: data export format and transition assistance | | |
| F3 | Logging and audit data available to the customer | | |
| F4 | Roadmap / deprecation notice commitments | | |

---

## Overall rating

| Rating | Meaning |
|---|---|
| **Approved** | No material findings; proceed per the intake review track |
| **Approved with conditions** | Proceed only after remediation items close (list them with owners and dates) |
| **Not approved** | Material unresolved findings; do not deploy |

**Assessor:** ______________________ **Date:** __________
**Reviewer (for Track C/D):** ______________________ **Date:** __________

## Remediation log

| Finding | Required action | Owner | Due | Status |
|---|---|---|---|---|
| | | | | |
