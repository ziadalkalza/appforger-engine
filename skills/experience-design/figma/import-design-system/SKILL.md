# Skill: Import Design System

## Purpose

Import an external design system, design `.md` file, Figma UI kit, brand guide, or visual critique skill into Appforger without polluting the reusable engine core.

This skill improves design quality while preserving:

- Appforger stage gates
- project-specific approval
- native SwiftUI/Compose compatibility
- license clarity
- engine/app separation

## Trigger when the user says

- "add this design system"
- "inject this design.md"
- "use Impeccable"
- "use this Figma kit"
- "make Appforger better at design"
- "import these brand guidelines"
- "use this open-source design file"

## Required inputs

At least one:

```text
- uploaded design file
- URL/source reference
- Figma file or UI kit link
- pasted design rules
- brand guideline document
```

Ask for missing source only if no design source was provided. If a source was provided, proceed with best-effort extraction.

## Files to read

```text
AGENTS.md
APPFORGER_PROJECT_STATUS.md
workflows/experience-design/design-workflow/global-design-system.md
workflows/experience-design/design-workflow/project-design-override-rules.md
integrations/design/figma/design-system-imports/README.md
integrations/design/generic/design-system-imports/design-system-import-protocol.md
integrations/design/generic/design-system-imports/license-and-attribution-checklist.md
integrations/design/generic/design-system-imports/design-system-conflict-resolution.md
registries/project-control/imported-design-system-registry.md
```

If available, also read the imported design file or connector-provided content.

## Workflow

### 1. Intake

Record:

```text
Name
Source
Type
License
Version/date
Project scope
Reason for import
```

### 2. License and attribution review

Classify as:

```text
APPROVED
APPROVED_WITH_ATTRIBUTION
INSPIRATION_ONLY
REJECTED
NEEDS_LEGAL_REVIEW
```

Do not copy restricted content into Appforger or production repos.

### 3. Extract design intelligence

Extract:

```text
principles
layout rules
spacing rules
typography rules
color rules
component rules
interaction rules
motion rules
accessibility rules
visual QA checks
anti-patterns
```

### 4. Map to Appforger design layers

Decide whether extracted rules affect:

```text
visual direction
Figma prompts
component specs
design tokens
SwiftUI implementation guidance
Compose implementation guidance
visual QA
```

### 5. Create mobile-native mapping

Use `integrations/design/generic/design-system-imports/mobile-native-mapping-template.md`.

### 6. Resolve conflicts

Use `integrations/design/generic/design-system-imports/design-system-conflict-resolution.md`.

### 7. Ask for approval

Before activating the imported design system, ask the user to approve:

```text
- import status
- scope
- attribution needs
- project-specific rules
- whether it should affect current Figma/design baseline
```

### 8. Update files

Update:

```text
registries/project-control/imported-design-system-registry.md
integrations/design/generic/design-system-imports/project-design-stack.md
DECISION_LOG.md
APPFORGER_PROJECT_STATUS.md
registries/project-control/pending-templates.md, if reusable patterns are found
```

If the import creates project-specific rules, update:

```text
workflows/experience-design/design-workflow/project-design-override-rules.md
```

Do not overwrite `workflows/experience-design/design-workflow/global-design-system.md` unless the user explicitly asks to upgrade the engine baseline.

## Output

Return:

```text
Import summary
License decision
Extracted rules
Mobile-native mapping summary
Conflicts or risks
Files updated
Approval needed
Next action
```

## Failure handling

If license is unclear:

```text
Use as inspiration only. Do not copy content/assets/tokens. Ask user to provide license or approval.
```

If design system is web-only:

```text
Create native adaptation notes before use.
```

If it conflicts with approved Figma:

```text
Open a design change request. Do not silently override the approved baseline.
```
