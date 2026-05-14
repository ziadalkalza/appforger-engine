# Remote Repo Access Policy

## Purpose

Codex and ChatGPT must know whether they can inspect a repo locally or remotely.

## Access modes

```text
local_clone      = repo exists on current machine
remote_github    = repo can be read through GitHub connector/MCP/web/manual file upload
artifact_packet  = relevant summary/export was imported into project-control
not_available    = no valid access exists
```

## Required metadata

Record each repo in `project-control/REGISTRIES/REPO_REGISTRY.md` with:

```yaml
repo_id: backend
name: appname-backend
local_path: ../backend
remote_url: git@github.com:org/appname-backend.git
access_mode: local_clone | remote_github | artifact_packet | not_available
current_branch: main
last_known_commit: abc123
last_verified_at:
owner:
status: active
```

## Rules

- Do not assume `../backend`, `../ios`, `../android`, or `../web` exists.
- Validate local paths before referencing them.
- If local path is missing, check remote access metadata.
- If remote access is unavailable, require an artifact packet or manual upload.
- If implementation code changed remotely, project-control must be refreshed before dependent work starts.
