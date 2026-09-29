# Controlled real-model evaluation

This record documents the controlled replacement for a stub-only model demonstration. The offline red-team harness remains useful for testing harness and judge mechanics, but its two built-in targets are explicitly illustrative. The Laya experiment is the real-model evaluation: an open-weight model was run locally and its saved predictions were analyzed independently.

## Environment

- Model: Laya 0.3.20, checkpoint `convaiinnovations/laya`
- Checkpoint SHA-256: `891102d372688fc2a094dac56a384bc537b87c63f21f9f3dac0be2b7cbc8d86c`
- Runtime: Python 3.12.3, `torch 2.14.0`, `transformers 5.17.0`, `safetensors 0.8.0`, `tokenizers 0.23.2`
- Hardware: CPU-only AMD EPYC 9D25; batch size 8 for safety/calibration and 2 for paired bias prompts
- Re-run: `pip install laya numpy` then `python3 laya-governance-experiments/run_experiments.py`; analysis-only replay needs no install: `python3 laya-governance-experiments/analyze.py`

## Prompts, risks, and cost

The safety set contains 60 hand-written prompts: 30 benign and 30 jailbreak attempts across direct override, roleplay, hypothetical, and obfuscation framing. The model only classifies prompts; it is never asked to generate harmful content. The bias probe contains six paired loan, hiring, and insurance scenarios with demographic name cues. The main risks are small convenience samples, prompt-set overfitting, single-language coverage, and false confidence from a single checkpoint and run. The run used local CPU time and no paid API; the exact wall-clock cost is hardware/runtime dependent rather than zero. Downloading the checkpoint is roughly 843 MB.

## Results and what changed

| Measure | Before: keyword baseline | After: Laya | Governance implication |
|---|---:|---:|---|
| Accuracy | 70% | 85% | useful directional improvement, not a benchmark |
| Jailbreak recall | 40% | 70% | still misses 9/30; cannot operate alone |
| Benign precision | 100% | 100% | no observed false positives in this sample |
| Calibration | not available | ECE 0.125 | do not set policy thresholds from mid-band confidence |

The change was methodological as much as numerical: the repo now separates stub mechanics from real-model evidence, records the checkpoint and runtime, keeps the raw result files, reports intervals, and turns the nine missed roleplay/hypothetical attacks into a concrete follow-up test requirement.

This is exploratory evidence only. It is not production validation, professional audit work, or a safety certification. See the full [Laya report](../laya-governance-experiments/report.md).
