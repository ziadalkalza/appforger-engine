#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
f = root/'policies/operations/parallel-agent-work/AGENT_BRAND_FAMILY_POLICY.md'
t = f.read_text(encoding='utf-8').lower() if f.exists() else ''
for term in ['openai','anthropic','cross-brand','reconciliation','high-risk']:
    if term not in t:
        print(f'Brand-family policy missing: {term}')
        sys.exit(1)
print('Brand-family policy validation passed.')
