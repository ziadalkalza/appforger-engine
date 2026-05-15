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
→ Add rules/templates/ai-prompts
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

- `registries/STACK_REGISTRY.md`
- `registries/CONNECTOR_REGISTRY.md`
- `registries/MCP_REGISTRY.md`
- `registries/SKILL_REGISTRY.md`
- `skills/operations/engine_upgrade_skills/`
- `templates/ai-prompts/`
- `docs/collaboration/handoffs/`
- Relevant stack/platform folder.

## Approval gate

No upgraded capability is usable until the user explicitly approves it.
