# Code Source of Truth Policy

Code repos and code snapshots can be source-of-truth assets.

A source is canonical only when the source registry marks it with:

```yaml
canonical: true
```

## Truth hierarchy for code-aware work

1. Actual source repo/folder/snapshot at the recorded branch, commit, or snapshot version.
2. Approved API/design/source baselines recorded in project-control.
3. Generated maps and summaries derived from code.
4. Context backend retrieval results.

If retrieved code context conflicts with actual source code, actual source code wins.

If a generated plan conflicts with canonical imported code, canonical imported code wins unless the user approves a migration, refactor, or replacement.

## Required metadata

Every canonical code source must record:

- source id
- role: backend, frontend_mobile, web, mobile, ios, android, ci_cd, infra
- location mode
- repo URL or local path or snapshot path
- branch and commit, where applicable
- snapshot id, where applicable
- access mode
- indexing mode
- sync mode
- bootstrap status
- staleness status
