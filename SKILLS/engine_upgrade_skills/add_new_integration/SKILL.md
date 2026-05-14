# Add New Integration

    ## Purpose
    Upgrade AppForge before using a new unsupported stack, connector, deployment target, architecture, or testing workflow.

    ## When to use
    Use this skill only when the current AppForge stage requires this exact workflow. Do not use this skill as a shortcut around approval gates.

    ## Inputs
    - Unsupported request
- Current project needs
- Existing registries

    ## Outputs
    - Upgrade proposal
- New/updated registry entries
- New rules/templates/prompts if approved

    ## Required context files
    - `ENGINE_UPGRADE_PROTOCOL.md`
- `STACK_REGISTRY.md`
- `CONNECTOR_REGISTRY.md`
- `MCP_REGISTRY.md`

    ## Rules
    - Read `APPFORGE_PROJECT_STATUS.md`, `DECISION_LOG.md`, `PENDING_QUESTIONS.md`, and all relevant registries before acting.
    - If required information is missing, write it to `PENDING_QUESTIONS.md` or make an explicit assumption in `ASSUMPTION_LOG.md`.
    - Do not invent unsupported stacks, connectors, platforms, or architectures. Use `ENGINE_UPGRADE_PROTOCOL.md` first.
    - Update all affected registries after producing outputs.
    - Prefer small, reviewable changes over large unreviewable rewrites.
    - If a reusable pattern emerges, add it to `REGISTRIES/PENDING_TEMPLATES.md`.

    ## Steps

      1. Classify unsupported request.
      2. Create upgrade proposal.
      3. Identify required docs, skills, prompts, handoffs, and tests.
      4. Identify manual actions and risks.
      5. Request approval.
      6. After approval, update AppForge files.


    ## Approval gates
    Explicit user approval required before the new capability can be used.

    ## Failure handling
    - If the task cannot be completed, document the blocker, affected files, and next safe action in `APPFORGE_PROJECT_STATUS.md` and `PENDING_QUESTIONS.md`.

    ## Handoffs
    - Update the relevant handoff file in `HANDOFFS/` when this skill produces an artifact another agent will consume.

## v11 Integration Governance Addendum

Before adding a new integration, use `SKILLS/engine_upgrade_skills/create_integration_pack/SKILL.md` and the schema in `INTEGRATIONS/`.

Do not treat the integration as active until its lifecycle state is `active` in the relevant registries and the user has approved activation for the project.
