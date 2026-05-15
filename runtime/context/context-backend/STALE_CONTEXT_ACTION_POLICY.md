# Stale Context Action Policy

When stale context is detected, AppForge must create a reindex/update action.

For low-risk tasks, stale context may produce a warning.

For high-risk tasks, stale context blocks completion until reindexing or canonical verification is done.

High-risk tasks include:
- security/auth
- payments/subscriptions
- database migrations
- API contract implementation
- privacy-sensitive features
- release decisions
