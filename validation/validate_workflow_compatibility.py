#!/usr/bin/env python3
from pathlib import Path
import sys
engine=Path(__file__).resolve().parents[1]
text=(engine/'validation/operational-audits/operational-audit/end-to-end-scenario-tests.md').read_text(encoding='utf-8').lower()
for term in ['standard mobile','standard web','html sandbox','backendless','existing frontend','team mode','qdrant','automation','release candidate']:
 if term not in text:
  print(f'Missing scenario term: {term}')
  sys.exit(1)
print('Workflow compatibility validation passed.')
