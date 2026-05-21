# MCP Lifecycle Policy

MCP configs and docs are not the same as a working MCP server.

## Required states

1. Config template exists.
2. Server/package installed where needed.
3. Credentials/permissions configured.
4. Connection tested.
5. Tool access validated in the active environment.
6. Capability marked active for the project.

## Safety rules

- Do not assume MCP access exists because a config template exists.
- Do not request production secrets in chat.
- Do not run high-risk MCP actions without explicit user approval.
- If MCP access is missing, fall back to local files, GitHub links, exported packets, or user-provided files.
