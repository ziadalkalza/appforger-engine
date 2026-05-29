#!/usr/bin/env python3
from pathlib import Path
import sys
root=Path(__file__).resolve().parents[1]
required=[
'skills/runtime-storage/setup-runtime-storage/SKILL.md',
'skills/runtime-storage/setup-cloud-runtime/SKILL.md',
'skills/context-backend/code-context/bootstrap-code-context/SKILL.md',
'skills/source-pipeline/confluence/fetch-source/SKILL.md',
'skills/integration-strategy/source-control/configure-git-provider/SKILL.md',
'skills/source-control/bitbucket/sync-code-source/SKILL.md',
'skills/source-pipeline/run-source-pipeline/SKILL.md',
'skills/project-onboarding/create-adoption-plan/SKILL.md',
'skills/cleanup-lifecycle/clean-appforge-from-project/SKILL.md',
]
missing=[r for r in required if not (root/r).exists()]
if missing:
    print('Missing skill files:')
    for m in missing: print('-',m)
    sys.exit(1)
print('validate_skill_layer: OK')
