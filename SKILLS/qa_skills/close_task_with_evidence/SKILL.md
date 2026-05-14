# Close Task With Evidence

## Purpose

Classify and close an AppForge task without confusing checkpoint progress with verified completion.

## Inputs

- Task ID
- Task packet
- User/Codex completion message
- Commit/branch/PR information, if available
- Test/build/QA results, if available
- Relevant baselines and registries

## Steps

1. Determine whether the update is a checkpoint, completion claim, user manual close, or reopen.
2. Load the completion criteria from the task packet.
3. Check required evidence using `TASK_COMPLETION_AND_EVIDENCE/COMPLETION_EVIDENCE_MATRIX.md`.
4. Assign the correct status.
5. Write or update the done report.
6. Update the task status registry and task completion registry.
7. Create follow-up validation tasks for missing evidence.
8. Warn only where evidence is missing; block only dependent high-risk stages.

## Outputs

- Updated task status
- Done report or checkpoint report
- Missing evidence list
- Follow-up tasks
- Registry updates

## Forbidden Actions

- Do not mark a task `completed_verified` based only on a commit.
- Do not reject a user manual close; record it with warning/risk instead.
- Do not delete previous task evidence when reopening.
