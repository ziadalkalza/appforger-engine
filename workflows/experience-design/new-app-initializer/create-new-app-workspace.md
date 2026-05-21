# Create New App Workspace

The distributed zip contains only the reusable engine:

```text
Appforger_v1/
  appforger-engine/
```

During onboarding/setup, Appforger creates the external workspace folders from engine templates.

## Shared folders always created

```text
my-app-workspace/
  appforger-engine/   # reusable engine copy/submodule
  project-control/   # app-specific state copied from Appforger templates
  docs/              # shared project documents
  design-assets/     # shared reusable visual assets
  exports/           # generated evidence/reports/handoffs
  local-only/        # scratch/drafts/debug, normally not committed
```

## Conditional implementation folders

```text
web app                         -> web/
generic mobile / Flutter         -> mobile/
native iOS                      -> ios/
native Android                  -> android/
native iOS + Android            -> ios/ + android/
web + generic mobile             -> web/ + mobile/
backend-only                     -> backend/
```

Do not put backend/frontend/mobile source code inside `appforger-engine/`.

## Docs folder

Every generated workspace includes `docs/` as a sibling of `project-control/`. Store shared project documents there or link to an approved external docs provider. Do not store full DOCX/PDF documents in `project-control/`.
