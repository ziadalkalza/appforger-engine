# Codex Bootstrap Files

This folder contains copyable instruction files for using Appforger across separate repositories.

Appforger normally lives in its own engine/project-management repo, while backend, iOS, and Android code live in separate repos. To keep Codex aligned, each code repo should include either:

- a repo-specific `AGENTS.md`, or
- an `APPFORGER_POINTER.md` pointing back to the Appforger engine folder/repo.

## Recommended setup

```text
workspace/
  appforger-engine/
  backend-repo/
    AGENTS.md
    APPFORGER_POINTER.md
  ios-repo/
    AGENTS.md
    APPFORGER_POINTER.md
  android-repo/
    AGENTS.md
    APPFORGER_POINTER.md
```

The repo-specific `AGENTS.md` should remind Codex that implementation must follow Appforger project state, approvals, registries, and relevant skills.
