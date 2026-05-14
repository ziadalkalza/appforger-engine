# Rollback Policy

Every release should have a rollback or recovery plan.

For mobile, rollback may mean:
- pausing rollout
- submitting hotfix
- disabling server-side feature flags

For web, rollback may mean:
- reverting deployment
- switching DNS/traffic back
- restoring previous environment config

For backend, rollback may require a migration strategy. Destructive database migrations require extra approval.
