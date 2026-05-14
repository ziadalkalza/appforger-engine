# Task Status Model

Use these statuses in task boards, registries, done reports, and handoffs.

## Active Statuses

- `not_started`
- `in_progress`
- `in_progress_committed`
- `blocked`
- `needs_input`
- `needs_review`

## Completion Statuses

- `implemented_unverified`
- `user_marked_done`
- `user_marked_done_needs_evidence`
- `completed_with_warnings`
- `completed_verified`
- `manually_closed`

## Failure / Change Statuses

- `failed`
- `cancelled`
- `superseded`
- `reopened`

## Recommended Meaning

### `in_progress_committed`

A checkpoint commit exists, but the task is not claiming completion.

### `implemented_unverified`

The expected output appears to exist, but required tests/reviews/evidence are incomplete.

### `user_marked_done_needs_evidence`

The user says the task is done, but AppForge cannot verify all required evidence.

### `completed_with_warnings`

The task is usable, but warnings or incomplete checks must remain visible.

### `completed_verified`

The task is complete, checked, recorded, and approved if approval is required.

### `manually_closed`

The user intentionally closed the task despite missing evidence. AppForge must record the risk and recommended follow-up.
