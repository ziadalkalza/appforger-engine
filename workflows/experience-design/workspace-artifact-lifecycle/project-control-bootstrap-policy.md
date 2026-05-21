# Project-Control Bootstrap Policy

Appforger must not leave `project-control/` empty and expect the user to populate it manually.

When a new app is initialized, Appforger must generate a minimum viable project-control folder with:

- `APPFORGER_PROJECT_STATUS.md`
- `PRODUCT_OVERVIEW.md`
- `DECISION_LOG.md`
- `ASSUMPTION_LOG.md`
- `PENDING_QUESTIONS.md`
- `APPFORGER_PROJECT.yaml`
- `README.md`
- `registries/project-control/repo-registry.md`
- `registries/project-control/feature-registry.md`
- `registries/project-control/screen-registry.md`
- `registries/project-control/api-registry.md`
- `registries/project-control/data-model-registry.md`
- `registries/project-control/change-request-registry.md`
- `registries/GENERATED_ARTIFACT_REGISTRY.md`
- `workflows/artifact-lifecycle/artifact-imports/import-inbox.md`
- `registries/project-control/baselines/design-baseline-registry.md`
- `registries/project-control/baselines/api-baseline-registry.md`
- `templates/execution-packets/code-agent-packets/README.md`
- `registries/decision-snapshots/STAGE_SUMMARY.md`
- `CONTEXT_PACKS/README.md`

If any of these are missing, external validation must fail or offer to repair them.
