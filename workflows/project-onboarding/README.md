# Project Onboarding and Initialization

This layer defines the first-use questionnaire and initialization gate for Appforger projects.

The goal is to collect only the fixed project rules needed to route skills, workflows, providers, storage, context, automation, and team logic correctly. Non-critical answers may stay `unknown_pending` and are asked later when they become relevant.

## Core rule

Appforger may answer general help/explanation questions before onboarding, but it must block real project work until the minimal required onboarding gate is complete. Onboarding should auto-trigger on the first real project-work request.

Allowed before onboarding:
- Explain Appforger concepts, folders, workflows, terms, or how to start.
- Explain what a provider, packet, visual baseline, project-control, docs folder, or context backend means.

Blocked before onboarding:
- Create execution packets.
- Start implementation work.
- Generate real app artifacts.
- Activate integrations.
- Start backend/frontend/design workflows.
- Configure storage, context backend, team operations backend, or automation jobs.

After onboarding, Appforger resumes the user's original paused request.
