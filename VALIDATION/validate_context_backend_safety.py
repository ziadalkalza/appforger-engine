#!/usr/bin/env python3
from pathlib import Path
import sys
engine=Path(__file__).resolve().parents[1]
text=(engine/'validation/audits/operational-audit/CONTEXT_BACKEND_AUDIT.md').read_text(encoding='utf-8').lower()
for term in ['optional','canonical','metadata','stale','secrets']:
 if term not in text:
  print(f'Missing context backend safety term: {term}')
  sys.exit(1)
print('Context backend safety validation passed.')
