# Khanmigo: Governance Risk Assessment

**System:** Khanmigo, Khan Academy's AI tutor and teaching assistant
**Assessment type:** Pre-adoption / third-party AI risk assessment (illustrative)
**Date:** September 2026
**Status:** Illustrative educational work sample, not legal advice, not an official audit of Khan Academy

> Every factual claim in this document is drawn from publicly available
> sources, cited in [SOURCES.md](./SOURCES.md). Vendor marketing claims are
> reported as vendor-stated and flagged for verification against a signed
> Data Privacy Agreement (DPA) before any real deployment decision.

---

## 1. System description (from public sources)

**What it is.** Khanmigo is an AI-powered tutoring and teaching assistant
built by Khan Academy in partnership with OpenAI, using GPT-4-class model
technology. It is integrated into Khan Academy's content library and
available within Khan Academy and (per third-party reporting) LMS
environments such as Canvas.

**Two user modes:**

- **Student tutor**: Socratic-style guided tutoring: the tool is explicitly
  designed to withhold final answers and respond with guiding questions,
  hints, and prompts so the student works through problems themselves. Modes
  include math/science/humanities/coding tutoring, a Writing Coach (feedback
  on drafts without rewriting the work), debate exercises, and conversation
  with historical or literary figures within bounded scenarios.
- **Teacher assistant**: lesson-plan drafts, learning objectives, discussion
  prompts, rubric generation, exit tickets, multiple-choice assessments,
  report-card comments, letters of recommendation, IEP progress-note
  drafting, class newsletters, "refresh my knowledge" summaries, and a
  teacher dashboard showing student activity including transcripts of
  student-AI conversations.

**Parents** can activate and manage child accounts (required for under-18
access), review conversation history, and receive moderation alerts.
**Districts** can arrange rostering, SSO, and support under separately
quoted district licensing.

**Users.** Elementary through college learners; K-12 teachers; parents;
school/district administrators.

**Pricing (publicly reported).** Teacher tools free; individual/family plans
$4/month or $44/year; district licensing quoted separately.

**Data and privacy posture (vendor-stated, verify via DPA):**
- Khan Academy states that no student or teacher data is used to train AI
  models, and that information sent to OpenAI is anonymized.
- Built-in moderation flags problematic content (self-harm, harmful
  language) and notifies connected adults; teachers can monitor student
  usage and parents can view conversation history.
- Caveat reported by third parties: student conversations pass through
  OpenAI's servers, and a "Khanmigo Lite" tier reportedly sends messages to
  OpenAI which may use them to improve models: the exact tier and retention
  terms could not be verified from primary sources (see §8).

**Publicly documented limitations and criticism:**
- Hallucination is publicly acknowledged by Khan Academy leadership as one
  of the biggest ongoing challenges; reporting notes there is no systematic
  "uncertainty signal" telling a child when the AI is guessing.
- A 2023-era Tennessee randomized controlled trial (RCT), covered by
  education press, found the Khanmigo tutor added no measurable math gains
  beyond Khan Academy alone, with low student engagement (passive "IDK"
  interactions).
- Published commentary (e.g., Dan Meyer) argues efficacy evidence is weak
  and that chatbot tutors cannot replicate human-tutor relational dynamics;
  an OER Project guide notes content-integration errors (responses drawing
  on data beyond Khan Academy content), task-execution failures, and prompt
  fragility.
- The teacher-tools tier was made free in the US through a Microsoft
  partnership (Azure-backed infrastructure).

---

## 2. EU AI Act tier classification (illustrative)

**Result: High-Risk (education), plus transparency obligations.**

**Reasoning:**

1. **Not prohibited.** Khanmigo does not fall under any Article 5
   prohibited practice (no social scoring, no manipulative subliminal
   techniques targeting vulnerable groups as a design objective, no
   biometric identification in scope of this assessment).
2. **High-risk candidate: Annex III, point 3 (education and vocational
   training).** Annex III lists as high-risk AI systems intended to
   (a) determine access/admission to education, **(b) evaluate learning
   outcomes**, (c) assess the appropriate level of education for an
   individual, or (d) monitor and detect prohibited behaviour during tests.
   Khanmigo's core function is tutoring students and *assessing their work*
