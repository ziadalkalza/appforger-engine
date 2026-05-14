# Project Creation Modes

AppForge supports four modes.

## Mode 1: Generic spec-first

Use when the user wants to design a platform-agnostic app before choosing platform priority.

Important:

- No Flutter.
- No React Native.
- No wrapper framework.
- No frontend prototype code.
- Figma handles prototypes.
- AppForge creates shared product specs, shared screen specs, shared API contracts, backend, and native implementation tasks.

## Mode 2: Native iOS first

Use when:

- The app launches on iOS first.
- The user wants SwiftUI as the lead implementation.
- Android will be adapted later.

Default stack:

- SwiftUI.
- MVVM or Clean Architecture depending on complexity.
- iOS feature specs must not assume Android-specific patterns.

## Mode 3: Native Android first

Use when:

- The app launches on Android first.
- The user wants Kotlin + Jetpack Compose as the lead implementation.
- iOS will be adapted later.

Default stack:

- Kotlin.
- Jetpack Compose.
- MVVM or MVI depending on complexity.

## Mode 4: Parallel native

Use when:

- iOS and Android should be implemented side-by-side.
- The product, backend, API, and design baseline are stable enough.
- The team can handle parallel QA.

## Mode selection checklist

- Target platforms:
- Business reason for platform order:
- Team skill availability:
- Design maturity:
- Backend maturity:
- Expected launch order:
- QA capacity:

## Approval gate

Do not proceed past requirements until the app mode is selected and recorded in `APPFORGE_PROJECT_STATUS.md` and `DECISION_LOG.md`.

## Optional web modes

AppForge can also activate a Web Track when requested.

- `web_only`: responsive web app only.
- `web_plus_backend`: web frontend with separate backend repo.
- `fullstack_web`: one fullstack web repo such as Next.js where approved.
- `shared_backend_web_mobile`: one backend/API used by web, iOS, and Android clients.

The web track is optional and must be explicitly selected or inferred from the user's app target. Mobile-native rules remain unchanged.

