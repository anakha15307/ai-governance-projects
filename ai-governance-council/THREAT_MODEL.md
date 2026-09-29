# Threat model: AI Governance Council experiment

An analyst exercise on what could go wrong with a multi-model oversight
setup like this one, and what the experiment did and did not test.

## Scope

The experiment only: three LLM seats voting on synthetic cases. No
deployment, no real determinations, no users.

## Threats observed or tested

| Threat | What happened | Implication |
|---|---|---|
| Seat unreliability | Ling failed 8 of 16 calls plus all 8 repairs (40 straight empty responses on repairs) | A council is only as reliable as its least reliable seat; quorum rules matter |
| Rate limiting | Gemini returned one 429 mid-experiment | Retries and backoff are part of the design, not an afterthought |
| Uninformative confidence | 0.943 correct vs 0.940 wrong | Confidence-weighted tie-breaks can be noise; the tie-break sank case 7 |
| Deliberation capture | 1 vote changed across 5 deliberations | Deliberation barely moved votes here; a stronger seat could dominate a weaker one |
| Ambiguous ground truth | Case 7 legally debatable | The "correct" answer in oversight is sometimes genuinely contestable |

## Threats NOT tested

Collusion or correlated failures between seats (all three share similar
training data), prompt injection into case descriptions, a seat gaming the
voting procedure, adversarial case wording designed to split the council,
and long-horizon drift in seat behavior.

## If this were a real oversight body, it would also need

- **Seat diversity requirements:** independent providers, and ideally
  different model families, to reduce correlated failure.
- **Quorum and fallback rules:** what happens when a seat is down (the
  experiment's repair script is a start, not a policy).
- **Human tie-break:** a person, not a confidence score, resolves
  high-stakes disagreements.
- **Audit of the council itself:** every vote, justification, and failure
  logged immutably (the experiment's `results.json` is the prototype of
  this).
- **The monitoring and rollback procedures** in
  `docs/monitoring-and-incident-response.md`.

## Residual risk

Even at 87.5% on 8 cases, an LLM council is an advisory input, not a
decision-maker. The experiment's own findings argue against trusting it
further than that.
