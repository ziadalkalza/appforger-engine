# iOS UI Quality Rules

## Must match

- Approved Figma visual baseline.
- Platform interaction expectations.
- Accessibility requirements.
- Asset exports.

## Visual QA

If implementation differs from Figma:

- If accidental: patch SwiftUI.
- If desired: open UI change request and update Figma/design baseline.

## Native feel

Use native navigation, gestures, sheets, keyboard handling, and safe areas unless Figma explicitly defines a custom behavior that remains platform-safe.
