#!/usr/bin/env python3
from pathlib import Path
import sys
engine=Path(__file__).resolve().parents[1]
root=engine.parent
checks=[engine/'templates/project-control', engine/'templates/workspace', engine/'workflows/operations/new-app-initializer/create_new_app.py']
missing=[str(p) for p in checks if not p.exists()]
if missing:
 print('Missing required structure:')
 print('\n'.join(missing))
 sys.exit(1)
# production code dirs must not exist as top-level inside engine
for forbidden in ['backend','ios','android','web','project-control','local-only']:
 if (engine/forbidden).exists():
  print(f'Forbidden app-specific folder inside engine: {forbidden}')
  sys.exit(1)
print('Engine structure validation passed.')
