# Create Visual Direction

    ## Purpose
    Create visual direction options and asset needs before Figma production.

    ## When to use
    Use this skill only when the current AppForge stage requires this exact workflow. Do not use this skill as a shortcut around approval gates.

    ## Inputs
    - Product brief
- UX flows
- User references
- Project-specific design rules if any

    ## Outputs
    - Visual direction options
- Asset inventory
- Image generation prompts
- Figma guidance

    ## Required context files
    - `DESIGN/global_design_system.md`
- `DESIGN/project_design_override_rules.md`
- `DESIGN_ASSET_REGISTRY.md`

    ## Rules
    - Read `APPFORGE_PROJECT_STATUS.md`, `DECISION_LOG.md`, `PENDING_QUESTIONS.md`, and all relevant registries before acting.
    - If required information is missing, write it to `PENDING_QUESTIONS.md` or make an explicit assumption in `ASSUMPTION_LOG.md`.
    - Do not invent unsupported stacks, connectors, platforms, or architectures. Use `ENGINE_UPGRADE_PROTOCOL.md` first.
    - Update all affected registries after producing outputs.
    - Prefer small, reviewable changes over large unreviewable rewrites.
    - If a reusable pattern emerges, add it to `REGISTRIES/PENDING_TEMPLATES.md`.

    ## Steps

      1. Read product and UX sources.
      2. Generate 2-4 visual direction options.
      3. Identify logos, icons, illustrations, animations, empty states, and screenshots needed.
      4. Write image-generation prompts if needed.
      5. Define what must be reviewed before Figma import.


    ## Approval gates
    User approval required before treating any visual direction as final.

    ## Failure handling
    - If the task cannot be completed, document the blocker, affected files, and next safe action in `APPFORGE_PROJECT_STATUS.md` and `PENDING_QUESTIONS.md`.

    ## Handoffs
    - Update the relevant handoff file in `HANDOFFS/` when this skill produces an artifact another agent will consume.
