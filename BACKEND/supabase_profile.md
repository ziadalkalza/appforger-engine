# Supabase Profile

## Scope

Supabase can act as:

- Full backend replacement.
- Database/auth/storage provider.
- Backend foundation with edge functions.

The exact role depends on project needs.

## Required decisions

- Auth required: yes/no.
- Auth providers.
- Tables.
- RLS policies.
- Storage buckets.
- Edge functions.
- Realtime needs.
- Local vs cloud development.

## Manual setup checklist

- Create Supabase project.
- Store project URL securely.
- Store anon key securely.
- Configure auth providers.
- Configure redirect URLs.
- Create tables/migrations.
- Create RLS policies.
- Create storage buckets.
- Configure edge functions if needed.

## Security

- Never expose service role key in client apps.
- RLS must be enabled where user-owned data exists.
- Production schema changes require approval.
