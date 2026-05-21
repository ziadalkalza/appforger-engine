#!/usr/bin/env python3
"""Validate AppForge design-system import layer exists."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    'integrations/design/figma/design-system-imports/README.md',
    'integrations/design/generic/design-system-imports/design-system-import-protocol.md',
    'integrations/design/figma/design-system-imports/imported-design-system-registry.md',
    'integrations/design/generic/design-system-imports/license-and-attribution-checklist.md',
    'integrations/design/generic/design-system-imports/design-system-conflict-resolution.md',
    'integrations/design/generic/design-system-imports/project-design-stack.md',
    'skills/experience-design/figma/import-design-system/SKILL.md',
    'registries/project-control/imported-design-system-registry.md',
]
missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print('Missing design import files:')
    for p in missing:
        print(f'- {p}')
    sys.exit(1)
print('Design import layer OK')
