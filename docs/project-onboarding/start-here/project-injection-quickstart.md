# Project Injection Quickstart

Appforger is a sidecar control layer. It should sit beside project folders, not inside app repos.

```text
workspace/
  appforger-engine/
  project-control/
  docs/
  local-only/
  backend/
  web/
```

Run:

```bash
python appforger-engine/workflows/operations/new-app-initializer/setup_appforge_project.py --target . --name "My Product"
```
