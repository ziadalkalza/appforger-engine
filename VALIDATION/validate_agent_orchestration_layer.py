#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
required = [
    'policies/provider-adapters/parallel-agent-work/README.md',
    'policies/security-and-privacy/parallel-agent-work/agent-brand-family-policy.md',
    'policies/provider-adapters/parallel-agent-work/reconciliation-record-policy.md',
    'templates/execution-packets/generic/sub-agent-execution-packet.md',
    'templates/execution-packets/generic/parallel-work-plan-template.md',
    'skills/operations/create-parallel-work-plan/SKILL.md',
]
missing=[p for p in required if not (root/p).exists()]
if missing:
    print('Missing agent orchestration files:')
    for p in missing: print('-', p)
    sys.exit(1)
print('Agent orchestration layer validation passed.')
