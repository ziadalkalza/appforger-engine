#!/usr/bin/env python3
"""Validate AppForge design-system import layer exists."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    'DESIGN_SYSTEM_IMPORTS/README.md',
    'DESIGN_SYSTEM_IMPORTS/DESIGN_SYSTEM_IMPORT_PROTOCOL.md',
    'DESIGN_SYSTEM_IMPORTS/IMPORTED_DESIGN_SYSTEM_REGISTRY.md',
    'DESIGN_SYSTEM_IMPORTS/LICENSE_AND_ATTRIBUTION_CHECKLIST.md',
    'DESIGN_SYSTEM_IMPORTS/DESIGN_SYSTEM_CONFLICT_RESOLUTION.md',
    'DESIGN_SYSTEM_IMPORTS/PROJECT_DESIGN_STACK.md',
    'SKILLS/design_skills/import_design_system/SKILL.md',
    'REGISTRIES/IMPORTED_DESIGN_SYSTEM_REGISTRY.md',
]
missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print('Missing design import files:')
    for p in missing:
        print(f'- {p}')
    sys.exit(1)
print('Design import layer OK')
