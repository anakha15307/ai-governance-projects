# Framework crosswalk

How the projects in this repo map to the three frameworks governance teams
use most: the NIST AI Risk Management Framework, ISO/IEC 42001, and the EU
AI Act. I only map what each project genuinely covers. Nothing here is a
certification claim.

## NIST AI RMF 1.0

The RMF organizes risk management into four functions: Govern, Map, Measure,
Manage. Here is where each function shows up in the repo, and what evidence
it produces.

| RMF function | What it means | Covered in | Evidence |
|---|---|---|---|
| Govern 1: culture of risk management | Roles, policies, accountability | 08 GenAI policy, 15 playbook Ch. 1 and Ch. 6 | Acceptable-use policy with roles and review path; program setup chapter |
| Govern 2: risk management as priority | Documented risk process | 15 playbook Ch. 3-4 | Risk tiering and assessment procedures |
| Govern 4: culture of communication | Stakeholder reporting | 06 dashboard, 15 Ch. 15 | Generated risk register dashboard; board reporting template |
| Govern 5: risk ownership | Named owners and approvers | 05 model registry, 07 intake registry | Approval workflow with reviewer names and timestamps |
| Map 1: context and categorization | Use-case inventory and tiering | 07 intake and triage, 01 EU AI Act classifier | Triaged registry entries; tier assignments with rationale |
| Map 5: human-AI teaming | Oversight levels | 07 triage rubric, 09 edtech assessment | Oversight-level fields in intake; human-in-loop controls |
| Measure 1: identification of risk | Testing and evaluation | 02 bias audit, 03 red team, 16 Laya experiments | Fairness report cards; before/after scoreboard; 85% accuracy report with CIs |
| Measure 2: evaluation of risk | Calibration, bias probes | 16 Laya (ECE 0.125, bias probe), 17 council (calibration finding) | report.md; FINDINGS.md |
| Manage 1: risk response | Controls and mitigations | 09 edtech assessment, 13 Khanmigo assessment | Control tables with owners and residual risk |
| Manage 4: monitoring | Post-deployment monitoring | 04 policy monitor, 06 dashboard, 15 Ch. 10 | Audit log and review queue; overdue-action reporting; monitoring plan template |

## ISO/IEC 42001:2023

The AI management system standard. Genuine coverage in the repo:

| 42001 clause / control area | Covered in | Evidence |
|---|---|---|
| 6.1 Actions to address risks and opportunities | 09, 13 risk assessments | Risk registers with likelihood, impact, controls |
| 7.5 Documented information | 15 playbook Ch. 16 | Documentation and record-keeping procedures |
| 8.1 Operational planning and control | 07 intake and triage | Intake form, scoring rubric, registry |
| A.7 Data for AI systems | 05 model registry | Dataset lineage records |
| A.8 Information for interested parties | 06 dashboard | Stakeholder-facing risk reporting |
| B.7.4 Monitoring, measurement, analysis | 04 policy monitor, 15 Ch. 10 | Violation audit log; monitoring plan template |

What is NOT covered: internal audit of the management system (clause 9.2),
management review (9.3), and continual improvement processes (10). Those need
a real organization, and I do not claim them.

## EU AI Act

| AI Act element | Covered in | Evidence |
|---|---|---|
| Risk-tier classification (Art. 5, 6, 50; Annex III) | 01 classifier, 09 edtech assessment, 13 Khanmigo assessment, 17 council cases | Tier assignments with matched categories and rationale |
| Transparency obligations for AI-generated content (Art. 50) | 17 council case 7 analysis | Deliberation on the human-review exemption in Art. 50(2) |
| Incident reporting (Art. 73) | 14 incident deconstructions, docs/monitoring-and-incident-response.md | Root-cause analyses; proposed reporting procedure |
| Documentation duties for high-risk systems (Annex IV) | 05 model registry, 13 Khanmigo assessment | Lineage and intended-use records; assessment structure |

The classifier and the council cases are educational simplifications of the
Act's tiers, not legal advice. Regulatory obligations should always be
verified against the official text and counsel.

## What the crosswalk does not claim

Mapping projects to frameworks is an analyst exercise, not an audit. No
project here has been independently validated, and none of this constitutes
a conformity assessment under the EU AI Act or certification under ISO 42001.
