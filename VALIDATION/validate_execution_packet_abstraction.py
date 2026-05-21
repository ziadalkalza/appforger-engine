from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
files = [
    root/'templates/execution-packets/generic/execution-packet-template.md',
    root/'templates/execution-packets/generic/code-agent-execution-packet.md',
    root/'templates/execution-packets/code-agent-packets/generic-code-agent-packet-template.md',
]
for f in files:
    text = f.read_text(encoding='utf-8') if f.exists() else ''
    for key in ['source_of_truth', 'required_capabilities', 'approval']:
        if key not in text.lower():
            print(f'Missing expected packet concept {key} in {f}')
            sys.exit(1)
print('Execution packet abstraction validation passed.')
