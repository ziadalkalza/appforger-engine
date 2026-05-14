#!/usr/bin/env python3
from pathlib import Path
import re, sys
root = Path(__file__).resolve().parents[1]
bad=[]
for p in root.iterdir():
    if p.is_file():
        bad.append(f'root file not allowed: {p.name}')
    elif p.is_dir():
        if re.match(r'^\d+_', p.name):
            bad.append(f'numbered-prefix root directory not allowed: {p.name}')
# Also reject numbered-prefix folders anywhere in the engine.
for p in root.rglob('*'):
    if p.is_dir() and re.match(r'^\d+_', p.name):
        bad.append(f'numbered-prefix directory not allowed: {p.relative_to(root).as_posix()}')
if bad:
    print('Clean engine root validation failed:')
    print('\n'.join('- '+x for x in bad))
    sys.exit(1)
print('validate_clean_engine_root: OK')
