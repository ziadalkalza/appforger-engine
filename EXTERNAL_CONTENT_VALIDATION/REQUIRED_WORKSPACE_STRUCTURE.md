# Required Workspace Structure

Minimum structure for a normal project:

```text
my-app-workspace/
  appforge-engine/
  project-control/
  backend/        # if backend selected
  ios/            # if iOS selected
  android/        # if Android selected
  web/            # if web selected
  design-assets/
  exports/
  local-only/
```

`appforge-engine/` may be the unzipped AppForge folder or a Git checkout of the engine.

`project-control/` is app-specific and must be generated during initialization.
