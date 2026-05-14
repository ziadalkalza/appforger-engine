# SwiftUI Rules

## Default

Use SwiftUI first.

Use UIKit only when:

- SwiftUI cannot reasonably implement a requirement.
- A specific platform API requires UIKit.
- Performance/behavior demands it.

## UI implementation rule

Implement from approved Figma baseline, screen specs, and design tokens. Do not invent visual design.

## Required quality

- Previews for important screens/components.
- Accessibility labels.
- Dynamic type consideration.
- Safe area handling.
- Loading/empty/error states.
- Small reusable components.
- Clear state management.

## Avoid

- Hardcoded secrets.
- Giant view files.
- Random styling inconsistent with Figma.
- Backend assumptions not in API contract.
