# Existing Project Import Questionnaire

Use this flow when the user says the project already exists or is running.

Required:

1. Where is project-control, if any?
2. Where are existing repos? backend, iOS, Android, web.
3. Which repo/branch is current source of truth?
4. Does existing design/Figma exist?
5. Does existing backend/API exist?
6. Are there existing docs? Where?
7. Is the app already released?
8. What should AppForge avoid changing?
9. Should AppForge run an import/gap analysis before generating new work?

Existing projects should default to import/gap-analysis before implementation.

## Mandatory ongoing project question

Ask this immediately after confirming whether the project is new or existing:

```text
Q2A. Is this an ongoing project?
```

Allowed answers:

1. `yes_active_project` - active/ongoing project with existing code, docs, design, or releases.
2. `no_new_project` - new project from scratch.
3. `no_snapshot_or_archived_project` - old/snapshot project imported as a fixed baseline.
4. `mixed_or_not_sure` - unclear or mixed.

If the project is ongoing, AppForge must register available code sources and run initial code context bootstrap before code-aware implementation.

Planning may continue before bootstrap, but implementation, refactoring, release, API contract changes, migrations, auth/security changes, CI/CD edits, and repo write operations are blocked until code context is bootstrapped, refreshed, or explicitly scoped as unavailable.
