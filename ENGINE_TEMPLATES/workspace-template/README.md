# Workspace Template

The AppForger zip is engine-only. This folder describes the workspace that onboarding/setup creates around the engine.

## Always-created shared folders

```text
my-app-workspace/
  appforge-engine/
  project-control/
  docs/
  design-assets/
  exports/
  local-only/
```

## Conditional implementation folders

Implementation folders are created based on onboarding answers:

```text
web app                         -> web/
generic mobile / Flutter         -> mobile/
native iOS                      -> ios/
native Android                  -> android/
native iOS + Android            -> ios/ + android/
web + generic mobile             -> web/ + mobile/
backend-only                     -> backend/
```

Do not create unused frontend folders. A web-only app should not get `ios/` or `android/`. A generic mobile app should get `mobile/`, not separate `ios/` and `android/`, unless the project chooses separate native tracks.
