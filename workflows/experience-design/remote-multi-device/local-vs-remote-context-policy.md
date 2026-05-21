# Local vs Remote Context Policy

## Purpose

Define how Appforger decides whether context should be loaded from local folders, remote GitHub repositories, connector/MCP access, or imported artifact packets.

## Context sources

| Source | Use when | Reliability |
|---|---|---|
| Local repo clone | The repo exists on the current device | Highest for code edits |
| GitHub repo/PR/branch | The repo is on another device or team-owned | High if current |
| Project-control repo | Shared project memory and baselines | Required for multi-device work |
| Figma file/MCP | Design context and approved frames | Required for design/frontend work |
| Supabase/Postgres | Backend runtime/context | Use only through approved connector/manual data |
| Artifact packet | A source was exported/imported into Appforger | Valid if approved/current |

## Default selection order

1. Prefer local repo if the task edits code and the repo exists locally.
2. Use remote GitHub connector/MCP if local repo is missing but remote access is configured.
3. Use an approved artifact packet if direct repo access is not available.
4. Ask for/import the missing context if none is available.

## Hard rule

Do not proceed with implementation if the required source-of-truth artifact is missing or stale.

Examples:

- Frontend task needs backend context → latest `API_BASELINE` must exist in `project-control/` or be fetched/imported from backend repo/PR.
- Backend task needs design behavior → relevant screen/flow baseline must exist in `project-control/` or be imported from Figma.
- QA task needs implementation proof → repo branch/commit/test output must be referenced.
