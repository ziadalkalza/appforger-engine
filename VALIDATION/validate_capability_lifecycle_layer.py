#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
required = [
 'CONNECTOR_MCP_SKILL_LIFECYCLE/LIFECYCLE_STATUS_MODEL.md',
 'CONNECTOR_MCP_SKILL_LIFECYCLE/SKILL_LIFECYCLE_POLICY.md',
 'CONNECTOR_MCP_SKILL_LIFECYCLE/MCP_LIFECYCLE_POLICY.md',
 'CONNECTOR_MCP_SKILL_LIFECYCLE/CONNECTOR_LIFECYCLE_POLICY.md',
 'REGISTRIES/CONNECTOR_LIFECYCLE_REGISTRY.md',
 'REGISTRIES/MCP_LIFECYCLE_REGISTRY.md',
 'REGISTRIES/SKILL_LIFECYCLE_REGISTRY.md',
]
missing=[p for p in required if not (ROOT/p).exists()]
if missing:
 print('Capability lifecycle missing files:')
 for p in missing: print('-', p)
 sys.exit(1)
print('Capability lifecycle validation passed.')
