# PostgreSQL MCP Review

## Status

Review required.

Unlike GitHub/Figma/Supabase, PostgreSQL MCP support depends on which MCP server is selected and what permissions it has.

## Before use

Approve:

- MCP server package/source.
- Read-only vs read-write access.
- Target database.
- Local/test/production environment.
- Connection method.
- Secret handling.
- Query limits.
- Migration policy.

## Default rule

For FastAPI + PostgreSQL projects, Appforger can produce SQL/migrations and backend code without direct PostgreSQL MCP access.

Direct PostgreSQL MCP access is optional and must be reviewed.
