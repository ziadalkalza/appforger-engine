#!/usr/bin/env python3
import argparse, shutil, os, subprocess
from pathlib import Path

APPFORGE_ADAPTER_MARKER = "AppForger"
APPFORGE_MARKER_FILES = {
    "project-control": [
        "appforge-project.yaml",
        "APPFORGE_PROJECT.yaml",
        "appforge-active-rules.md",
        "APPFORGE_ACTIVE_RULES.md",
        "appforge-scaffold-summary.md",
    ],
    "local-only": [
        ".appforge-created",
    ],
    "appforger-engine": [
        "mcp/server/appforge_mcp_server.py",
        "registries/APPFORGE_FEATURE_MANIFEST.json",
    ],
}
SAFE_ROOT_FILES = [
    "APPFORGE_INJECTION_SUMMARY.md",
]
SAFE_ADAPTER_FILES = [
    "AGENTS.md",
    "CLAUDE.md",
    ".cursor/rules/appforge.mdc",
    ".github/copilot-instructions.md",
]

def rm(path, yes):
    if not path.exists(): return
    print(("delete: " if yes else "would delete: ") + str(path))
    if yes:
        if path.is_dir() and not path.is_symlink(): shutil.rmtree(path)
        else: path.unlink()

def is_empty_dir(path):
    return path.is_dir() and not any(path.iterdir())

def has_appforge_marker(path, marker_group):
    for rel in APPFORGE_MARKER_FILES.get(marker_group, []):
        if (path/rel).exists():
            return True
    return False

def rm_if_appforge_owned(path, yes, marker_group, allow_empty=False):
    if not path.exists():
        return
    if has_appforge_marker(path, marker_group) or (allow_empty and is_empty_dir(path)):
        rm(path, yes)
    else:
        print(f"skip, not proven AppForger-created: {path}")

def remove_generated_adapters(target, yes):
    for rel in SAFE_ADAPTER_FILES + SAFE_ROOT_FILES:
        p=Path(target)/rel
        if p.exists():
            txt=p.read_text(encoding="utf-8", errors="ignore")
            if APPFORGE_ADAPTER_MARKER in txt:
                rm(p, yes)
            else:
                print(f"skip, no AppForger marker: {p}")

def restore_adopted(target, yes):
    mf=Path(target)/"project-control/adoption/adoption-manifest.yaml"
    if not mf.exists(): return
    text=mf.read_text(encoding="utf-8", errors="ignore").splitlines()
    items=[]; cur={}
    for line in text:
        if line.strip().startswith("- "):
            if cur: items.append(cur); cur={}
        if ":" in line:
            k,v=line.split(":",1); cur[k.strip().lstrip("- ").strip()]=v.strip()
    if cur: items.append(cur)
    for it in items:
        if it.get("adoption_mode")=="move":
            src=Path(target)/it.get("adopted_path","")
            dst=Path(it.get("original_path",""))
            if dst.exists(): raise SystemExit(f"restore blocked, original path exists: {dst}")
            print(("restore: " if yes else "would restore: ") + f"{src} -> {dst}")
            if yes and src.exists():
                shutil.move(str(src), str(dst))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--target", default=".")
    ap.add_argument("--mode", choices=["remove-engine","remove-local","remove-project-keep-engine","remove-runtime-containers","remove-runtime-volumes"], required=True)
    ap.add_argument("--yes", action="store_true")
    ap.add_argument("--restore-adopted-sources", action="store_true")
    ap.add_argument("--project-name-confirmation", default="")
    args=ap.parse_args()
    target=Path(args.target).resolve()
    if args.restore_adopted_sources:
        restore_adopted(target,args.yes)
    if args.mode=="remove-local":
        rm_if_appforge_owned(target/"local-only", args.yes, "local-only", allow_empty=True)
    elif args.mode=="remove-engine":
        rm_if_appforge_owned(target/"project-control", args.yes, "project-control")
        rm_if_appforge_owned(target/"appforger-engine", args.yes, "appforger-engine")
        remove_generated_adapters(target,args.yes)
    elif args.mode=="remove-project-keep-engine":
        if not args.project_name_confirmation:
            raise SystemExit("project-name confirmation required")
        rm_if_appforge_owned(target/"project-control", args.yes, "project-control")
        rm_if_appforge_owned(target/"local-only", args.yes, "local-only", allow_empty=True)
        remove_generated_adapters(target,args.yes)
        print("skip generic project folders: docs, assets, exports, backend, web, mobile, ios, android")
    elif args.mode=="remove-runtime-containers":
        print("Use docker compose down via project-control/runtime/scripts/appforge_runtime.py down")
    elif args.mode=="remove-runtime-volumes":
        if not args.project_name_confirmation:
            raise SystemExit("project-name confirmation required for runtime volumes")
        print("Remove runtime volumes only after explicit confirmation; run docker compose down -v manually or through runtime script.")
if __name__=="__main__": main()
