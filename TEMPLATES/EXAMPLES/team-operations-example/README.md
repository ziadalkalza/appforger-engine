# Team Operations Backend Example

This example shows how a team can use the Team Operations Backend for live state while keeping project-control as canonical truth.

Scenario:
- Project-control contains the task packet and approval records.
- The operations backend stores task status, blocker status, owner, and next action.
- The backend row points back to the source packet path.
- A sync packet is required before backend-originated status changes become canonical.

Example query:
"Show all frontend tasks blocked by API approval."

Expected source link:
`project-control/EXECUTION_PACKETS/TASK-IOS-LOGIN-001.md`
