# Implement SwiftUI Feature

    ## Purpose
    Create a code-agent task for implementing a SwiftUI feature from approved design and API contracts.

    ## When to use
    Use this skill only when the current Appforger stage requires this exact workflow. Do not use this skill as a shortcut around approval gates.

    ## Inputs
    - Approved Figma baseline
- Screen spec
- API contract
- iOS architecture rules

    ## Outputs
    - SwiftUI implementation task
- File plan
- Acceptance checklist
- Test checklist

    ## Required context files
    - `workflows/experience-design/native-ios/swiftui-rules.md`
- `workflows/backend-implementation/native-ios/ios-architecture.md`
- `ai-models/codex/docs/handoffs/figma-to-codex.md`
- `docs/collaboration/handoffs/backend-to-frontend.md`

    ## Rules
    - Read `APPFORGER_PROJECT_STATUS.md`, `DECISION_LOG.md`, `PENDING_QUESTIONS.md`, and all relevant registries before acting.
    - If required information is missing, write it to `PENDING_QUESTIONS.md` or make an explicit assumption in `ASSUMPTION_LOG.md`.
    - Do not invent unsupported stacks, connectors, platforms, or architectures. Use `ENGINE_UPGRADE_PROTOCOL.md` first.
    - Update all affected registries after producing outputs.
    - Prefer small, reviewable changes over large unreviewable rewrites.
    - If a reusable pattern emerges, add it to `registries/project-control/pending-templates.md`.

    ## Steps

      1. Identify screens/components to implement.
      2. Map Figma components to SwiftUI components.
      3. Map API contract to models/services/view models.
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
