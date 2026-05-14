#!/usr/bin/env python3
from pathlib import Path
root=Path(__file__).resolve().parents[1]
required=['DOC_SOURCE_INTEGRATIONS/README.md', 'DOC_SOURCE_INTEGRATIONS/python/doc_source_integrations/confluence_provider.py', 'ENGINE_TEMPLATES/project-control-template/doc_sources/scripts/fetch_confluence.py', 'SKILLS/doc_source_skills/fetch_confluence_source/SKILL.md']
missing=[r for r in required if not (root/r).exists()]
if missing:
    print("missing:", missing); raise SystemExit(1)
print("validate_doc_source_integrations: OK")
