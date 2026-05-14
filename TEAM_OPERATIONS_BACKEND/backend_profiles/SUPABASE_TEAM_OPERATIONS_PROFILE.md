# Supabase Team Operations Profile

Use Supabase when you want a hosted Postgres database, authentication support, RLS policies, and a built-in dashboard.

Recommended for small-to-medium teams that want less infrastructure work.

Setup includes:
1. Create Supabase project.
2. Run `supabase_team_operations_schema.sql`.
3. Review starter RLS policies.
4. Configure allowed roles.
5. Add connection metadata to project-control.
6. Run validation.

Secrets: store Supabase service credentials in deployment/CI secrets, never in AppForge files or operations tables.
