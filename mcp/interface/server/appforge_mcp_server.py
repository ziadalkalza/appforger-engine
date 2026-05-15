#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from http.server import BaseHTTPRequestHandler, HTTPServer

THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(THIS_DIR))

from appforge_resource_provider import ResourceProvider
from appforge_prompt_provider import list_prompts, get_prompt
from appforge_tool_provider import tool_schemas, ToolProvider
from auth import check_http_authorization


class AppForgerMCP:
    def __init__(self, engine_root: Path):
        self.engine_root = engine_root.resolve()
        self.resources = ResourceProvider(self.engine_root)
        self.tools = ToolProvider(self.engine_root, self.resources)

    def handle(self, req: dict) -> dict:
        rid = req.get("id")
        method = req.get("method")
        params = req.get("params") or {}
        try:
            if method == "initialize":
                result = {
                    "protocolVersion": params.get("protocolVersion", "2025-06-18"),
                    "serverInfo": {"name":"appforger-mcp", "version":"1.0.0"},
                    "capabilities": {"resources": {}, "prompts": {}, "tools": {}}
                }
            elif method == "resources/list":
                result = {"resources": self.resources.list_resources()}
            elif method == "resources/read":
                r = self.resources.read_resource(params["uri"])
                result = {"contents": [{"uri": r["uri"], "mimeType": r.get("mimeType", "text/plain"), "text": r["text"]}]}
            elif method == "prompts/list":
                result = {"prompts": list_prompts()}
            elif method == "prompts/get":
                result = get_prompt(params["name"], params.get("arguments"))
            elif method == "tools/list":
                result = {"tools": tool_schemas()}
            elif method == "tools/call":
                data = self.tools.call(params["name"], params.get("arguments") or {})
                result = {"content": [{"type":"text", "text": json.dumps(data, indent=2)}]}
            elif method in {"notifications/initialized", "$/cancelRequest"}:
                return {}
            else:
                raise KeyError(f"Unsupported method: {method}")
            return {"jsonrpc":"2.0", "id": rid, "result": result}
        except Exception as e:
            return {"jsonrpc":"2.0", "id": rid, "error": {"code": -32000, "message": str(e)}}


def run_stdio(server: AppForgerMCP):
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = server.handle(req)
        except Exception as e:
            resp = {"jsonrpc":"2.0", "id": None, "error": {"code": -32700, "message": str(e)}}
        if resp:
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()


def make_handler(server: AppForgerMCP):
    class Handler(BaseHTTPRequestHandler):
        def _send(self, code: int, obj: dict):
            body = json.dumps(obj).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):
            if self.path in {"/health", "/"}:
                self._send(200, {"status":"ok", "server":"appforger-mcp"})
            else:
                self._send(404, {"error":"not found"})

        def do_POST(self):
            ok, reason = check_http_authorization(self.headers)
            if not ok:
                self._send(401, {"error": "unauthorized", "reason": reason})
                return
            length = int(self.headers.get("Content-Length", "0"))
            raw = self.rfile.read(length).decode("utf-8")
            try:
                req = json.loads(raw)
                if isinstance(req, list):
                    resp = [server.handle(x) for x in req]
                else:
                    resp = server.handle(req)
                self._send(200, resp)
            except Exception as e:
                self._send(400, {"jsonrpc":"2.0", "id": None, "error": {"code": -32700, "message": str(e)}})

        def log_message(self, fmt, *args):
            return
    return Handler


def main():
    ap = argparse.ArgumentParser(description="AppForger MCP logic server. Remote mode returns plans/commands only; it does not execute project actions.")
    ap.add_argument("--engine-root", default=str(Path(__file__).resolve().parents[3]))
    ap.add_argument("--workspace-root", default=None, help="Optional local workspace root for future local mode; not used for remote execution.")
    ap.add_argument("--transport", choices=["stdio","http"], default="stdio")
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=8080)
    args = ap.parse_args()
    server = AppForgerMCP(Path(args.engine_root))
    if args.transport == "stdio":
        run_stdio(server)
    else:
        httpd = HTTPServer((args.host, args.port), make_handler(server))
        print(f"AppForger MCP HTTP server listening on http://{args.host}:{args.port}", flush=True)
        httpd.serve_forever()


if __name__ == "__main__":
    main()
