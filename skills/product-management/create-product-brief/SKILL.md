# Create Product Brief

    ## Purpose
    Convert a raw app idea into a reusable product brief that drives UX, backend, design, and native development.

    ## When to use
    Use this skill only when the current Appforger stage requires this exact workflow. Do not use this skill as a shortcut around approval gates.

    ## Inputs
    - Raw idea
- Target users
- Business constraints
- Platform goals
- Any references

    ## Outputs
    - Product brief
- MVP scope
- Non-goals
- Success criteria
- Initial feature registry entries

    ## Required context files
    - `APPFORGER_PROJECT_STATUS.md`
- `templates/specifications/product-brief-template.md`
- `registries/project-control/feature-registry.md`

    ## Rules
    - Read `APPFORGER_PROJECT_STATUS.md`, `DECISION_LOG.md`, `PENDING_QUESTIONS.md`, and all relevant registries before acting.
    - If required information is missing, write it to `PENDING_QUESTIONS.md` or make an explicit assumption in `ASSUMPTION_LOG.md`.
    - Do not invent unsupported stacks, connectors, platforms, or architectures. Use `ENGINE_UPGRADE_PROTOCOL.md` first.
    - Update all affected registries after producing outputs.
    - Prefer small, reviewable changes over large unreviewable rewrites.
    - If a reusable pattern emerges, add it to `registries/project-control/pending-templates.md`.

    ## Steps

      1. Read current project state.
      2. Ask only blocking questions; otherwise make reversible assumptions.
      3. Define target users, problem, value, MVP, non-goals, and risks.
      4. Create initial feature candidates.
      5. Update `FEATURE_REGISTRY.md`.
      6. Save reusable wording or prompt patterns to `PENDING_TEMPLATES.md`.


    ## Approval gates
    User approval required before app mode selection.

    ## Failure handling
    - If the task cannot be completed, document the blocker, affected files, and next safe action in `APPFORGER_PROJECT_STATUS.md` and `PENDING_QUESTIONS.md`.

    ## Handoffs
    - Update the relevant handoff file in `docs/collaboration/handoffs/` when this skill produces an artifact another agent will consume.
