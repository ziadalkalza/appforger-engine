# Context Backend Failure Recovery

If indexing fails:

1. Keep project-control canonical.
2. Mark context backend as stale/unavailable.
3. Fall back to file-based context loading.
4. Do not block urgent work unless dependent on retrieved context.
5. Fix connection/schema/embedding issue.
6. Re-run validation.
