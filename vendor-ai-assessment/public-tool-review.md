# Completed Vendor Assessment — ChatGPT (OpenAI), Illustrative

> **Illustrative sample, prepared 2026-09-24.** Based solely on publicly
> available information (OpenAI's published trust, privacy, and security
> pages as generally understood). Not legal advice, not a certification, and
> not a substitute for a real procurement review — vendor terms change, so
> verify everything against current contracts and documentation before any
> purchasing decision. No affiliation with OpenAI.
> Checklist: [vendor-ai-checklist.md](./vendor-ai-checklist.md).

**Tool:** ChatGPT (OpenAI) — public AI assistant
**Use case under review (illustrative):** internal productivity (drafting,
summarization) with an enterprise/workspace tier; **not** approved here for
confidential or regulated-decision use.
**Assessment scope:** publicly documented posture only; no contract review,
no technical testing.

---

## Findings

### A. Vendor profile

| # | Item | Rating | Evidence / notes (illustrative) |
|---|---|---|---|
| A1 | Identity, ownership, viability | Pass | Well-established vendor; public company disclosures available |
| A2 | Security/privacy contacts | Pass | Published trust center and support channels |
| A3 | Subprocessors disclosed | Conditional | Subprocessor list published; confirm change-notification terms in the enterprise agreement |

### B. Data practices

| # | Item | Rating | Evidence / notes (illustrative) |
|---|---|---|---|
| B1 | DPA executed | Conditional | Enterprise/workspace tiers offer DPAs — must be actually executed, not assumed |
| B2 | No training on customer data by default | Conditional | Enterprise tiers state business data is not used for training; **consumer/free tiers differ** — confirm the exact tier in writing |
| B3 | Retention and deletion | Conditional | Retention controls exist on business tiers; verify settings and deletion-on-termination in the agreement |
| B4 | Data residency / transfers | Conditional | Review published data-residency options against your requirements |
| B5 | Data minimization | Pass | Service collects account and usage data as documented; no evidence of excess collection for the stated scope |

### C. Model and AI safety

| # | Item | Rating | Evidence / notes (illustrative) |
|---|---|---|---|
| C1 | Model identity / versioning | Conditional | Model names published; confirm change-notification behavior for API/workspace use |
| C2 | Evaluation results shared | Conditional | Public system cards describe safety evaluations; request specifics relevant to your use case |
| C3 | Limitations documented | Pass | Published usage policies and model limitations documentation |
| C4 | Safety controls described | Pass | Documented content policies and refusal behavior |
| C5 | Human-oversight hooks | Pass | Human-in-the-loop is a deployment choice; tool supports review-before-send workflows |

### D. Security

| # | Item | Rating | Evidence / notes (illustrative) |
|---|---|---|---|
| D1 | Independent attestation | Pass | SOC 2 Type II and related certifications publicly claimed — verify current reports under NDA |
| D2 | Encryption | Pass | TLS in transit; encryption at rest as documented |
| D3 | SSO/MFA/RBAC/audit logging | Conditional | Available on business tiers; verify SSO and audit-log access are enabled for your tenant |
| D4 | Incident notification | Conditional | Confirm notification timelines in the enterprise agreement |
| D5 | Pen-test summary | N/A | Not required for this illustrative internal-productivity scope |

### E. Compliance and legal

| # | Item | Rating | Evidence / notes (illustrative) |
|---|---|---|---|
| E1 | Privacy posture | Conditional | Published privacy controls; legal to confirm GDPR/CCPA alignment for your data classes |
| E2 | EU AI Act role allocation | Conditional | Clarify provider vs. deployer responsibilities for your use in writing |
| E3 | IP / indemnity | Conditional | Legal review of output-ownership and indemnity terms required before approval |
| E4 | Regulated industry | N/A | Out of scope for this illustrative review |

### F. Operational

| # | Item | Rating | Evidence / notes (illustrative) |
|---|---|---|---|
| F1 | SLA / support | Pass | Published uptime and support tiers |
| F2 | Exit plan | Conditional | Confirm data-export format and transition assistance in the agreement |
| F3 | Logging / audit data | Conditional | Verify admin audit-log availability on the chosen tier |
| F4 | Deprecation notices | Pass | Published model deprecation policy |

---

## Overall rating: **Approved with conditions** (illustrative)

Suitable for the illustrative internal-productivity scope **only after**
the remediation items below close. Not approved for confidential data,
personal data beyond the agreed classes, or decisions about individuals.

## Remediation (illustrative)

| Finding | Required action | Owner | Due |
|---|---|---|---|
| B1–B3, D3 | Execute enterprise-tier DPA; confirm no-training-on-data and retention/deletion settings in writing | Legal + IT | Before rollout |
| E2–E3 | Legal review of AI Act role allocation, IP, and indemnity terms | Legal | Before rollout |
| A3, D4, F2 | Confirm subprocessor change notices, incident timelines, and exit terms in the agreement | Procurement | Before rollout |
| User control | Deploy with SSO enforced, consumer-tier use prohibited by policy, and mandatory user training | AI governance lead | Before rollout |

*This sample demonstrates the assessment method. A real review would be
grounded in executed contracts, current attestations obtained under NDA,
and technical validation.*
