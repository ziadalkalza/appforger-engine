# run_project_onboarding_questionnaire

## Purpose

Ask the adaptive minimal or full onboarding questionnaire, save answers, and return to the paused user request.

## Rules

- Trigger this skill automatically on the first real project-work request when onboarding is incomplete.
- Do not wait for the user to explicitly ask to start onboarding.
- Do not ask all optional questions unless the user requests full setup.
- Allow `unknown_pending` only for non-critical answers.
- If an unknown answer blocks the requested workflow, ask it before continuing and provide recommendations.
- Save answers in both Markdown and YAML.
- Do not store secrets.
- Generate or update active rules after saving answers.
- Resume the original user request when the minimal gate is complete.
