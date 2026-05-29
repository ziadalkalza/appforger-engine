# Backend Contract

## Required input

```text
approved or active draft BRD, approved design and backend choice
```

Backend work must trace data, auth, security, privacy, integration, reporting, and operational decisions to BRD requirements or record a waiver.

## Allowed tools

- ChatGPT for reasoning, review, and packet creation
- Codex only if files/scripts need editing
- External tools only if listed in the stage or approved through engine upgrade

## Required output

```text
backend implementation packet
```

## Approval gate

```text
backend works in local/test cloud
```

## Registry updates

Update whichever apply:

```text
APPFORGER_PROJECT_STATUS.md
DECISION_LOG.md
PENDING_QUESTIONS.md
REGISTRIES/FEATURE_REGISTRY.md
REGISTRIES/SCREEN_REGISTRY.md
REGISTRIES/API_REGISTRY.md
REGISTRIES/DESIGN_BASELINE_REGISTRY.md
REGISTRIES/TEST_REGISTRY.md
```

## Iteration path

If issues are found, create an entry in `CHANGE_REQUEST_REGISTRY.md`, classify impact, update only affected artifacts, rerun relevant checks, and continue.
