# Supabase Context Profile

Supabase can act as a context backend with:

- Postgres for structured state
- Supabase Storage for artifacts
- pgvector for optional vector memory
- RLS for future team/security rules

## Stronger Profile Rules

Supabase may support SQL state, storage metadata, and pgvector retrieval. Use Supabase for context only after indexing scope, security, and cost are approved. Do not treat pgvector retrieval as canonical truth.
