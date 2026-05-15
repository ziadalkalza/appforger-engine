#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
required = [
    'policies/operations/parallel-agent-work/README.md',
    'policies/operations/parallel-agent-work/AGENT_BRAND_FAMILY_POLICY.md',
    'policies/operations/parallel-agent-work/RECONCILIATION_RECORD_POLICY.md',
    'templates/packets/execution-packets/SUB_AGENT_EXECUTION_PACKET.md',
    'templates/packets/execution-packets/PARALLEL_WORK_PLAN_TEMPLATE.md',
    'skills/operations/agent_orchestration_skills/create_parallel_work_plan/SKILL.md',
]
missing=[p for p in required if not (root/p).exists()]
if missing:
    print('Missing agent orchestration files:')
    for p in missing: print('-', p)
    sys.exit(1)
print('Agent orchestration layer validation passed.')
