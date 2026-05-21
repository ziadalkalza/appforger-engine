# Workspace Template

This is a reference layout. In a real app, the initializer creates these folders outside the reusable engine.

```text
my-app-workspace/
  appforger-engine/
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

`appforger-engine/` contains reusable engine logic. The other folders are generated or live project components.


## Onboarding gate

Before real project work starts, Appforger checks `project-control/APPFORGER_SETUP_STATUS.md` and `project-control/APPFORGER_PROJECT.yaml`.

If the minimal onboarding gate is incomplete, Appforger pauses the requested task, asks the critical setup questions, saves answers, generates active rules, and then resumes the original request.
