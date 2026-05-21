# Cleanup Guide

Use `workflows/operations/workspace-artifact-lifecycle/scripts/appforge_clean.py` for safe cleanup. Cleanup is allowlist-based: it removes only AppForger-specific artifacts or marked AppForger-owned folders.

It must not delete generic project folders such as `docs/`, `assets/`, `exports/`, `backend/`, `web/`, `mobile/`, `ios/`, or `android/`.

Dry-run by default:

```bash
python appforger-engine/workflows/operations/workspace-artifact-lifecycle/scripts/appforge_clean.py --target . --mode remove-local
```

Apply changes:

```bash
python appforger-engine/workflows/operations/workspace-artifact-lifecycle/scripts/appforge_clean.py --target . --mode remove-local --yes
```

Runtime volume deletion requires project-name confirmation.

If a path is not proven AppForger-created, cleanup skips it and reports the skip.
