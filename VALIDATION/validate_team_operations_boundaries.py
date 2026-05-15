from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
layer = root/'appforge-engine'/'runtime/collaboration/team-operations-backend'
text='\n'.join(p.read_text(encoding='utf-8', errors='ignore') for p in layer.rglob('*.md')).lower()
checks = {
    'secret values boundary': 'must never store secret values' in text,
    'project-control canonical boundary': 'project-control' in text and 'canonical' in text,
    'no full canonical documents boundary': 'must not store full canonical documents' in text or 'must not store full documents' in text,
}
failed=[name for name, ok in checks.items() if not ok]
if failed:
    print('Boundary checks failed:', failed)
    sys.exit(1)
print('Team Operations Backend boundary validation passed.')
