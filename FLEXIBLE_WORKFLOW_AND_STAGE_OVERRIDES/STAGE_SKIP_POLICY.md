# Stage Skip Policy

A stage may be skipped only when it is truly not required for the selected workflow.

Examples:
- backend skipped for a static website;
- mobile release skipped for web-only project;
- web publishing skipped for mobile-only project.

A skipped stage must be recorded as:
- skipped_not_required;
- skipped_by_user_waiver;
- skipped_replaced_by_substitute;
- skipped_deferred.

Security, privacy, source-of-truth, release blocker, secret management, and production approval checks may not be skipped silently.
