# Provider Selection Questionnaire

Ask tool consistency mode before asking preferred providers.

## Tool consistency mode

Options:

```text
A. Keep one tool family for dependent tasks.
B. Keep one tool family only for high-risk dependent tasks.
C. Allow mixed tools with reconciliation checks.
```

Recommended default: B.

## Provider preferences

Ask:

- Preferred planning/orchestration provider: ChatGPT, Claude, decide per task.
- Preferred code agent: Codex, Claude Code, other, decide per task.
- Preferred design/prototype tool: Figma, Figma Make, HTML sandbox, other.
- Preferred image/visual asset provider.
- Local/offline provider needs.

If provider choices conflict with the selected tool consistency mode, warn and ask the user to switch to one tool family or accept reconciliation requirements.