, judging correctness, giving feedback on writing and code, and guiding
   progression. That is closest to **evaluating learning outcomes**,
   Annex III(3)(b). The presence of minors as the primary user group
   strengthens the case for the high-risk track in a conservative
   assessment.
3. **Transparency obligations (Article 50)** apply in any case: students,
   parents, and teachers must be informed they are interacting with an AI
   system rather than a human, and AI-generated content (lesson materials,
   feedback) should be identifiable as such.

**Consequence of the illustrative classification:** a deploying district or
institution would need risk management, data governance, technical
documentation, record-keeping (logs), transparency to users, human
oversight, and accuracy/robustness measures: the controls in §6 are
drafted against those expectations.

*This classification is an analyst's illustrative judgment based on public
information, not legal advice. Confirm with qualified counsel and the
vendor's own conformity documentation.*

---

## 3. NIST AI RMF mapping

| RMF function | How it applies to Khanmigo (this assessment) |
|---|---|
| **GOVERN** | Roles and accountability for the adoption decision (§6 controls with owners); AI-use policy alignment (acceptable-use rules for students and teachers); oversight of the vendor relationship (DPA, sub-processor review); culture of human oversight, teacher remains the accountable educator. |
| **MAP** | Context established in §1 (users, data flows, deployment modes); risk categorization in §2; impact analysis for minors (§4 risks R1, R5); human-AI teaming defined (tutor assists, teacher decides; AI drafts, teacher reviews). |
| **MEASURE** | Pre-pilot gates: accuracy sampling on curriculum-aligned tasks, red-team probes for harmful-content bypass, bias checks across demographic proxies, engagement/efficacy review (see §5); ongoing metrics in §7. |
| **MANAGE** | Risk responses in §4-§6 (mitigate, monitor, accept-with-conditions); incident and escalation paths (§7); decommissioning/exit plan, data deletion and student-data return on contract end (verify via DPA). |

---

## 4. Risk register

Likelihood (L) and Impact (I) rated Low / Medium / High. Residual risk is
post-control.

| # | Risk | L | I | Key controls (§6) | Residual |
|---|---|---|---|---|---|
| R1 | **Hallucination to minors**: confident wrong explanations or facts delivered to K-12 students building foundational knowledge; no systematic uncertainty signaling. | M-H | H | C1, C6, C7 | M |
| R2 | **Academic-integrity erosion**: students steer the tutor toward direct answers; Writing Coach output submitted as own work. | M | M | C1, C9, C10 | M |
| R3 | **Student-data exposure via third party**: conversations transit OpenAI servers; retention/training-use terms tier-dependent and unverified; COPPA/FERPA obligations attach to the district. | L-M | H | C3, C4, C11 | M |
| R4 | **Biased or uneven feedback**: quality of tutoring varies across subjects, dialects, or disability-related needs; developmental-stage adaptation undocumented. | M | M | C7, C12 | M |
| R5 | **Harmful content / self-harm disclosure**: minor discloses self-harm or encounters harmful content; moderation exists but bypass is possible. | L | Critical | C5, C10 | M |
| R6 | **Teacher over-reliance**: unreviewed AI-generated lesson plans, rubrics, or IEP notes containing errors reach students/parents. | M | M | C1, C10 | L-M |
| R7 | **Equity gap**: paid learner tier ($4/mo) disadvantages low-income families; district licensing uneven across districts. | M | M | C8 | M |
| R8 | **Vendor/sub-processor dependency**: model, infrastructure, or terms change (Microsoft/OpenAI partnership evolution); service continuity and data-portability risk. | L | M | C4, C13 | L |

---

## 5. Pre-pilot evaluation gates

The pilot does not start until all gates pass:

1. **Accuracy sampling**, 200+ curriculum-aligned prompts graded by
   subject teachers; hallucination/error rate recorded per subject.
2. **Safety red-teaming**: adversarial probes for harmful-content,
   self-harm, and cheating-assistance bypasses; moderation-flag rate
   measured.
3. **Bias spot-checks**: feedback quality compared across grade bands
   and, where feasible, demographic proxies.
