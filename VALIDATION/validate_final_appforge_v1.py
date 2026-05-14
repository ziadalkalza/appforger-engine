#!/usr/bin/env python3
from pathlib import Path
import sys, subprocess
ROOT = Path(__file__).resolve().parents[1]
required = [
    'OPERATIONAL_AUDIT/REPORTS/FINAL_APPFORGE_V1_REVIEW_REPORT.md',
    'PROJECT_ONBOARDING_AND_INITIALIZATION/INITIALIZATION_GATE_POLICY.md',
    'MODEL_AND_TOOL_AGNOSTIC_PROVIDER_LAYER/PROVIDER_AGNOSTIC_POLICY.md',
    'PARALLEL_WORK_AND_SUB_AGENT_ORCHESTRATION/PARALLEL_WORK_POLICY.md',
    'TEAM_OPERATIONS_BACKEND/TEAM_OPERATIONS_BACKEND_POLICY.md',
    'PROJECT_DOCS_LIBRARY/PROJECT_DOCS_LIBRARY_POLICY.md',
    'CONTEXT_BACKEND/SOURCE_OF_TRUTH_POLICY.md',
    'ENGINE_TEMPLATES/workspace-template/docs/README.md',
    'ENGINE_TEMPLATES/project-control-template/APPFORGE_PROJECT_PROFILE.md',
    'CONTEXT_SYNC_AND_RETRIEVAL/code_context_sources/README.md',
    'ENGINE_TEMPLATES/workspace-template/local-only/.env.local.example',
]
missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print('Missing final AppForge v1 required files:')
    for m in missing:
        print('-', m)
    sys.exit(1)
# Check for stale docs path wording outside final report/audit mention contexts.
stale = []
for p in ROOT.rglob('*'):
    if p.is_file() and p.suffix.lower() in {'.md','.sql','.yaml','.yml','.txt'}:
        s = p.read_text(encoding='utf-8', errors='ignore')
        if 'project-control/docs/' in s or 'project-control/TEAM/MEETING_NOTES' in s:
            stale.append(str(p.relative_to(ROOT)))
if stale:
    print('Stale project-control docs references found:')
    for item in stale[:20]:
        print('-', item)
    sys.exit(1)
print('Final AppForge v1 validation passed.')
