# Create UX Flows

    ## Purpose
    Define app journeys, navigation, screen map, and interaction states before visual design.

    ## When to use
    Use this skill only when the current AppForge stage requires this exact workflow. Do not use this skill as a shortcut around approval gates.

    ## Inputs
    - Product brief
- Features
- User roles
- App mode

    ## Outputs
    - UX flow document
- Screen registry draft
- Navigation model
- Edge-case list

    ## Required context files
    - `FEATURE_REGISTRY.md`
- `SCREEN_REGISTRY.md`
- `templates/specs/screen_spec_template.md`

    ## Rules
    - Read `APPFORGE_PROJECT_STATUS.md`, `DECISION_LOG.md`, `PENDING_QUESTIONS.md`, and all relevant registries before acting.
    - If required information is missing, write it to `PENDING_QUESTIONS.md` or make an explicit assumption in `ASSUMPTION_LOG.md`.
    - Do not invent unsupported stacks, connectors, platforms, or architectures. Use `ENGINE_UPGRADE_PROTOCOL.md` first.
    - Update all affected registries after producing outputs.
    - Prefer small, reviewable changes over large unreviewable rewrites.
    - If a reusable pattern emerges, add it to `registries/PENDING_TEMPLATES.md`.

    ## Steps

      1. Identify primary user journeys.
      2. Map screens needed for each journey.
      3. Define navigation model.
      4. Add empty/error/loading/offline states.
      5. Update `SCREEN_REGISTRY.md`.
      6. Prepare input for visual direction and Figma prompts.


    ## Approval gates
    UX flow approval recommended before visual direction.

    ## Failure handling
    - If the task cannot be completed, document the blocker, affected files, and next safe action in `APPFORGE_PROJECT_STATUS.md` and `PENDING_QUESTIONS.md`.

    ## Handoffs
    - Update the relevant handoff file in `docs/collaboration/handoffs/` when this skill produces an artifact another agent will consume.
