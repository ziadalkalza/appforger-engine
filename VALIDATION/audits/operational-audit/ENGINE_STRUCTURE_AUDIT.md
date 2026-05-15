# Engine Structure Audit

Checks that AppForge remains a reusable engine and does not absorb generated app-specific content.

## Required package layout

```text
AppForge_vXX/
  README.md
  appforge-engine/
    templates/engine/
      project-control-template/
      workspace-template/
```

## Required real project layout

```text
my-app-workspace/
  appforge-engine/
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

- Engine rules/templates/skills remain inside `appforge-engine/`.
- Generated project state comes from templates and lives outside the engine.
- Production app code is not stored inside `appforge-engine/`.
- Examples are clearly isolated under `appforge-engine/templates/examples/`.
- Project-control templates contain the registries required by all enabled layers.
- Workspace template supports external code repos and local-only/draft areas.
