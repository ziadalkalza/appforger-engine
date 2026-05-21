# Team Operating Model

Appforger v17 supports team collaboration without becoming a real-time multi-user server.

## Collaboration primitives
- `project-control/` stores shared memory and approval records.
- GitHub PRs are used to review and merge project-control changes.
- Role context packs keep each person's loaded context focused.
- Handoff packets transfer work between roles.
- Conflict records prevent silent overwrites.

## Team mode states
- `inactive`: no registered active members.
- `setup`: members and roles are being added.
- `active`: team workflow rules apply.
- `suspended`: collaboration paused due to access/configuration issues.
