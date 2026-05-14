# Cleanup Guide

Use `WORKSPACE_AND_ARTIFACT_LIFECYCLE/scripts/appforge_clean.py` for safe cleanup.

Dry-run by default:

```bash
python appforge-engine/WORKSPACE_AND_ARTIFACT_LIFECYCLE/scripts/appforge_clean.py --target . --mode remove-local
```

Apply changes:

```bash
python appforge-engine/WORKSPACE_AND_ARTIFACT_LIFECYCLE/scripts/appforge_clean.py --target . --mode remove-local --yes
```

Runtime volume deletion requires project-name confirmation.
