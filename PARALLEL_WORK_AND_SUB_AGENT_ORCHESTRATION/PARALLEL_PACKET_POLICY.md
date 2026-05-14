# Parallel Packet Policy

Parallel packets must be small, bounded, and dependency-aware.

Each packet must define:
- target agent/role
- target provider type
- brand family preference
- target repo/branch/path
- dependencies
- can-run-in-parallel-with
- conflicts-with
- forbidden actions
- evidence required

Do not use one giant packet for an entire app when multiple small packets can reduce risk.
