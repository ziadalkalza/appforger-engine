# Questionnaire Versioning Policy

The onboarding questionnaire must have a version.

```yaml
questionnaire_version: 1
completed_at: null
last_reviewed_at: null
```

If AppForge adds new required questions in a future upgrade, mark affected projects as `needs_onboarding_update` and ask only the new required questions.
