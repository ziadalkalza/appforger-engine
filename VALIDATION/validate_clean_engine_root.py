#!/usr/bin/env python3
from pathlib import Path
import re, sys
root = Path(__file__).resolve().parents[1]
allowed_root_files = {'.gitignore', 'README.md', 'STRUCTURE_NOTES.md', 'desktop.ini'}
allowed_root_dirs = {
    '.git',
    'ai-models',
    'docs',
    'examples',
    'integrations',
    'mcp',
    'policies',
    'registries',
    'runtime',
    'tools',
    'skills',
    'templates',
    'validation',
    'workflows',
}
bad=[]
for p in root.iterdir():
    if p.is_file():
        if p.name not in allowed_root_files:
            bad.append(f'root file not allowed: {p.name}')
    elif p.is_dir():
        if p.name not in allowed_root_dirs:
            bad.append(f'unexpected root directory: {p.name}')
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
