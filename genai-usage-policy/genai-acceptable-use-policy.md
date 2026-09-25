# Generative AI Acceptable Use Policy

> **Illustrative sample policy.** Not legal advice. Adapt scope, roles, and
> control details to your organization's structure and counsel's guidance
> before adoption.
> Part of the [GenAI usage policy project](./README.md).

**Document ID:** POL-AI-001
**Version:** 1.0 (illustrative)
**Effective date:** 2026-10-01 (illustrative)
**Owner:** AI Governance Lead (illustrative role)
**Review cycle:** Annual, or on material regulatory or technology change

---

## 1. Purpose

This policy sets the rules for safe, lawful, and responsible use of generative
AI (GenAI) tools by staff. It exists to capture GenAI's productivity benefits
while controlling data leakage, legal, quality, and reputational risk.

## 2. Scope

Applies to all employees, contractors, and temporary staff ("users") who use
GenAI tools: including chatbots, coding assistants, image generators, and
GenAI features embedded in business software: for any work purpose, on any
device.

Consumer-grade GenAI accounts used for personal purposes are out of scope,
but work content must never be entered into them.

## 3. Definitions

- **Approved tool:** a GenAI tool on the approved-tool list maintained by the
  AI governance team, with a completed vendor review and data processing terms.
- **High-risk use:** any use that makes or materially influences decisions
  about people, handles sensitive personal data, or is customer-facing.
- **Confidential information:** anything classified Confidential or above
  under the information classification policy, plus customer and employee
  personal data.

## 4. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Users | Use only approved tools for work; follow data rules in §6; complete required training; report incidents |
| Managers | Ensure their teams know this policy; approve exception requests for their staff |
| AI governance lead | Maintain the approved-tool list; run the review path in §7; own policy updates |
| Security | Review new tools for security posture; monitor for unapproved-tool usage |
| Legal / privacy | Advise on data-protection impact; review high-risk uses and exception requests |
| Internal audit | Periodically verify compliance with this policy |

## 5. Acceptable use

Permitted with an **approved tool**:

- Drafting, summarizing, and editing business documents, emails, and reports
- Brainstorming, research synthesis, and meeting preparation
- Code assistance (completion, explanation, test scaffolding) with human review
- Translation and plain-language rewriting of internal materials
- Data analysis support where the user validates results before acting

All output must be reviewed by a competent human before it is relied upon,
sent externally, or published. The user is accountable for the accuracy of
what they submit.

## 6. Data rules

1. **Never** enter confidential information, customer or employee personal
   data, credentials, or source code from restricted repositories into a tool
   that is not approved for that data class.
2. Check the approved-tool list for each tool's permitted data classes before
   first use; when in doubt, use synthetic or redacted inputs.
3. Do not use GenAI to re-identify anonymized data.
4. Retain and log prompts/outputs where the tool's audit features support it;
   do not keep copies of sensitive outputs longer than the business need.

## 7. Prohibited uses

- Entering confidential or personal data into unapproved or consumer tools
- Generating content intended to deceive (deepfakes, fabricated reviews,
  impersonation)
- Using GenAI to make solely automated decisions about individuals (hiring,
  credit, access) without an approved human-oversight design
- Circumventing a tool's safety controls or this policy's review path
- Representing AI-generated work as solely human-authored where authorship matters

## 8. Review path for new tools

1. **Request:** submit the [AI use-case intake form](../ai-use-case-intake/intake-form.md).
2. **Triage:** the governance analyst scores the use case per the
   [triage rubric](../ai-use-case-intake/triage-rubric.md).
3. **Vendor review:** Track B and above require the
   [vendor AI assessment](../vendor-ai-assessment/vendor-ai-checklist.md).
4. **Approval:** Track C and above require governance committee sign-off;
   Track D requires executive + legal sign-off.
5. **Listing:** approved tools are added to the approved-tool list with their
   permitted data classes and review date.

Tools already in use without approval ("shadow AI") must be disclosed within
30 days of this policy's effective date and enter the review path; continued
unapproved use after that window is a policy violation.

## 9. Controls

| Control | Detail |
|---|---|
| Approved-tool list | Single authoritative list; reviewed quarterly |
| Access management | Enterprise accounts with SSO; no shared credentials |
| Logging | Tool-level audit logs retained per the retention schedule |
| Training | Mandatory GenAI awareness training on hire and annually; role-specific modules for high-risk uses |
| Monitoring | Security monitors for unapproved-tool traffic; quarterly usage reviews |
| Incident response | Suspected data leakage or misuse reported to the AI governance lead and security within 24 hours |

## 10. Exceptions

Exceptions require a written request using the
[exception request template](./exception-request-template.md), manager
sponsorship, and approval by the AI governance lead (plus legal for
high-risk uses). Exceptions are time-boxed (max 6 months), logged, and
reviewed at expiry.

## 11. Enforcement

Violations are handled under the employee code of conduct and may result in
tool access revocation, retraining, or disciplinary action proportionate to
the risk created.

## 12. Version history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Illustrative initial release |

---

*Related artifacts: [exception request template](./exception-request-template.md) ·
[project README](./README.md) · [vendor AI checklist](../vendor-ai-assessment/vendor-ai-checklist.md)*
