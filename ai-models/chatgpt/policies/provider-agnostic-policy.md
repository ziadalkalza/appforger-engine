# Provider Agnostic Policy

Appforger must not assume a task belongs to ChatGPT, Codex, Claude, Claude Code, Figma, or any other provider by default.

## Required behavior

1. Identify the task type.
2. Identify required capabilities.
3. Check active provider preferences in project-control.
4. Recommend the best provider/tool.
5. If the current provider is not suitable, warn the user and offer:
   - create an execution packet for the right provider, or
   - continue here in draft-only/planning-only mode.
6. Record provider decisions when they affect execution, privacy, cost, security, or project state.

## Specific provider profiles

Specific provider profiles must be based on current official/provider documentation or user-supplied setup information. If current details cannot be verified, mark the profile or recommendation as draft-only.
