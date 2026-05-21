# Package Draft Workflow

Package experiments are allowed before approving a dependency.

## Rules

- Test packages in sandbox/local-only or draft branch.
- Do not add them to production dependencies until package decision approval.
- Record findings in `PACKAGE_DECISION_REGISTRY.md` only after review.
- If package is rejected, record the reason so future agents do not suggest it again without new evidence.
