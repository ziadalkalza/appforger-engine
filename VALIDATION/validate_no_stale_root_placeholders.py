#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
# These are deprecated artifact names from earlier builds. New canonical names like
# PENDING_QUESTIONS.md, DECISION_LOG.md, PROJECT_PROFILE.md, and .env.local are allowed.
forbidden = [
    'OPEN' + '_QUESTIONS', 'VERSION' + '_NOTES', 'APPFORGE' + '_MANIFEST', 'PROJECT' + '_CONTROL' + '_TEMPLATES',
    'appforge' + '-private.local.yaml', 'PROJECT' + '_STATE.md', 'PRODUCT' + '_BRIEF.md', 'ASSUMP' + 'TIONS.md',
    'DECI' + 'SIONS.md', 'appforge' + '.project.yaml', 'validate' + '_appforge_v5.py', 'validate' + '_appforge_v6.py',
    'validate' + '_appforge_v8.py', 'validate' + '_appforge_v9.py', 'validate' + '_appforge_v11.py'
]
violations=[]
for p in root.rglob('*'):
    if p.is_dir():
        continue
    rel=str(p.relative_to(root))
    if rel == 'validation/validate_no_stale_root_placeholders.py':
        continue
    for term in forbidden:
        if term in rel:
            violations.append(rel)
            break
    if p.suffix.lower() in {'.md','.yaml','.yml','.json','.py','.example','.txt'}:
        try: text=p.read_text(encoding='utf-8', errors='ignore')
        except Exception: continue
        for term in forbidden:
            if term in text:
                violations.append(rel+':contains:'+term)
                break
if violations:
    print('Stale/deprecated artifacts found:')
    for v in sorted(set(violations)):
        print('-',v)
    sys.exit(1)
print('validate_no_stale_root_placeholders: OK')
