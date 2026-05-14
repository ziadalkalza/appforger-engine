#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
required = [
    root/'TEAM_COLLABORATION/README.md',
    root/'TEAM_GITHUB_WORKFLOW/GITHUB_BRANCH_PROTECTION_SETUP.md',
    root/'TEAM_HANDOFF_PACKETS/HANDOFF_PACKET_TEMPLATE.md',
    root/'TEAM_APPROVALS_AND_GOVERNANCE/APPROVAL_RECORD_TEMPLATE.md',
    root/'TEAM_SECRETS_AND_ACCESS/SECRET_ACCESS_POLICY.md',
    root/'ENGINE_TEMPLATES/project-control-template/REGISTRIES/TEAM_MEMBER_REGISTRY.md',
    root/'ENGINE_TEMPLATES/project-control-template/REGISTRIES/APPROVAL_REGISTRY.md',
    root/'ENGINE_TEMPLATES/project-control-template/TEAM/TEAM_STATUS.md',
]
missing = [str(p) for p in required if not p.exists()]
if missing:
    print('Missing team layer files:')
    print('\n'.join(missing))
    sys.exit(1)
print('Team layer validation passed.')
