# Approve Design Baseline

    ## Purpose
    Convert approved Figma output into a versioned visual source of truth.

    ## When to use
    Use this skill only when the current Appforger stage requires this exact workflow. Do not use this skill as a shortcut around approval gates.

    ## Inputs
    - Figma file/frame links
- Screen specs
- Design asset registry
- User approval

    ## Outputs
    - `DESIGN_BASELINE_V#`
- Updated screen registry
- Implementation-ready design handoff

    ## Required context files
    - `DESIGN_BASELINE_REGISTRY.md`
- `SCREEN_REGISTRY.md`
- `ai-models/codex/docs/handoffs/figma-to-codex.md`

    ## Rules
    - Read `APPFORGER_PROJECT_STATUS.md`, `DECISION_LOG.md`, `PENDING_QUESTIONS.md`, and all relevant registries before acting.
    - If required information is missing, write it to `PENDING_QUESTIONS.md` or make an explicit assumption in `ASSUMPTION_LOG.md`.
    - Do not invent unsupported stacks, connectors, platforms, or architectures. Use `ENGINE_UPGRADE_PROTOCOL.md` first.
    - Update all affected registries after producing outputs.
    - Prefer small, reviewable changes over large unreviewable rewrites.
    - If a reusable pattern emerges, add it to `registries/project-control/pending-templates.md`.

    ## Steps

      1. Confirm user approval.
      2. Assign baseline version.
      3. Record Figma links and covered screens.
      4. Document what visual rules this baseline supersedes.
      5. Define what it does not override: accessibility, security, backend/API, platform constraints.
      6. Update implementation handoff.


    ## Approval gates
    Explicit user approval is required.

    ## Failure handling
    - If the task cannot be completed, document the blocker, affected files, and next safe action in `APPFORGER_PROJECT_STATUS.md` and `PENDING_QUESTIONS.md`.

    ## Handoffs
    - Update the relevant handoff file in `docs/collaboration/handoffs/` when this skill produces an artifact another agent will consume.
