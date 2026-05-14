# Task Completion Policy

## Purpose

AppForge must classify task status honestly without blocking normal development flow.

## Completion Definition

A task is complete only when all required completion criteria for that task type are satisfied.

Completion usually requires:

1. Expected output exists.
2. Acceptance criteria are satisfied.
3. Required checks/tests are recorded.
4. Required post-actions are completed.
5. Required approvals are captured, if applicable.
6. Evidence is linked or attached.

## Important Distinction

A commit is evidence of work, not proof of completion.

A task may be:

- partially implemented and committed,
- implemented but not tested,
- tested but not approved,
- approved manually with missing evidence,
- fully verified and closed.

## User Authority

The user may always mark work as done or manually close a task.

If required evidence is missing, AppForge must not reject the user's decision. It must record the correct status and risk:

- `user_marked_done_needs_evidence`
- `completed_with_warnings`
- `manually_closed`

AppForge must create follow-up validation tasks when missing evidence matters.

## Dependent Stage Blocking

Missing evidence does not automatically stop all work.

It may block or warn only when the missing evidence affects a dependent stage.

Examples:

- Missing API baseline approval blocks production frontend integration.
- Missing visual QA does not block backend development.
- Missing unit tests may allow exploration but should block release readiness.
