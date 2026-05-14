# Multi-Device Workspace Setup

## Recommended setup

Use GitHub as the common synchronization layer.

```text
GitHub organization/project:
  appname-appforge-engine        # reusable engine; changes rarely
  appname-project-control        # shared app memory, baselines, packets
  appname-backend                # backend code
  appname-ios                    # iOS app code
  appname-android                # Android app code
  appname-web                    # web app code, if selected
  appname-design-assets          # optional approved exported assets
```

## Frontend device

```text
frontend-workspace/
  project-control/
  ios/ or android/ or web/
  design-assets/ optional
  exports/
  local-only/
```

## Backend device

```text
backend-workspace/
  project-control/
  backend/
  exports/
  local-only/
```

## Designer device

```text
design-workspace/
  project-control/
  design-assets/
  exports/figma/
  local-only/
```

## Rule

Every device must know where `project-control/` is. It is the shared contract between devices.

Each local workspace should include an `APPFORGE_WORKSPACE.md` file, generated from `WORKSPACE_POINTER_TEMPLATE.md`, that records local paths and remote URLs.
