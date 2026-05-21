# Connector, MCP, and Skill Lifecycle

This folder tracks whether Appforger capabilities are merely documented, generated, installed, authorized, validated, or active.

Core rule:

```text
Appforger may generate connector/MCP/skill definitions, but it must not assume they are usable until validation passes.
```

This prevents confusion between:

- a skill file existing,
- Codex actually loading/using the skill,
- an MCP config template existing,
- the MCP server being installed and authorized,
- a connector being listed,
- the connector actually being active.
