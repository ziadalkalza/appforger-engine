from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    ROOT/'PROJECT_ONBOARDING_AND_INITIALIZATION'/'README.md',
    ROOT/'PROJECT_ONBOARDING_AND_INITIALIZATION'/'INITIALIZATION_GATE_POLICY.md',
    ROOT/'PROJECT_ONBOARDING_AND_INITIALIZATION'/'questionnaire_schema.yaml',
    ROOT/'ENGINE_TEMPLATES'/'project-control-template'/'APPFORGE_PROJECT_PROFILE.md',
    ROOT/'ENGINE_TEMPLATES'/'project-control-template'/'APPFORGE_ONBOARDING_ANSWERS.md',
    ROOT/'ENGINE_TEMPLATES'/'project-control-template'/'APPFORGE_ACTIVE_RULES.md',
    ROOT/'ENGINE_TEMPLATES'/'project-control-template'/'APPFORGE_SETUP_STATUS.md',
]
missing = [str(p.relative_to(ROOT)) for p in required if not p.exists()]
if missing:
    raise SystemExit('Missing onboarding files: ' + ', '.join(missing))
print('validate_project_onboarding_layer: OK')
