# Engine vs App Workspace Boundaries

Appforger is the reusable engine. It must not become the app codebase.

## Golden rule

Do not place production backend, iOS, Android, or generated frontend code inside the Appforger engine folder.

Appforger contains:
- rules
- prompts
- agents
- skills
- registries
- handoff packets
- project state
- connector and MCP setup docs
- validation and bootstrap utilities

Appforger does not contain:
- production SwiftUI source code
- production Kotlin/Compose source code
- production FastAPI source code
- generated Xcode projects
- generated Android Studio projects
- database secrets
- cloud credentials
- compiled assets as the source of truth

## Recommended local layout

```text
my-app-workspace/
  appforge/                 # reusable engine copy or engine submodule
  appforge-project-state/   # optional app-specific state repo if you keep engine pristine
  backend/                  # standalone GitHub repo: appname-backend
  ios/                      # standalone GitHub repo: appname-ios
  android/                  # standalone GitHub repo: appname-android
  design-assets/            # optional standalone repo: appname-design-assets
  exports/                  # temporary exports from Figma, screenshots, QA files
  local-only/               # local scratch, never synced
```

## GitHub repo mapping

Each implementation part should be independently syncable:

```text
backend/  -> GitHub repo: appname-backend
ios/      -> GitHub repo: appname-ios
android/  -> GitHub repo: appname-android
design-assets/ -> GitHub repo: appname-design-assets, optional
appforge/ -> GitHub repo: appname-appforge or reusable Appforger engine repo
```

The Appforger registries track links between the repos, but the app source code lives in the relevant repo.

## How Appforger drives implementation

Appforger creates the specification and task packet. Codex applies that packet in the correct repo.

Example:

```text
Appforger creates:
templates/execution-packets/artifact-packets/ios-implementation-packet-template.md-derived task

Codex opens:
my-app-workspace/ios/

Codex reads:
ios/AGENTS.md
ios/APPFORGER_POINTER.md
Appforger packet

Codex edits:
ios source files only

Codex reports back:
changed files, tests run, screenshots, unresolved issues

Appforger updates:
FEATURE_REGISTRY.md
SCREEN_REGISTRY.md
TEST_REGISTRY.md
CHANGE_REQUEST_REGISTRY.md
```

## Forbidden mixing

Do not do this:

```text
Appforger/
  ios/MyApp.xcodeproj
  android/app/src/main
  backend/app/main.py
```

Do this instead:

```text
my-app-workspace/
  appforge/
  ios/
  android/
  backend/
```

## Exceptions

Only tiny examples, templates, or non-production sample snippets may live inside Appforger, and they must stay under:

```text
templates/examples/
templates/
workflows/implementation/native-repo-scaffolds/
```

If real app code is accidentally created in the engine folder, open a change request and move it to the correct repo.
