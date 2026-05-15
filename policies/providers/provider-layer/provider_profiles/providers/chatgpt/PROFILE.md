# ChatGPT Provider Profile

```yaml
provider_id: chatgpt
name: ChatGPT
type: planning_orchestration
status: available_or_configurable
capabilities: [product_planning, architecture_reasoning, documentation_generation, prompt_generation, review, image_generation_if_available]
limits:
  - does not directly modify local repos unless connected; code output in chat is draft until applied/tested
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
