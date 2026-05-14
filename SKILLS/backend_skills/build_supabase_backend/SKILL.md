# Build Supabase Backend

    ## Purpose
    Plan and generate Supabase backend artifacts after backend stack approval.

    ## When to use
    Use this skill only when the current AppForge stage requires this exact workflow. Do not use this skill as a shortcut around approval gates.

    ## Inputs
    - Approved backend decision
- Data model needs
- Auth decision
- Screen/API needs

    ## Outputs
    - Supabase schema plan
- RLS policy plan
- Edge function plan if needed
- Manual setup checklist
- API contract draft

    ## Required context files
    - `BACKEND/supabase_profile.md`
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

      1. Define tables and relationships.
      2. Define auth behavior if accounts are required.
      3. Define RLS policies.
      4. Define storage buckets if needed.
      5. Define edge functions if custom server logic is needed.
      6. Produce setup checklist for user/manual actions.
      7. Update API and data registries.


    ## Approval gates
    Schema/security approval required before production data use.

    ## Failure handling
    If Supabase project access is unavailable, produce SQL/policy instructions and manual checklist instead of pretending setup was done.

    ## Handoffs
    - Update the relevant handoff file in `HANDOFFS/` when this skill produces an artifact another agent will consume.
