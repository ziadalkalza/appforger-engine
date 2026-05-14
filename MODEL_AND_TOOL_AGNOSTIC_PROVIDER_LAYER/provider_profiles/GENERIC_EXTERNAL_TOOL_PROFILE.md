# Generic external tool Provider Profile

```yaml
provider_id: generic_external_tool
name: Generic external tool
type: external_tool
status: available_or_configurable
capabilities: [tool_specific_capabilities]
limits:
  - must be added through provider/integration profile before production use
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
