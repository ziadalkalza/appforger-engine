# Sub-Agent Model

A sub-agent is a scoped execution unit, not necessarily an autonomous AI.

A sub-agent must define:
- agent ID
- role
- provider or human executor
- brand family
- execution packet
- allowed repos/paths
- forbidden actions
- dependencies
- expected outputs
- completion evidence
- audit log destination

Sub-agents can be executed by:
- Codex
- Claude Code
- ChatGPT/Claude in planning or draft-only mode
- a human developer/designer/tester
- future Appforger MCP/server workers

A sub-agent must not infer permission from its title. Permission is granted only through its packet and the active project policies.
