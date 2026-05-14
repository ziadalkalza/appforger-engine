# Codex Test Before Done Policy

Before reporting done, Codex should run the smallest reliable checks available.

Examples:
- backend: unit tests, API tests, lint/import checks
- iOS: build/test target if available
- Android: Gradle build/test if available
- Markdown engine: validation scripts if available

If tests cannot be run, report why and provide manual test steps.
