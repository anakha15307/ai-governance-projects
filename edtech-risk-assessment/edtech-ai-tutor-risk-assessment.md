# Risk Assessment: AI Tutoring Assistant — "StudyBuddy" Pilot

> **Illustrative sample assessment.** All organizations, people, products, and
> figures are fictional. Not legal advice; EU AI Act analysis is a simplified
> illustration and must be validated with counsel for any real deployment.
> Part of the [risk assessment project](./README.md).

**Assessment ID:** RA-2026-011 (illustrative)
**Date:** 2026-09-24 (illustrative)
**Assessor:** AI Governance Analyst (illustrative role)
**System:** StudyBuddy — AI tutoring assistant (fictional product)
**Deployer:** Example School District (fictional organization)
**Stage:** Pre-pilot (proposed)

---

## 1. System description

StudyBuddy is a conversational AI tutoring assistant for middle-school
mathematics. Students ask questions and receive step-by-step explanations,
practice problems, and encouragement. The system also generates a weekly
"progress snapshot" for teachers summarizing each student's topics attempted,
accuracy trend, and suggested focus areas.

- **Model:** fictional vendor-supplied large language model, fine-tuned on
  open educational content (illustrative).
- **Users:** students aged 11–14 (minors), teachers, district administrators.
- **Data:** student prompts, generated responses, interaction logs; linked to
  the district's student information system for rostering (illustrative).
- **Human oversight:** teachers review progress snapshots before any
  intervention decision; the tutor cannot change grades or records.

## 2. EU AI Act tier classification

| Question | Analysis |
|---|---|
| Prohibited use? | No. The system does not perform social scoring, real-time remote biometric identification, emotion inference in education, or other prohibited practices. |
| High-risk? | **Yes — illustrative classification: High-Risk.** The progress snapshot evaluates learning outcomes and informs teacher intervention decisions, which falls within the education high-risk category (evaluation of learning outcomes / assessing the appropriate level of education). |
| Limited-risk (transparency) obligations? | Also yes: the conversational tutor must disclose that students are interacting with AI. |

**Result:** treat as **High-Risk** (illustrative). The high-risk obligations
(risk management, data governance, technical documentation, logging,
transparency, human oversight, accuracy/robustness) apply to the assessment
and intervention-support functions; transparency obligations apply to the
conversational interface. A real deployment requires counsel to confirm the
classification against the final Act text and implementing guidance.

## 3. NIST AI RMF mapping

Mapped to the AI Risk Management Framework's four functions (Govern, Map,
Measure, Manage). Illustrative mapping of key subcategories:

| RMF function | Subcategory (illustrative) | How this assessment addresses it |
|---|---|---|
| **Govern 1** — culture of risk management | GV-1.1: policies and accountability | GenAI usage policy roles applied; named business owner and assessor |
| **Govern 2** — risk management roles | GV-2.1: roles and responsibilities defined | §6 assigns owners per control |
| **Map 1** — context established | MP-1.1: business value and intended use documented | §1 system description; §4 use-case context |
| **Map 2** — categorization | MP-2.1: knowledge limits documented | §4 limitations; §2 tier classification |
| **Map 5** — impacts characterized | MP-5.1: impacts to individuals assessed | §4 risk register |
| **Measure 1** — risks identified and assessed | MS-1.1: test and evaluation | §5 evaluation plan; bias and accuracy testing pre-pilot |
| **Measure 2** — bias and fairness | MS-2.x: fairness across groups | Risk R3; disaggregated accuracy testing |
| **Manage 1** — risks prioritized | MG-1.1: response planning | §6 controls; residual risk ratings |
| **Manage 2** — residual risk | MG-2.1: residual risk documented and communicated | §6 residual risk column; stakeholder sign-off §8 |
| **Manage 4** — monitoring | MG-4.1: post-deployment monitoring | §7 monitoring plan |

## 4. Risk register

Likelihood and impact rated Low / Medium / High. Residual risk assumes the
§6 controls are implemented.

| ID | Risk | Likelihood | Impact | Controls (§6) | Residual |
|---|---|---|---|---|---|
| R1 | **Incorrect explanations** teach wrong methods; students internalize errors | High | High | C1 eval suite + human spot-checks; C2 confidence signaling; C3 teacher review of snapshots | Medium |
| R2 | **Student personal data exposure** via prompts/logs or vendor processing | Medium | High | C4 data minimization; C5 DPA + retention limits; C6 access controls | Medium |
| R3 | **Performance disparity** across student groups (e.g., non-native English speakers) | Medium | High | C7 disaggregated testing; C8 escalation if gaps exceed threshold | Medium |
| R4 | **Over-reliance:** students substitute the tutor for learning; reduced teacher contact | Medium | Medium | C9 usage guardrails + teacher dashboards; C10 classroom integration guidance | Low |
| R5 | **Snapshot misinterpretation:** teacher acts on a misleading progress summary | Medium | High | C11 snapshot includes uncertainty notes; C12 teacher training; human-in-the-loop rule for interventions | Medium |
| R6 | **Inappropriate content** (off-topic, biased, or unsafe responses to minors) | Medium | High | C13 content filters + red-teaming; C14 reporting channel for students/teachers | Medium |
| R7 | **Regulatory non-compliance** (EU AI Act high-risk obligations, student-privacy law) | Low | High | C15 documentation package; C16 legal review; C17 transparency disclosures | Low |

