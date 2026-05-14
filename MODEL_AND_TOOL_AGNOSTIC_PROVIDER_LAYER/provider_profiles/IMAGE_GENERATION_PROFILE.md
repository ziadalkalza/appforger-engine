# Image generation Provider Profile

```yaml
provider_id: image_generation
name: Image generation
type: visual_generation
status: available_or_configurable
capabilities: [icon_generation, illustration_generation, visual_asset_drafts]
limits:
  - assets are candidate until reviewed, licensed/approved, and registered
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
