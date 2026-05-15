from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'workflows/implementation/web-frontend/README.md',
    'workflows/implementation/web-frontend/web_stack_selection.md',
    'integrations/design/apps/figma/to-web/FIGMA_TO_REACT_MAPPING.md',
    'workflows/delivery/web-deployment/README.md',
    'validation/domains/web-qa/PLAYWRIGHT_WORKFLOW.md',
    'skills/implementation/web_skills/select_web_stack/SKILL.md',
    'templates/packets/code-agent-packets/providers/codex/CODEX_WEB_PACKET_TEMPLATE.md',
    'registries/WEB_ROUTE_REGISTRY.md',
]
missing = [p for p in REQUIRED if not (ROOT / p).exists()]
if missing:
    print('Missing web track files:')
    for p in missing:
        print('-', p)
    raise SystemExit(1)
print('AppForge web track validation passed.')
