# GitHub Context Fetch Protocol

## Purpose

Define how Appforger retrieves code context when a required repo is not local.

## Fetch levels

### Level 1 — Registry metadata

Use `REPO_REGISTRY.md`, branch names, commit IDs, PR links, and done reports.

### Level 2 — GitHub connector/MCP

If available, inspect:

- relevant files/directories,
- latest branch/commit,
- pull request diffs,
- issue/task references,
- CI/test results.

### Level 3 — User-provided artifact

If no connector is available, ask the user to provide one of:

- file upload,
- PR diff/export,
- repo summary,
- Codex done report,
- generated code map.

## Required fetch packet

When remote code context is fetched, create or update an entry in `REMOTE_CONTEXT_REGISTRY.md`:

```yaml
context_id: REMOTE-CONTEXT-001
source_repo: appname-backend
source_type: github_pr | github_branch | github_commit | uploaded_diff | done_report
source_ref:
retrieved_at:
retrieved_by:
used_for_task:
summary:
files_or_paths:
staleness_risk: low | medium | high
```

## Do not

- Do not treat remote code as current unless commit/branch/PR is recorded.
- Do not implement frontend against undocumented backend behavior.
- Do not overwrite project-control based only on a vague chat summary.
