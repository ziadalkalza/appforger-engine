# Scheduled Job Policy

v19 supports schedule definitions and optional GitHub Actions cron templates.

Examples:

- weekly draft cleanup reminder
- daily stale-context check
- nightly test report in active development

Scheduled jobs must record every run and must not perform high-risk actions without approval.
