#!/usr/bin/env python3
"""Validate AppForger engine-only distribution assumptions."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
ENGINE = ROOT / 'appforger-engine'

errors = []
if not ENGINE.exists():
    errors.append('Missing appforger-engine/ at package root')
for forbidden in ['project-control', 'backend', 'web', 'mobile', 'ios', 'android', 'docs', 'design-assets', 'exports', 'local-only']:
    if (ROOT / forbidden).exists():
        errors.append(f'Generated workspace folder exists in engine package root: {forbidden}/')
for required in ['templates/project-control', 'templates/workspace', 'workflows/operations/new-app-initializer/create_new_app.py']:
    if not (ENGINE / required).exists():
        errors.append(f'Missing engine template/initializer path: {required}')

if errors:
    print('Engine-only package validation failed:')
    for e in errors:
        print('-', e)
    sys.exit(1)
print('Engine-only package validation passed.')
