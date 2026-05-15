# Android Repo Agent Instructions

This is a native Android repository controlled by AppForge.

## Required context

Before making Android changes, read:

- `APPFORGE_POINTER.md`
- AppForge `APPFORGE_PROJECT_STATUS.md`
- AppForge `DECISION_LOG.md`
- AppForge `registries/DESIGN_BASELINE_REGISTRY.md`
- AppForge `registries/SCREEN_REGISTRY.md`
- AppForge `registries/API_REGISTRY.md`
- AppForge `workflows/implementation/native-android/compose_rules.md`
- AppForge `skills/implementation/android_skills/implement_compose_feature/SKILL.md`

## Android rules

- Use Kotlin + Jetpack Compose by default.
- Use XML Views only when explicitly justified.
- Do not invent aesthetic UI from vague text.
- Implement from the latest approved design baseline, screen spec, or explicit mock-only task.
- If the requested UI change differs from the approved baseline, create a UI change request instead of silently changing design.
- Keep API integration aligned with AppForge `API_REGISTRY.md`.
- Run simple compile/static checks when available.

## After work

Report or update:

- Screens/components changed.
- API dependencies used.
- Design baseline followed.
- Test/build result.
- Any design/API mismatch discovered.
