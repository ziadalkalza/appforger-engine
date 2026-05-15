#!/usr/bin/env python3
from pathlib import Path
import sys
root=Path(__file__).resolve().parents[1]
required=[
 root/'validation/audits/operational-audit/README.md',
 root/'validation/audits/operational-audit/OPERATIONAL_AUDIT_POLICY.md',
 root/'validation/audits/operational-audit/ENGINE_STRUCTURE_AUDIT.md',
 root/'validation/audits/operational-audit/SOURCE_OF_TRUTH_AUDIT.md',
 root/'validation/audits/operational-audit/WORKFLOW_COMPATIBILITY_AUDIT.md',
 root/'validation/audits/operational-audit/AUTOMATION_SAFETY_AUDIT.md',
 root/'validation/audits/operational-audit/END_TO_END_SCENARIO_TESTS.md',
]
missing=[str(p.relative_to(root)) for p in required if not p.exists()]
if missing:
 print('Missing operational audit files:')
 print('\n'.join(missing))
 sys.exit(1)
print('Operational audit layer validation passed.')
