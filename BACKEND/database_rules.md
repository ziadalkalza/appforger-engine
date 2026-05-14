# Database Rules

## General

- Database design follows product and UI data needs.
- Do not create tables before product requirements and major UX flows are clear.
- Do not use destructive migrations without approval.
- Keep data model registry updated.

## Supabase

- Use RLS for user-owned/private data.
- Keep service role keys server-only.
- Document policies.

## FastAPI + PostgreSQL

- Use migrations.
- Avoid schema drift.
- Keep models/schemas/migrations aligned.
- Include test data and seed strategy when useful.

## Registry

Update `DATA_MODEL_REGISTRY.md` for each model/table.
