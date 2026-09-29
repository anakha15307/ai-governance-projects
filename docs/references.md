# References

Citations for the legal, regulatory, and technical claims made in this repo.
I cite the official sources and link to them where a stable public URL
exists.

## Frameworks and standards

- National Institute of Standards and Technology (NIST). *Artificial
  Intelligence Risk Management Framework (AI RMF 1.0).* January 2023.
  The four functions (Govern, Map, Measure, Manage) structure the
  crosswalk in `docs/framework-crosswalk.md`.
  https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- International Organization for Standardization. *ISO/IEC 42001:2023,
  Information technology: Artificial intelligence: Management system.*
  December 2023. Referenced for the management-system clauses mapped in
  the crosswalk.
- European Parliament and Council. *Regulation (EU) 2024/1689 laying down
  harmonised rules on artificial intelligence (Artificial Intelligence
  Act).* Official Journal of the EU, July 2024. Risk tiers (Art. 5, 6, 50;
  Annex III), transparency duties (Art. 50), serious-incident reporting
  (Art. 73), and high-risk documentation duties (Annex IV).
  https://eur-lex.europa.eu/eli/reg/2024/1689/oj

## Privacy law (referenced in assessments, not legal advice)

- *Children's Online Privacy Protection Act (COPPA),* 15 U.S.C. sections
  6501-6506. Referenced in the edtech and Khanmigo assessments for
  under-13 data rules.
- *Family Educational Rights and Privacy Act (FERPA),* 20 U.S.C. section
  1232g. Referenced for student education records.

## Methods

- Confidence intervals in the Laya report use the Wilson score interval for
  binomial proportions and a percentile bootstrap (2,000 resamples) for
  calibration error. Both are standard; the report gives the exact numbers
  and the reproduction commands.
- The bias-audit and red-team methods follow the standard practice of
  paired probes and adversarial prompt suites against a target model; the
  innovation here is the packaging for governance review, not the method.

## Project sources

- Laya model: the open-source decision model used in project 16; model
  hash and package versions are recorded in the Laya report.
- AI incident deconstructions (project 14): each deconstruction lists its
  public sources in `ai-incident-deconstructions/SOURCES.md`.
- Khanmigo assessment (project 13): every claim is drawn from public
  sources cited in `khanmigo-risk-assessment/SOURCES.md`.
