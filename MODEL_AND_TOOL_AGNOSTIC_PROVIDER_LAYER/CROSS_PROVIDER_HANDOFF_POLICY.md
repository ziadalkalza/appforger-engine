# Cross Provider Handoff Policy

When one provider plans and another executes:

1. Planning provider creates an execution packet.
2. Execution provider follows packet boundaries.
3. Execution provider produces a done report.
4. AppForge imports the done report into project-control.
5. Any conflicts, missing evidence, or skipped tests are recorded.

Chat history is not the source of truth. The shared handoff is project-control plus execution packets and done reports.
