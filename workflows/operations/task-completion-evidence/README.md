# Task Completion and Evidence

This folder defines how Appforger decides whether a task is merely saved, partially complete, ready for review, verified, manually closed, or reopened.

Core rule:

```text
A task is not complete because someone says "done" or because a commit exists.
A task is complete when the required output exists, acceptance criteria are met, checks are recorded, post-actions are complete, and required approvals are captured.
```

This layer prevents confusion between:

- checkpoint commits that save partial work,
- completion commits that claim a task is done,
- user-marked completion with missing evidence,
- verified completion,
- manual override closure,
- reopened work.

Use these files whenever a task is committed, reviewed, closed, reopened, or carried forward between sessions.
