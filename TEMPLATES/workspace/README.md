# Workspace Template

The Appforger zip is engine-only. This folder describes the workspace that onboarding/setup creates around the engine.

## Minimal shared folders

```text
my-app-workspace/
  project-control/
  docs/
  assets/
  exports/
```

`assets/` is generic and starts empty. If design assets are requested during onboarding, create `assets/design/`. Other asset categories should live under `assets/<category>/` only when needed.

`local-only/` is optional. Create it only when onboarding or a later workflow requires private local config, sandbox work, failed outputs, or local-only mirrors.

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
