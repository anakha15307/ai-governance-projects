# Deconstruction 01: Air Canada chatbot: held liable for its own AI's misrepresentation

**Incident:** AI Incident Database Incident 639 - "Air Canada Chatbot Reportedly Provides
Inaccurate Bereavement Fare Information, Leading to Customer Overpayment"
**Decision:** *Moffatt v. Air Canada*, 2024 BCCRT 149 (British Columbia Civil Resolution
Tribunal, 14 February 2024)
**Analyst note:** Independent analysis from public reporting and the published tribunal
decision. Not legal advice.

---

## What happened: timeline

| Date | Event |
|---|---|
| Nov 2022 | On the day his grandmother died, Jake Moffatt visited Air Canada's website to book a Vancouver → Toronto flight and asked the site's chatbot to explain the airline's bereavement fare policy. |
| Nov 2022 | The chatbot replied that bereavement fares could be claimed retroactively: *"If you need to travel immediately or have already travelled and would like to submit your ticket for a reduced bereavement rate, kindly do so within 90 days of the date your ticket was issued by completing our Ticket Refund Application form."* The response included a link to the airline's actual bereavement policy page, which stated the opposite: no refunds for bereavement travel after booking. |
| Nov 2022 | Relying on the chatbot, Moffatt booked at full fare (one-way tickets reported at CA$794.98 and CA$845.38). He also spoke to an Air Canada representative who confirmed a bereavement discount would apply (roughly $380 round trip) but did not say it could not be claimed retroactively. |
| Nov 2022 - 2023 | Moffatt submitted a refund claim with his grandmother's death certificate, well within the 90-day window. Air Canada refused. The airline offered a $200 future-travel coupon and said it would update the chatbot. Moffatt refused the coupon. |
| 2023 | Moffatt filed a claim with the BC Civil Resolution Tribunal. |
| 14 Feb 2024 | Tribunal member Christopher Rivers held Air Canada liable for **negligent misrepresentation** and awarded **CA$812.02** (CA$650.88 damages + CA$36.14 pre-judgment interest + CA$125 tribunal fees). |

Air Canada's defense included the argument that the chatbot was *"a separate legal entity
that is responsible for its own actions"*: a submission Rivers described as
"remarkable." The tribunal rejected it outright:

> "It should be obvious to Air Canada that it is responsible for all the information on
> its website. It makes no difference whether the information comes from a static page
> or a chatbot.". Christopher Rivers, 2024 BCCRT 149

The American Bar Association called the decision "a helpful reminder that companies
remain liable for the actions of their AI tools." (Sources: AIID Incident 639 reports;
CanLII 2024 BCCRT 149; BBC, 23 Feb 2024; ABA Business Law Today, Feb 2024.)

---

## Root cause analysis

### Technical cause
The chatbot generated a fluent, confident answer about fare policy that contradicted the
airline's own published policy: a hallucination (or stale grounding) presented with no
uncertainty signal. The response even linked to the correct policy page while stating the
opposite of what it said, which suggests the generation layer was not constrained by, or
checked against, the retrieved source. The underlying model and vendor were not publicly
disclosed: the tribunal decision does not name them, and this analysis does not
speculate.

### Governance cause
The deeper failure is organizational, not algorithmic:

1. **No accountability for AI output.** The "separate legal entity" defense is the
   clearest possible evidence that nobody inside Air Canada owned the chatbot's
   statements. If legal's position is that the bot speaks for no one, then no one was
   governing it.
2. **Consequential use without commensurate assurance.** The chatbot was authorized to
   answer questions that create financial commitments (fare eligibility, refund rights)
, a high-consequence use case: with apparently the same (or no) validation applied
   to low-stakes FAQs.
3. **No contradiction testing.** The bot's answer and the linked policy page disagreed
   with each other. Any pre-deployment evaluation set built from the airline's own
   policy pages would have caught this on day one.
