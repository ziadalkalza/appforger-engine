# Action Risk Classification

Classify actions before executing them.

## Low risk

Examples: update draft docs, create prompt, summarize stage, create local checklist.
Action: proceed with assumptions if needed.

## Medium risk

Examples: generate execution packet, alter design baseline candidate, change non-production config.
Action: ask if missing critical details; record assumptions.

## High risk

Examples: change architecture, add integration, modify API contract, alter database schema, push code, connect external service.
Action: enter plan mode and request approval.

## Critical risk

Examples: production deployment, paid billing, destructive migration, live payment/auth changes, secrets exposure.
Action: require explicit approval and evidence checklist.
