#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('../project-control')
required = [root/'REGISTRIES/PACKAGE_DECISION_REGISTRY.md']
missing = [str(p) for p in required if not p.exists()]
if missing:
    print('Missing package decision registry')
    sys.exit(1)
print('Package decision layer validation passed')
