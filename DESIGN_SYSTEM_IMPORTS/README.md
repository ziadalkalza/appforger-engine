# Design System Imports

This folder lets AppForge use external design intelligence without mixing it into the reusable engine core.

Use this area when the user wants to inject:

- open-source design `.md` files
- design skills such as Impeccable-style rules
- Figma Community design systems or UI kits
- internal company brand guidelines
- exported design tokens
- component documentation
- motion/animation guidelines

Imported design systems are **inputs to the design process**, not production app code.

## Core rule

Imported design systems extend AppForge. They do not replace AppForge workflow rules, stage gates, security rules, accessibility rules, or repo boundaries.

## Where imports live

Recommended local app workspace layout:

```text
my-app-workspace/
  appforge/                  # reusable AppForge engine
  design-systems/            # imported reusable design systems for this app
    imported/
      impeccable/
      company-brand-guide/
      figma-ui-kit-name/
    selected/
      active-design-stack.md
  backend/
  ios/
  android/
  exports/
```

Do not paste third-party design systems directly into `DESIGN/global_design_system.md`. Instead, register them in `REGISTRIES/IMPORTED_DESIGN_SYSTEM_REGISTRY.md` and summarize how they should influence the current project.

## When to use

Use this folder when:

- the base AppForge design rules are too generic
- the user wants a stronger design taste layer
- the project has a brand guide
- the user imports an external design `.md` file
- the user wants a Figma UI kit to influence app screens
- Codex repeatedly creates weak-looking native UI

## Required output from an import

Every imported design system should produce:

1. License/attribution decision.
2. Design-system summary.
3. Extracted rules.
4. Extracted tokens/components if available.
5. Mobile-native mapping to SwiftUI and Compose.
6. Conflict resolution notes.
7. Approval status.
8. Registry update.

Use `SKILLS/design_skills/import_design_system/SKILL.md` for the full workflow.
