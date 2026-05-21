# Task Completion Registry

This project-control file records task completion state, checkpoint commits, done reports, missing evidence, warnings, manual overrides, and reopen events.

In a generated app workspace, this file belongs in:

```text
project-control/REGISTRIES/TASK_COMPLETION_REGISTRY.md
```

## Status Values

- `not_started`
- `in_progress`
- `in_progress_committed`
- `blocked`
- `needs_review`
- `implemented_unverified`
- `user_marked_done`
- `user_marked_done_needs_evidence`
- `completed_with_warnings`
- `completed_verified`
- `manually_closed`
- `failed`
- `cancelled`
- `superseded`
- `reopened`

## Entries

Add task entries here or in the app-specific project-control repository.
