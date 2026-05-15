#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
required = [
    "runtime/context/context-backend/README.md",
    "runtime/context/apps/qdrant/QDRANT_SETUP_CHECKLIST.md",
    "runtime/context/apps/supabase/SUPABASE_CONTEXT_BACKEND_SETUP.md",
    "workflows/operations/context-sync-retrieval/RETRIEVE_CONTEXT_PACK.md",
    "templates/engine/project-control-template/context-backend/scripts/index_project_control.py",
    "templates/engine/project-control-template/context-backend/schemas/supabase_context_schema.sql",
    "skills/context/context-backend/setup_context_backend/SKILL.md",
]
missing = [p for p in required if not (root/p).exists()]
if missing:
    print("Missing context backend layer files:")
    for p in missing: print("-", p)
    sys.exit(1)
print("Context backend layer validation passed.")
