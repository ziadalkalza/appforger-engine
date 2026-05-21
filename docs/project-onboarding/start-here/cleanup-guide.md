# Cleanup Guide

Use `workflows/operations/workspace-artifact-lifecycle/scripts/appforge_clean.py` for safe cleanup.

Dry-run by default:

```bash
python appforger-engine/workflows/operations/workspace-artifact-lifecycle/scripts/appforge_clean.py --target . --mode remove-local
```

Apply changes:

```bash
python appforger-engine/workflows/operations/workspace-artifact-lifecycle/scripts/appforge_clean.py --target . --mode remove-local --yes
```

Runtime volume deletion requires project-name confirmation.
