#!/usr/bin/env python3
from pathlib import Path
import sys
root=Path(__file__).resolve().parents[1]
required=[
'SKILLS/runtime_skills/setup_runtime_storage/SKILL.md',
'SKILLS/runtime_skills/setup_cloud_runtime/SKILL.md',
'SKILLS/code_context_skills/bootstrap_code_context/SKILL.md',
'SKILLS/doc_source_skills/fetch_confluence_source/SKILL.md',
'SKILLS/git_provider_skills/configure_git_provider/SKILL.md',
'SKILLS/git_provider_skills/sync_bitbucket_code_source/SKILL.md',
'SKILLS/source_pipeline_skills/run_source_pipeline/SKILL.md',
'SKILLS/project_adoption_skills/create_adoption_plan/SKILL.md',
'SKILLS/cleanup_skills/clean_appforge_from_project/SKILL.md',
]
missing=[r for r in required if not (root/r).exists()]
if missing:
    print('Missing skill files:')
    for m in missing: print('-',m)
    sys.exit(1)
print('validate_skill_layer: OK')
