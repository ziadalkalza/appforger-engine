# Skill: Import Design System

## Purpose

Import an external design system, design `.md` file, Figma UI kit, brand guide, or visual critique skill into AppForge without polluting the reusable engine core.

This skill improves design quality while preserving:

- AppForge stage gates
- project-specific approval
- native SwiftUI/Compose compatibility
- license clarity
- engine/app separation

## Trigger when the user says

- "add this design system"
- "inject this design.md"
- "use Impeccable"
- "use this Figma kit"
- "make AppForge better at design"
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
APPFORGE_PROJECT_STATUS.md
DESIGN/global_design_system.md
DESIGN/project_design_override_rules.md
DESIGN_SYSTEM_IMPORTS/README.md
DESIGN_SYSTEM_IMPORTS/DESIGN_SYSTEM_IMPORT_PROTOCOL.md
DESIGN_SYSTEM_IMPORTS/LICENSE_AND_ATTRIBUTION_CHECKLIST.md
DESIGN_SYSTEM_IMPORTS/DESIGN_SYSTEM_CONFLICT_RESOLUTION.md
REGISTRIES/IMPORTED_DESIGN_SYSTEM_REGISTRY.md
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

Do not copy restricted content into AppForge or production repos.

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

### 4. Map to AppForge design layers

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

Use `DESIGN_SYSTEM_IMPORTS/MOBILE_NATIVE_MAPPING_TEMPLATE.md`.

### 6. Resolve conflicts

Use `DESIGN_SYSTEM_IMPORTS/DESIGN_SYSTEM_CONFLICT_RESOLUTION.md`.

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
REGISTRIES/IMPORTED_DESIGN_SYSTEM_REGISTRY.md
DESIGN_SYSTEM_IMPORTS/PROJECT_DESIGN_STACK.md
DECISION_LOG.md
APPFORGE_PROJECT_STATUS.md
REGISTRIES/PENDING_TEMPLATES.md, if reusable patterns are found
```

If the import creates project-specific rules, update:

```text
DESIGN/project_design_override_rules.md
```

Do not overwrite `DESIGN/global_design_system.md` unless the user explicitly asks to upgrade the engine baseline.

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
