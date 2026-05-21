# Manual Override Policy

The user may manually close or advance a task even when evidence is incomplete.

Appforger must:

1. Respect the user decision.
2. Record the override.
3. Record missing evidence.
4. Record risk.
5. Create follow-up validation tasks if needed.
6. Avoid pretending the task was verified.

## Override Entry Template

```yaml
override_id:
task_id:
override_by:
date:
reason:
missing_evidence:
risk_level:
follow_up_tasks:
status: manually_closed
```
