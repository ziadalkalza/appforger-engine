# Artifact Lifecycle Policy

Every artifact generated or imported during an app project must be classified before storage.

## Lifecycle classes

| Class | Meaning | Default location | Persist? |
|---|---|---|---|
| `engine_static` | reusable engine logic | `appforger-engine/` | yes, engine repo only |
| `project_memory` | app-specific decisions, registries, baselines | `project-control/` | yes |
| `source_code` | production implementation code | `backend/`, `ios/`, `android/`, `web/` | yes |
| `approved_asset` | approved app assets | `design-assets/approved/` or Figma/storage | yes |
| `candidate_asset` | asset awaiting approval | `design-assets/pending/` | maybe |
| `report_evidence` | QA, visual, release, test evidence | `exports/reports/`, `exports/qa/` | usually yes |
| `temporary` | scratch/drafts/failed outputs/logs | `local-only/` | no by default |
| `session_only` | context used only during current chat/task | not stored unless promoted | no |
| `engine_upgrade` | modifications to Appforger itself | `appforger-engine/` | yes, engine repo |

## Metadata block

Persistent artifacts should include or be registered with:

```yaml
artifact_id:
artifact_type:
lifecycle:
storage_location:
source:
status:
related_stage:
related_feature:
related_repo:
commit_policy:
promotion_rule:
```
