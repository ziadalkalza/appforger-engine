# Design System Activation Prompt

Use this prompt after a design system has been imported, checked, mapped, and approved.

```text
Operate inside AppForge.
Activate the imported design system [NAME / ID] for this project with this scope: [SCOPE].

Read:
- AGENTS.md
- APPFORGE_PROJECT_STATUS.md
- integrations/design/generic/design-system-imports/IMPORTED_DESIGN_SYSTEM_REGISTRY.md
- integrations/design/generic/design-system-imports/MOBILE_NATIVE_MAPPING_TEMPLATE.md or the completed mapping file
- workflows/experience-design/design-workflow/global_design_system.md
- workflows/experience-design/design-workflow/project_design_override_rules.md
- docs/getting-started/start-here/HUMAN_APPROVAL_GATES.md

Use the imported system as a design quality and critique layer.
Do not override accessibility, security, backend/API truth, or platform constraints.
Do not generate production frontend code inside AppForge.
Update the relevant design registry and pending templates if reusable rules emerge.
```
