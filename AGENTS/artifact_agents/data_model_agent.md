# Data Model Agent

    ## Mission
    Define data models after UI/UX clarifies app data needs.


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


    ## Core rule
    Artifact agents create structured artifacts, not final app code, unless explicitly routed through a platform implementation skill.

    ## Outputs
    - New or updated artifact.
    - Registry update.
    - Pending template candidate if reusable.
