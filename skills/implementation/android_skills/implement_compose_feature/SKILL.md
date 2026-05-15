# Implement Compose Feature

    ## Purpose
    Create a code-agent task for implementing a Kotlin Jetpack Compose feature from approved design and API contracts.

    ## When to use
    Use this skill only when the current AppForge stage requires this exact workflow. Do not use this skill as a shortcut around approval gates.

    ## Inputs
    - Approved Figma baseline
- Screen spec
- API contract
- Android architecture rules

    ## Outputs
    - Compose implementation task
- File plan
- Acceptance checklist
- Test checklist

    ## Required context files
    - `workflows/implementation/native-android/compose_rules.md`
- `workflows/implementation/native-android/android_architecture.md`
- `docs/ai-clients/providers/codex/handoffs/figma_to_codex.md`
- `docs/collaboration/handoffs/backend_to_frontend.md`

    ## Rules
    - Read `APPFORGE_PROJECT_STATUS.md`, `DECISION_LOG.md`, `PENDING_QUESTIONS.md`, and all relevant registries before acting.
    - If required information is missing, write it to `PENDING_QUESTIONS.md` or make an explicit assumption in `ASSUMPTION_LOG.md`.
    - Do not invent unsupported stacks, connectors, platforms, or architectures. Use `ENGINE_UPGRADE_PROTOCOL.md` first.
    - Update all affected registries after producing outputs.
    - Prefer small, reviewable changes over large unreviewable rewrites.
    - If a reusable pattern emerges, add it to `registries/PENDING_TEMPLATES.md`.

    ## Steps

      1. Identify screens/components to implement.
      2. Map Figma components to Compose components.
      3. Map API contract to models/repositories/view models.
      4. Define file changes.
      5. Define accessibility and preview requirements.
      6. Define tests.
      7. Produce a code-agent prompt/task.


    ## Approval gates
    Do not run until design baseline and API contract are approved or explicitly mocked.

    ## Failure handling
    If UI mismatch is found, open UI change request instead of improvising.

    ## Handoffs
    - Update the relevant handoff file in `docs/collaboration/handoffs/` when this skill produces an artifact another agent will consume.
