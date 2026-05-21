# Android Repo Agent Instructions

This is a native Android repository controlled by Appforger.

## Required context

Before making Android changes, read:

- `APPFORGER_POINTER.md`
- Appforger `APPFORGER_PROJECT_STATUS.md`
- Appforger `DECISION_LOG.md`
- Appforger `registries/project-control/design-baseline-registry.md`
- Appforger `registries/project-control/screen-registry.md`
- Appforger `registries/project-control/api-registry.md`
- Appforger `workflows/experience-design/native-android/compose-rules.md`
- Appforger `skills/mobile-implementation/implement-compose-feature/SKILL.md`

## Android rules

- Use Kotlin + Jetpack Compose by default.
- Use XML Views only when explicitly justified.
- Do not invent aesthetic UI from vague text.
- Implement from the latest approved design baseline, screen spec, or explicit mock-only task.
- If the requested UI change differs from the approved baseline, create a UI change request instead of silently changing design.
- Keep API integration aligned with Appforger `API_REGISTRY.md`.
- Run simple compile/static checks when available.

## After work

Report or update:

- Screens/components changed.
- API dependencies used.
- Design baseline followed.
- Test/build result.
- Any design/API mismatch discovered.