4. **Reactive remediation only.** The error persisted for months (the interaction was
   November 2022; the airline promised to "update the chatbot" only after the dispute
   escalated). There is no public evidence of monitoring that would have caught the
   wrong answer before a customer relied on it.

---

## Controls that failed or were missing

| Control | Type | Status |
|---|---|---|
| Ground answers in authoritative policy sources; flag or refuse when no source supports the answer | Preventive | **Missing/failed**: answer contradicted the linked source |
| Pre-deployment evaluation set covering fare-policy Q&A, including adversarial and edge-case variants | Preventive | **Missing**: no evidence any policy-accuracy testing existed |
| Human escalation path for fare/refund disputes ("this answer affects money, confirm with an agent") | Preventive | **Missing** |
| Monitoring of chatbot answers for policy contradictions or customer complaints about wrong information | Detective | **Missing**: the failure surfaced via a tribunal filing, not internal monitoring |
| Defined owner accountable for chatbot output accuracy | Preventive (governance) | **Missing**: evidenced by the "separate legal entity" defense |
| Incident response / correction workflow when wrong information is reported | Corrective | **Failed**: months of dispute, $200 coupon offered instead of correction |

---

## What a competent AI governance program would have done differently

| # | Recommendation | Owner |
|---|---|---|
| 1 | Classify customer-facing Q&A by consequence: fare eligibility, refunds, and rebooking rules are **high-consequence** and require grounded answers with source citations, not free generation. | AI Governance + Product |
| 2 | Build a policy-accuracy evaluation set from the airline's own fare pages; run it before every release and re-run on any model, prompt, or retrieval change. Include contradiction tests (bot answer vs. linked source). | AI Governance |
| 3 | Add a confidence/escalation rule: when the bot cannot ground a fare answer in a current policy source, it must say so and route to a human agent, never invent the policy. | Product / Engineering |
| 4 | Name a single accountable owner for chatbot output accuracy, with a documented review cadence. Legal signs off on the accountability statement before deployment, never after a tribunal does. | AI Governance + Legal |
| 5 | Monitor production conversations for policy-related answers; sample and review weekly; track complaint tags about wrong information as a KPI. | Customer Operations |
| 6 | Define the incident workflow in advance: wrong-information report → verify against source → correct the answer → notify affected customers → retest. A $200 coupon is not an incident response. | Customer Operations + AI Governance |

---

## NIST AI RMF mapping: where it failed

| Function | Failure |
|---|---|
| **GOVERN** | No accountability structure for the chatbot's outputs. The legal defense itself demonstrates the governance gap: the organization had not decided who was responsible for what the AI said. |
| **MAP** | The context of use was never properly mapped: a chatbot answering fare/refund questions operates in a financially consequential context, but was apparently treated as a generic FAQ widget. |
| **MEASURE** | No measurement of answer accuracy against authoritative policy sources, the core risk (misinformation about fares) was never tested. |
| **MANAGE** | No monitoring, no incident response, no remediation until external legal action forced it. Residual risk was unmanaged for months. |

---

## Key sources

- AI Incident Database, Incident 639: reports 3673, 3674, 3731, 3968, 6091
  (https://incidentdatabase.ai/reports/6091/ and linked reports)
- *Moffatt v. Air Canada*, 2024 BCCRT 149 (CanLII:
  https://www.canlii.org/en/bc/bccrt/doc/2024/2024bccrt149/2024bccrt149.html)
- BBC, "Airline held liable for its chatbot giving passenger bad advice," 23 Feb 2024
  (https://www.bbc.com - "what this means for travellers")
- American Bar Association, Business Law Today, "BC Tribunal Confirms Companies Remain
  Liable for Information Provided by AI Chatbot," Feb 2024
  (https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/)
- Washington Post reporting on the dispute (via AIID report 3673)

**Could not verify:** the model vendor or architecture behind Air Canada's chatbot, 
neither the tribunal decision nor reputable reporting names it, so this deconstruction
does not speculate. Exact date of the November 2022 chatbot interaction (day) is not
stated in the sources reviewed; AIID lists the incident date as 2022-11-11.
