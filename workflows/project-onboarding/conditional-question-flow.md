# Conditional Question Flow

Appforger must ask follow-up questions based on previous answers.

## Existing project

Ask:
- Where are the existing repos?
- Which repo is current source of truth for frontend/backend?
- Does existing Figma/design exist?
- Does existing backend exist?
- What docs exist?
- What is already released?
- What should Appforger treat as current truth?

## Team mode

Ask:
- Who are the members?
- Which roles do they hold?
- Who approves product/design/API/release?
- Should project-control changes require PRs?
- Should Team Operations Backend be enabled?

## Backend not sure

Allow `unknown_pending` during ideation/design. Re-ask before API contracts, data models, auth, database, or frontend integration.

## Tool consistency mode before provider choice

Ask tool consistency preference before model/provider preference. If the user chooses one-tool-family dependent work, Appforger must warn when they pick providers from different tool families for dependent tasks.

## Ongoing project

If `ongoing_project = yes_active_project`, ask:

- Which backend/frontend/mobile repos are current source of truth?
- Are sources local, remote Git, snapshot, CI-generated context, or summary-only?
- Who owns backend code?
- Who owns frontend/mobile code?
- Which roles can write?
- Which roles can read raw files versus maps/summaries only?
- Where are repo credentials stored as references?
- Should CI-generated context be used for restricted repos?
- Should raw code indexing remain disabled? Recommended: yes.

Then require initial code context bootstrap before code-aware implementation.
