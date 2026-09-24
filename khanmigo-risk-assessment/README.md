# Khanmigo — Governance Risk Assessment

An audit-ready, pre-adoption risk assessment of **Khanmigo** (Khan Academy's
AI tutor and teaching assistant) as an educational AI use case — with EU AI
Act tier classification, NIST AI RMF mapping, a risk register, controls with
owners, and a monitoring plan. All claims are drawn from public sources
(cited in [SOURCES.md](./SOURCES.md)); the assessment is illustrative and
educational, not legal advice and not an official audit of Khan Academy.

## Problem

K-12 AI tools combine three hard governance problems: the users are minors,
the system influences learning outcomes, and regulators treat educational AI
as high-risk. A governance analyst must be able to take a real, publicly
documented product, scope it from public information, classify it under the
EU AI Act, map it to NIST AI RMF, and produce a defensible risk register
with controls and monitoring — before a district signs, not after an
incident. Khanmigo is the canonical case: widely adopted, well documented,
non-profit, and still carrying the core risks (hallucination to children,
third-party data flows, contested efficacy evidence).

## Users / Stakeholders

- **AI governance analyst** — authors and maintains the assessment.
- **School/district leadership** — accountable for the adopt / pilot /
  decline decision.
- **Teachers** — need to understand the tool's limits, the review burden,
  and the alert workflow.
- **Parents** — need to understand what data is collected, who sees
  conversations, and how to consent.
- **Legal, privacy, security, procurement** — review DPA, COPPA/FERPA,
  SSO/rostering, and sub-processor terms.
- **Auditors / regulators** — read the assessment as evidence of a risk
  management process.

## Methods

- **Public-source scoping** ([ASSESSMENT.md §1](./ASSESSMENT.md)):
  product modes (student tutor, teacher assistant, parent, district),
  pricing, data/privacy posture, and documented limitations assembled from
  reviews, guides, and press — no vendor access, no invented facts.
- **EU AI Act tiering** (§2): prohibited → high-risk → transparency
  analysis with reasoning recorded. Illustrative result: **High-Risk**
  (Annex III education — evaluation of learning outcomes), plus Article 50
  transparency obligations for the conversational interface.
- **NIST AI RMF mapping** (§3): Govern / Map / Measure / Manage traced to
  assessment sections, so the document doubles as framework evidence.
- **Risk register** (§4): eight risks with likelihood, impact, mapped
  controls, and residual risk — including hallucination to minors,
  third-party data flows, self-harm disclosure handling, and equity.
- **Pre-pilot evaluation gates** (§5): accuracy sampling, safety
  red-teaming, bias spot-checks, privacy/DPA review, teacher acceptance —
  the pilot does not start until all pass.
- **Monitoring plan** (§7): metrics, cadence, thresholds, and escalation
  paths, including an efficacy off-ramp if engagement or learning gains
  fail.

## Results

- A complete assessment artifact
  ([ASSESSMENT.md](./ASSESSMENT.md)): 8 risks, 13 controls with named
  role-owners, residual-risk ratings, and a **conditional pilot**
  recommendation (limited classrooms, all gates passed, 90-day review).
- Demonstrates third-party AI assessment from public sources only — the
  exact skill districts and edtech employers need when no vendor
  cooperation exists.
- [SOURCES.md](./SOURCES.md) records every source with quality notes
  (secondary vs. commentary vs. vendor-stated), modeling defensible
  sourcing discipline.

## Risks and Controls

The assessment itself is a risk artifact, so this section covers the
*meta*-risks of the work:

- **Source risk** — secondary review sites may be outdated; mitigated by
  source-quality notes and "verify via DPA" flags on vendor claims.
- **Classification risk** — the EU AI Act analysis is illustrative; the
  document states plainly it is not legal advice.
- **Staleness risk** — the product is reportedly being redesigned;
  reassess before any real adoption decision.

## Next Steps

- Verify data-retention and training-use terms per tier against a signed
  DPA (see §8 unverified claims).
- Re-run the §5 gates against the current product version before piloting.
- Reuse the §2–§8 structure as a template for any education AI vendor
  assessment.
