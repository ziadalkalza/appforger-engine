# Workspace Layout

Recommended local structure:

```text
my-app-workspace/
  appforge/          # Appforger engine
  backend/           # Git repo: appname-backend
  ios/               # Git repo: appname-ios
  android/           # Git repo: appname-android
  design-assets/     # Optional Git repo: appname-design-assets
  exports/           # Figma exports, screenshots, QA artifacts
  local-only/        # Scratch files, ignored
```

The engine wraps the other folders through registries and handoff packets. It does not absorb their source code.
