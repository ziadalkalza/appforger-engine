# Deployment Rules

## Supabase

Default deployment target is Supabase.

## FastAPI + PostgreSQL

Default testing target:

- Local.
- Render/free cloud.

Default final target:

- DigitalOcean.

## Unsupported deployment

AWS, GCP, Azure, Firebase, Railway, Fly.io, and other targets require engine upgrade before use.

## Production guardrails

- No secrets in Markdown.
- No production destructive migrations without approval.
- Backups must be documented.
- Environment variables must be documented but not exposed.
