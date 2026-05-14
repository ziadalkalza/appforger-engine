# Build FastAPI PostgreSQL Backend

    ## Purpose
    Plan and generate FastAPI + PostgreSQL backend artifacts after backend stack approval.

    ## When to use
    Use this skill only when the current AppForge stage requires this exact workflow. Do not use this skill as a shortcut around approval gates.

    ## Inputs
    - Approved backend decision
- Data model needs
- Auth decision
- Screen/API needs

    ## Outputs
    - Backend architecture
- API routes
- SQLAlchemy models
- Pydantic schemas
- Test plan
- Render/local test deployment checklist

    ## Required context files
    - `BACKEND/fastapi_postgres_profile.md`
- `API_REGISTRY.md`
- `DATA_MODEL_REGISTRY.md`

    ## Rules
    - Read `APPFORGE_PROJECT_STATUS.md`, `DECISION_LOG.md`, `PENDING_QUESTIONS.md`, and all relevant registries before acting.
    - If required information is missing, write it to `PENDING_QUESTIONS.md` or make an explicit assumption in `ASSUMPTION_LOG.md`.
    - Do not invent unsupported stacks, connectors, platforms, or architectures. Use `ENGINE_UPGRADE_PROTOCOL.md` first.
    - Update all affected registries after producing outputs.
    - Prefer small, reviewable changes over large unreviewable rewrites.
    - If a reusable pattern emerges, add it to `REGISTRIES/PENDING_TEMPLATES.md`.

    ## Steps

      1. Define app module structure.
      2. Define database schema and migrations.
      3. Define API routes and error states.
      4. Define auth if required.
      5. Define tests.
      6. Define local and Render testing workflow.
      7. Define DigitalOcean production deployment documentation.
      8. Update registries.


    ## Approval gates
    User approval required before schema freeze or production deployment.

    ## Failure handling
    If cloud credentials/resources are not available, produce manual setup checklist and local run commands.

    ## Handoffs
    - Update the relevant handoff file in `HANDOFFS/` when this skill produces an artifact another agent will consume.
