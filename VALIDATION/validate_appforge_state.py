#!/usr/bin/env python3
from pathlib import Path
import sys
engine = Path(__file__).resolve().parents[1]
default_state = engine/'templates/engine/project-control-template/APPFORGE_PROJECT_STATUS.md'
state_path = Path(sys.argv[1]) if len(sys.argv) > 1 else default_state
if not state_path.exists():
    print(f'APPFORGE_PROJECT_STATUS.md is missing at {state_path}')
    sys.exit(1)
text = state_path.read_text(encoding='utf-8', errors='ignore').lower()
required = ['project', 'stage']
missing = [k for k in required if k not in text]
if missing:
    print('APPFORGE_PROJECT_STATUS.md may be incomplete. Missing hints:', ', '.join(missing))
    sys.exit(1)
print('OK: APPFORGE_PROJECT_STATUS.md exists and appears initialized/template-ready.')
