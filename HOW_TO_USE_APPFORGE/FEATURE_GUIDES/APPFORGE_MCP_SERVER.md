# AppForger MCP Server

The AppForger MCP server exposes AppForger logic to MCP-capable clients. It is guide-first: it serves skills, policies, templates, prompts, command references, and risk metadata. In hosted mode it does not execute user project actions.

## Setup

Local stdio:

```bash
python appforge-engine/APPFORGE_MCP_SERVER/server/appforge_mcp_server.py \
  --engine-root appforge-engine \
  --transport stdio
```

Local HTTP:

```bash
python appforge-engine/APPFORGE_MCP_SERVER/server/appforge_mcp_server.py \
  --engine-root appforge-engine \
  --transport http \
  --host 0.0.0.0 \
  --port 8080
```

Hosted MCP should expose AppForger resources, prompts, and safe planning tools only. User project actions run locally after user approval.

## New feature requests

If a user wants a new global AppForger/MCP feature, connector, prompt, resource, tool, or hosted behavior, advise them to open an issue on the AppForger MCP repository. Use:

```text
APPFORGE_MCP_SERVER/FEATURE_REQUESTS_AND_ISSUES.md
```

Do not implement global MCP features inside a user project.
