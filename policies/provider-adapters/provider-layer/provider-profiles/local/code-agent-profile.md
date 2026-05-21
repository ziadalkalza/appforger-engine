# Generic local code agent Provider Profile

```yaml
provider_id: local_code_agent
name: Generic local code agent
type: local_code_agent
status: available_or_configurable
capabilities: [repo_inspection, code_editing, command_execution_if_configured, test_execution_if_configured]
limits:
  - capabilities depend on local tool setup; must follow packet and safety policy
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
