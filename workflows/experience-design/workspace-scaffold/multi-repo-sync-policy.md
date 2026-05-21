# Multi-Repo Sync Policy

Each code repo owns its own implementation history.

Appforger tracks:
- repo URLs
- active branches
- packet IDs
- PR links
- test results
- design/API baselines

Implementation repos track:
- source code
- tests
- build files
- repo-specific AGENTS.md
- APPFORGER_POINTER.md

A PR is not complete until Appforger registry updates are recorded or explicitly deferred.
