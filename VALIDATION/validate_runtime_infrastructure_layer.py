#!/usr/bin/env python3
from pathlib import Path
root=Path(__file__).resolve().parents[1]
required=['runtime/platform/storage/README.md', 'templates/engine/project-control-template/runtime/scripts/appforge_runtime.py', 'templates/engine/project-control-template/runtime/docker/docker-compose.appforge-runtime.yml']
missing=[r for r in required if not (root/r).exists()]
if missing:
    print("missing:", missing); raise SystemExit(1)
print("validate_runtime_infrastructure_layer: OK")
