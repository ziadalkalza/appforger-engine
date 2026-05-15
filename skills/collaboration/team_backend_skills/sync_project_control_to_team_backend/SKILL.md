# Sync Project Control To Team Backend

## Purpose
Create a sync packet to mirror approved project-control state into the operations backend.

## Rules
- Do not store full docs, full meeting notes, source code, or secret values in the operations backend.
- project-control remains canonical.
- Write-back to project-control must happen through sync packets or PRs.
- Record warnings, conflicts, and audit events.
