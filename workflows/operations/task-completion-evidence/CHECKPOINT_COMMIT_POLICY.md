# Checkpoint Commit Policy

## Definition

A checkpoint commit saves partial progress. It does not claim the task is complete.

Checkpoint commits are normal and encouraged for safe development.

## When to Use

Use a checkpoint commit when:

- work is partially complete,
- the developer is stopping for the day,
- a risky change needs to be saved,
- another person needs to review progress,
- the task will continue later.

## Required Record

When a checkpoint commit is made, record:

- task ID,
- repo,
- branch,
- commit hash if available,
- what is done,
- what remains,
- known issues,
- whether tests were run.

## Status

Set task status to:

```text
in_progress_committed
```

unless the user explicitly says the task is complete.

## No False Warning

Do not warn as if the task failed simply because tests or visual QA are missing after a checkpoint commit.

Use this wording:

```text
Progress saved. Task remains in progress. Final tests, QA, and done report are required before completion.
```
