#!/usr/bin/env python3
"""Validate remote/multi-device AppForge context readiness.

This script checks that project-control exists and that repo access metadata is present.
It does not require network access; it validates declared structure and local paths.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import sys

REQUIRED_PROJECT_CONTROL_FILES = [
    'APPFORGE_PROJECT_STATUS.md',
    'APPFORGE_PROJECT.yaml',
    'REGISTRIES/REPO_REGISTRY.md',
    'REGISTRIES/REMOTE_CONTEXT_REGISTRY.md',
    'REGISTRIES/DEVICE_WORKSPACE_REGISTRY.md',
]


def check(path: Path, label: str, errors: list[str]):
    if not path.exists():
        errors.append(f'MISSING {label}: {path}')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--workspace', required=True, help='Workspace root containing project-control and repos')
    ap.add_argument('--require', default='', help='Comma-separated repos required locally: backend,ios,android,web,design-assets')
    args = ap.parse_args()
    ws = Path(args.workspace).resolve()
    errors: list[str] = []
    pc = ws / 'project-control'
    check(pc, 'project-control folder', errors)
    for rel in REQUIRED_PROJECT_CONTROL_FILES:
        check(pc / rel, rel, errors)
    for repo in [r.strip() for r in args.require.split(',') if r.strip()]:
        check(ws / repo, f'required local repo/folder {repo}', errors)
    if errors:
        print('Remote context validation failed:')
        for e in errors:
            print('-', e)
        sys.exit(1)
    print('Remote context validation passed.')

if __name__ == '__main__':
    main()
