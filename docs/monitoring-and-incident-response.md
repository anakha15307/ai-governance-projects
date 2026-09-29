# Monitoring and incident response: proposed procedures

These are proposed procedures, written as templates a governance team would
adapt. They describe what a monitoring and incident program should do, using
this repo's tooling where it fits. Nothing here is a running production
system.

## Proposed monitoring plan

Adapted from
[`ai-governance-playbook/templates/monitoring-plan.md`](../ai-governance-playbook/templates/monitoring-plan.md)
and [`ai-governance-playbook/chapters/10-monitoring.md`](../ai-governance-playbook/chapters/10-monitoring.md).

**What to monitor, and how often:**

1. **Output screening (continuous).** Route model outputs through the policy
   monitor ([`policy-violation-monitor/`](../policy-violation-monitor/)). Track
   the block rate and escalation rate weekly; a sudden change means something
   shifted upstream.
2. **Control compliance (monthly).** Rebuild the governance dashboard
   ([`governance-dashboard/`](../governance-dashboard/)) from the current
   risk register. Review overdue actions at the monthly committee meeting.
3. **Model behavior (quarterly).** Re-run the bias audit suite
   ([`bias-audit-suite/`](../bias-audit-suite/)) and the red-team harness
   ([`red-team-harness/`](../red-team-harness/)) against the deployed model
   or its replacement. Compare against the recorded baseline; the Laya
   project's monitoring section shows what a regression plan looks like.
4. **Regulatory change (monthly).** Publish the regulatory brief
   ([`regulatory-tracker/`](../regulatory-tracker/)) and check whether new
   rules change any system's tier or obligations.

**Who owns it:** each system has a named owner in the registry; the
governance analyst runs the monthly cycle; the committee reviews exceptions.

## Incident reporting

Anyone, staff, teacher, parent, or user, can report a suspected AI incident
to the governance analyst. The report should include: what happened, when,
which system, who was affected, and any screenshots or outputs. Reports go
into the incident log the same day they arrive.

Severity guide:

- **Sev 1 (critical):** harm to a person, legal or regulatory exposure, data
  breach, or widespread wrong outputs. Respond within hours.
- **Sev 2 (major):** a control failed but harm was contained, or a pattern of
  concerning outputs. Respond within one business day.
- **Sev 3 (minor):** a single odd output with no harm. Log and review in the
  weekly queue.

## Escalation

1. **Analyst triage (same day).** Confirm the report, assign severity, and
   pull the relevant audit log entries and registry records.
2. **Containment.** For Sev 1 and Sev 2: pause the affected use case first,
   investigate second. A paused pilot is embarrassing; a running harmful
   system is worse.
3. **Committee review (within 48 hours for Sev 1/2).** The analyst presents
   findings using the incident runbook template. The committee decides:
   resume, resume with new controls, or retire the use case.
4. **External reporting.** If the incident meets a regulatory threshold (for
   example, the EU AI Act's serious-incident reporting duties for high-risk
   systems), legal is looped in and the filing clock starts. The analyst
   does not file alone.
5. **Deconstruction.** After resolution, write it up the way project 14
   does: what failed technically, what failed organizationally, which
   controls were missing, and what changes as a result.

## Rollback

Every approved deployment keeps a rollback plan on file before launch:

- **What "previous good state" means** for that system (prior model version,
  prior prompt, or manual process fallback), recorded in the model registry.
- **Who can order a rollback:** the system owner or the governance lead, no
  committee vote required in an emergency. The decision is documented after.
- **How long it takes:** the plan states a target (for example, disable the
  integration within one hour) and it is tested at least once before launch.
- **Communication:** affected users and stakeholders are told what happened,
  what changed, and when service resumes. No silent rollbacks.

## What is proposed vs what exists

What exists in this repo: the monitoring tooling (policy monitor, dashboard,
audit and red-team harnesses), the templates (monitoring plan, incident
runbook, decision record), and the worked examples. What is proposed: the
cadence, the ownership, the severity SLAs, and the rollback testing. Those
only become real inside an organization. I wrote them as procedures so the
thinking is visible, not to suggest they are running anywhere.
