# Threat model: Laya safety gate experiment

This threat model covers the experiment as run, and sketches what would
change if a gate like this were ever deployed. It is an analyst exercise,
not a security review.

## Scope

The experiment: a decision model classifies prompts as benign or jailbreak
attempts. There is no deployment, no users, and no adversary beyond my own
test prompts.

## Threats tested

| Threat | How it was tested | Result |
|---|---|---|
| Direct harmful requests | 30 jailbreak prompts incl. direct asks | Caught |
| Roleplay framing ("pretend you are...") | Prompts in the jailbreak set | 9 of 30 jailbreaks missed; all misses used roleplay or hypothetical framing |
| Hypothetical framing ("what if...") | Prompts in the jailbreak set | Same as above |
| Demographic skew in judgments | 6 paired bias scenarios | Zero decision flips, <1% probability shift |
| Overconfidence | Calibration measurement (ECE 0.125) | 92% correct on calls made at 90%+ confidence; error concentrated in mid-confidence band |

## Threats NOT tested

Multi-turn attacks, prompt injection via tool outputs, multilingual
jailbreaks, paraphrase variants of blocked prompts, adversarial suffixes,
model extraction, data poisoning of the gate itself, and denial-of-service
via expensive prompts.

## If this were deployed, the threat model would also need

- **Adversarial adaptation:** attackers iterate against the gate; a static
  60-prompt test says nothing about round two.
- **Gate bypass paths:** any path that skips the gate (direct model access,
  cached responses) voids the whole control.
- **Confidence misuse:** downstream systems must not treat the gate's
  confidence as a safety guarantee; calibration was measured on 60 prompts.
- **Monitoring and rollback:** per `docs/monitoring-and-incident-response.md`,
  block-rate drift alarms and a tested rollback to manual review.

## Residual risk

Even at 85% measured accuracy, a gate that misses 30% of jailbreaks in
testing cannot be a sole control. Defense in depth (human review, output
monitoring, access controls) is not optional.
