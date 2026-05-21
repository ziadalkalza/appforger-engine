# New App Initializer

The Appforger package is engine-only. This initializer expands the reusable engine templates into project-specific workspace folders during onboarding/setup.

The initializer copies `templates/project-control/` into the generated `project-control/` folder and creates shared folders such as `docs/`, `design-assets/`, `exports/`, and `local-only/`.

Implementation folders are conditional:

```text
web app                         -> web/
generic mobile / Flutter         -> mobile/
native iOS                      -> ios/
native Android                  -> android/
native iOS + Android            -> ios/ + android/
web + generic mobile             -> web/ + mobile/
backend-only                     -> backend/
```

Backend is created only when selected/needed.

Use `create_new_app.py` only to scaffold folders and starter project-control state. It does not generate production app code.
