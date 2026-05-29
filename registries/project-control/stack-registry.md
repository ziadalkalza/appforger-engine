# Stack Registry

## Approved stacks

### Native iOS

- SwiftUI first.
- UIKit only when justified.

### Native Android

- Kotlin + Jetpack Compose first.
- XML Views only when justified.

### Backend

- Supabase.
- FastAPI + PostgreSQL.

## Unsupported stacks

Any unlisted stack requires `ENGINE_UPGRADE_PROTOCOL.md`.

| Stack/tool | Status | Notes | Upgrade required |
|---|---|---|---|
| Flutter | unsupported for frontend implementation | Figma handles prototypes. Generic mode is spec-first only. | yes |
| React Native | unsupported | no wrapper frameworks by default | yes |
| Firebase | unsupported v1 | can be added through upgrade | yes |
| Django | unsupported v1 | can be added through upgrade | yes |
| NestJS | unsupported v1 | can be added through upgrade | yes |
