from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    'MODEL_AND_TOOL_ROUTING/MODEL_TOOL_ROUTING_POLICY.md',
    'MODEL_AND_TOOL_ROUTING/TASK_TO_TOOL_DECISION_MATRIX.md',
    'SKILLS/governance_skills/recommend_best_tool_for_task/SKILL.md',
    'ENGINE_TEMPLATES/project-control-template/REGISTRIES/TOOL_RECOMMENDATION_REGISTRY.md',
]
missing = [p for p in required if not (ROOT/p).exists()]
if missing:
    raise SystemExit('Missing tool routing layer files: ' + ', '.join(missing))
print('Tool routing layer validation passed.')
