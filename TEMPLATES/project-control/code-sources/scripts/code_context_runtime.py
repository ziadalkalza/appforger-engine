from pathlib import Path
import re, json, os

EXTS={".py",".js",".jsx",".ts",".tsx",".dart",".swift",".kt",".kts"}

def scan_files(base):
    base=Path(base)
    for p in base.rglob("*"):
        if p.is_file() and p.suffix in EXTS and ".git" not in p.parts:
            yield p

def parse_symbols(path):
    text=path.read_text(encoding="utf-8", errors="ignore")
    out=[]
    for pat,kind in [(r"^\s*def\s+([A-Za-z_]\w*)","function"),(r"^\s*class\s+([A-Za-z_]\w*)","class"),(r"function\s+([A-Za-z_]\w*)","function"),(r"class\s+([A-Za-z_]\w*)","class")]:
        for m in re.finditer(pat,text,re.M):
            out.append({"name":m.group(1),"kind":kind,"line":text[:m.start()].count("\n")+1})
    for m in re.finditer(r"@(app|router)\.(get|post|put|delete|patch)\(['\"]([^'\"]+)", text):
        out.append({"name":m.group(3),"kind":"api_endpoint","method":m.group(2).upper(),"line":text[:m.start()].count("\n")+1})
    return out

def build_context(target, source_id="backend-main", source_path="backend"):
    target=Path(target)
    src=target/source_path
    outdir=target/"project-control/code_sources"/source_id
    outdir.mkdir(parents=True, exist_ok=True)
    files=[]; nodes=[]; edges=[]; chunks=[]
    for p in scan_files(src):
        rel=p.relative_to(target).as_posix()
        symbols=parse_symbols(p)
        files.append({"path":rel,"symbols":symbols})
        nodes.append({"id":f"file:{rel}","type":"CodeFile","path":rel})
        for s in symbols:
            sid=f"symbol:{rel}:{s.get('name')}"
            nodes.append({"id":sid,"type":s.get("kind","Symbol"),"name":s.get("name"),"path":rel})
            edges.append({"from":f"file:{rel}","to":sid,"type":"CONTAINS"})
        chunks.append({"source_id":source_id,"source_type":"code_summary","path":rel,"text":f"{rel}: {', '.join(s['name'] for s in symbols[:20])}"})
    (outdir/"repo-summary.md").write_text(f"# {source_id} Summary\n\nFiles scanned: {len(files)}\n", encoding="utf-8")
    (outdir/"symbol-map.json").write_text(json.dumps(files,indent=2), encoding="utf-8")
    (outdir/"api-route-map.md").write_text("# API Route Map\n\n"+"\n".join(f"- {s.get('method','')} {s['name']} ({f['path']})" for f in files for s in f["symbols"] if s["kind"]=="api_endpoint"), encoding="utf-8")
    (outdir/"dependency-map.md").write_text("# Dependency Map\n\nGenerated from source scan.\n", encoding="utf-8")
    idx=target/"project-control/context-backend/local-jsonl/source_index.jsonl"; idx.parent.mkdir(parents=True, exist_ok=True)
    with idx.open("a",encoding="utf-8") as fh:
        for c in chunks: fh.write(json.dumps(c)+"\n")
    gdir=target/"project-control/runtime/graph"; gdir.mkdir(parents=True, exist_ok=True)
    (gdir/"graph_nodes.jsonl").write_text("\n".join(json.dumps(n) for n in nodes)+"\n", encoding="utf-8")
    (gdir/"graph_edges.jsonl").write_text("\n".join(json.dumps(e) for e in edges)+"\n", encoding="utf-8")
    return {"files":len(files),"nodes":len(nodes),"edges":len(edges)}
