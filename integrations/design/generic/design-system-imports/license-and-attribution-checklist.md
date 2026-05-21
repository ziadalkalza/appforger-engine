# License and Attribution Checklist

Complete this before importing an external design system into an Appforger project.

## Source identity

```text
Design system name:
Source URL or file path:
Author/organization:
Version/date:
License name:
License file found? yes/no
Attribution requirements:
Commercial use allowed? yes/no/unknown
Modification allowed? yes/no/unknown
Redistribution allowed? yes/no/unknown
```

## Decision

Choose one:

```text
APPROVED
APPROVED_WITH_ATTRIBUTION
INSPIRATION_ONLY
REJECTED
NEEDS_LEGAL_REVIEW
```

## Rules

- If commercial use is not clearly allowed, do not copy assets/code/tokens into the project.
- If attribution is required, record exactly where attribution must appear.
- If the design system includes trademarked logos, characters, icons, or brand references, treat those as restricted unless the user has rights.
- If license is missing or unclear, use only high-level ideas and do not copy exact files/assets.
- Do not store paid, private, or confidential design systems in reusable Appforger core unless the user explicitly owns the rights and wants that.

## Output

Update:

```text
integrations/design/figma/design-system-imports/imported-design-system-registry.md
DECISION_LOG.md
```
