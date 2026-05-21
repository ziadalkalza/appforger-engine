# Impeccable-Style Import Adapter

This adapter describes how to import an Impeccable-style design skill or similar open-source design `.md` file into Appforger.

Do not bundle third-party content into Appforger core by default. Instead, let the user provide the file or source link, then register and adapt it for the current project.

## Intended use

Use an Impeccable-style design import to improve:

- visual critique quality
- UI polish
- anti-generic design checks
- spacing, hierarchy, and composition reviews
- frontend screenshot reviews
- design tool prompt quality
- native UI implementation feedback

## Import workflow

1. User provides the design `.md` file or repository link.
2. Run the license checklist.
3. Summarize the design skill without copying unnecessary content.
4. Extract reusable rules into a project-specific adapter.
5. Map rules to the selected design tool, SwiftUI, and Compose.
6. Add a visual QA checklist based on the imported rules.
7. Ask user to approve activation.

## Activation prompt

```text
Use the approved imported design system named [NAME] as an additional critique and polish layer.
Do not replace Appforger stage gates.
Do not override the approved design baseline unless a design change request is approved.
Apply the imported design system only to: [scope].
```

## Mobile-native adaptation notes

Many design skills are web-oriented. Before using them for native apps, adapt rules for:

```text
iOS safe areas
Android navigation bars
native gestures
bottom sheets
tab bars
navigation stacks
system fonts or project fonts
touch targets
platform accessibility
performance constraints
```

## Output files

Create or update:

```text
integrations/design/figma/design-system-imports/imported-design-system-registry.md
integrations/design/generic/design-system-imports/mobile-native-mapping-template.md
validation/quality-assurance/visual-qa-runtime/visual-diff-report-template.md
workflows/experience-design/design-workflow/project-design-override-rules.md, if the user approves project-specific use
```
