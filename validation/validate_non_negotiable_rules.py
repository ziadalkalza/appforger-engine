#!/usr/bin/env python3
from pathlib import Path
root = Path(__file__).resolve().parents[1]
text=(root/'policies/operations/workflow-stage-overrides'/'NON_NEGOTIABLE_RULES.md').read_text(encoding='utf-8').lower()
required=['secrets','security','privacy','release blocker','source-of-truth','draft/sandbox']
missing=[r for r in required if r not in text]
if missing:
    raise SystemExit('Missing non-negotiable topics: '+', '.join(missing))
print('Non-negotiable rules validation passed.')
