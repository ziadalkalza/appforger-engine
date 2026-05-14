#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
required = [
    root/'FLEXIBLE_WORKFLOW_AND_STAGE_OVERRIDES'/'FLEXIBLE_WORKFLOW_POLICY.md',
    root/'FLEXIBLE_WORKFLOW_AND_STAGE_OVERRIDES'/'NON_NEGOTIABLE_RULES.md',
    root/'ENGINE_TEMPLATES'/'project-control-template'/'REGISTRIES'/'STAGE_OVERRIDE_REGISTRY.md',
    root/'ENGINE_TEMPLATES'/'project-control-template'/'REGISTRIES'/'WORKFLOW_VARIANT_REGISTRY.md',
]
missing = [str(p) for p in required if not p.exists()]
if missing:
    print('Missing stage override files:')
    print('\n'.join(missing))
    sys.exit(1)
print('Stage override layer validation passed.')
