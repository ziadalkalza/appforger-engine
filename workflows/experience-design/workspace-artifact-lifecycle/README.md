# Workspace and Artifact Lifecycle

This folder defines where Appforger-generated content belongs and when it must persist.

Core rule:

```text
Appforger-engine is reusable static logic.
Anything generated for a specific app must live outside the engine.
```

Required workspace model:

```text
my-app-workspace/
  appforger-engine/     # reusable engine files only
  project-control/     # app-specific memory, state, registries, packets, baselines
  backend/             # live backend code repo, if used
  ios/                 # live iOS code repo, if used
  android/             # live Android code repo, if used
  web/                 # live web code repo, if used
  design-assets/       # approved exported assets
  exports/             # screenshots, reports, Figma exports, QA evidence
  local-only/          # temporary scratch, failed outputs, debug files
```

Appforger must classify every generated artifact before writing it.
