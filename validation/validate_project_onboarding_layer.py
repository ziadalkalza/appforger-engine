from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    ROOT/'workflows/product/project-onboarding'/'README.md',
    ROOT/'workflows/product/project-onboarding'/'INITIALIZATION_GATE_POLICY.md',
    ROOT/'workflows/product/project-onboarding'/'questionnaire-schema.yaml',
    ROOT/'templates'/'project-control'/'appforge-project-profile.md',
    ROOT/'templates'/'project-control'/'appforge-onboarding-answers.md',
    ROOT/'templates'/'project-control'/'appforge-active-rules.md',
    ROOT/'templates'/'project-control'/'appforge-setup-status.md',
]
missing = [str(p.relative_to(ROOT)) for p in required if not p.exists()]
if missing:
    raise SystemExit('Missing onboarding files: ' + ', '.join(missing))
print('validate_project_onboarding_layer: OK')
