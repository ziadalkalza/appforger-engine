# ChatGPT to Codex Handoff

When ChatGPT has completed planning or review, it should produce a execution packet instead of directly editing app code.

## Packet minimum

```text
Target repo:
Task name:
Current Appforger stage:
Required Appforger files to read:
Relevant design/API packets:
Implementation scope:
Out of scope:
Acceptance criteria:
Tests to run:
Registry updates required:
Rollback notes:
```

## Handoff rule

ChatGPT prepares intent and context. Codex applies code changes in the target repo.

After Codex finishes, it must report:
- changed files
- tests run
- build status
- screenshots if UI changed
- unresolved issues
- whether Appforger registries need updates
