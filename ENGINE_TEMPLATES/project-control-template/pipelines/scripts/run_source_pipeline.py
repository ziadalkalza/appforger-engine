#!/usr/bin/env python3
import argparse, subprocess, sys, os
from pathlib import Path

def run(cmd):
    print(" ".join(cmd))
    return subprocess.call(cmd)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--target", default=".")
    ap.add_argument("--source")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--storage-mode", default="rag_only")
    ap.add_argument("--mock-confluence")
    ap.add_argument("--graph", action="store_true")
    args=ap.parse_args()
    target=Path(args.target)
    if args.all:
        sources=["product-space","backend-main"]
    else:
        sources=[args.source]
    rc=0
    for s in sources:
        if s in {"product-space"} or "space" in (s or ""):
            cmd=[sys.executable, str(target/"project-control/doc_sources/scripts/fetch_confluence.py"), "--target", str(target), "--source", s, "--storage-mode", args.storage_mode]
            if args.mock_confluence: cmd += ["--mock-json", args.mock_confluence]
            if args.graph: cmd += ["--graph"]
            rc=max(rc, run(cmd))
        else:
            cmd=[sys.executable, str(target/"project-control/code_sources/scripts/bootstrap_code_context.py"), "--target", str(target), "--source", s]
            rc=max(rc, run(cmd))
    raise SystemExit(rc)
if __name__=="__main__": main()
