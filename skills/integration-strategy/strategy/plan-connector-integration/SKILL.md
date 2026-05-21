# Plan Connector Integration Skill

Use this skill when an official/trusted connector, plugin, or MCP is the selected approach.

Output:
- connector name/type;
- setup steps;
- required permissions/scopes;
- whether write actions are disabled by default;
- AI client configuration notes;
- what Appforger will and will not store;
- fallback plan if connector cannot satisfy the goal.

Write-capable connectors must default to read-only until the user chooses otherwise per integration.
