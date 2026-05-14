#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
required = [
    'DRAFT_AND_SANDBOX_MODE/README.md',
    'DRAFT_AND_SANDBOX_MODE/DRAFT_MODE_POLICY.md',
    'DRAFT_AND_SANDBOX_MODE/PROMOTE_DRAFT_TO_PROJECT.md',
    'SKILLS/draft_skills/start_draft_experiment/SKILL.md',
    'SKILLS/draft_skills/promote_draft_to_project/SKILL.md',
    'ENGINE_TEMPLATES/project-control-template/REGISTRIES/DRAFT_REGISTRY.md',
    'ENGINE_TEMPLATES/project-control-template/REGISTRIES/SANDBOX_EXPERIMENT_REGISTRY.md',
    'ENGINE_TEMPLATES/project-control-template/REGISTRIES/PROMOTION_REGISTRY.md',
]
missing = [p for p in required if not (root/p).exists()]
if missing:
    print('Missing draft/sandbox files:')
    for m in missing: print('-', m)
    sys.exit(1)
print('Draft/sandbox layer validation passed.')
