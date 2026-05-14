# Workspace Template

This is a reference layout. In a real app, the initializer creates these folders outside the reusable engine.

```text
my-app-workspace/
  appforge-engine/
  project-control/
  docs/
  backend/
  ios/
  android/
  web/
  design-assets/
  exports/
  local-only/
```

`appforge-engine/` contains reusable engine logic. The other folders are generated or live project components.


## Onboarding gate

Before real project work starts, AppForge checks `project-control/APPFORGE_SETUP_STATUS.md` and `project-control/APPFORGE_PROJECT.yaml`.

If the minimal onboarding gate is incomplete, AppForge pauses the requested task, asks the critical setup questions, saves answers, generates active rules, and then resumes the original request.