4. **Privacy review**: DPA signed; data-flow map (Khan Academy → OpenAI)
   confirmed; retention and training-use terms verified in writing.
5. **Teacher acceptance**: pilot teachers review AI-generated materials
   and confirm the review workload is sustainable.

---

## 6. Controls with owners

| # | Control | Owner |
|---|---|---|
| C1 | **Human-in-the-loop review**: teachers review all AI-generated lesson materials, rubrics, and IEP notes before student/parent use; students taught to verify AI explanations. | Classroom teacher |
| C2 | **AI-interaction disclosure**: students, parents, teachers informed they are interacting with AI (Art. 50-style transparency), in onboarding and in-product. | District communications / vendor |
| C3 | **Data minimization & no-PII rule**: no student names, IEP details, or photos in prompts; de-identified practice data only. | District IT + teachers |
| C4 | **Signed DPA & sub-processor review**: executed agreement covering FERPA/COPPA, retention, no-training-use, breach notification; OpenAI sub-processing terms verified. | District legal / procurement |
| C5 | **Moderation alert workflow**: flagged self-harm/harmful-content alerts routed to counselor/admin within defined SLA; response procedure documented and drilled. | School counselor / admin |
| C6 | **Uncertainty routine**: classroom norm: when unsure, students/ teachers "verify together" against Khan Academy source material; no systematic uncertainty label is assumed. | Teacher |
| C7 | **Periodic accuracy sampling**: quarterly sampling of tutor explanations by subject leads; results logged and trended. | Governance analyst |
| C8 | **Equity provision**: district-funded access for students unable to pay the learner tier; usage monitored for access gaps. | District leadership |
| C9 | **Academic-integrity policy**: written rules on acceptable Khanmigo use for assignments; Writing Coach boundaries communicated to students and parents. | School administration |
| C10 | **Training & awareness**: teacher PD on AI literacy, prompt review, and moderation-alert response before rollout. | District PD coordinator |
| C11 | **Tier verification**: confirm which product tier (full vs. Lite) is deployed and its exact data-use terms before go-live; re-verify on contract renewal. | Governance analyst / IT |
| C12 | **Fairness review**: annual review of feedback quality across grade bands and student groups; findings fed back to vendor. | Governance analyst |
| C13 | **Exit plan**: contract terms for data deletion/return and service continuity if the vendor or partnership changes. | District legal / procurement |

---

## 7. Monitoring plan

| Metric | Cadence | Threshold / trigger | Escalation |
|---|---|---|---|
| Hallucination/error incidents (teacher-reported) | Monthly | >2% of sampled sessions | Pause rollout in affected subject → vendor ticket → C7 deep-dive |
| Moderation flags (self-harm, harmful content) | Real-time alerts; weekly rollup | Any self-harm disclosure | C5 workflow; counselor notified same day |
| Teacher override rate on AI-generated materials | Monthly | >30% of materials substantially rewritten | Review prompt/workflow design; retrain (C10) |
| Student engagement (passive "IDK" rate) | Monthly | Rising trend 2 quarters | Reassess efficacy; consider discontinuing tutor mode |
| Data-subject/parent complaints | Quarterly | Any verified complaint | Legal review; DPA compliance check |
| Vendor terms / sub-processor changes | On notice + annual | Any material change | C4 re-review before continued use |

**Recommendation:** conditional pilot, limited to volunteer classrooms,
all §5 gates passed, controls C1-C13 assigned, 90-day review before wider
rollout. Discontinue or renegotiate if efficacy or safety thresholds fail.

---

## 8. Limitations and unverified claims

- **Data retention and training-use terms** for each Khanmigo tier
  (full vs. Lite) could not be verified from primary sources; vendor
  marketing claims must be confirmed in a signed DPA.
- **"Redesigned for summer 2026"** reports about the teacher-tools
  experience are unconfirmed; verify against current product
  documentation.
- **Efficacy evidence** is mixed and publicly contested; this assessment
  takes no position beyond reporting the published RCT and commentary.
- No security incidents specific to Khanmigo were found in public
  sources during this research; absence of public incidents is not
  evidence of absence.
- EU AI Act analysis is illustrative and simplified; confirm with
  qualified legal counsel.
