# AI Incident Runbook

Per Playbook Chapter 11. Pre-delegate containment authority, do not convene
a committee while harm continues.

Program: [Organization]. Version: [v1.0]. Date: [YYYY-MM-DD]
Owner: [Program owner]

## Severity levels

| Level | Definition | Response lead | Declare-to-contain target |
|---|---|---|---|
| SEV-4 | Near-miss, caught by controls | Analyst | 5 business days (review) |
| SEV-3 | Limited real impact | Use-case owner + analyst | 1 business day |
| SEV-2 | Significant impact or pattern | Program owner | 4 hours |
| SEV-1 | Severe harm / legal / regulatory / press | Executive sponsor + legal | 1 hour |

When in doubt, escalate one level.

## Response steps

### 1. Detect & declare

- Anyone may declare a suspected AI incident to: [channel / contact]
- Coordinator confirms severity within: [4 hours / 1 hour SEV-1]
- Log in incident register: [location]

### 2. Contain

- Pre-delegated containment authority: [Name/role, may pause use case immediately]
- Containment options: [pause use case / roll back version / disable feature / revoke access]
- Preserve logs and evidence: [what to snapshot, where]

### 3. Assess

- Scope: [who affected, for how long, what data involved]
- Technical cause: [ ]
- Governance cause: [which controls failed or were missing. P/D/C language]

### 4. Notify

| Audience | Trigger | Owner | SLA |
|---|---|---|---|
| Internal leadership | SEV-2+ | [Name] | [e.g., 24h] |
| Affected individuals | [per obligation] | [Name] | [per obligation] |
| Regulator | [per obligation: know your clocks in advance] | Legal | [per obligation] |
| Vendor | [if vendor-caused] | [Name] | [per contract SLA] |

### 5. Remediate

- Technical fix: [owner, due]
- Governance fix (control gap): [owner, due]

### 6. Learn

- Post-incident review within 10 business days: [owner]
- Filed: [location], fed into training: [date]

## Contacts

| Role | Name | Contact | After-hours |
|---|---|---|---|
| Coordinator | [ ] | [ ] | [ ] |
| Program owner | [ ] | [ ] | [ ] |
| Legal | [ ] | [ ] | [ ] |
| Security | [ ] | [ ] | [ ] |

## Tabletop schedule

- [ ] Annual tabletop completed: [date], scenario: [description], gaps found: [ ]
- Next tabletop due: [YYYY-MM-DD]
