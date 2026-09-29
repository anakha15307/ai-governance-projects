# Assumptions and limitations

This page states what I assume, what I know is limited, and what this repo
is and is not for. I would rather under-claim than over-claim.

## Who I am, and what this repo is

I am a teacher transitioning into AI governance. These are independent
portfolio projects I started in May 2026, built with AI coding assistance,
to learn the work and show how I think. I hold the IAPP AIGP certification
(2026). I have not worked as an AI governance professional, auditor, or
consultant, and nothing here should be read as professional experience.

## Assumptions

- Readers have a general technical background but may be new to AI
  governance; docs explain terms as they go.
- Sample data, stub models, and fictional scenarios are clearly marked where
  they appear. Anything not marked fictional should be treated as
  illustrative unless its sources are cited.
- The EU AI Act analysis throughout is an educational simplification of the
  regulation's risk tiers. It is not legal advice.
- Cost and effort estimates in templates (for example, the playbook) are
  illustrative, not benchmarks.

## Limitations

- **Small, hand-built test sets.** The Laya experiments use 60 prompts I
  wrote; the council experiment uses 8 synthetic cases. Confidence intervals
  are reported, but small samples still limit what can be concluded. The
  Laya report says explicitly that nothing in it is evidence of production
  readiness.
- **Stub models and targets.** The bias audit suite and red-team harness run
  against deterministic stub models, not real LLMs. They demonstrate the
  method, not a finding about any real model. Both READMEs explain how to
  plug in a real endpoint.
- **Rules baseline tuned on its own test set.** The Laya keyword baseline was
  tuned on the same 60 prompts it was measured on, which flatters it. The
  report says so.
- **Free-tier API flakiness.** The council experiment's reliability findings
  are about free tiers in September 2026, not about the models themselves.
- **Bias testing is narrow.** Probes cover a small set of identities and
  prompt framings. They do not cover intersectional groups, paraphrase
  robustness, multilingual inputs, or larger samples. Expanding them is
  listed as future work, not done work.
- **Adversarial testing is narrow.** The red-team harness covers 26 attacks
  in 4 categories against stub targets. It does not cover prompt injection
  chains, indirect attacks, multi-turn attacks, or multilingual jailbreaks.
- **No held-out test sets.** Evaluation projects re-use their development
  prompts for measurement. A proper held-out set is future work.
- **No independent validation.** No project here has been reviewed, audited,
  or validated by anyone but me. Claims like "audit-ready" do not appear in
  this repo for that reason.

## Intended use

- Learning AI governance: reading the code, running the demos, adapting the
  templates.
- Job applications: showing how I approach risk assessment, evaluation,
  policy drafting, and incident analysis.
- Starting points: teams can adapt the intake form, rubrics, checklists, and
  runbooks to their own context.

## Prohibited use

- Do not use the EU AI Act classifier or the council cases as legal advice
  or as a compliance determination for a real system.
- Do not deploy the policy monitor, model registry, or dashboard as
  production controls without real security review, testing, and ownership.
- Do not present any project as audited, certified, or validated work.
- Do not submit real personal data to any demo or example; all fixtures are
  synthetic.
