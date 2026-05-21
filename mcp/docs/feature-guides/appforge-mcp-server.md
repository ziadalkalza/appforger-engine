# Appforger MCP Server

The Appforger MCP server exposes Appforger logic to MCP-capable clients. It is guide-first: it serves skills, policies, templates, prompts, command references, and risk metadata. In hosted mode it does not execute user project actions.

## Setup

Install the engine once in a stable location and configure clients to point at that shared path. The MCP server is part of the engine, not part of each app project.

Local stdio:

```bash
python /absolute/path/to/appforger-engine/mcp/server/appforge_mcp_server.py \
  --engine-root /absolute/path/to/appforger-engine \
  --transport stdio
```

Local HTTP:

```bash
python /absolute/path/to/appforger-engine/mcp/server/appforge_mcp_server.py \
  --engine-root /absolute/path/to/appforger-engine \
  --transport http \
  --host 0.0.0.0 \
  --port 8080
```

Hosted MCP should expose Appforger resources, prompts, and safe planning tools only. User project actions run locally after user approval.

## New feature requests

If a user wants a new global Appforger/MCP feature, connector, prompt, resource, tool, or hosted behavior, advise them to open an issue on the Appforger MCP repository. Use:

```text
mcp/docs/feature-requests-and-issues.md
```

Do not implement global MCP features inside a user project.
