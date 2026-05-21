# High-Risk Tasks

High-risk tasks require stricter routing, approval, and evidence.

Examples:

- authentication, authorization, roles, permissions
- payments, subscriptions, refunds, billing
- secrets, production environment variables, key rotation
- security/privacy-sensitive features
- personal data handling, location tracking, notifications, messaging
- database migrations that can lose/corrupt data
- production deployment or release publishing
- package/integration activation
- MCP/server permissions and tool access
- automation that can push, merge, deploy, delete, or waive blockers
- backend/API contract changes after frontend work started

If attempted in an unsuitable provider, Appforger must switch to plan/packet mode or require explicit high-risk override.
