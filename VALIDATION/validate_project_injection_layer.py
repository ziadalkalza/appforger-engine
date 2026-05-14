#!/usr/bin/env python3
from pathlib import Path
root=Path(__file__).resolve().parents[1]
required=['NEW_APP_INITIALIZER/setup_appforge_project.py', 'START_HERE/START_HERE_FOR_AGENTS.md', 'START_HERE/PROJECT_INJECTION_QUICKSTART.md', 'ENGINE_TEMPLATES/workspace-template/local-only/.env.local.example']
missing=[r for r in required if not (root/r).exists()]
if missing:
    print("missing:", missing); raise SystemExit(1)
print("validate_project_injection_layer: OK")
