# Initial Code Context Bootstrap Policy

When Appforger is applied to an existing or ongoing project with registered backend, frontend, mobile, iOS, or Android code sources, it must perform an initial code context bootstrap before using code context for implementation decisions.

The bootstrap registers the source, validates access, fetches or imports available code context, applies exclusion rules, generates summaries/maps, records commit or snapshot metadata, and marks the code context as fresh, stale, partial, summary-only, blocked, or unavailable.

The bootstrap must not modify source code.

If raw code access is unavailable, Appforger may bootstrap from CI-generated context artifacts, uploaded snapshots, approved summaries, or maps.

If bootstrap is partial or stale, Appforger may continue planning, but must block implementation, refactoring, release, migration, auth/security, CI/CD, and API contract changes until fresh code context or actual source inspection is available.

## Bootstrap status values

```yaml
bootstrap_status:
  not_started: "No initial code context exists."
  complete: "Code source was fetched/scanned and summaries/maps are fresh."
  partial: "Only some repos, files, or summaries were available."
  summary_only: "No raw code was fetched; approved summaries/maps only."
  blocked: "Access required before context can be created."
  stale: "Bootstrap exists but source changed since indexing."
```
