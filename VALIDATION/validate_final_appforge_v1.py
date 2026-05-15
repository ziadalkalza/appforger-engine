#!/usr/bin/env python3
from pathlib import Path
import sys, subprocess
ROOT = Path(__file__).resolve().parents[1]
required = [
    'validation/audits/operational-audit/REPORTS/FINAL_APPFORGE_V1_REVIEW_REPORT.md',
    'workflows/product/project-onboarding/INITIALIZATION_GATE_POLICY.md',
    'policies/providers/provider-layer/PROVIDER_AGNOSTIC_POLICY.md',
    'policies/operations/parallel-agent-work/PARALLEL_WORK_POLICY.md',
    'runtime/collaboration/team-operations-backend/TEAM_OPERATIONS_BACKEND_POLICY.md',
    'docs/document-management/project-docs-library/PROJECT_DOCS_LIBRARY_POLICY.md',
    'runtime/context/context-backend/SOURCE_OF_TRUTH_POLICY.md',
    'templates/engine/workspace-template/docs/README.md',
    'templates/engine/project-control-template/APPFORGE_PROJECT_PROFILE.md',
    'workflows/operations/context-sync-retrieval/code_context_sources/README.md',
    'templates/engine/workspace-template/local-only/.env.local.example',
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
