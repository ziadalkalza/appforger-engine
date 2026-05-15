#!/usr/bin/env python3
from pathlib import Path
import argparse, sys

REQUIRED = [
    "context-backend/config/context_backend_config.yaml",
    "context-backend/scripts/index_project_control.py",
    "context-backend/scripts/retrieve_context_pack.py",
    "context-backend/schemas/postgres_context_schema.sql",
    "context-backend/schemas/supabase_context_schema.sql",
]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--project-control", default=".")
    args = ap.parse_args()
    root = Path(args.project_control).resolve()
    missing = [r for r in REQUIRED if not (root/r).exists()]
    if missing:
        print("Missing context backend files:")
        for m in missing: print("-", m)
        sys.exit(1)
    print("Context backend scaffold validation passed.")

if __name__ == "__main__":
    main()
