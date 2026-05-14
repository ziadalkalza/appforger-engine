#!/usr/bin/env python3
"""Validate conditional workspace folder generation."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ENGINE = Path(__file__).resolve().parents[1]
INIT = ENGINE / 'NEW_APP_INITIALIZER' / 'create_new_app.py'

cases = [
    ('web_only', ['--app-type','web','--backend','none'], {'web'}, {'ios','android','mobile','backend'}),
    ('flutter_mobile', ['--app-type','mobile','--mobile-strategy','flutter','--backend','none'], {'mobile'}, {'ios','android','web','backend'}),
    ('native_both', ['--app-type','mobile','--mobile-strategy','native_both','--backend','supabase'], {'ios','android','backend'}, {'mobile','web'}),
    ('backend_only', ['--app-type','backend_only','--backend','fastapi_postgres'], {'backend'}, {'ios','android','mobile','web'}),
    ('web_flutter_backend', ['--app-type','both','--mobile-strategy','flutter','--backend','supabase'], {'web','mobile','backend'}, {'ios','android'}),
]

errors = []
for name, args, expected, forbidden in cases:
    td = Path(tempfile.mkdtemp(prefix=f'appforger_{name}_'))
    target = td / 'workspace'
    try:
        subprocess.run([sys.executable, str(INIT), '--name', name, '--target', str(target), *args], check=True, capture_output=True, text=True)
        for d in ['project-control','docs','design-assets','exports','local-only']:
            if not (target/d).exists():
                errors.append(f'{name}: missing shared folder {d}/')
        for d in expected:
            if not (target/d).exists():
                errors.append(f'{name}: missing expected implementation folder {d}/')
        for d in forbidden:
            if (target/d).exists():
                errors.append(f'{name}: forbidden implementation folder created: {d}/')
    except subprocess.CalledProcessError as e:
        errors.append(f'{name}: initializer failed: {e.stderr or e.stdout}')
    finally:
        shutil.rmtree(td, ignore_errors=True)

if errors:
    print('Workspace folder selection validation failed:')
    for e in errors:
        print('-', e)
    sys.exit(1)
print('Workspace folder selection validation passed.')
