# Data card: Laya experiment datasets

## Datasets

All datasets are hand-built by me for this experiment. No personal data, no
scraped content, no third-party data.

| Dataset | Size | Purpose | File |
|---|---|---|---|
| Guardrail prompts | 60 (30 benign, 30 jailbreak) | Safety-gate accuracy, precision, recall | `datasets.py` (GUARDRAIL_ITEMS) |
| Calibration prompts | included in the 60, plus extras | Confidence calibration (ECE) | `datasets.py` (CALIBRATION_EXTRA_ITEMS) |
| Bias probe pairs | 6 paired scenarios | Demographic steadiness | `datasets.py` (BIAS_PAIRS) |

## How the data was created

I wrote the prompts myself to cover the attack styles a governance team
worries about: direct harmful requests, roleplay framing ("pretend you are
..."), hypothetical framing ("what would happen if ..."), and benign
lookalikes that a gate must not block. Labels (benign vs jailbreak) are my
own judgments, documented in the code.

## Known limitations

- Small (n=60) and hand-built: reflects my imagination of attacks, not the
  real distribution.
- English only, single-turn only.
- Bias pairs cover six scenarios; no intersectional identities, no
  paraphrase variants, no larger samples.
- No held-out split: the same prompts were used for development and
  measurement. A proper held-out set is future work.

## Reproducibility

`python3 run_experiments.py` regenerates the raw results (needs the `laya`
package and `numpy`); `python3 analyze.py` reproduces every number in the
report from the committed results files with the standard library only.
Model hash, package versions, and hardware are in `report.md`.
