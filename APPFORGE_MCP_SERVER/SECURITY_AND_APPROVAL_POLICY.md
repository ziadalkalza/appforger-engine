# MCP Security and Approval Policy

The AppForger MCP server is read/plan/search by default.

## Risk levels

- `low`: read-only guidance or template lookup.
- `medium`: creates files or fetches/indexes data when run locally.
- `high`: can modify project structure, Git history, runtime storage, cloud resources, or sensitive context.
- `critical`: destructive cleanup, runtime volume deletion, production deployment, secret handling, raw code indexing, or Git push.

## Required rule

Remote hosted MCP must never execute high/critical project actions. It may return command references with:

- `requires_user_approval: true`
- `mcp_executes: false`
- `run_location: user_local_workspace`



Safety invariant: remote hosted AppForger MCP does not execute project actions; it returns command references with `mcp_executes: false` and approval requirements.
