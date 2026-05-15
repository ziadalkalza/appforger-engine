#!/usr/bin/env python3
from pathlib import Path
root=Path(__file__).resolve().parents[1]
required=['workflows/operations/new-app-initializer/setup_appforge_project.py', 'docs/getting-started/start-here/START_HERE_FOR_AGENTS.md', 'docs/getting-started/start-here/PROJECT_INJECTION_QUICKSTART.md', 'templates/engine/workspace-template/local-only/.env.local.example']
missing=[r for r in required if not (root/r).exists()]
if missing:
    print("missing:", missing); raise SystemExit(1)
print("validate_project_injection_layer: OK")
