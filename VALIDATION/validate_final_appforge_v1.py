#!/usr/bin/env python3
from pathlib import Path
import sys, subprocess
ROOT = Path(__file__).resolve().parents[1]
required = [
    'validation/operational-audits/operational-audit/reports/final-appforge-v1-review-report.md',
    'workflows/project-onboarding/initialization-gate-policy.md',
    'ai-models/chatgpt/policies/provider-agnostic-policy.md',
    'policies/governance/parallel-agent-work/parallel-work-policy.md',
    'runtime/collaboration/team-operations-backend/team-operations-backend-policy.md',
    'docs/project-docs-library/project-docs-library-policy.md',
    'runtime/context-backend/source-of-truth-policy.md',
    'templates/workspace/docs/README.md',
    'templates/project-control/appforge-project-profile.md',
    'workflows/operations/context-sync-retrieval/code-context-sources/README.md',
    'templates/workspace/local-only/.env.local.example',
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
