# Backend Stack Selection

Backend selection happens after product, UX, and design direction are clear enough to know what data, auth, storage, and app behavior are needed.

## Supported profile types

- Backend app profiles, such as managed backend platforms.
- Backend stack profiles, such as framework plus database combinations.

Use the selected profile under `workflows/implementation/backend/apps/` or `workflows/implementation/backend/stacks/` for provider-specific details.

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
