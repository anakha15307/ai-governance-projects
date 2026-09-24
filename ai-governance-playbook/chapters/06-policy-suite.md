# Chapter 6: Policy Suite

**Purpose:** Give people clear, enforceable rules for everyday AI use —
acceptable use, procurement, and data handling — so governance isn't only
something that happens in assessments.

**When to use it:** Draft early (policies govern Tier 1 uses that never get
assessed); review annually or after incidents.

## Procedure

### 1. Write the three core policies

**a) Acceptable-use policy** — what anyone in the organization may and may
not do with AI tools. Must cover: approved vs. unapproved tools; data that
may never go into AI tools (customer PII, credentials, trade secrets —
enumerate, don't wave at "sensitive data"); required human review before
external outputs; disclosure rules (when AI assistance must be declared);
consequences and the exception process.

**b) Procurement policy** — no AI capability is bought without governance
involvement. Must cover: mandatory intake (Chapter 2) before purchase or
pilot; minimum vendor evidence (Chapter 12); contract terms that must be
present (data use limits, audit rights, change notification); who can sign
off by tier.

**c) Data-handling rules for AI** — how data flows into and out of AI
systems. Must cover: data classification mapped to AI use (what can be used
for training vs. inference vs. never); retention and deletion; cross-border
considerations; logging of AI data access.

### 2. Make each policy enforceable

A policy needs: a named owner, an effective date, who it applies to, the
exception process (Chapter 5, control G-3), and a review date. Policies
without owners become folklore.

### 3. Roll out in this order

1. Publish with a one-page summary — nobody reads the full text first.
2. Train the affected roles (Chapter 14) — policy without training is a trap.
3. Enable the technical guardrails that make compliance easy (approved tool
   lists, DLP rules, SSO).
4. Start monitoring compliance (Chapter 10) — measure before you punish.

### 4. Handle exceptions properly

Exception requests use a standard form: what rule, why, for how long, what
compensating control, who approves. Time-limit every exception (90 days
default) — permanent exceptions are policy rewrites wearing a disguise.

## Worked mini-example (illustrative)

*Meridian Logistics* publishes its acceptable-use policy after the Relay
pilot is discovered. Key rules: only approved AI tools (listed in the
inventory); no customer PII in public AI tools; all customer-facing AI
drafts require human approval before sending; AI-assisted hiring decisions
prohibited without Tier-4 assessment. The sales team gets a 90-day exception
to keep using Relay while completing retroactive intake — with the
compensating control that every draft is agent-reviewed. The exception's
expiry forces the assessment to actually finish.

## Common pitfalls

- **Policy as PDF on an intranet.** If people can't find it in 30 seconds,
  it doesn't exist.
- **Banning everything.** A policy nobody can follow produces shadow AI.
  Regulate the risky uses; bless the safe ones explicitly.
- **No exception path.** Without one, exceptions happen anyway — invisibly.
- **Writing policy before understanding use.** Inventory first (Chapter 2),
  then write rules for what's actually happening.

## Templates

- Exception requests: see this repo's
  [`genai-usage-policy/`](../../genai-usage-policy/) exception template.

## Repo tooling

- [`genai-usage-policy/`](../../genai-usage-policy/) — complete GenAI
  acceptable-use policy + exception request template implementing this chapter.
