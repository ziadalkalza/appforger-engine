# Draft Mode Policy

Draft mode is for exploration. It allows AppForge, ChatGPT, Codex, Figma, or the user to test ideas without changing the approved system.

## Allowed draft uses

- Try a UI layout before updating Figma baseline.
- Create a quick HTML prototype for a native/mobile or web concept.
- Generate image/logo/icon candidates before importing them as approved assets.
- Try Codex code in `local-only/drafts/` or a draft branch.
- Test a package/library before approving it.
- Explore mock backend/API responses before API contract approval.

## Forbidden in draft mode

Draft mode must not directly:

- update approved baselines;
- mark a task complete;
- modify production app code without a draft branch label;
- add package dependencies to real repos without package approval;
- replace Figma source of truth;
- change API contracts;
- update release docs as if the work is completed.

## Draft record

Every meaningful draft should have a registry record with:

```yaml
draft_id: DRAFT-0001
title: "Onboarding layout HTML exploration"
type: html_prototype
status: active
created_for: STORY-001
location: local-only/drafts/html-prototypes/onboarding-v1/
affects_project_truth: false
promotion_required: true
expiry_review_date: YYYY-MM-DD
owner: user_or_role
```
