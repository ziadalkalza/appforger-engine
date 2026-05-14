# Generic local LLM Provider Profile

```yaml
provider_id: local_llm
name: Generic local LLM
type: local_model
status: available_or_configurable
capabilities: [offline_reasoning, draft_generation, private_context_reasoning_if_configured]
limits:
  - capabilities vary by model; outputs need review; may lack current facts
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
