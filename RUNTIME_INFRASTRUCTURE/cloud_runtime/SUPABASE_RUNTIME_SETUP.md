# Supabase Runtime Setup

Supabase can provide Postgres and optionally pgvector for context storage.

Required references:
- `SUPABASE_URL`
- `SUPABASE_SERVICE_ROLE_KEY` or a scoped service token for setup only
- `POSTGRES_URL` if direct SQL setup is used

The service-role key is high-risk and must not be committed, indexed, or stored in `project-control`.
