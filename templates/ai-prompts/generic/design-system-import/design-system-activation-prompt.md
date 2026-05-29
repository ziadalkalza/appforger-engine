# Design System Activation Prompt

Use this prompt after a design system has been imported, checked, mapped, and approved.

```text
Operate inside Appforger.
Activate the imported design system [NAME / ID] for this project with this scope: [SCOPE].

Read:
- AGENTS.md
- APPFORGER_PROJECT_STATUS.md
- integrations/design/figma/design-system-imports/imported-design-system-registry.md
- integrations/design/generic/design-system-imports/mobile-native-mapping-template.md or the completed mapping file
- workflows/experience-design/design-workflow/global-design-system.md
- workflows/experience-design/design-workflow/project-design-override-rules.md
- docs/project-onboarding/start-here/human-approval-gates.md

Use the imported system as a design quality and critique layer.
Do not override accessibility, security, backend/API truth, or platform constraints.
Do not generate production frontend code inside Appforger.
Update the relevant design registry and pending templates if reusable rules emerge.
```
