# Audit Log Policy

Every backend write or sync-relevant action should create an audit event.

Audit events should record:
- actor
- action
- affected entity
- old status if applicable
- new status if applicable
- source packet or PR
- timestamp
- approval requirement
- risk level
