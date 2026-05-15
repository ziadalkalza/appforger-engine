# Claude Provider Profile

```yaml
provider_id: claude
name: Claude
type: planning_orchestration
status: available_or_configurable
capabilities: [product_planning, architecture_reasoning, review, documentation_generation, code_reasoning]
limits:
  - chat output is draft unless applied by a code agent; provider capability must be verified for current setup
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
