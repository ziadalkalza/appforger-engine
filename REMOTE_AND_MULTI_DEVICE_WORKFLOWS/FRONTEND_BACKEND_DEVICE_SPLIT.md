# Frontend / Backend Device Split

## Scenario

Frontend code is on one device and backend code is on another.

## Required shared context

At minimum, both devices need access to:

- `project-control/`, preferably through GitHub,
- relevant implementation repo remote URLs,
- approved design baseline,
- approved or draft API baseline,
- change request registry.

## Backend device responsibility

After backend work:

1. Push backend code or PR.
2. Record branch/commit/PR in `REPO_REGISTRY.md` or handoff registry.
3. Update `API_REGISTRY.md` and `DATA_MODEL_REGISTRY.md` if changed.
4. Update or create API/backend baseline.
5. Add done report and tests.
6. Push project-control updates.

## Frontend device responsibility

Before frontend work:

1. Pull/update project-control.
2. Validate API baseline freshness.
3. Confirm design baseline.
4. Generate or read the frontend execution packet.
5. Implement against approved API/design contracts.

## If backend repo is not available locally

Frontend Codex must use one of:

- GitHub connector/MCP to inspect backend branch/PR,
- backend handoff summary,
- API baseline packet,
- uploaded backend diff or docs.

It must not guess backend behavior.
