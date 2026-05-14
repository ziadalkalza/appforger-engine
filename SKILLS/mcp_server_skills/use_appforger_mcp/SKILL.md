# Use AppForger MCP Skill

Use this skill when a user asks an AI client to use AppForger through MCP.

Steps:

1. List AppForger MCP resources and prompts.
2. Read the relevant skill/policy/template resources.
3. Prefer MCP prompts for workflow guidance.
4. Use tools only for read/plan/search outputs.
5. For actions, return command references for local execution by the user's model/client.
6. Flag dangerous actions as approval-required.

Do not assume the remote MCP can access the user's local project files or credentials.
