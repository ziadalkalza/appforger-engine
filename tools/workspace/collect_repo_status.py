#!/usr/bin/env python3
"""
Print simple Git status for sibling repos in an AppForge workspace.
Run from workspace root, not from inside AppForge.
"""
from pathlib import Path
import subprocess

ROOT = Path.cwd()
for name in ["backend", "ios", "android", "design-assets", "appforge"]:
    path = ROOT / name
    if not path.exists():
        continue
    if not (path / ".git").exists():
        print(f"{name}: folder exists, not a git repo")
        continue
    try:
        out = subprocess.check_output(["git", "-C", str(path), "status", "--short"], text=True)
        branch = subprocess.check_output(["git", "-C", str(path), "branch", "--show-current"], text=True).strip()
        print(f"\n{name} [{branch}]")
        print(out.strip() or "clean")
    except Exception as e:
        print(f"{name}: error reading git status: {e}")
