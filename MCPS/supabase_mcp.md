# Supabase MCP

## Role

Use Supabase MCP for supported Supabase-backed projects.

Possible uses:

- Inspect Supabase project configuration.
- Review schema.
- Assist with migrations.
- Review RLS policies.
- Assist with edge functions.

## Guardrails

- Never expose service role keys in docs.
- Production database changes require approval.
- Destructive migration requires approval.
- RLS policies must be reviewed before app data is considered safe.

## Manual actions

The user may need to:

- Create Supabase project.
- Enable auth providers.
- Copy project URL and anon key into secure environment storage.
- Configure storage buckets.
- Configure redirect URLs.

## Handoff

Update:

- `BACKEND/supabase_profile.md`
- `API_REGISTRY.md`
- `DATA_MODEL_REGISTRY.md`
