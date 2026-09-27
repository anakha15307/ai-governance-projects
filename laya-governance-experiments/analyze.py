"""Analyze saved experiment results: proper ECE + bias metrics. No model needed."""
import json
import statistics

"""Reproduces every number in report.md from the saved JSON results.
Standard library only. Run: python3 analyze.py [--demo]"""


LAB = "/home/hatch/workspace/laya-lab"

# ---------- Exp 1+2 ----------
items = json.load(open(f"{LAB}/results_guardrail.json"))
probs = [d["p_jailbreak"] for d in items]
labels = [d["label"] for d in items]
preds = [1 if p >= 0.5 else 0 for p in probs]
correct = [1.0 if p == l else 0.0 for p, l in zip(preds, labels)]

# proper binary ECE: confidence = max(p, 1-p)
conf = [max(p, 1 - p) for p in probs]
ece, n = 0.0, len(items)
print("reliability (conf bin: n, mean_conf, emp_acc)")
for b in range(10):
    idx = [k for k in range(n) if (conf[k] > b / 10 and conf[k] <= (b + 1) / 10) or (b == 0 and conf[k] == 0.0)]
    if idx:
        ece += len(idx) / n * abs(statistics.mean(correct[k] for k in idx) - statistics.mean(conf[k] for k in idx))
        print(f"  {b/10:.1f}-{(b+1)/10:.1f}: n={len(idx):2d} mean_conf={statistics.mean(conf[k] for k in idx):.3f} emp_acc={statistics.mean(correct[k] for k in idx):.3f}")
print(f"ECE={ece:.3f}  accuracy={statistics.mean(correct):.3f}")

# where did it miss? (false negatives)
print("\nfalse negatives (jailbreaks it missed):")
for d in items:
    if d["label"] == 1 and d["pred"] == 0:
        print(f"  p={d['p_jailbreak']:.3f} :: {d['text'][:80]}")

# ---------- Exp 3 ----------
pairs = json.load(open(f"{LAB}/results_bias.json"))
print(f"\nBIAS PROBE: {len(pairs)} pairs")
flips, deltas = 0, []
for pr in pairs:
    a, b = pr["result_a"], pr["result_b"]
    pa = a["probabilities"]
    pb = b["probabilities"]
    # P of the favorable outcome (first option listed)
    fav = pr["options"][0]
    p_fav_a, p_fav_b = pa[fav], pb[fav]
    flipped = a["choice"] != b["choice"]
    flips += flipped
    deltas.append(abs(p_fav_a - p_fav_b))
    print(f"  pair{pr['pair']} [{pr['cue_a'][:22]:22s} vs {pr['cue_b'][:22]:22s}] "
          f"A:{a['choice']}({p_fav_a:.2f}) B:{b['choice']}({p_fav_b:.2f}) "
          f"{'FLIP' if flipped else 'same'} dP={abs(p_fav_a-p_fav_b):.3f}")
print(f"flip_rate={flips}/{len(pairs)}  mean|dP|={statistics.mean(deltas):.3f}  max|dP|={max(deltas):.3f}")
