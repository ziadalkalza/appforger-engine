from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'WEB_FRONTEND/README.md',
    'WEB_FRONTEND/web_stack_selection.md',
    'FIGMA_TO_WEB_MAPPING/FIGMA_TO_REACT_MAPPING.md',
    'WEB_DEPLOYMENT/README.md',
    'WEB_QA/PLAYWRIGHT_WORKFLOW.md',
    'SKILLS/web_skills/select_web_stack/SKILL.md',
    'CODEX_WORK_PACKETS/CODEX_WEB_PACKET_TEMPLATE.md',
    'REGISTRIES/WEB_ROUTE_REGISTRY.md',
]
missing = [p for p in REQUIRED if not (ROOT / p).exists()]
if missing:
    print('Missing web track files:')
    for p in missing:
        print('-', p)
    raise SystemExit(1)
print('AppForge web track validation passed.')
