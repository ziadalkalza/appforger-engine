from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
required = [
    'MODEL_AND_TOOL_AGNOSTIC_PROVIDER_LAYER/README.md',
    'MODEL_AND_TOOL_AGNOSTIC_PROVIDER_LAYER/PROVIDER_AGNOSTIC_POLICY.md',
    'MODEL_AND_TOOL_AGNOSTIC_PROVIDER_LAYER/CAPABILITY_ROUTING_MODEL.md',
    'MODEL_AND_TOOL_AGNOSTIC_PROVIDER_LAYER/provider_profiles/CHATGPT_PROFILE.md',
    'MODEL_AND_TOOL_AGNOSTIC_PROVIDER_LAYER/provider_profiles/CODEX_PROFILE.md',
    'MODEL_AND_TOOL_AGNOSTIC_PROVIDER_LAYER/provider_profiles/CLAUDE_CODE_PROFILE.md',
    'EXECUTION_PACKETS/EXECUTION_PACKET_TEMPLATE.md',
    'SKILLS/provider_skills/select_provider_for_task/SKILL.md',
]
missing = [p for p in required if not (root/p).exists()]
if missing:
    print('Missing provider layer files:')
    print('\n'.join(missing))
    sys.exit(1)
print('Provider layer validation passed.')
