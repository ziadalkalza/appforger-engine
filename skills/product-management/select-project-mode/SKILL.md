# Select Project Mode

    ## Purpose
    Choose how the app will be developed: generic spec-first, iOS first, Android first, or parallel native.

    ## When to use
    Use this skill only when the current Appforger stage requires this exact workflow. Do not use this skill as a shortcut around approval gates.

    ## Inputs
    - Product brief
- Launch goals
- Platform requirements
- Team constraints

    ## Outputs
    - Selected mode recorded in `APPFORGER_PROJECT_STATUS.md`
- Decision entry
- Mode-specific next steps

    ## Required context files
    - `docs/project-onboarding/start-here/project-creation-modes.md`
- `APPFORGER_PROJECT_STATUS.md`
- `DECISION_LOG.md`

    ## Rules
    - Read `APPFORGER_PROJECT_STATUS.md`, `DECISION_LOG.md`, `PENDING_QUESTIONS.md`, and all relevant registries before acting.
    - If required information is missing, write it to `PENDING_QUESTIONS.md` or make an explicit assumption in `ASSUMPTION_LOG.md`.
    - Do not invent unsupported stacks, connectors, platforms, or architectures. Use `ENGINE_UPGRADE_PROTOCOL.md` first.
    - Update all affected registries after producing outputs.
    - Prefer small, reviewable changes over large unreviewable rewrites.
    - If a reusable pattern emerges, add it to `registries/project-control/pending-templates.md`.

    ## Steps

      1. Compare app goals against the four supported modes.
      2. Recommend a mode with tradeoffs.
      3. Confirm whether iOS, Android, or both are targeted.
      4. Record final decision after approval.
      5. Update repo expectations.


    ## Approval gates
    User approval required before UX/UI work is locked.

    ## Failure handling
    - If the task cannot be completed, document the blocker, affected files, and next safe action in `APPFORGER_PROJECT_STATUS.md` and `PENDING_QUESTIONS.md`.

    ## Handoffs
    - Update the relevant handoff file in `docs/collaboration/handoffs/` when this skill produces an artifact another agent will consume.
