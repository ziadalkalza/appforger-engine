# Kotlin Jetpack Compose Rules

## Default

Use Kotlin + Jetpack Compose first.

Use XML Views only when:

- Required by a specific platform/library need.
- Justified and documented.

## UI implementation rule

Implement from approved Figma baseline, screen specs, and design tokens. Do not invent visual design.

## Required quality

- Reusable composables.
- Previews for important screens/components.
- Accessibility semantics.
- Loading/empty/error states.
- State hoisting where appropriate.
- Clear separation from data layer.

## Avoid

- Hardcoded secrets.
- Massive composables.
- Random styling inconsistent with Figma.
- Backend assumptions not in API contract.
