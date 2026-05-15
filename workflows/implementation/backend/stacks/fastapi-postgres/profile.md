# FastAPI + PostgreSQL Profile

## Scope

Use FastAPI + PostgreSQL when custom backend logic is required.

## Default architecture

```text
backend/
  app/
    main.py
    core/
    api/
    models/
    schemas/
    services/
    repositories/
    db/
    tests/
  alembic/
  pyproject.toml or requirements.txt
```

## Testing deployment

- Local first when possible.
- Render/free cloud for test deployment.
- DigitalOcean for final deployment documentation.

## Required decisions

- Auth required: yes/no.
- Database hosting.
- Migration tool.
- Environment handling.
- API versioning.
- Error model.
- Logging.
- Background jobs if needed.

## Manual setup checklist

- Create repo.
- Create local `.env`.
- Create PostgreSQL database.
- Create Render test service if needed.
- Create DigitalOcean droplet/app platform for final deployment.
- Configure secrets in hosting provider.
