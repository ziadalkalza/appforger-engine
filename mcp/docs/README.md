# Appforger MCP Server

This folder contains the Appforger MCP interface layer. It exposes Appforger's engine logic, skills, templates, prompts, command references, and risk rules to MCP-capable AI clients.

## Boundary

The hosted Appforger MCP is **guide-first and non-executing**:

- It does not run project actions on a user's machine.
- It does not delete files, move folders, push Git commits, fetch private repositories, start Docker containers, or provision cloud resources.
- It returns structured plans, command references, risk levels, and approval requirements.
- The user's AI model/client runs approved commands in the user's own environment.

Local MCP mode may inspect the engine and optionally a workspace, but destructive actions must still be surfaced as approval-required command references.

## Main files

- `server/appforge_mcp_server.py` — minimal dependency MCP server supporting stdio and simple HTTP JSON-RPC modes.
- `server/appforge_resource_provider.py` — manifest-selected resource discovery and reads.
- `server/appforge_prompt_provider.py` — reusable Appforger workflow prompts.
- `server/appforge_tool_provider.py` — read/plan/search tools only.
- `server/appforge_risk_classifier.py` — risk metadata for commands/workflows.
- `MCP_RESOURCE_MAP.json` — controls which engine resources are exposed.
- `MCP_PROMPT_CATALOG.md` — prompt catalog.
- `MCP_TOOL_CATALOG.md` — tool catalog and safety boundary.
- `REMOTE_HOSTING_GUIDE.md` — remote hosting guide.
- `deployment/` — Docker and DigitalOcean examples.

## Quick local run

```bash
python /absolute/path/to/appforger-engine/mcp/server/appforge_mcp_server.py \
  --engine-root /absolute/path/to/appforger-engine \
  --transport stdio
```

Install the engine once and point your MCP client at that path. Do not place an MCP copy inside each app project.

## Quick HTTP run

```bash
python /absolute/path/to/appforger-engine/mcp/server/appforge_mcp_server.py \
  --engine-root /absolute/path/to/appforger-engine \
  --transport http \
  --host 0.0.0.0 \
  --port 8080
```



Safety invariant: remote hosted Appforger MCP does not execute project actions; it returns command references with `mcp_executes: false` and approval requirements.

## Setup model

Appforger MCP is a server interface over the Appforger engine. It exposes manifest-selected resources, prompts, and safe planning tools. It does not execute user project actions in hosted mode.

Typical local stdio run:

```bash
python /absolute/path/to/appforger-engine/mcp/server/appforge_mcp_server.py \
  --engine-root /absolute/path/to/appforger-engine \
  --transport stdio
```

Typical local HTTP run:

```bash
python /absolute/path/to/appforger-engine/mcp/server/appforge_mcp_server.py \
  --engine-root /absolute/path/to/appforger-engine \
  --transport http \
  --host 0.0.0.0 \
  --port 8080
```

Hosted/remote mode should expose Appforger logic only: resources, prompts, command references, risk metadata, and approval requirements. Project actions run in the user workspace after user approval.

## Feature requests

If a user wants Appforger MCP to support a new global feature, connector, prompt, resource, or tool, advise them to open an issue request on the Appforger MCP repository. Use `FEATURE_REQUESTS_AND_ISSUES.md` as the issue template.
