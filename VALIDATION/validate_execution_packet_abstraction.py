from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
files = [
    root/'templates/packets/execution-packets/EXECUTION_PACKET_TEMPLATE.md',
    root/'templates/packets/execution-packets/CODE_AGENT_EXECUTION_PACKET.md',
    root/'templates/packets/code-agent-packets/GENERIC_CODE_AGENT_PACKET_TEMPLATE.md',
]
for f in files:
    text = f.read_text(encoding='utf-8') if f.exists() else ''
    for key in ['source_of_truth', 'required_capabilities', 'approval']:
        if key not in text.lower():
            print(f'Missing expected packet concept {key} in {f}')
            sys.exit(1)
print('Execution packet abstraction validation passed.')
