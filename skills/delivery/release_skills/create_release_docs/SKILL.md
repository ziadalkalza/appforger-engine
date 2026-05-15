# Create Release Documentation

    ## Purpose
    Prepare release documentation and checklists without automating App Store or Play Store submission.

    ## When to use
    Use this skill only when the current AppForge stage requires this exact workflow. Do not use this skill as a shortcut around approval gates.

    ## Inputs
    - QA status
- Platform targets
- Build notes
- Privacy/permissions
- App assets

    ## Outputs
    - Release checklist
- Store metadata draft
- Privacy checklist
- Production readiness report

    ## Required context files
    - `workflows/delivery/release-docs/`
- `RELEASE_REGISTRY.md`

    ## Rules
    - Read `APPFORGE_PROJECT_STATUS.md`, `DECISION_LOG.md`, `PENDING_QUESTIONS.md`, and all relevant registries before acting.
    - If required information is missing, write it to `PENDING_QUESTIONS.md` or make an explicit assumption in `ASSUMPTION_LOG.md`.
    - Do not invent unsupported stacks, connectors, platforms, or architectures. Use `ENGINE_UPGRADE_PROTOCOL.md` first.
    - Update all affected registries after producing outputs.
    - Prefer small, reviewable changes over large unreviewable rewrites.
    - If a reusable pattern emerges, add it to `registries/PENDING_TEMPLATES.md`.

    ## Steps

      1. Check QA status.
      2. Collect app metadata, screenshots, icons, permissions, privacy notes.
      3. Create iOS and/or Android release checklist.
      4. Document manual store steps.
      5. Update release registry.


    ## Approval gates
    User approval required before submission. AppForge v1 documents release but does not automate submission.

    ## Failure handling
    - If the task cannot be completed, document the blocker, affected files, and next safe action in `APPFORGE_PROJECT_STATUS.md` and `PENDING_QUESTIONS.md`.

    ## Handoffs
    - Update the relevant handoff file in `docs/collaboration/handoffs/` when this skill produces an artifact another agent will consume.
