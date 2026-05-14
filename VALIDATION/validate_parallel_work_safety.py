#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
texts = [
    root/'PARALLEL_WORK_AND_SUB_AGENT_ORCHESTRATION/PARALLEL_WORK_POLICY.md',
    root/'PARALLEL_WORK_AND_SUB_AGENT_ORCHESTRATION/SAFE_PARALLELISM_MATRIX.md',
    root/'PARALLEL_WORK_AND_SUB_AGENT_ORCHESTRATION/MID_JOB_CONFLICT_FIX_POLICY.md',
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
