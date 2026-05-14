# Engine Upgrade Protocol

Use this whenever a user requests an unsupported integration, stack, deployment target, architecture, testing strategy, or tool.

## Hard rule

Do not use unsupported options directly inside a project. Upgrade AppForge first, then use the new capability.

## Upgrade workflow

```text
Unsupported request
→ Create upgrade proposal
→ Define capability profile
→ Define connector/MCP/tool needs
→ Define risks and manual actions
→ Add rules/templates/prompts
→ Add testing checklist
→ Update registries
→ Get approval
→ Use in active project
```

## Upgrade proposal template

```md
### UPG-0001: Add support for [capability]

- Requested by:
- Date:
- Capability type:
  - backend stack
  - deployment target
  - connector
  - MCP
  - architecture
  - testing workflow
  - third-party tool
- Why needed:
- Current workaround:
- Proposed support:
- Required files to add/update:
- Required manual user actions:
- Security/privacy implications:
- Cost implications:
- Test plan:
- Approval status:
```

## Files usually touched

- `REGISTRIES/STACK_REGISTRY.md`
- `REGISTRIES/CONNECTOR_REGISTRY.md`
- `REGISTRIES/MCP_REGISTRY.md`
- `REGISTRIES/SKILL_REGISTRY.md`
- `SKILLS/engine_upgrade_skills/`
- `PROMPTS/`
- `HANDOFFS/`
- Relevant stack/platform folder.

## Approval gate

No upgraded capability is usable until the user explicitly approves it.
