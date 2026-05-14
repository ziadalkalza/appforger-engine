# CI/CD Secrets Manifest

Do not store secret values here. Store only the expected secret names and where they should be configured.

| Environment | Provider | Secret Name | Required For | Owner Role | Status |
|---|---|---|---|---|---|
| staging | GitHub Actions | DATABASE_URL | backend deploy/tests | admin | not_configured |
| production | GitHub Actions | JWT_SECRET | backend runtime | admin | not_configured |
