# Backend Repo Agent Instructions

This is a backend implementation repository controlled by Appforger.

## Required context

Before making backend changes, read:

- `APPFORGER_POINTER.md`
- Appforger `APPFORGER_PROJECT_STATUS.md`
- Appforger `DECISION_LOG.md`
- Appforger `workflows/experience-design/backend/generic/backend-stack-selection.md`
- Appforger `registries/project-control/api-registry.md`
- Appforger `registries/project-control/data-model-registry.md`
- Appforger `skills/implementation/backend/*/SKILL.md` relevant to this task

## Backend rules

- Do not invent unsupported backend stacks.
- If the requested backend stack is not approved in Appforger, run the engine upgrade protocol first.
- Keep API contracts synchronized with implementation.
- Do not hardcode secrets.
- Prefer environment variables and documented `.env.example` files.
- Run simple code/import/lint/error checks by default when possible.
- If a change affects frontend integration, mark it in Appforger `CHANGE_REQUEST_REGISTRY.md` and `API_REGISTRY.md`.

## After work

Report or update:

- API changes.
- Data model changes.
- Migration changes.
- Test results.
- Manual actions required.
