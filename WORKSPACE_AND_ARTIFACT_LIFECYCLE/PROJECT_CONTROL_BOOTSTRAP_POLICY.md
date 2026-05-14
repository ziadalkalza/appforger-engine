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
- `REGISTRIES/REPO_REGISTRY.md`
- `REGISTRIES/FEATURE_REGISTRY.md`
- `REGISTRIES/SCREEN_REGISTRY.md`
- `REGISTRIES/API_REGISTRY.md`
- `REGISTRIES/DATA_MODEL_REGISTRY.md`
- `REGISTRIES/CHANGE_REQUEST_REGISTRY.md`
- `REGISTRIES/GENERATED_ARTIFACT_REGISTRY.md`
- `ARTIFACT_IMPORTS/IMPORT_INBOX.md`
- `BASELINES/DESIGN_BASELINE_REGISTRY.md`
- `BASELINES/API_BASELINE_REGISTRY.md`
- `CODEX_WORK_PACKETS/README.md`
- `DECISION_SNAPSHOTS/STAGE_SUMMARY.md`
- `CONTEXT_PACKS/README.md`

If any of these are missing, external validation must fail or offer to repair them.
