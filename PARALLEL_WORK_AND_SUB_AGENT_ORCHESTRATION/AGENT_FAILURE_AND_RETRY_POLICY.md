# Agent Failure and Retry Policy

Agent failures are handled by risk level.

Low-risk failures may retry once after recording the failure.
High-risk failures must stop and ask for review.
Critical failures must stop immediately and create a blocker/conflict record.

Examples of critical failures:
- production secret exposure
- destructive database operation
- release blocker introduced
- auth/security behavior changed without approval
- baseline changed without authorization
