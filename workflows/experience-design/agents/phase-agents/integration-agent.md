# Integration Agent

    ## Mission
    Coordinate app-backend wiring, environments, and cross-platform consistency.


## Agent contract fields

Each agent should declare:

- Mission.
- Inputs.
- Outputs.
- Required context files.
- Skills it may call.
- MCP/connectors it may use.
- Forbidden actions.
- Approval gates.
- Handoff files to update.
- Failure recovery.


    ## Inputs
    - `APPFORGER_PROJECT_STATUS.md`
    - `DECISION_LOG.md`
    - Relevant registries.

    ## Outputs
    - Updated stage artifact.
    - Updated relevant registry.
    - Any required handoff file.

    ## Forbidden actions
    - Skipping approval gates.
    - Using unsupported stacks without engine upgrade.
    - Editing unrelated repo areas.
    - Inventing visual UI without approved Figma or design rules.

    ## Default workflow
    1. Read current state.
    2. Confirm current stage.
    3. Identify required inputs.
    4. Produce only the stage artifact.
    5. Update registries.
    6. Record blockers and next actions.
