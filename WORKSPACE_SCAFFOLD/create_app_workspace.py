#!/usr/bin/env python3
"""
Create an AppForge app workspace without putting app code inside the engine.

Usage:
  python create_app_workspace.py --name my-app --target /path/to/workspaces
"""
from pathlib import Path
import argparse
import shutil
import re

def safe_name(name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9._-]+", "-", name.strip()).strip("-").lower()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True, help="App/workspace name")
    parser.add_argument("--target", default=".", help="Parent directory")
    parser.add_argument("--copy-engine", action="store_true", help="Copy current AppForge engine into workspace/appforge")
    args = parser.parse_args()

    name = safe_name(args.name)
    parent = Path(args.target).resolve()
    workspace = parent / f"{name}-workspace"
    workspace.mkdir(parents=True, exist_ok=True)

    for folder in ["backend", "ios", "android", "design-assets", "exports", "local-only"]:
        (workspace / folder).mkdir(exist_ok=True)

    current_appforge = Path(__file__).resolve().parents[1]
    if args.copy_engine:
        dest = workspace / "appforge"
        if dest.exists():
            print(f"AppForge already exists: {dest}")
        else:
            shutil.copytree(current_appforge, dest, ignore=shutil.ignore_patterns(".git", "__pycache__"))
    else:
        (workspace / "APPFORGE_LOCATION.txt").write_text(
            f"Place or clone AppForge at: {workspace / 'appforge'}\n",
            encoding="utf-8",
        )

    print(f"Created workspace: {workspace}")
    print("Next: copy AGENTS.md and APPFORGE_POINTER.md templates into backend/ios/android repos.")

if __name__ == "__main__":
    main()
