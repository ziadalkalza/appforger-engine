# iOS Repo Agent Instructions

This is a native iOS repository controlled by AppForge.

## Required context

Before making iOS changes, read:

- `APPFORGE_POINTER.md`
- AppForge `APPFORGE_PROJECT_STATUS.md`
- AppForge `DECISION_LOG.md`
- AppForge `REGISTRIES/DESIGN_BASELINE_REGISTRY.md`
- AppForge `REGISTRIES/SCREEN_REGISTRY.md`
- AppForge `REGISTRIES/API_REGISTRY.md`
- AppForge `NATIVE_IOS/swiftui_rules.md`
- AppForge `SKILLS/ios_skills/implement_swiftui_feature/SKILL.md`

## iOS rules

- Use SwiftUI by default.
- Use UIKit only when explicitly justified.
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
