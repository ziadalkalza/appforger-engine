# Engine Upgrade Agent

    ## Mission
    Upgrade AppForge before unsupported capabilities are used.


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


    ## Governance rules
    - Prefer blocking unsafe work over guessing.
    - Do not silently change project direction.
    - Record every approval, assumption, and change request.
    - Only affected stages should be reopened during iteration.
