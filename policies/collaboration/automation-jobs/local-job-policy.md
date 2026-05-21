# Local Job Policy

Local jobs may run scripts and validators on the user's machine.

Allowed examples:

- validate project-control
- validate stage gates
- reindex local context backend
- generate draft next-step packets
- run local tests

Local jobs must not assume every team member has the same hooks installed. If a local job affects shared context, record the run and commit/push the report through the normal project-control workflow.
