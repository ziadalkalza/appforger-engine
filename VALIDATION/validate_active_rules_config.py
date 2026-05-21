from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
pc = ROOT/'templates'/'project-control'
required = [
    'project-initialization-registry.md',
    'active-features-registry.md',
    'active-workflow-rules-registry.md',
    'provider-preference-registry.md',
    'storage-mode-registry.md',
    'pending-onboarding-questions-registry.md',
]
missing = [name for name in required if not (pc/'registries'/name).exists()]
if missing:
    raise SystemExit('Missing onboarding registries: ' + ', '.join(missing))
print('validate_active_rules_config: OK')
