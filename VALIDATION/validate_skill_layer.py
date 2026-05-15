#!/usr/bin/env python3
from pathlib import Path
import sys
root=Path(__file__).resolve().parents[1]
required=[
'skills/runtime/runtime_skills/setup_runtime_storage/SKILL.md',
'skills/runtime/runtime_skills/setup_cloud_runtime/SKILL.md',
'skills/context/code-context/bootstrap_code_context/SKILL.md',
'skills/integrations/apps/confluence/fetch_source/SKILL.md',
'skills/integrations/generic/source-control/configure_git_provider/SKILL.md',
'skills/integrations/apps/bitbucket/sync_code_source/SKILL.md',
'skills/operations/source_pipeline_skills/run_source_pipeline/SKILL.md',
'skills/onboarding/project_adoption_skills/create_adoption_plan/SKILL.md',
'skills/operations/cleanup_skills/clean_appforge_from_project/SKILL.md',
]
missing=[r for r in required if not (root/r).exists()]
if missing:
    print('Missing skill files:')
    for m in missing: print('-',m)
    sys.exit(1)
print('validate_skill_layer: OK')
