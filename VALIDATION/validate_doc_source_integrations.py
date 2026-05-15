#!/usr/bin/env python3
from pathlib import Path
root=Path(__file__).resolve().parents[1]
required=['integrations/document-sources/confluence/README.md', 'integrations/document-sources/confluence/python/doc_source_integrations/confluence_provider.py', 'templates/engine/project-control-template/doc_sources/scripts/fetch_confluence.py', 'skills/integrations/apps/confluence/fetch_source/SKILL.md']
missing=[r for r in required if not (root/r).exists()]
if missing:
    print("missing:", missing); raise SystemExit(1)
print("validate_doc_source_integrations: OK")
