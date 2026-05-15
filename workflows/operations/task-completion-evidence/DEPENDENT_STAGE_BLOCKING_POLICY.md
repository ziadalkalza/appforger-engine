# Dependent Stage Blocking Policy

Evidence rules should not make AppForge brittle.

Block only when missing evidence affects the safety or correctness of a dependent stage.

## Examples

| Missing Evidence | Can Continue? | Notes |
|---|---:|---|
| Backend tests missing | Maybe | frontend can use mock mode, production integration should wait |
| API baseline not approved | No for production integration | mock/prototype allowed |
| Visual QA missing | Maybe | backend unaffected, release blocked |
| Security review missing | No for release | implementation can continue with warning |
| Checkpoint commit only | Yes | task remains in progress |

## Rule

Warn broadly. Block narrowly.
