# Parallel Work and Sub-Agent Orchestration

This layer lets Appforger coordinate multiple role-scoped workers without pretending that the file-based engine can launch autonomous agents by itself.

A sub-agent is a bounded worker defined by an execution packet. The worker may be Codex, Claude Code, ChatGPT in draft-only mode, a human team member, or a future MCP/server agent.

Parallel work is allowed only when a formal parallel work plan exists, dependencies are declared, conflict risk is classified, and every agent has an output contract and audit trail.

Key rules:
- Appforger is provider-agnostic, but brand-family consistency is preferred for dependent work.
- Multiple agents may touch the same repo only on separate branches and non-overlapping paths, with conflict risk recorded.
- Project-control updates in team mode must use separate PRs.
- Agents may propose baseline updates; approval remains with the assigned user/role unless explicitly authorized.
- Draft/sandbox agents cannot update approved baselines until promoted.
- Mock-first frontend/backend parallelism is allowed when the mock contract is recorded.
