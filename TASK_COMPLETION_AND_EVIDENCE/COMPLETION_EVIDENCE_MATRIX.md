# Completion Evidence Matrix

| Task Type | Minimum Evidence | Typical Status If Missing |
|---|---|---|
| Product decision | decision entry, owner, date | needs_review |
| Figma/design baseline | Figma link/frames, screenshots, approval | needs_review |
| Backend implementation | changed files, tests, API registry update | implemented_unverified |
| API contract | endpoint list, schemas, approval | needs_review |
| iOS frontend | changed files, build result, visual QA if UI | implemented_unverified |
| Android frontend | changed files, build result, visual QA if UI | implemented_unverified |
| Web frontend | changed files, build result, responsive QA if UI | implemented_unverified |
| QA task | test report, pass/fail summary, evidence links | needs_review |
| Release docs | checklist completed, owner approval | needs_review |

## Evidence Quality Levels

- `none`
- `self_reported`
- `commit_recorded`
- `tests_recorded`
- `reviewed`
- `approved`
- `verified`
