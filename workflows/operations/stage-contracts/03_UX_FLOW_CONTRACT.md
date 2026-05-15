# UX Flow Contract

## Required input

```text
requirements
```

## Allowed tools

- ChatGPT for reasoning, review, and packet creation
- Codex only if files/scripts need editing
- External tools only if listed in the stage or approved through engine upgrade

## Required output

```text
flows, navigation, states
```

## Approval gate

```text
UX approval
```

## Registry updates

Update whichever apply:

```text
APPFORGE_PROJECT_STATUS.md
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
