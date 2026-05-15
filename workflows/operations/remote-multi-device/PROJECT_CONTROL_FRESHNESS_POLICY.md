# Project-Control Freshness Policy

## Purpose

Project-control is the shared app memory. It must not drift behind implementation repos, Figma, or backend runtime state.

## Freshness checks

Before starting a task, compare the task requirements to:

- latest `APPFORGE_PROJECT_STATUS.md`,
- latest relevant baseline,
- repo commit/branch recorded in `REPO_REGISTRY.md`,
- recent done reports,
- open change requests.

## Staleness warning examples

```text
Backend repo has a newer commit than the backend baseline.
API contract changed in PR but API_REGISTRY.md was not updated.
Figma baseline was superseded but frontend packet points to old baseline.
Project-control has unmerged changes in GitHub.
```

## Action if stale

1. Pause dependent implementation.
2. Create/import a freshness report.
3. Update the relevant registry/baseline or mark as intentionally unchanged.
4. Re-run external workspace validation.
5. Continue only after state is consistent.

## Freshness report template

```yaml
freshness_report_id: FRESH-001
checked_at:
checked_by:
component: backend | ios | android | web | figma | project-control
local_ref:
remote_ref:
project_control_ref:
status: fresh | stale | unknown
required_action:
```
