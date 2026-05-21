# Onboarding Questionnaire Policy

The questionnaire is adaptive. It should not ask every possible question immediately.

Use these modes:

- `quick_setup`: minimal critical answers only.
- `full_setup`: full project configuration.
- `existing_project_import`: for projects with existing repos/design/backend/docs.
- `team_setup`: adds team roles/members/approvals when team mode is selected.
- `advanced_setup`: context backend, automation, storage, providers, and operations backend details.

## Required minimal questions

1. Project name.
2. New project or existing/running project?
2A. Is this an ongoing project?
3. Single-user or team mode?
4. Target app type: mobile, web, both, backend-only, unknown?
5. Starting point: scratch, existing code, existing design, existing docs?
6. Workflow preference: standard, flexible, not sure?
7. Backend needed: yes, no, not sure?
8. Design workflow: Figma, HTML sandbox, existing design/frontend, not sure?
9. Tool consistency mode for dependent work (single tool family vs mixed tools with reconciliation).
10. Preferred code agent/provider or decide per task.
11. Docs storage location.
12. Context backend mode.
13. Automation level.
14. Public release expected: yes/no/not sure.
15. Likely integration needs: payments, maps, notifications, analytics, email/SMS, none, not sure.

## Conditional questions

- If team mode is selected, ask team roles/members/approval questions.
- If existing project is selected, ask existing repo/design/backend/docs truth questions.
- If ongoing project is selected, require initial code context bootstrap before code-aware implementation.
- If backend is needed, ask backend stack questions.
- If context backend is enabled, ask indexing/storage/privacy questions.
- If a non-critical answer becomes blocking later, ask it at that point.
