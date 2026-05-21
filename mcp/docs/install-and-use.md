# Install and Use Appforger MCP

## Local usage

1. Install or extract `appforger-engine/` once in a stable location outside your app repositories.
2. Run the local stdio server:

```bash
python /absolute/path/to/appforger-engine/mcp/server/appforge_mcp_server.py \
  --engine-root /absolute/path/to/appforger-engine \
  --transport stdio
```

3. Point your MCP-capable client at that command.
4. Open any app project separately in the AI client, wherever that project lives. The client uses Appforger MCP for plans/resources and applies approved work in the selected project root.

Do not copy the MCP server into each app project. The MCP server belongs to the shared engine; project-specific files belong in the app project's own workspace.

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

Initial setup creates only core project-control driver files and minimal workspace folders. `assets/` starts as an empty generic folder; optional sections such as `assets/design/`, `local-only/`, team, runtime, or context are added only when onboarding answers activate them. Later changes, such as switching from single-user to team mode, should use the project-control module plan instead of copying every optional folder.

## What setup means

1. Place or host one shared `appforger-engine/`.
2. Run the MCP server from `mcp/server/appforge_mcp_server.py`.
3. Point your MCP-capable client at the stdio command or HTTP endpoint.
4. The model can then read Appforger resources/prompts/tools.
5. The MCP returns local commands and risk flags using the shared engine path and a separate project target chosen by the user/client; it does not run project actions in hosted mode.

## New Appforger MCP feature requests

If the requested change is to the MCP itself, such as adding a new tool, prompt, connector, workflow, or globally useful template, create an issue on the Appforger MCP repository instead of modifying a user project. Use `mcp/docs/feature-requests-and-issues.md`.
