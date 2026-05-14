# Backend Stack Selection

Backend selection happens after UI/UX/Figma direction is clear enough to know what data, auth, storage, and app behavior are needed.

## Supported choices

### Supabase

Best when the app benefits from:

- Managed PostgreSQL.
- Auth.
- Storage.
- Realtime.
- Edge functions for moderate custom logic.
- Fast iteration.

### FastAPI + PostgreSQL

Best when the app needs:

- Custom backend logic.
- Greater control.
- Complex integrations.
- Custom auth/session model.
- Python ecosystem.
- Event processing or advanced services.

## Selection questions

- Does the app need user accounts?
- Does it need roles/permissions?
- Does it need file/media storage?
- Does it need realtime updates?
- Does it need scheduled jobs?
- Does it need custom integrations?
- Does it need complex business logic?
- Does it need admin dashboards?
- What is the expected scale?
- Is the backend mostly CRUD or custom workflows?

## Approval

Record the selected backend in `APPFORGE_PROJECT_STATUS.md` and `DECISION_LOG.md`.
