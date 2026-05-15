# Job Dependency Policy

A job may declare:

- `depends_on_jobs`
- `depends_on_baselines`
- `conflicts_with_jobs`
- `blocks_stages`
- `produces_artifacts`

The task runner must not run jobs whose required baselines are missing, stale, or superseded unless the job is explicitly draft/mock/sandbox.
