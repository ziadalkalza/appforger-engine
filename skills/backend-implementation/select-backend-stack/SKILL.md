# Select Backend Stack

    ## Purpose
    Choose Supabase or FastAPI + PostgreSQL after UI/UX/design direction clarifies backend needs.

    ## When to use
    Use this skill only when the current Appforger stage requires this exact workflow. Do not use this skill as a shortcut around approval gates.

    ## Inputs
    - Product brief
- UX flows
- Approved/draft Figma
- Data needs
- Auth decision

    ## Outputs
    - Backend stack decision
- Backend implementation plan
- Manual action checklist

    ## Required context files
    - `workflows/experience-design/backend/generic/backend-stack-selection.md`
- `STACK_REGISTRY.md`
- `DECISION_LOG.md`

    ## Rules
    - Read `APPFORGER_PROJECT_STATUS.md`, `DECISION_LOG.md`, `PENDING_QUESTIONS.md`, and all relevant registries before acting.
    - If required information is missing, write it to `PENDING_QUESTIONS.md` or make an explicit assumption in `ASSUMPTION_LOG.md`.
    - Do not invent unsupported stacks, connectors, platforms, or architectures. Use `ENGINE_UPGRADE_PROTOCOL.md` first.
    - Update all affected registries after producing outputs.
    - Prefer small, reviewable changes over large unreviewable rewrites.
    - If a reusable pattern emerges, add it to `registries/project-control/pending-templates.md`.

    ## Steps

      1. Determine whether the app needs auth, storage, realtime, edge functions, custom logic, or admin tools.
      2. Compare Supabase vs FastAPI + PostgreSQL.
      3. Recommend one stack.
      4. Record decision after approval.
      5. Create manual setup checklist.


    ## Approval gates
    User approval required before backend implementation.

    ## Failure handling
    - If the task cannot be completed, document the blocker, affected files, and next safe action in `APPFORGER_PROJECT_STATUS.md` and `PENDING_QUESTIONS.md`.

    ## Handoffs
    - Update the relevant handoff file in `docs/collaboration/handoffs/` when this skill produces an artifact another agent will consume.
