# Import Team Operations State

## Purpose
Import backend state as a candidate sync packet, not direct canonical truth.

## Rules
- Do not store full docs, full meeting notes, source code, or secret values in the operations backend.
- project-control remains canonical.
- Write-back to project-control must happen through sync packets or PRs.
- Record warnings, conflicts, and audit events.
