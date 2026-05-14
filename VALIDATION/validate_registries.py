#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
registry_dir = ROOT / "REGISTRIES"
if not registry_dir.exists():
    print("REGISTRIES directory missing.")
    sys.exit(1)

files = list(registry_dir.glob("*.md"))
empty = [f.name for f in files if len(f.read_text(encoding="utf-8", errors="ignore").strip()) < 20]
if empty:
    print("Warning: very small/empty registry files:")
    for f in empty:
        print("-", f)

print(f"Found {len(files)} registry files.")
