# save_onboarding_answers

## Purpose

Persist onboarding answers to Markdown, YAML, and initialization registries.

## Rules

- Do not ask all optional questions unless the user requests full setup.
- Allow `unknown_pending` only for non-critical answers.
- If an unknown answer blocks the requested workflow, ask it before continuing and provide recommendations.
- Save answers in both Markdown and YAML.
- Do not store secrets.
- Generate or update active rules after saving answers.
- Resume the original user request when the minimal gate is complete.
