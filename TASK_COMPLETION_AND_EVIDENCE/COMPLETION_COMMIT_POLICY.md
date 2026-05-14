# Completion Commit Policy

## Definition

A completion commit claims that the task implementation is complete.

## Required Evidence

Before marking a task completed verified, collect evidence appropriate to the task type.

Common evidence:

- branch name,
- commit hash,
- PR link if available,
- changed files,
- test/build result,
- screenshots or visual QA if UI changed,
- done report,
- affected registry updates,
- unresolved warnings.

## If Evidence Is Missing

Do not silently mark the task as complete.

Use one of:

- `implemented_unverified`
- `user_marked_done_needs_evidence`
- `completed_with_warnings`

Create follow-up validation tasks when needed.
