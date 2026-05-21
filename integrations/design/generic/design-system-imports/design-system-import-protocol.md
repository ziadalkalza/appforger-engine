# Design System Import Protocol

This protocol controls how external design systems enter Appforger.

## Goal

Let the user improve Appforger's design quality by importing strong external design guidance while preserving:

- engine reusability
- legal/license clarity
- project-specific control
- design-tool approval as the implementation baseline
- native SwiftUI/Compose compatibility

## Accepted input types

```text
- Markdown design files
- provider-specific design skills
- brand guideline PDFs or docs
- design tool UI kits
- exported design tool tokens
- design token JSON
- component specs
- animation/motion guidelines
- screenshot/reference collections
```

## Import stages

### 1. Intake

Record:

```text
Name:
Source:
License:
Owner:
Version/date:
Project scope:
Why imported:
```

### 2. License and attribution check

Before using any imported system, complete `LICENSE_AND_ATTRIBUTION_CHECKLIST.md`.

If the license is unclear, the import may be used only as inspiration and may not be copied into project deliverables.

### 3. Classification

Classify as one or more:

```text
Design language
Component library
Design tokens
Motion system
Brand guide
Visual critique skill
design tool UI kit
Accessibility guide
Platform-specific guide
```

### 4. Extraction

Extract only what is useful:

```text
Design principles
Spacing rules
Typography rules
Color rules
Component anatomy
Interaction rules
Motion timing
Accessibility requirements
Anti-patterns
Visual QA heuristics
```

### 5. Mobile-native mapping

Map imported rules to:

```text
SwiftUI
Kotlin Jetpack Compose
design tool components
design tool tokens
```

Do not import rules that only work for web unless they are adapted to native mobile.

### 6. Conflict resolution

Use `DESIGN_SYSTEM_CONFLICT_RESOLUTION.md`.

### 7. Approval

Imported rules are not active until the user approves them for the current project.

### 8. Registry update

Update:

```text
REGISTRIES/IMPORTED_DESIGN_SYSTEM_REGISTRY.md
REGISTRIES/DESIGN_ASSET_REGISTRY.md, if assets were imported
REGISTRIES/DESIGN_BASELINE_REGISTRY.md, if an approved baseline changed
DECISION_LOG.md
APPFORGER_PROJECT_STATUS.md
```

## Non-negotiable restrictions

Imported design systems may not:

- override accessibility requirements
- override legal/privacy/security constraints
- force production code into the Appforger engine folder
- bypass design-tool approval
- bypass visual QA
- bypass platform usability rules
- silently change the app's approved visual baseline

## Activation rule

An imported design system is only active when:

```text
license_status: approved or allowed_with_attribution
user_approval: approved
project_scope: defined
mobile_mapping: completed
conflicts: resolved or accepted
```
