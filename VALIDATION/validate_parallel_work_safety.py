#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
texts = [
    root/'policies/operations/parallel-agent-work/PARALLEL_WORK_POLICY.md',
    root/'policies/operations/parallel-agent-work/SAFE_PARALLELISM_MATRIX.md',
    root/'policies/operations/parallel-agent-work/MID_JOB_CONFLICT_FIX_POLICY.md',
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
