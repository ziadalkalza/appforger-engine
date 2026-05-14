#!/usr/bin/env python3
from pathlib import Path
root = Path(__file__).resolve().parents[1]
text=(root/'FLEXIBLE_WORKFLOW_AND_STAGE_OVERRIDES'/'WORKFLOW_VARIANT_TEMPLATES.md').read_text(encoding='utf-8')
required=['html_sandbox_first','existing_frontend_import','backendless_static_web','frontend_first_mock_api','figma_less_visual_baseline']
missing=[r for r in required if r not in text]
if missing:
    raise SystemExit('Missing workflow variants: '+', '.join(missing))
print('Workflow variant validation passed.')
