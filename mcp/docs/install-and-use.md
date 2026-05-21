# Install and Use Appforger MCP

## Local usage

1. Extract Appforger so the workspace contains `appforger-engine/`.
2. Run the local stdio server:

```bash
python appforger-engine/mcp/server/appforge_mcp_server.py \
  --engine-root appforger-engine \
  --transport stdio
```

3. Point your MCP-capable client at that command.

## Remote hosted usage

For remote hosting, deploy the HTTP server using the Docker or DigitalOcean examples in `deployment/`.

Remote MCP mode exposes Appforger logic only. It returns plans and commands for the user's AI client to run locally after approval.

## Typical model workflow

User asks:

> Set up Appforger for this project.

The model calls MCP prompts/tools:

1. `setup_appforge_project` prompt.
2. `create_setup_plan` tool.
3. Returns the local command to run.
4. Flags any risky action before execution.

## What setup means

1. Place or host `appforger-engine/`.
2. Run the MCP server from `mcp/server/appforge_mcp_server.py`.
3. Point your MCP-capable client at the stdio command or HTTP endpoint.
4. The model can then read Appforger resources/prompts/tools.
5. The MCP returns local commands and risk flags; it does not run project actions in hosted mode.

## New Appforger MCP feature requests

If the requested change is to the MCP itself, such as adding a new tool, prompt, connector, workflow, or globally useful template, create an issue on the Appforger MCP repository instead of modifying a user project. Use `mcp/docs/feature-requests-and-issues.md`.
