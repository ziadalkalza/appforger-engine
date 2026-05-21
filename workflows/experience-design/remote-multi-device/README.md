# Remote and Multi-Device Workflows

This folder defines how Appforger works when frontend, backend, design, QA, or project-control work happens on different devices or by different people.

Appforger does not require every repo to be local on one machine. It requires that every needed context source is either:

- locally available,
- available through a GitHub/connector/MCP route,
- supplied as an approved artifact packet, or
- explicitly marked not required for the current task.

## Core rule

No task may depend on another person's local machine as the only source of truth.

For multi-device work, `project-control/` and implementation repos must be synchronized through GitHub or another approved remote source.

## Read next

1. `LOCAL_VS_REMOTE_CONTEXT_POLICY.md`
2. `MULTI_DEVICE_WORKSPACE_SETUP.md`
3. `REMOTE_REPO_ACCESS_POLICY.md`
4. `GITHUB_CONTEXT_FETCH_PROTOCOL.md`
5. `CROSS_DEVICE_HANDOFF_PROTOCOL.md`
6. `PROJECT_CONTROL_FRESHNESS_POLICY.md`
7. `FRONTEND_BACKEND_DEVICE_SPLIT.md`
8. `REMOTE_CONTEXT_VALIDATION_CHECKLIST.md`
