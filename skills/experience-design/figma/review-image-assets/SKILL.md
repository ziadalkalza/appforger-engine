# Review Image Assets

    ## Purpose
    Review generated or third-party visual assets before importing them into Figma or app repos.

    ## When to use
    Use this skill only when the current Appforger stage requires this exact workflow. Do not use this skill as a shortcut around approval gates.

    ## Inputs
    - Asset images/files
- Intended usage
- Visual direction
- Brand rules

    ## Outputs
    - Approved/rejected asset list
- Required revisions
- Asset registry update

    ## Required context files
    - `DESIGN_ASSET_REGISTRY.md`
- `workflows/experience-design/design-workflow/image-generation-review-workflow.md`

    ## Rules
    - Read `APPFORGER_PROJECT_STATUS.md`, `DECISION_LOG.md`, `PENDING_QUESTIONS.md`, and all relevant registries before acting.
    - If required information is missing, write it to `PENDING_QUESTIONS.md` or make an explicit assumption in `ASSUMPTION_LOG.md`.
    - Do not invent unsupported stacks, connectors, platforms, or architectures. Use `ENGINE_UPGRADE_PROTOCOL.md` first.
    - Update all affected registries after producing outputs.
    - Prefer small, reviewable changes over large unreviewable rewrites.
    - If a reusable pattern emerges, add it to `registries/project-control/pending-templates.md`.

    ## Steps

      1. Compare asset to intended purpose.
      2. Check style consistency.
      3. Check platform/app usage constraints.
      4. Mark asset approved, rejected, or needs revision.
      5. Update design asset registry.


    ## Approval gates
    User approval required before importing final brand-critical assets.

    ## Failure handling
    - If the task cannot be completed, document the blocker, affected files, and next safe action in `APPFORGER_PROJECT_STATUS.md` and `PENDING_QUESTIONS.md`.

    ## Handoffs
    - Update the relevant handoff file in `docs/collaboration/handoffs/` when this skill produces an artifact another agent will consume.
