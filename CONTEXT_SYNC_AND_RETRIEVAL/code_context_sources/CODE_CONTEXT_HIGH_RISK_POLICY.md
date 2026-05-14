# Code Context High-Risk Policy

The following code-context actions are high-risk:

- raw code indexing
- repo write access
- production branch changes
- auth/security files
- payment files
- database migrations
- secrets/env files
- API contract changes
- role/access policy changes
- CI/CD workflow edits
- remote repo credentials

High-risk actions require explicit approval, access verification, and an audit record.

If a user asks to waive a high-risk blocker, AppForge must label the waiver as high-risk and record the affected source, reason, approver, and scope.
