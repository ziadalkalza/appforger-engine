# Agent Merge and Reconciliation Policy

Parallel outputs are not automatically merged into truth.

Reconciliation step:
1. Collect agent done reports.
2. Compare outputs against baselines and dependencies.
3. Detect mismatches and conflicts.
4. Create follow-up packets if needed.
5. Update project-control through allowed path.
6. Record reconciliation if cross-agent/cross-brand consistency was checked.

In team mode, project-control updates should go through PRs.
