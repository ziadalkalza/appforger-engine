# Project Injection Quickstart

AppForger is a sidecar control layer. It should sit beside project folders, not inside app repos.

```text
workspace/
  appforge-engine/
  project-control/
  docs/
  local-only/
  backend/
  web/
```

Run:

```bash
python appforge-engine/workflows/operations/new-app-initializer/setup_appforge_project.py --target . --name "My Product"
```