## 5. Evaluation plan (pre-pilot gates)

The pilot does **not** start until all gates pass:

1. **Accuracy eval:** curriculum-aligned question bank (illustrative target:
   ≥ 90% correct step-by-step solutions on a held-out set, human-graded).
2. **Fairness eval:** accuracy disaggregated by student group proxies
   (illustrative); investigate any gap above the agreed threshold.
3. **Red-team:** adversarial prompts (jailbreaks, requests for disallowed
   content, attempts to extract other students' data) — methodology per the
   [red-team harness](../red-team-harness/).
4. **Privacy review:** data-flow walkthrough with the district privacy lead;
   confirm minimization and retention settings.
5. **Teacher acceptance:** pilot teachers review snapshots for
   interpretability before student rollout.

## 6. Controls

| ID | Control | Owner (illustrative) | Status |
|---|---|---|---|
| C1 | Pre-pilot accuracy eval suite with human grading; regression suite on each model update | AI Governance Analyst | Planned |
| C2 | Tutor signals uncertainty ("I'm not sure — check with your teacher") instead of guessing | Vendor / integrator | Planned |
| C3 | Teachers review weekly snapshots; no automated intervention decisions | Teaching staff | Planned |
| C4 | Data minimization: collect only prompts, responses, and roster IDs needed for the pilot | Data steward | Planned |
| C5 | Data processing agreement with retention limits and no training on student data without consent | Legal | Planned |
| C6 | Role-based access to logs and snapshots; audit logging enabled | Security | Planned |
| C7 | Disaggregated accuracy testing across student groups | AI Governance Analyst | Planned |
| C8 | Pre-agreed halt threshold if group performance gaps exceed tolerance | Governance committee | Planned |
| C9 | Usage guardrails (session limits) and teacher visibility into student usage | Teaching staff | Planned |
| C10 | Classroom integration guidance so the tutor supplements, not replaces, instruction | Curriculum lead | Planned |
| C11 | Snapshots include data-coverage and uncertainty notes | Vendor / integrator | Planned |
| C12 | Teacher training on interpreting snapshots and AI limitations | Training lead | Planned |
| C13 | Content filters plus pre-pilot red-teaming; blocklist review cadence | Security / analyst | Planned |
| C14 | In-product reporting channel for students and teachers; triage SLA 2 business days | Support lead | Planned |
| C15 | Technical documentation package (system description, eval results, logs) maintained for audit | AI Governance Analyst | Planned |
| C16 | Legal review of EU AI Act high-risk obligations and student-privacy compliance | Legal | Planned |
| C17 | AI disclosure in the tutor interface and parent/student notices | Communications | Planned |

## 7. Monitoring plan (post-pilot)

| Metric | Cadence | Threshold / action (illustrative) |
|---|---|---|
| Solution accuracy on sampled sessions (human-graded) | Monthly | Drop > 5 pp → investigate; > 10 pp → pause and remediate |
| Disaggregated accuracy gap between student groups | Monthly | Gap above tolerance → escalate to governance committee |
| Filter bypass / unsafe-response reports | Continuous; weekly review | Any confirmed incident → incident process; repeat pattern → model/config change |
| Data access anomalies | Continuous | Per security monitoring runbooks |
| Teacher satisfaction / snapshot usefulness survey | Quarterly | Declining trend → review snapshot design and training |
| Regulatory watch | Monthly | Any relevant EU AI Act guidance or state student-privacy change → reassess §2 |

All monitoring results feed a quarterly governance review; material findings
update this assessment (new version, dated).

## 8. Decision and sign-off

**Recommendation (illustrative):** Proceed to a limited pilot (≤ 5
classrooms) **only after** the §5 pre-pilot gates pass and controls C1–C17
are evidenced. Reassess before any expansion.

| Role (illustrative) | Name | Decision | Date |
|---|---|---|---|
| Business owner | | | |
| AI governance analyst | | | |
| Legal / privacy | | | |
| Security | | | |
| Teaching representative | | | |
