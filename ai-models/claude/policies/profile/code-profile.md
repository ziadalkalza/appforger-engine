# Claude Code Provider Profile

```yaml
provider_id: claude_code
name: Claude Code
type: code_agent
status: available_or_configurable
capabilities: [repo_inspection, code_editing, command_execution, test_execution, MCP_tool_usage_if_configured, done_report_generation]
limits:
  - requires Claude Code setup/access; must follow execution packet; provider facts must be verified from current official docs/user setup
requires_setup:
  - depends_on_user_environment
requires_approval_for:
  - private_context
  - paid_usage
  - source_code_changes
  - production_affecting_actions
preferred_for:
  - tasks_matching_capabilities
not_recommended_for:
  - tasks_outside_declared_capabilities
```

Use this profile through capability routing. Do not assume extra capabilities unless the project records them in ACTIVE_PROVIDER_REGISTRY.
