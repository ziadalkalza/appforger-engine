# Managed Postgres Setup

Required reference:
- `POSTGRES_URL`

Appforger uses Postgres for live operational state:
- users, roles, permissions
- tasks, approvals, handoffs
- agent runs, sync runs, bootstrap status
- runtime health events
- optional graph tables

Actual project documents, source code, and secret values do not live in the Appforger operational database.
