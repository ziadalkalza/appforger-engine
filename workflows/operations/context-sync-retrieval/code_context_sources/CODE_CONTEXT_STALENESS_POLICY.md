# Code Context Staleness Policy

Every indexed code context record must include source metadata such as commit, branch, snapshot version, or CI artifact id.

## Status values

```yaml
context_status:
  fresh: "Context matches the recorded source version."
  stale: "Source changed after indexing or current commit is unknown."
  partial: "Only some repos/files/maps are available."
  summary_only: "Only approved summaries/maps are available."
  blocked: "Access is required before context can be created."
  not_started: "No initial code context bootstrap has run."
```

## Gate behavior

Stale or partial code context may be used for planning.

Stale or partial code context blocks:

- implementation
- refactoring
- release work
- database migrations
- auth/security changes
- payment changes
- API contract changes
- CI/CD edits
- production branch changes

unless actual source files are freshly inspected or the relevant source is refreshed.
