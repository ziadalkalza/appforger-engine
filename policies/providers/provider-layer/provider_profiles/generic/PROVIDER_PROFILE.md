# Generic provider Provider Profile

```yaml
provider_id: generic_provider
name: Generic provider
type: generic
status: available_or_configurable
capabilities: [capability_declared_by_profile]
limits:
  - draft until reviewed and approved
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
