# Required Workspace Structure

Minimum structure for a normal project:

```text
my-app-workspace/
  appforger-engine/
  project-control/
  backend/        # if backend selected
  ios/            # if iOS selected
  android/        # if Android selected
  web/            # if web selected
  design-assets/
  exports/
  local-only/
```

`appforger-engine/` may be the unzipped Appforger folder or a Git checkout of the engine.

`project-control/` is app-specific and must be generated during initialization.
