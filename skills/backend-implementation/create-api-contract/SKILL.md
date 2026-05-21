# Create API Contract

    ## Purpose
    Turn backend design into a frontend-consumable API contract.

    ## When to use
    Use this skill only when the current Appforger stage requires this exact workflow. Do not use this skill as a shortcut around approval gates.

    ## Inputs
    - Backend plan/code
- Screen specs
- Data models
- Auth decision

    ## Outputs
    - API contract
- Error model
- Loading/empty/error state mapping
- Frontend integration notes

    ## Required context files
    - `templates/specifications/api-contract-template.md`
- `API_REGISTRY.md`
- `docs/collaboration/handoffs/backend-to-frontend.md`

    ## Rules
    - Read `APPFORGER_PROJECT_STATUS.md`, `DECISION_LOG.md`, `PENDING_QUESTIONS.md`, and all relevant registries before acting.
    - If required information is missing, write it to `PENDING_QUESTIONS.md` or make an explicit assumption in `ASSUMPTION_LOG.md`.
    - Do not invent unsupported stacks, connectors, platforms, or architectures. Use `ENGINE_UPGRADE_PROTOCOL.md` first.
    - Update all affected registries after producing outputs.
    - Prefer small, reviewable changes over large unreviewable rewrites.
    - If a reusable pattern emerges, add it to `registries/project-control/pending-templates.md`.

    ## Steps

      1. Define endpoints/functions.
      2. Define request/response schemas.
      3. Define auth requirements.
      4. Define error codes and app-facing messages.
      5. Map APIs to screens/features.
      6. Update API registry.


    ## Approval gates
    Explicit approval required before native frontend implementation unless using a clearly marked mock strategy.

    ## Failure handling
    - If the task cannot be completed, document the blocker, affected files, and next safe action in `APPFORGER_PROJECT_STATUS.md` and `PENDING_QUESTIONS.md`.

    ## Handoffs
    - Update the relevant handoff file in `docs/collaboration/handoffs/` when this skill produces an artifact another agent will consume.
