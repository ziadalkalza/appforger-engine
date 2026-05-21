#!/usr/bin/env python3
from pathlib import Path
import json, sys
root = Path(__file__).resolve().parents[1]
required = [
    'workflows/integration-strategy/integration-strategy-advisor/README.md',
    'workflows/integration-strategy/integration-strategy-advisor/integration-strategy-policy.md',
    'workflows/integration-strategy/integration-strategy-advisor/connector-first-policy.md',
    'workflows/integration-strategy/integration-strategy-advisor/connector-vs-api-decision-tree.md',
    'workflows/integration-strategy/integration-strategy-advisor/official-connector-research-policy.md',
    'workflows/integration-strategy/integration-strategy-advisor/hybrid-integration-policy.md',
    'workflows/integration-strategy/integration-strategy-advisor/custom-code-iteration-policy.md',
    'skills/integration-strategy/strategy/choose-integration-approach/SKILL.md',
    'skills/integration-strategy/strategy/research-official-connectors/SKILL.md',
    'skills/integration-strategy/strategy/plan-hybrid-integration/SKILL.md',
    'templates/project-control/integrations/integration-strategy-registry.yaml',
    'templates/project-control/integrations/integration-decision-log.md',
    'templates/project-control/integrations/connector-catalog.yaml',
    'templates/project-control/integrations/integration-decision-packet.template.md',
    'mcp/docs/feature-guides/integration-strategy-advisor.md',
    'templates/integration-strategy/mcp-prompts/choose-integration-approach.md',
]
missing = [p for p in required if not (root/p).exists()]
if missing:
    print('Missing Integration Strategy Advisor paths:')
    for p in missing: print('-', p)
    sys.exit(1)
policy=(root/'workflows/integration-strategy/integration-strategy-advisor/integration-strategy-policy.md').read_text(encoding='utf-8')
needles=['official connector','custom API/Python','decision packet']
for n in needles:
    if n.lower() not in policy.lower():
        print('Policy missing wording:', n)
        sys.exit(1)
# MCP resource check
m=root/'mcp/MCP_RESOURCE_MAP.json'
if m.exists():
    data=json.loads(m.read_text(encoding='utf-8'))
    ids={r.get('id') for r in data.get('resources',[])}
    for rid in ['integration-strategy-policy','integration-strategy-skill','connector-catalog-template']:
        if rid not in ids:
            print('MCP resource map missing', rid)
            sys.exit(1)
print('validate_integration_strategy_advisor: OK')
