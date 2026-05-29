# Requirements Contract

## Required input

```text
approved idea
```

The Business Requirements Document (BRD) is mandatory. If the user provides a BRD template, use it for the project-specific BRD under `project-control/requirements/`. If no template is provided, use the engine template at `templates/specifications/business-requirements-document-template.md`.

## Allowed tools

- ChatGPT for reasoning, review, and packet creation
- Codex only if files/scripts need editing
- External tools only if listed in the stage or approved through engine upgrade

## Required output

```text
approved or active draft BRD, product brief, feature list, constraints, user types
```

## Approval gate

```text
requirements approval
```

## Registry updates

Update whichever apply:

```text
APPFORGER_PROJECT_STATUS.md
DECISION_LOG.md
PENDING_QUESTIONS.md
REGISTRIES/REQUIREMENTS_DOCUMENT_REGISTRY.md
REGISTRIES/FEATURE_REGISTRY.md
REGISTRIES/SCREEN_REGISTRY.md
REGISTRIES/API_REGISTRY.md
REGISTRIES/DESIGN_BASELINE_REGISTRY.md
REGISTRIES/TEST_REGISTRY.md
```

## Downstream gate

Do not proceed to UX, visual design, Figma, backend/API, frontend implementation, QA, or release work unless the BRD is approved, explicitly marked draft-only/mock-only, or waived with risk and affected stages recorded.

## Iteration path

If issues are found, create an entry in `CHANGE_REQUEST_REGISTRY.md`, classify impact, update only affected artifacts, rerun relevant checks, and continue.
