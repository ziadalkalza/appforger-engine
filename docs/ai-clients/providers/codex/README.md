# Codex Bootstrap Files

This folder contains copyable instruction files for using AppForge across separate repositories.

AppForge normally lives in its own engine/project-management repo, while backend, iOS, and Android code live in separate repos. To keep Codex aligned, each code repo should include either:

- a repo-specific `AGENTS.md`, or
- an `APPFORGE_POINTER.md` pointing back to the AppForge engine folder/repo.

## Recommended setup

```text
workspace/
  appforge-engine/
  backend-repo/
    AGENTS.md
    APPFORGE_POINTER.md
  ios-repo/
    AGENTS.md
    APPFORGE_POINTER.md
  android-repo/
    AGENTS.md
    APPFORGE_POINTER.md
```

The repo-specific `AGENTS.md` should remind Codex that implementation must follow AppForge project state, approvals, registries, and relevant skills.
