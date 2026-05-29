#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
required = [
    root/'policies/collaboration/team-collaboration/README.md',
    root/'integrations/source-control/github/docs/team-workflow/github-branch-protection-setup.md',
    root/'templates/execution-packets/team-handoff-packets/handoff-packet-template.md',
    root/'policies/collaboration/team-approvals-governance/approval-record-template.md',
    root/'policies/collaboration/team-secrets-access/secret-access-policy.md',
    root/'templates/project-control/registries/TEAM_MEMBER_REGISTRY.md',
    root/'templates/project-control/registries/APPROVAL_REGISTRY.md',
    root/'templates/project-control/team/team-status.md',
]
missing = [str(p) for p in required if not p.exists()]
if missing:
    print('Missing team layer files:')
    print('\n'.join(missing))
    sys.exit(1)
print('Team layer validation passed.')
