# Automation Failure Policy

Failure behavior depends on risk level.

- Low risk: retry once if safe, then write failure report.
- Medium risk: write failure report and ask user before retry.
- High risk: stop immediately and request review.
- Critical: stop immediately, create blocker, require explicit approval to proceed.

Every failure is recorded in `AUTOMATION_FAILURE_REGISTRY.md`.
