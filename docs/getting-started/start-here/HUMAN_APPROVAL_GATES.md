# Human Approval Gates

## Purpose

Approval gates prevent uncontrolled agentic changes.

## Mandatory gates

The user must approve before:

- Selecting project creation mode.
- Choosing backend stack.
- Using a paid service or paid model.
- Creating cloud resources.
- Approving design baseline.
- Freezing API contract.
- Adding or changing auth/security architecture.
- Running destructive database migrations.
- Starting native frontend implementation.
- App store / Play Store submission.
- Engine upgrades.

## Do-not-proceed examples

Do not start native frontend implementation unless:

- App mode is selected.
- Design baseline is approved.
- Backend stack is selected.
- API contract is approved or explicitly marked as draft with a safe mock strategy.
- Required assets are available or placeholders are approved.
- Target platform rules are loaded.

## Flexible iteration rule

Approval gates prevent premature stage entry. They do not prevent returning to an earlier stage.

If the user changes approved UI during frontend development:

- Open a change request.
- Classify impact.
- Update only affected artifacts.
- Approve the new baseline if needed.
- Continue.

## Approval record template

```md
### APPROVAL-0001

- Date:
- Approved by:
- Gate:
- Approved artifact/version:
- Conditions:
- Notes:
```
