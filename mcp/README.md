# AppForger MCP Server

This folder contains the AppForger MCP interface layer. It exposes AppForger's engine logic, skills, templates, prompts, command references, and risk rules to MCP-capable AI clients.

## Boundary

The hosted AppForger MCP is **guide-first and non-executing**:

- It does not run project actions on a user's machine.
- It does not delete files, move folders, push Git commits, fetch private repositories, start Docker containers, or provision cloud resources.
- It returns structured plans, command references, risk levels, and approval requirements.
- The user's AI model/client runs approved commands in the user's own environment.

Local MCP mode may inspect the engine and optionally a workspace, but destructive actions must still be surfaced as approval-required command references.

## Main files

- `server/appforge_mcp_server.py` — minimal dependency MCP server supporting stdio and simple HTTP JSON-RPC modes.
- `server/appforge_resource_provider.py` — manifest-selected resource discovery and reads.
- `server/appforge_prompt_provider.py` — reusable AppForger workflow prompts.
- `server/appforge_tool_provider.py` — read/plan/search tools only.
- `server/appforge_risk_classifier.py` — risk metadata for commands/workflows.
- `MCP_RESOURCE_MAP.json` — controls which engine resources are exposed.
- `MCP_PROMPT_CATALOG.md` — prompt catalog.
- `MCP_TOOL_CATALOG.md` — tool catalog and safety boundary.
- `REMOTE_HOSTING_GUIDE.md` — remote hosting guide.
- `deployment/` — Docker and DigitalOcean examples.

## Quick local run

```bash
python appforge-engine/mcp/interface/server/appforge_mcp_server.py \
  --engine-root appforge-engine \
  --transport stdio
```

## Quick HTTP run

```bash
python appforge-engine/mcp/interface/server/appforge_mcp_server.py \
  --engine-root appforge-engine \
  --transport http \
  --host 0.0.0.0 \
  --port 8080
```



Safety invariant: remote hosted AppForger MCP does not execute project actions; it returns command references with `mcp_executes: false` and approval requirements.

## Setup model

AppForger MCP is a server interface over the AppForger engine. It exposes manifest-selected resources, prompts, and safe planning tools. It does not execute user project actions in hosted mode.

Typical local stdio run:

```bash
python appforge-engine/mcp/interface/server/appforge_mcp_server.py \
  --engine-root appforge-engine \
  --transport stdio
```

Typical local HTTP run:

```bash
python appforge-engine/mcp/interface/server/appforge_mcp_server.py \
  --engine-root appforge-engine \
  --transport http \
  --host 0.0.0.0 \
  --port 8080
```

Hosted/remote mode should expose AppForger logic only: resources, prompts, command references, risk metadata, and approval requirements. Project actions run in the user workspace after user approval.

## Feature requests

If a user wants AppForger MCP to support a new global feature, connector, prompt, resource, or tool, advise them to open an issue request on the AppForger MCP repository. Use `FEATURE_REQUESTS_AND_ISSUES.md` as the issue template.
