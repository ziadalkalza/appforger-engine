from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    'ai-models/codex/policies/model-tool-routing/model-tool-routing-policy.md',
    'ai-models/chatgpt/policies/model-tool-routing/task-to-tool-decision-matrix.md',
    'skills/governance/recommend-best-tool-for-task/SKILL.md',
    'templates/project-control/registries/TOOL_RECOMMENDATION_REGISTRY.md',
]
missing = [p for p in required if not (ROOT/p).exists()]
if missing:
    raise SystemExit('Missing tool routing layer files: ' + ', '.join(missing))
print('Tool routing layer validation passed.')
