from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
files = [
    root/'EXECUTION_PACKETS/EXECUTION_PACKET_TEMPLATE.md',
    root/'EXECUTION_PACKETS/CODE_AGENT_EXECUTION_PACKET.md',
    root/'CODEX_WORK_PACKETS/GENERIC_CODE_AGENT_PACKET_TEMPLATE.md',
]
for f in files:
    text = f.read_text(encoding='utf-8') if f.exists() else ''
    for key in ['source_of_truth', 'required_capabilities', 'approval']:
        if key not in text.lower():
            print(f'Missing expected packet concept {key} in {f}')
            sys.exit(1)
print('Execution packet abstraction validation passed.')
