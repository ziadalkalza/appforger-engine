# Figma MCP

## Role

Use Figma MCP for:

- Reading Figma design context.
- Extracting layout/component information.
- Feeding design context to Codex.
- Optionally writing native Figma content when explicitly requested.

## Approval rule

Approved Figma baselines are the current visual source of truth.

If Figma changes after approval, create a new design baseline.

## Do not override

Figma does not override:

- Accessibility.
- Security.
- Backend/API contracts.
- Platform constraints.
- App store requirements.
- Legal/privacy constraints.

## Handoff outputs

- Figma links.
- Frame/component names.
- Asset export list.
- Design baseline version.
- Notes for SwiftUI/Compose implementation.
