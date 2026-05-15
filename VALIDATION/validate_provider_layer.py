from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
required = [
    'policies/providers/provider-layer/README.md',
    'policies/providers/provider-layer/PROVIDER_AGNOSTIC_POLICY.md',
    'policies/providers/provider-layer/CAPABILITY_ROUTING_MODEL.md',
    'policies/providers/provider-layer/provider_profiles/providers/chatgpt/PROFILE.md',
    'policies/providers/provider-layer/provider_profiles/providers/codex/PROFILE.md',
    'policies/providers/provider-layer/provider_profiles/providers/claude/CODE_PROFILE.md',
    'templates/packets/execution-packets/EXECUTION_PACKET_TEMPLATE.md',
    'skills/providers/generic/select_provider_for_task/SKILL.md',
]
missing = [p for p in required if not (root/p).exists()]
if missing:
    print('Missing provider layer files:')
    print('\n'.join(missing))
    sys.exit(1)
print('Provider layer validation passed.')
