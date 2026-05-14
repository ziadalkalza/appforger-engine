#!/usr/bin/env python3
import argparse, shutil, os, sys
from pathlib import Path

ROLE_DIR = {"backend":"backend","web":"web","frontend":"web","mobile":"mobile","ios":"ios","android":"android"}

def append_gitignore(target):
    block = """# >>> AppForger managed ignore rules
/appforge-engine/
/local-only/
*.local.yaml
*.local.env
.env
.env.*
# <<< AppForger managed ignore rules
"""
    gi = Path(target)/".gitignore"
    cur = gi.read_text(encoding="utf-8") if gi.exists() else ""
    if "# >>> AppForger managed ignore rules" not in cur:
        gi.write_text((cur.rstrip()+"\n\n"+block).lstrip(), encoding="utf-8")

def scan(target):
    target=Path(target)
    for p in target.iterdir():
        if p.is_dir() and p.name not in {"appforge-engine","project-control","local-only",".git"}:
            print(f"candidate: {p.name}")

def adopt(target, sources, apply=False, yes=False):
    target=Path(target)
    manifest = target/"project-control/adoption/adoption-manifest.yaml"
    manifest.parent.mkdir(parents=True, exist_ok=True)
    lines = ["adopted_sources:"]
    for spec in sources:
        role, rest = spec.split("=",1)
        path_s, mode = rest.split(":",1) if ":" in rest else (rest,"register")
        src=Path(path_s)
        dst=target/ROLE_DIR.get(role, role)
        if mode in {"move","copy","symlink"} and not (apply and yes):
            raise SystemExit("Physical adoption requires --apply --yes after approval file.")
        if mode=="move":
            if dst.exists(): raise SystemExit(f"target exists: {dst}")
            shutil.move(str(src), str(dst))
        elif mode=="copy":
            if dst.exists(): raise SystemExit(f"target exists: {dst}")
            shutil.copytree(src,dst)
        elif mode=="symlink":
            if dst.exists(): raise SystemExit(f"target exists: {dst}")
            dst.symlink_to(src.resolve(), target_is_directory=True)
        lines += [f"  - role: {role}", f"    original_path: {src}", f"    adopted_path: {dst.relative_to(target)}", f"    adoption_mode: {mode}", f"    reversible: {str(mode=='move').lower()}"]
    manifest.write_text("\n".join(lines)+"\n", encoding="utf-8")
    append_gitignore(target)
    print(f"wrote {manifest}")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--target", default=".")
    sub=ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("scan")
    ad=sub.add_parser("adopt"); ad.add_argument("--source", action="append", default=[]); ad.add_argument("--apply", action="store_true"); ad.add_argument("--yes", action="store_true")
    args=ap.parse_args()
    if args.cmd=="scan": scan(args.target)
    if args.cmd=="adopt": adopt(args.target, args.source, args.apply, args.yes)
if __name__=="__main__": main()
