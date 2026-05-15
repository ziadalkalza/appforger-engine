# Project-Control Bootstrap Policy

AppForge must not leave `project-control/` empty and expect the user to populate it manually.

When a new app is initialized, AppForge must generate a minimum viable project-control folder with:

- `APPFORGE_PROJECT_STATUS.md`
- `PRODUCT_OVERVIEW.md`
- `DECISION_LOG.md`
- `ASSUMPTION_LOG.md`
- `PENDING_QUESTIONS.md`
- `APPFORGE_PROJECT.yaml`
- `README.md`
- `registries/REPO_REGISTRY.md`
- `registries/FEATURE_REGISTRY.md`
- `registries/SCREEN_REGISTRY.md`
- `registries/API_REGISTRY.md`
- `registries/DATA_MODEL_REGISTRY.md`
- `registries/CHANGE_REQUEST_REGISTRY.md`
- `registries/GENERATED_ARTIFACT_REGISTRY.md`
- `workflows/operations/artifact-imports/IMPORT_INBOX.md`
- `registries/baselines/DESIGN_BASELINE_REGISTRY.md`
- `registries/baselines/API_BASELINE_REGISTRY.md`
- `templates/packets/code-agent-packets/README.md`
- `registries/decision-snapshots/STAGE_SUMMARY.md`
- `CONTEXT_PACKS/README.md`

If any of these are missing, external validation must fail or offer to repair them.
