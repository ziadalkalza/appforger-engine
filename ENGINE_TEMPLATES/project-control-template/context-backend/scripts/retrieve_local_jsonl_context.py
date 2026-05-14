#!/usr/bin/env python3
"""Simple local JSONL retrieval by keyword/metadata.

This is a starter, not a replacement for Qdrant/Supabase retrieval.
"""
from pathlib import Path
import argparse, json, re, datetime

def score(query, text):
    q=[w.lower() for w in re.findall(r'\w+', query)]
    t=text.lower()
    return sum(t.count(w) for w in q)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--workspace', required=True)
    ap.add_argument('--query', required=True)
    ap.add_argument('--index', default='project-control/context-backend/indexes/context.jsonl')
    ap.add_argument('--top-k', type=int, default=8)
    ap.add_argument('--out', default=None)
    args=ap.parse_args()
    ws=Path(args.workspace).resolve()
    idx=ws/args.index
    rows=[]
    for line in idx.read_text(encoding='utf-8').splitlines():
        if line.strip():
            rec=json.loads(line)
            s=score(args.query, rec.get('text',''))
            if s>0:
                rows.append((s, rec))
    rows=sorted(rows, key=lambda x:x[0], reverse=True)[:args.top_k]
    pack={'query':args.query,'generated_at':datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00','Z'),'results':[]}
    for s,rec in rows:
        pack['results'].append({
            'score':s,
            'source_path_or_url':rec.get('source_path_or_url'),
            'source_type':rec.get('source_type'),
            'artifact_type':rec.get('artifact_type'),
            'is_current':rec.get('is_current'),
            'retrieval_reason':f'keyword/metadata starter match, score={s}',
            'preview':rec.get('text','')[:500]
        })
    text=json.dumps(pack, indent=2, ensure_ascii=False)
    if args.out:
        out=ws/args.out; out.parent.mkdir(parents=True, exist_ok=True); out.write_text(text, encoding='utf-8')
        print(f'Wrote retrieval pack to {out}')
    else:
        print(text)
if __name__=='__main__': main()
