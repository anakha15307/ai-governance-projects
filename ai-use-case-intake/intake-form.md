# AI Use-Case Intake Form: Template

> **Illustrative template.** Adapt to your organization's governance program before use.
> Part of the AI use-case intake project: see [README.md](./README.md).

All fields below should be completed by the requestor before a triage review begins.
Incomplete forms are returned to the requestor; they do not enter the review queue.

---

## 1. Requestor information

| Field | Value |
|---|---|
| Requestor name | |
| Team / department | |
| Contact email | |
| Business owner (accountable) | |
| Date submitted | |

## 2. Use-case description

| Field | Value |
|---|---|
| Use-case name (short) | |
| Business problem this solves | |
| Proposed AI capability | |
| Intended users (internal staff / customers / students / public) | |
| Expected number of users | |
| Deployment stage (idea / pilot / production) | |
| Target go-live date | |

## 3. Data

| Field | Value |
|---|---|
| Data sources used | |
| Data categories (business / personal / sensitive) | |
| Whose data is involved (employees, customers, students, other) | |
| Does it involve minors' data? (yes / no) | |
| Data residency requirements | |

## 4. Technology and deployment

| Field | Value |
|---|---|
| Model / tool (vendor name, model, version: or "to be selected") | |
| Deployment (internal / vendor SaaS / public model API / unmanaged tool) | |
| Integration points (systems it connects to) | |
| Human oversight (fully automated / human-in-the-loop / human-on-the-loop / advisory only) | |

## 5. Risk indicators (check all that apply)

- [ ] Makes or materially influences decisions about people (hiring, grading, lending, access, pricing)
- [ ] Customer- or public-facing output
- [ ] Processes personal or sensitive data
- [ ] Biometric identification or emotion inference
- [ ] Content generation published without human review
- [ ] Autonomous action (sends messages, executes transactions, changes records)
- [ ] New vendor or unapproved tool
- [ ] Regulated domain (education, employment, finance, healthcare, legal, safety)

## 6. Approvals

| Role | Name | Date |
|---|---|---|
| Business owner sign-off | | |
| Data steward (if personal data) | | |
| Security review (if new vendor/integration) | | |

---

**Next step:** Submit the completed form to the AI governance intake channel.
Triage follows the [triage scoring rubric](./triage-rubric.md); scored use cases are
recorded in [registry.json](./registry.json).
