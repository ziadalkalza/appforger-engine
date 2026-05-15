from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    'policies/providers/model-tool-routing/MODEL_TOOL_ROUTING_POLICY.md',
    'policies/providers/model-tool-routing/TASK_TO_TOOL_DECISION_MATRIX.md',
    'skills/governance/governance_skills/recommend_best_tool_for_task/SKILL.md',
    'templates/engine/project-control-template/registries/TOOL_RECOMMENDATION_REGISTRY.md',
]
missing = [p for p in required if not (ROOT/p).exists()]
if missing:
    raise SystemExit('Missing tool routing layer files: ' + ', '.join(missing))
print('Tool routing layer validation passed.')
