# MCP Registry

## MCP principles

MCPs expose external context/tools to agents. Use the least powerful MCP permissions that can complete the task.

## Approved/default MCP profiles

| MCP | Role | Status | Risk |
|---|---|---|---|
| GitHub MCP | repo read/write, issues, PRs | approved | code changes require branch/PR policy |
| Figma MCP | design context and optional writeback | approved | design changes need approval baseline |
| Supabase MCP | Supabase project context/actions | approved | secrets and production DB access must be restricted |

## Review-required MCP profiles

| MCP | Role | Status | Required review |
|---|---|---|---|
| PostgreSQL MCP | direct DB access | review_required | server choice, permissions, read/write limits, production guardrails |

## Future

See `mcp/catalog/future_engine_mcp_server_plan.md`.
