# Backend Repo Agent Instructions

This is a backend implementation repository controlled by AppForge.

## Required context

Before making backend changes, read:

- `APPFORGE_POINTER.md`
- AppForge `APPFORGE_PROJECT_STATUS.md`
- AppForge `DECISION_LOG.md`
- AppForge `workflows/implementation/backend/generic/backend_stack_selection.md`
- AppForge `registries/API_REGISTRY.md`
- AppForge `registries/DATA_MODEL_REGISTRY.md`
- AppForge `skills/implementation/backend/*/SKILL.md` relevant to this task

## Backend rules

- Do not invent unsupported backend stacks.
- If the requested backend stack is not approved in AppForge, run the engine upgrade protocol first.
- Keep API contracts synchronized with implementation.
- Do not hardcode secrets.
- Prefer environment variables and documented `.env.example` files.
- Run simple code/import/lint/error checks by default when possible.
- If a change affects frontend integration, mark it in AppForge `CHANGE_REQUEST_REGISTRY.md` and `API_REGISTRY.md`.

## After work

Report or update:

- API changes.
- Data model changes.
- Migration changes.
- Test results.
- Manual actions required.
