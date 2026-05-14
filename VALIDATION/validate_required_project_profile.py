from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
pc = ROOT/'ENGINE_TEMPLATES'/'project-control-template'
text = (pc/'APPFORGE_PROJECT.yaml').read_text(encoding='utf-8')
required_terms = ['initialization:', 'minimal_gate_complete', 'allow_help_before_onboarding', 'project_profile:', 'provider_preferences:', 'storage_modes:']
missing = [t for t in required_terms if t not in text]
if missing:
    raise SystemExit('Missing APPFORGE_PROJECT.yaml onboarding terms: ' + ', '.join(missing))
print('validate_required_project_profile: OK')
