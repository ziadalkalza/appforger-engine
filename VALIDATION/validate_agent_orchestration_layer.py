#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
required = [
    'PARALLEL_WORK_AND_SUB_AGENT_ORCHESTRATION/README.md',
    'PARALLEL_WORK_AND_SUB_AGENT_ORCHESTRATION/AGENT_BRAND_FAMILY_POLICY.md',
    'PARALLEL_WORK_AND_SUB_AGENT_ORCHESTRATION/RECONCILIATION_RECORD_POLICY.md',
    'EXECUTION_PACKETS/SUB_AGENT_EXECUTION_PACKET.md',
    'EXECUTION_PACKETS/PARALLEL_WORK_PLAN_TEMPLATE.md',
    'SKILLS/agent_orchestration_skills/create_parallel_work_plan/SKILL.md',
]
missing=[p for p in required if not (root/p).exists()]
if missing:
    print('Missing agent orchestration files:')
    for p in missing: print('-', p)
    sys.exit(1)
print('Agent orchestration layer validation passed.')
