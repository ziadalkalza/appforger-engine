from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
pc = ROOT/'templates/engine'/'project-control-template'
required = [
    'PROJECT_INITIALIZATION_REGISTRY.md',
    'ACTIVE_FEATURES_REGISTRY.md',
    'ACTIVE_WORKFLOW_RULES_REGISTRY.md',
    'PROVIDER_PREFERENCE_REGISTRY.md',
    'STORAGE_MODE_REGISTRY.md',
    'PENDING_ONBOARDING_QUESTIONS_REGISTRY.md',
]
missing = [name for name in required if not (pc/'registries'/name).exists()]
if missing:
    raise SystemExit('Missing onboarding registries: ' + ', '.join(missing))
print('validate_active_rules_config: OK')
