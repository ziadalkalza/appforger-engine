# Review Automation Risk

## Purpose
Classify the risk of an automation request and determine approvals required.

## Required context
- `AGENTS.md`
- `policies/operations/automation-jobs/`
- `templates/jobs/automation-jobs/`
- `project-control/registries/AUTOMATED_JOB_REGISTRY.md`
- `project-control/registries/JOB_RUN_REGISTRY.md`
- `project-control/APPFORGE_PROJECT.yaml`

## Steps
1. Confirm current automation level and whether the requested action is allowed.
2. Classify risk: low, medium, high, or critical.
3. Identify required approval mode: local, GitHub PR, hybrid, or future server.
4. Load only the task-specific context needed.
5. Create or use a job definition.
6. Execute only allowed actions, or produce a packet/template if execution is not allowed.
7. Record outputs, warnings, and evidence.
8. Update or propose updates to the relevant registries.
9. Stop at approval gates.

## Forbidden
- Do not silently approve baselines, releases, integrations, or package additions.
- Do not read secrets or index forbidden files.
- Do not push, merge, deploy, or publish without approval.

## Output
- Job definition, job run record, report, failure record, or approval request as appropriate.
