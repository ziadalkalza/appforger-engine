# Integration Clarification Questions

Before building an integration pack, AppForge must ask only the questions needed to avoid unsafe or wrong implementation. Batch questions to save tokens.

## Universal questions

1. What exact job should this third-party service do in this app?
2. Which app tracks need it: backend, web, iOS, Android, design, QA?
3. Is this for prototype/test mode, staging, or production?
4. Are paid services, billing, or account creation allowed now?
5. Do you already have an account/project/API key for the service?
6. Should AppForge create a reusable engine integration pack or only a project-specific runbook?
7. Are there privacy, compliance, client, or region constraints?

## High-risk integrations

For payments, auth, location, messaging, healthcare, finance, or personal data, require explicit user approval before activation.

## If the user says “just do it”

Proceed only in plan/draft mode using safe assumptions. Do not activate production use until assumptions are reviewed and approved.
