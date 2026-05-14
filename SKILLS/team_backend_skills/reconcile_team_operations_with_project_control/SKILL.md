# Reconcile Team Operations With Project Control

## Purpose
Resolve mismatches between operations backend state and project-control canonical records.

## Rules
- Do not store full docs, full meeting notes, source code, or secret values in the operations backend.
- project-control remains canonical.
- Write-back to project-control must happen through sync packets or PRs.
- Record warnings, conflicts, and audit events.
