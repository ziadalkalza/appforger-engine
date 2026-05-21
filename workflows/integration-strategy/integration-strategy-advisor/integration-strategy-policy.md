# Integration Strategy Policy

When a user asks Appforger to add an integration, Appforger must first select an integration approach before generating integration code.

The decision order is:

1. Research current official connector/plugin/MCP options.
2. Check whether Appforger already has a built-in integration.
3. Evaluate direct API integration.
4. Evaluate custom Python only if safer options do not satisfy the goal or the user explicitly approves it.
5. Recommend hybrid if the user needs both live connector access and persistent Appforger RAG/graph/project-control indexing.

The advisor is mandatory before creating custom API/Python integration code.

Every integration decision must record:

- user goal
- candidate approaches
- selected approach
- security notes
- cost/hosting notes
- data storage mode
- RAG/graph impact
- credential placement
- approval requirements
- commands or setup steps
- testing/iteration expectations for custom code

Every selected integration approach must produce an integration decision packet before implementation or custom code generation.
