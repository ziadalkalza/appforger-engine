from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
required = [
    'ai-models/chatgpt/policies/README.md',
    'ai-models/chatgpt/policies/provider-agnostic-policy.md',
    'policies/experience-design/figma/capability-routing-model.md',
    'ai-models/chatgpt/policies/profile/profile.md',
    'ai-models/codex/policies/profile/profile.md',
    'ai-models/claude/policies/profile/code-profile.md',
    'templates/execution-packets/generic/execution-packet-template.md',
    'skills/provider-adapters/select-provider-for-task/SKILL.md',
]
missing = [p for p in required if not (root/p).exists()]
if missing:
    print('Missing provider layer files:')
    print('\n'.join(missing))
    sys.exit(1)
print('Provider layer validation passed.')
