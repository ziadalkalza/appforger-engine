# Automation Safety Audit

Checks that v19 automation jobs cannot bypass Appforger governance.

## Allowed low-risk automation

- validators;
- draft packet generation;
- report generation;
- tests;
- context reindexing after approved setup;
- stale context detection.

## Approval required

- commits/pushes/merges;
- integration activation;
- external package addition;
- baseline approvals;
- production environment changes;
- release blocker waivers;
- app/web publishing.

## Forbidden silent automation

No job may silently approve baselines, index secrets, publish production, waive critical blockers, delete production data, or promote drafts into truth.
