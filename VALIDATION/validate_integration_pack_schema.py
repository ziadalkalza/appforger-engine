#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / 'integrations/catalog' / 'INTEGRATION_PACK_TEMPLATE'
required = [
    'README.md','BOUNDARY.md','CLARIFICATION_QUESTIONS.md','OFFICIAL_DOCS_RESEARCH.md',
    'SETUP_CHECKLIST.md','SECRETS_POLICY.md','COST_AND_RISK_REVIEW.md','SECURITY_PRIVACY_REVIEW.md',
    'BACKEND_RUNBOOK.md','FRONTEND_RUNBOOK.md','PLATFORM_SPECIFIC_RUNBOOKS.md','TEST_CHECKLIST.md',
    'FAILURE_RECOVERY.md','CODEX_PACKET_TEMPLATE.md','REGISTRY_UPDATES.md'
]
missing=[f for f in required if not (TEMPLATE/f).exists()]
if missing:
    print('Integration pack template missing files:')
    for f in missing: print('-', f)
    sys.exit(1)
print('Integration pack schema/template validation passed.')
