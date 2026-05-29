# Engine Structure Audit

Checks that Appforger remains a reusable engine and does not absorb generated app-specific content.

## Required package layout

```text
Appforger_vXX/
  README.md
  appforger-engine/
    templates/engine/
      project-control-template/
      workspace-template/
```

## Required real project layout

```text
my-app-workspace/
  appforger-engine/
  project-control/
  backend/
  ios/
  android/
  web/
  design-assets/
  exports/
  local-only/
```

## Checks

- Engine rules/templates/skills remain inside `appforger-engine/`.
- Generated project state comes from templates and lives outside the engine.
- Production app code is not stored inside `appforger-engine/`.
- Examples are clearly isolated under `appforger-engine/templates/examples/`.
- Project-control templates contain the registries required by all enabled layers.
- Workspace template supports external code repos and local-only/draft areas.
