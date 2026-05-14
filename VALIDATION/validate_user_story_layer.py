#!/usr/bin/env python3
from pathlib import Path
import sys
engine = Path(__file__).resolve().parents[1]
default_root = engine/'ENGINE_TEMPLATES/project-control-template'
root = Path(sys.argv[1]) if len(sys.argv) > 1 else default_root
required = [
 root/'REGISTRIES/USER_STORY_REGISTRY.md',
 root/'REGISTRIES/EPIC_REGISTRY.md',
 root/'REGISTRIES/PRODUCT_BACKLOG_REGISTRY.md',
]
missing = [str(p) for p in required if not p.exists()]
if missing:
    print('Missing user story layer files:')
    print('\n'.join(missing))
    sys.exit(1)
print('User story layer validation passed')
