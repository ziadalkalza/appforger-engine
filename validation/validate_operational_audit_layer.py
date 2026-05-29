#!/usr/bin/env python3
from pathlib import Path
import sys
root=Path(__file__).resolve().parents[1]
required=[
 root/'validation/operational-audits/operational-audit/README.md',
 root/'validation/operational-audits/operational-audit/operational-audit-policy.md',
 root/'validation/operational-audits/operational-audit/engine-structure-audit.md',
 root/'validation/operational-audits/operational-audit/source-of-truth-audit.md',
 root/'validation/operational-audits/operational-audit/workflow-compatibility-audit.md',
 root/'validation/operational-audits/operational-audit/automation-safety-audit.md',
 root/'validation/operational-audits/operational-audit/end-to-end-scenario-tests.md',
]
missing=[str(p.relative_to(root)) for p in required if not p.exists()]
if missing:
 print('Missing operational audit files:')
 print('\n'.join(missing))
 sys.exit(1)
print('Operational audit layer validation passed.')
