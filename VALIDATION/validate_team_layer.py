#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
required = [
    root/'policies/collaboration/team-collaboration/README.md',
    root/'integrations/source-control/github/team-workflow/GITHUB_BRANCH_PROTECTION_SETUP.md',
    root/'templates/packets/team-handoff-packets/HANDOFF_PACKET_TEMPLATE.md',
    root/'policies/collaboration/team-approvals-governance/APPROVAL_RECORD_TEMPLATE.md',
    root/'policies/collaboration/team-secrets-access/SECRET_ACCESS_POLICY.md',
    root/'templates/engine/project-control-template/registries/TEAM_MEMBER_REGISTRY.md',
    root/'templates/engine/project-control-template/registries/APPROVAL_REGISTRY.md',
    root/'templates/engine/project-control-template/TEAM/TEAM_STATUS.md',
]
missing = [str(p) for p in required if not p.exists()]
if missing:
    print('Missing team layer files:')
    print('\n'.join(missing))
    sys.exit(1)
print('Team layer validation passed.')
