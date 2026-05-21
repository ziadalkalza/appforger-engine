#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import sys

SETUP_DIR = Path(__file__).resolve().parents[1] / "new-app-initializer"
sys.path.insert(0, str(SETUP_DIR))

from setup_appforge_project import PROJECT_CONTROL_MODULES, copy_path


def enable_module(engine_root: Path, target: Path, module: str) -> None:
    module = module.lower().strip()
    if module not in PROJECT_CONTROL_MODULES:
        known = ", ".join(sorted(PROJECT_CONTROL_MODULES))
        raise SystemExit(f"Unknown project-control module: {module}. Known modules: {known}")
    src = engine_root / "templates" / "project-control"
    dst = target / "project-control"
    dst.mkdir(parents=True, exist_ok=True)
    for rel in PROJECT_CONTROL_MODULES[module]:
        copy_path(src, dst, Path(rel))
    log = dst / "appforge-scaffold-summary.md"
    with log.open("a", encoding="utf-8") as f:
        f.write(f"\nEnabled module: {module}\n")


def main() -> None:
    ap = argparse.ArgumentParser(description="Enable optional AppForger project-control modules after onboarding changes.")
    ap.add_argument("--target", default=".", help="Project root containing project-control/.")
    ap.add_argument("--engine-root", default=str(Path(__file__).resolve().parents[3]))
    ap.add_argument("action", choices=["enable", "list"])
    ap.add_argument("--module", action="append", default=[], help="Module to enable. May be passed multiple times.")
    args = ap.parse_args()

    if args.action == "list":
        print("\n".join(sorted(PROJECT_CONTROL_MODULES)))
        return

    if not args.module:
        raise SystemExit("At least one --module is required for enable.")

    engine_root = Path(args.engine_root).resolve()
    target = Path(args.target).resolve()
    for module in args.module:
        enable_module(engine_root, target, module)
        print(f"Enabled project-control module '{module}' in {target}")


if __name__ == "__main__":
    main()
