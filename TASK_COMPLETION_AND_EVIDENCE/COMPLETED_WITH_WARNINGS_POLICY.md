# Completed With Warnings Policy

Use `completed_with_warnings` when the work is usable but not fully verified.

Examples:

- Code compiles but visual QA was skipped.
- UI implemented but one animation was approximated.
- Backend endpoint works locally but has not been deployed.
- User accepts the task even though tests were not run.

## Requirements

Record:

- warning summary,
- missing evidence,
- risk level,
- follow-up validation task,
- user/owner who accepted the warning.

## Dependency Handling

Dependent tasks may continue if the missing evidence is low risk.

High-risk warnings should block release readiness and production integration.
