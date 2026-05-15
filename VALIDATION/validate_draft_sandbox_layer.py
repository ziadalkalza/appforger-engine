#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
required = [
    'workflows/operations/draft-sandbox/README.md',
    'workflows/operations/draft-sandbox/DRAFT_MODE_POLICY.md',
    'workflows/operations/draft-sandbox/PROMOTE_DRAFT_TO_PROJECT.md',
    'skills/workflow/draft_skills/start_draft_experiment/SKILL.md',
    'skills/workflow/draft_skills/promote_draft_to_project/SKILL.md',
    'templates/engine/project-control-template/registries/DRAFT_REGISTRY.md',
    'templates/engine/project-control-template/registries/SANDBOX_EXPERIMENT_REGISTRY.md',
    'templates/engine/project-control-template/registries/PROMOTION_REGISTRY.md',
]
missing = [p for p in required if not (root/p).exists()]
if missing:
    print('Missing draft/sandbox files:')
    for m in missing: print('-', m)
    sys.exit(1)
print('Draft/sandbox layer validation passed.')
