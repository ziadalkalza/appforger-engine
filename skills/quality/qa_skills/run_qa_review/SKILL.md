# Run QA Review

    ## Purpose
    Plan and execute or document QA checks depending on user preference.

    ## When to use
    Use this skill only when the current AppForge stage requires this exact workflow. Do not use this skill as a shortcut around approval gates.

    ## Inputs
    - Current implementation state
- Test registry
- Platform targets
- Feature/API specs

    ## Outputs
    - QA report
- Defect/change requests
- Updated test registry

    ## Required context files
    - `validation/domains/qa/`
- `TEST_REGISTRY.md`
- `CHANGE_REQUEST_REGISTRY.md`

    ## Rules
    - Read `APPFORGE_PROJECT_STATUS.md`, `DECISION_LOG.md`, `PENDING_QUESTIONS.md`, and all relevant registries before acting.
    - If required information is missing, write it to `PENDING_QUESTIONS.md` or make an explicit assumption in `ASSUMPTION_LOG.md`.
    - Do not invent unsupported stacks, connectors, platforms, or architectures. Use `ENGINE_UPGRADE_PROTOCOL.md` first.
    - Update all affected registries after producing outputs.
    - Prefer small, reviewable changes over large unreviewable rewrites.
    - If a reusable pattern emerges, add it to `registries/PENDING_TEMPLATES.md`.

    ## Steps

      1. Identify test scope.
      2. Separate automatic tests from manual tests.
      3. Run simple error checks by default when possible.
      4. Ask user preference for deeper tests if needed.
      5. Create change requests for failures.
      6. Update test registry.


    ## Approval gates
    User may choose automatic or manual test execution, except simple code error checks should run by default when possible.

    ## Failure handling
    - If the task cannot be completed, document the blocker, affected files, and next safe action in `APPFORGE_PROJECT_STATUS.md` and `PENDING_QUESTIONS.md`.

    ## Handoffs
    - Update the relevant handoff file in `docs/collaboration/handoffs/` when this skill produces an artifact another agent will consume.
