#!/usr/bin/env python3
from pathlib import Path
import json, subprocess, sys, tempfile
root = Path(__file__).resolve().parents[1]
base = root / 'APPFORGE_MCP_SERVER'
required = [
 'README.md','INSTALL_AND_USE.md','REMOTE_HOSTING_GUIDE.md','SECURITY_AND_APPROVAL_POLICY.md',
 'MCP_RESOURCE_MAP.json','MCP_PROMPT_CATALOG.md','MCP_TOOL_CATALOG.md',
 'server/appforge_mcp_server.py','server/auth.py','server/appforge_resource_provider.py','server/appforge_prompt_provider.py',
 'server/appforge_tool_provider.py','server/appforge_risk_classifier.py','server/manifest_loader.py',
 'deployment/docker/Dockerfile','deployment/docker/docker-compose.mcp.yml',
 'deployment/digitalocean/digitalocean-app.yaml.example','deployment/digitalocean/DIGITALOCEAN_DEPLOYMENT_GUIDE.md',
 'deployment/env/mcp.env.example',
 'client_examples/claude_desktop_config.json','client_examples/cursor_config_example.json','client_examples/vscode_mcp_example.json',
 'client_examples/chatgpt_connector_notes.md','client_examples/gemini_cli_mcp_config.json','client_examples/generic_stdio_example.md',
 'client_examples/generic_streamable_http_example.md'
]
missing=[p for p in required if not (base/p).exists()]
if missing:
    print('Missing AppForger MCP files:')
    print('\n'.join('- '+m for m in missing))
    sys.exit(1)
# Resource map should be valid and only reference existing or optional paths.
rm=json.loads((base/'MCP_RESOURCE_MAP.json').read_text(encoding='utf-8'))
if rm.get('exposure_mode') != 'manifest_selected':
    print('MCP_RESOURCE_MAP.json must use exposure_mode=manifest_selected')
    sys.exit(1)
missing_resources=[]
for r in rm.get('resources',[]):
    p=root/r['path']
    if not p.exists() and not r.get('optional'):
        missing_resources.append((r['uri'], r['path']))
if missing_resources:
    print('Missing MCP resources:')
    for uri, path in missing_resources:
        print(f'- {uri}: {path}')
    sys.exit(1)
# Remote boundary checks: no project action execution should be advertised.
text='\n'.join(p.read_text(encoding='utf-8', errors='replace') for p in [base/'README.md', base/'SECURITY_AND_APPROVAL_POLICY.md', base/'REMOTE_HOSTING_GUIDE.md'])
required_phrases=['does not execute project actions','command references','requires_user_approval','mcp_executes: false']
for phrase in required_phrases:
    if phrase not in text:
        print(f'Missing MCP safety phrase: {phrase}')
        sys.exit(1)
# Smoke JSON-RPC stdio.
server = base/'server/appforge_mcp_server.py'
proc = subprocess.Popen([sys.executable, str(server), '--engine-root', str(root), '--transport', 'stdio'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
try:
    proc.stdin.write(json.dumps({'jsonrpc':'2.0','id':1,'method':'initialize','params':{}})+'\n')
    proc.stdin.write(json.dumps({'jsonrpc':'2.0','id':2,'method':'tools/list','params':{}})+'\n')
    proc.stdin.flush()
    out1=proc.stdout.readline(); out2=proc.stdout.readline()
finally:
    proc.kill()
if 'appforger-mcp' not in out1 or 'list_features' not in out2:
    print('MCP stdio smoke test failed')
    print(out1); print(out2)
    sys.exit(1)
print('validate_appforger_mcp_server: OK')
