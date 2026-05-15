#!/usr/bin/env python3
"""Validate AppForge design-system import layer exists."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    'integrations/design/generic/design-system-imports/README.md',
    'integrations/design/generic/design-system-imports/DESIGN_SYSTEM_IMPORT_PROTOCOL.md',
    'integrations/design/generic/design-system-imports/IMPORTED_DESIGN_SYSTEM_REGISTRY.md',
    'integrations/design/generic/design-system-imports/LICENSE_AND_ATTRIBUTION_CHECKLIST.md',
    'integrations/design/generic/design-system-imports/DESIGN_SYSTEM_CONFLICT_RESOLUTION.md',
    'integrations/design/generic/design-system-imports/PROJECT_DESIGN_STACK.md',
    'skills/design/generic/import_design_system/SKILL.md',
    'registries/IMPORTED_DESIGN_SYSTEM_REGISTRY.md',
]
missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print('Missing design import files:')
    for p in missing:
        print(f'- {p}')
    sys.exit(1)
print('Design import layer OK')
