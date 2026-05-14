#!/usr/bin/env python3
from pathlib import Path
import sys,re
engine=Path(__file__).resolve().parents[1]
policy=(engine/'OPERATIONAL_AUDIT/SOURCE_OF_TRUTH_AUDIT.md').read_text(encoding='utf-8').lower()
required=['project-control','canonical','rag/qdrant','retrieval','drafts/sandboxes','approved visual baseline']
missing=[x for x in required if x not in policy]
if missing:
 print('Source-of-truth policy missing terms:', missing)
 sys.exit(1)
print('Source-of-truth rules validation passed.')
