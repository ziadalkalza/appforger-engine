#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
texts = [
    root/'policies/governance/parallel-agent-work/parallel-work-policy.md',
    root/'policies/release-delivery/parallel-agent-work/safe-parallelism-matrix.md',
    root/'policies/provider-adapters/parallel-agent-work/mid-job-conflict-fix-policy.md',
]
required_terms = ['parallel work plan', 'conflict', 'baseline']
errors=[]
for f in texts:
    t=f.read_text(encoding='utf-8').lower() if f.exists() else ''
    for term in required_terms:
        if term not in t:
            errors.append(f'{f.name} missing term: {term}')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print('Parallel work safety validation passed.')
