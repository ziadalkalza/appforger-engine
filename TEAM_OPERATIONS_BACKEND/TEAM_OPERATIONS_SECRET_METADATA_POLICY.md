# Secret Metadata Policy

The Team Operations Backend must never store secret values.

Allowed metadata:
- secret name
- environment
- storage location type, e.g. GitHub Actions Secrets, hosting env vars, Supabase config, cloud secret manager
- owner role
- configuration status
- last rotation date if known
- related integration

Forbidden:
- API keys
- tokens
- private keys
- passwords
- service role keys
- webhook signing secrets
