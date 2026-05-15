# Failure Recovery

If backend state becomes stale, unavailable, or inconsistent:
1. Fall back to project-control as canonical truth.
2. Mark operations backend status as degraded.
3. Generate a reconciliation report.
4. Re-sync from project-control after approval.
5. Do not use stale backend state to approve, release, or dispatch dependent work.
