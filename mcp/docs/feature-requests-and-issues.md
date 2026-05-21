# Appforger MCP Feature Requests and Issues

Use this guide when a user wants to add or change Appforger MCP behavior, expose a new workflow, add a new connector, or request a new Appforger feature.

## Default rule

Do not silently implement new MCP/server features inside a user project. If the request changes Appforger itself, create an issue request on the Appforger MCP repository.

The MCP should guide the user/model to open an issue rather than modifying the hosted MCP server or engine package ad hoc.

## When to create an issue

Create an issue request when the user asks for:

- a new MCP resource, prompt, or tool;
- a new connector or integration strategy;
- support for a new AI client;
- changes to MCP security, auth, or approval behavior;
- new project-control templates;
- new runtime storage support;
- new code/doc/source pipeline behavior;
- changes that affect all users of the hosted MCP service.

## When not to create an issue

Do not create an Appforger MCP issue for project-local work such as:

- setting up Appforger in the current workspace;
- registering a project-specific code source;
- configuring a local Confluence source;
- filling `local-only/.env.local`;
- running a local pipeline command;
- creating an execution packet for the current project.

Those actions belong in the user project, not in the MCP server repository.

## Issue template

```md
# Feature request

## Summary
What should Appforger MCP support?

## User goal
What user workflow does this enable?

## Proposed MCP surface
- Resources:
- Prompts:
- Tools:
- Command references:

## Risk level
- Low / Medium / High
- Does this involve deletion, Git push, secret access, cloud provisioning, raw code indexing, or write actions?

## Execution boundary
Should MCP only return plans/commands, or should any local tool be allowed to execute after approval?

## Alternatives considered
Official connector/MCP, built-in Appforger pipeline, direct API, custom Python, hybrid.

## Acceptance criteria
- Required files/templates/skills/docs:
- Validation required:
- Smoke test required:

## Notes
Any client-specific needs: Claude, Cursor, VS Code/Copilot, ChatGPT, Gemini, generic MCP.
```

## MCP response rule

When the user asks for a new Appforger/MCP feature, the MCP should return:

```json
{
  "workflow": "request_appforge_mcp_feature",
  "mcp_executes": false,
  "recommended_action": "open_issue_on_appforge_mcp_repo",
  "requires_user_approval": false,
  "issue_template": "mcp/docs/feature-requests-and-issues.md"
}
```

The user or their model can then create the issue in the Appforger MCP repository.
