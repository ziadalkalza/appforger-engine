#!/usr/bin/env python3
"""Build a simple local JSONL context index from project-control Markdown and docs summaries.

This starter script is intentionally conservative:
- indexes project-control Markdown
- indexes docs/summaries Markdown if present
- excludes secrets, local-only, binaries, and sensitive docs by default
- writes source metadata for each record
"""
from pathlib import Path
import json, argparse, hashlib, datetime

EXCLUDE_NAMES = {'.env', '.env.local', 'node_modules', 'build', 'dist', '.git'}

def should_index(path: Path) -> bool:
    if any(part in EXCLUDE_NAMES for part in path.parts):
        return False
    return path.suffix.lower() in {'.md', '.txt'}

def record_for(path: Path, workspace: Path):
    text = path.read_text(encoding='utf-8', errors='ignore')
    rel = path.relative_to(workspace).as_posix()
    return {
        'context_id': hashlib.sha1(rel.encode()).hexdigest()[:16],
        'source_path_or_url': rel,
        'source_type': 'docs_summary' if rel.startswith('docs/summaries/') else 'project_control',
        'artifact_type': 'markdown',
        'approval_status': 'unknown',
        'lifecycle_status': 'unknown',
        'is_current': True,
        'sensitivity': 'unknown',
        'indexing_allowed': True,
        'last_indexed': datetime.date.today().isoformat(),
        'text': text[:20000],
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--workspace', required=True)
    ap.add_argument('--out', default='project-control/context-backend/indexes/context.jsonl')
    args = ap.parse_args()
    ws = Path(args.workspace).resolve()
    out = ws / args.out
    out.parent.mkdir(parents=True, exist_ok=True)
    roots = [ws/'project-control', ws/'docs'/'summaries']
    count=0
    with out.open('w', encoding='utf-8') as f:
        for root in roots:
            if not root.exists():
                continue
            for p in root.rglob('*'):
                if p.is_file() and should_index(p):
                    f.write(json.dumps(record_for(p, ws), ensure_ascii=False)+'\n')
                    count += 1
    print(f'Wrote {count} records to {out}')

if __name__ == '__main__':
    main()
