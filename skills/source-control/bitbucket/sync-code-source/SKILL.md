# Sync Bitbucket Code Source Skill

Use this skill when the user asks to fetch, bootstrap, or sync code context from a Bitbucket Cloud or Bitbucket Data Center repository.

## Procedure

1. Read `project-control/code_sources/code-source-registry.yaml` and locate the requested source.
2. Confirm the source provider is `bitbucket` and identify Cloud vs Data Center from the provider registry or URL.
3. Read `project-control/integrations/source-control/generic/python/git_providers/git-provider-registry.yaml` if present.
4. Confirm credentials are referenced through `local-only/.env.local` and never copied into `project-control`.
5. Confirm the requested access level: read-only, task-scoped files, or write branch.
6. For context sync, prefer running:

```bash
python project-control/pipelines/scripts/run_source_pipeline.py --source <source_id>
```

7. If the pipeline runner is unavailable, run:

```bash
python project-control/code_sources/scripts/bootstrap_code_context.py --source <source_id>
```

8. Report:
   - source id
   - provider id
   - branch/commit if known
   - files scanned/fetched
   - maps generated
   - RAG index updates
   - graph updates
   - stale or blocked status

## Boundaries

- Do not store Bitbucket API tokens in `project-control`.
- Do not create branches, commits, or pull requests unless the source access policy allows write-branch/admin access.
- Do not index raw proprietary code unless the source has raw-code indexing approval.
