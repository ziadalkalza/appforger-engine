#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
required = [
 'policies/providers/connector-mcp-skill-lifecycle/LIFECYCLE_STATUS_MODEL.md',
 'policies/providers/connector-mcp-skill-lifecycle/SKILL_LIFECYCLE_POLICY.md',
 'policies/providers/connector-mcp-skill-lifecycle/MCP_LIFECYCLE_POLICY.md',
 'policies/providers/connector-mcp-skill-lifecycle/CONNECTOR_LIFECYCLE_POLICY.md',
 'registries/CONNECTOR_LIFECYCLE_REGISTRY.md',
 'registries/MCP_LIFECYCLE_REGISTRY.md',
 'registries/SKILL_LIFECYCLE_REGISTRY.md',
]
missing=[p for p in required if not (ROOT/p).exists()]
if missing:
 print('Capability lifecycle missing files:')
 for p in missing: print('-', p)
 sys.exit(1)
print('Capability lifecycle validation passed.')
