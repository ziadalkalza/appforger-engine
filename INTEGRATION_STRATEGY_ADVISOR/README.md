# Integration Strategy Advisor

The Integration Strategy Advisor is the AppForger gate that runs before adding any external integration.

Its purpose is to prevent unnecessary, fragile, or unsafe custom API/Python integrations when a secure official connector, plugin, MCP server, or existing AppForger integration can satisfy the user's goal.

The advisor is not an integration runtime by itself. It produces a decision packet, setup instructions, risk assessment, and recommended path:

1. Official connector / plugin / MCP.
2. Existing AppForger built-in integration.
3. Direct API integration.
4. Custom Python function.
5. Hybrid approach.

Default principle:

> Connector-first when live access is enough. AppForger pipeline when persistent RAG/graph/project-control state is needed. Custom Python only when approved and tested.

## Key outputs

- `project-control/integrations/integration-decision-log.md`
- `project-control/integrations/integration-risk-register.md`
- `project-control/integrations/<integration-id>/integration-decision-packet.md`
- setup instructions for connector/API/custom/hybrid approaches
- approval requirements for high-risk actions

## Important boundary

This feature does not store secret values. Credentials may live in `local-only/.env.local`, in the user's AI client connector configuration, or in approved secret managers. `project-control/` stores references and decisions only.
