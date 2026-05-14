#!/usr/bin/env python3
"""Context backend health check starter."""
from pathlib import Path
import argparse, json, sys

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--workspace', required=True); args=ap.parse_args()
    ws=Path(args.workspace).resolve()
    issues=[]
    if not (ws/'project-control').exists(): issues.append('missing project-control/')
    if not (ws/'docs').exists(): issues.append('missing docs/')
    idx=ws/'project-control/context-backend/indexes/context.jsonl'
    if idx.exists():
        for i,line in enumerate(idx.read_text(encoding='utf-8').splitlines(),1):
            if not line.strip(): continue
            try:
                rec=json.loads(line)
            except Exception:
                issues.append(f'invalid JSONL line {i}')
                continue
            if not rec.get('source_path_or_url'): issues.append(f'missing source path line {i}')
    else:
        issues.append('local JSONL index not found')
    if issues:
        print('Context health warnings:')
        for x in issues: print('-', x)
        sys.exit(1)
    print('Context health check passed')
if __name__=='__main__': main()
