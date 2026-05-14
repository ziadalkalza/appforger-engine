# Third-Party Integration System

This folder defines how AppForge adds and uses third-party integrations such as Stripe, Firebase, Mapbox, Twilio, SendGrid, Sentry, RevenueCat, Rive, LottieFiles, AWS, or any other external service.

AppForge must not improvise unsupported integrations. A third-party tool becomes usable only after an integration pack exists, has been reviewed, registered, and activated for the project.

## Core rule

```text
No integration pack may be created from memory alone.
No unsupported service may be implemented directly into app code.
Integration research, clarification, pack generation, approval, and activation must happen before implementation.
```

## Integration flow

```text
User requests a third-party service
→ AppForge checks whether an integration pack exists
→ if missing, enter plan mode and run integration research
→ ask required clarification questions
→ research official docs when current behavior/API/setup matters
→ generate draft integration pack from schema
→ record sources, unknowns, assumptions, risks, costs, and required secrets
→ user approves or rejects
→ integration is registered and activated
→ Codex work packets may use the integration
```

## Important distinction

```text
Engine upgrade = teach AppForge how to use the integration safely and repeatably.
Project implementation = use the approved integration in this specific app's repos.
```

Integration packs belong to the reusable engine. Project-specific secrets, account IDs, concrete keys, environment values, and implementation code do not.
