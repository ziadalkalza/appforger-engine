# Figma Provider Profile

```yaml
provider_id: figma
name: Figma
type: design_tool
status: available_or_configurable
capabilities: [high_fidelity_design, prototyping, design_baseline_authoring, asset_layout, motion_handoff]
limits:
  - Figma output must be imported into project-control baseline before implementation
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
