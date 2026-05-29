#!/usr/bin/env python3
from pathlib import Path
root=Path(__file__).resolve().parents[1]
required=['workflows/operations/new-app-initializer/setup_appforge_project.py', 'docs/project-onboarding/start-here/start-here-for-agents.md', 'docs/project-onboarding/start-here/project-injection-quickstart.md', 'templates/workspace/local-only/.env.local.example']
missing=[r for r in required if not (root/r).exists()]
if missing:
    print("missing:", missing); raise SystemExit(1)
print("validate_project_injection_layer: OK")
