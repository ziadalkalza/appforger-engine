# AppForge User Operator Manual — DO NOT LOAD AS AGENT CONTEXT

This file is for the human user. It is not meant to be read by ChatGPT/Codex during normal project work.

Use it as your cheat sheet for what to write and when. Agents should follow `AGENTS.md`, stage contracts, skills, and task packets instead.

## Why this file exists

AppForge is an engine. You should not repeat all engine rules in every prompt.

You usually write only the thing you want to do:

```text
Start a new app.
Create the Figma prompt for onboarding.
Import this Figma baseline.
Create a Codex work packet for the login screen.
Save memory for this stage.
```

## 1. Starting a new app in ChatGPT

Use this when beginning a new project:

```text
You are operating inside AppForge.
Start a new app project.
Run the new app wizard, create the initial product brief, choose the app mode, identify design/backend/frontend decisions, and tell me which AppForge files should be updated.

My app idea is:
[describe app]
```

## 2. Continuing an existing app

Use this at the start of a new ChatGPT session:

```text
You are operating inside AppForge.
Read only the operating context:
- AGENTS.md
- APPFORGE_PROJECT_STATUS.md
- APPFORGE_PROJECT.yaml
- DECISION_LOG.md
- PENDING_QUESTIONS.md
- registries/decision-snapshots/PROJECT_MEMORY_COMPACTION.md

Do not read the whole engine.
Continue from the current stage and tell me the next best action.
```

## 3. Starting a stage

```text
Use AppForge to start the [stage name] stage.
Read the matching stage contract and relevant skill only.
Create the stage plan, required inputs, expected outputs, approval gate, and manual actions.
```

Examples of stages:

```text
requirements
UX flow
visual direction
Figma design
backend
API contract
native frontend
integration
QA
release documentation
```

## 4. Working with Image generation

Use this when you need visuals:

```text
Use AppForge to create an image-generation request packet for [logo/icon/onboarding illustration/empty state/app store screenshot].
Include style direction, constraints, review checklist, and Figma import steps.
```

After generating assets:

```text
Use AppForge to review these generated image assets and prepare the approved ones for Figma import.
```

## 5. Working with Figma

Start in ChatGPT/AppForge:

```text
Create the Figma Make prompt and manual Figma checklist for [flow/screen/feature].
```

Then go to Figma, design/prototype/edit/test.

When done, return with:

```text
Import this Figma work as a candidate design baseline.
Figma link: [link]
Frames: [frame names]
Screenshots/assets: [attached or linked]
Notes: [anything important]
```

## 6. Approving a design baseline

```text
Review the candidate Figma baseline.
Tell me what is complete, what is missing, what affects backend/API, and what must be approved before backend or frontend work.
```

After you approve:

```text
Mark this as DESIGN_BASELINE_V[number] and update AppForge memory.
```

## 7. Starting backend work

```text
Use AppForge to select the backend stack for this approved design.
Compare Supabase and FastAPI + PostgreSQL for this app, list manual setup actions, and create the backend implementation plan.
```

After backend planning:

```text
Create the backend Codex work packet for the next backend task.
```

## 8. Starting Codex development

In the target repo, use this style:

```text
You are operating in the [backend/ios/android] repo under AppForge control.
Read this repo's AGENTS.md and APPFORGE_POINTER.md.
Use the supplied Codex work packet only.
Implement the task, run required checks, and produce a done report.
```

Do not ask Codex to read the whole AppForge folder.

## 9. After Codex finishes

Bring the result back to ChatGPT/AppForge:

```text
Import this Codex done report.
Update task status, affected registries, baselines if needed, and tell me the next action.

Done report:
[paste report]
```

## 10. Saving memory

Although AppForge should do this automatically at stage/task completion, you can force it:

```text
Save AppForge memory for what we just did.
Update APPFORGE_PROJECT_STATUS.md, affected registries, decisions, open questions, and create a compact summary for the next session.
```

For a stage:

```text
Complete the [stage name] stage memory save.
Create a stage summary, update baselines/registries, list approvals, and specify what the next session should read.
```

For a GitHub commit/PR:

```text
Record this GitHub update in AppForge memory.
Repo:
Branch:
Commit/PR:
Summary:
Tests:
Impact on registries/baselines:
```

## 11. Changing something after approval

```text
Open a change request for [what changed].
Classify the impact, identify affected artifacts, tell me what needs to be updated, and avoid restarting the project.
```

## 12. Token-saving rules for you

Do not say:

```text
Read everything.
Review the whole folder.
Use all context.
```

Say:

```text
Read the operating context and the current stage files only.
Use the relevant packet/baseline for this task.
```

## 13. Common one-line prompts

```text
Continue AppForge from the current stage.
Create the next task packet.
Import this artifact and update registries.
Save memory for this session.
Open a change request.
Create a Figma Make prompt.
Create an Image 2 asset request.
Create a execution packet for backend.
Create a execution packet for iOS.
Create a execution packet for Android.
Run a stage gate check.
```

## Starting plan mode manually

Use this when the task is large, risky, unclear, or may require many tokens:

```text
Enter AppForge plan mode. Do not write code or change files yet.
Clarify the goal, missing information, assumptions, options, risks, files/stages affected, and ask only the questions required before real work starts.
```

## Adding a third-party integration

Use this when you want a new service like Stripe, Firebase, Mapbox, Twilio, SendGrid, Sentry, RevenueCat, etc.:

```text
Run AppForge integration upgrade for [SERVICE].
First ask required clarification questions, research official docs if needed, create a draft integration pack, and do not activate or implement it until I approve.
```

## Checking whether a connector/MCP/skill is usable

Use:

```text
Check the AppForge lifecycle status for [GitHub/Figma/Supabase/Codex skill/etc.].
Tell me whether it is only documented/generated or actually installed, authorized, validated, and active. If not active, give me the next manual action.
```
