#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
required = [
    'workflows/artifact-lifecycle/draft-sandbox/README.md',
    'workflows/operations/draft-sandbox/draft-mode-policy.md',
    'workflows/experience-design/draft-sandbox/promote-draft-to-project.md',
    'skills/workflow-orchestration/start-draft-experiment/SKILL.md',
    'skills/workflow-orchestration/promote-draft-to-project/SKILL.md',
    'templates/project-control/registries/DRAFT_REGISTRY.md',
    'templates/project-control/registries/SANDBOX_EXPERIMENT_REGISTRY.md',
    'templates/project-control/registries/PROMOTION_REGISTRY.md',
]
missing = [p for p in required if not (root/p).exists()]
if missing:
    print('Missing draft/sandbox files:')
    for m in missing: print('-', m)
    sys.exit(1)
print('Draft/sandbox layer validation passed.')
