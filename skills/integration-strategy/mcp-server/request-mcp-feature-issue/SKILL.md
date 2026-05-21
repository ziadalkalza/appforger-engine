# Request MCP Feature Issue Skill

Use this skill when the user asks to add a new global Appforger MCP feature, connector, prompt, resource, tool, client support, or hosted MCP behavior.

## Goal

Route global Appforger/MCP changes into an issue request on the Appforger MCP repository instead of silently changing a user project.

## Steps

1. Classify the request:
   - project-local configuration, or
   - global Appforger/MCP feature request.
2. If it is project-local, use the relevant Appforger project skill.
3. If it is a global Appforger/MCP feature, create an issue request plan.
4. Include:
   - summary;
   - user goal;
   - proposed MCP resources/prompts/tools;
   - risk level;
   - approval requirements;
   - alternatives considered;
   - acceptance criteria;
   - validation/smoke-test requirements.
5. Tell the user to open the issue on the Appforger MCP repository.

## Boundary

The MCP should not modify the hosted server or engine package for a single user request unless the maintainers approve and implement the change.
