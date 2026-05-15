# Approval vs Completion Rules

Implementation complete is not the same as approved.

## Implementation Complete

The actor finished the work and provided evidence.

## Review Complete

A reviewer checked the work.

## Approved

The required owner accepted the work as a baseline, release candidate, or closed task.

## Examples

- Codex can mark implementation complete.
- QA can mark tests passed.
- Designer/user approves design baseline.
- Backend lead approves API baseline.
- Project owner approves release readiness.

## Rule

If approval is required but missing, status should be `needs_review`, not `completed_verified`.
