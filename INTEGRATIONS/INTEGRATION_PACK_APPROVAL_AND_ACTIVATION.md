# Integration Pack Approval and Activation

An integration has three different states:

1. **Supported by engine** — AppForge has a reusable pack.
2. **Activated for project** — this app is allowed to use it.
3. **Implemented in code** — actual app repos contain working integration code.

Do not confuse these states.

## Activation checklist

- Integration pack exists.
- Official docs reviewed or draft-only status accepted.
- User use case recorded.
- Manual setup steps understood.
- Secrets policy defined.
- Cost/risk approved if relevant.
- Security/privacy review completed if relevant.
- Test checklist exists.
- Registry entries updated.

## Activation output

Update:

- `REGISTRIES/CONNECTOR_REGISTRY.md`
- `REGISTRIES/MCP_REGISTRY.md` when relevant
- `COST_AND_DEPENDENCIES/SERVICE_DEPENDENCY_REGISTRY.md`
- `ENVIRONMENTS_AND_SECRETS/`
- project-control integration status if active for a specific app
