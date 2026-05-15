#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
required = [
    root/'policies/operations/workflow-stage-overrides'/'FLEXIBLE_WORKFLOW_POLICY.md',
    root/'policies/operations/workflow-stage-overrides'/'NON_NEGOTIABLE_RULES.md',
    root/'templates/engine'/'project-control-template'/'registries'/'STAGE_OVERRIDE_REGISTRY.md',
    root/'templates/engine'/'project-control-template'/'registries'/'WORKFLOW_VARIANT_REGISTRY.md',
]
missing = [str(p) for p in required if not p.exists()]
if missing:
    print('Missing stage override files:')
    print('\n'.join(missing))
    sys.exit(1)
print('Stage override layer validation passed.')
