# Code-Agent Execution Packet

Use for Codex, Claude Code, Cursor-like agents, Aider-like tools, Continue-like tools, or approved local code agents.

Must include:

- target repo and branch
- files/directories to inspect first
- likely files to edit
- forbidden paths
- source baselines
- tests/build commands
- done report destination
- registry update permissions

## Required packet metadata

Every code-agent execution packet must include `source_of_truth`, `required_capabilities`, and `approval_requirements` fields before execution.
