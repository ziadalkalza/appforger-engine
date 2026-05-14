# Block and Resume Policy

When a user requests real work before onboarding is complete:

1. Save the original request as a pending request.
2. Explain that initialization is required.
3. Ask the minimal required questions.
4. Save answers to Markdown and YAML.
5. Generate active project rules.
6. Resume the original request.

Trigger timing:

- This flow starts automatically on the first real project-work request when onboarding is incomplete.
- Do not wait for the user to ask to "start onboarding".

Pending request format:

```yaml
pending_user_request:
  request_id: PENDING-001
  text: "Build the login screen"
  status: paused_for_onboarding
  resumed: false
```

After onboarding:

```text
Onboarding complete. Resuming original request: Build the login screen.
```
