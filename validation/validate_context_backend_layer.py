#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
required = [
    "runtime/context-backend/README.md",
    "runtime/context-backend/qdrant/qdrant-setup-checklist.md",
    "runtime/backend-platforms/supabase/supabase-context-backend-setup.md",
    "workflows/operations/context-sync-retrieval/retrieve-context-pack.md",
    "templates/project-control/context-backend/scripts/index_project_control.py",
    "templates/project-control/context-backend/schemas/supabase_context_schema.sql",
    "skills/context-backend/setup-context-backend/SKILL.md",
]
missing = [p for p in required if not (root/p).exists()]
if missing:
    print("Missing context backend layer files:")
    for p in missing: print("-", p)
    sys.exit(1)
print("Context backend layer validation passed.")
