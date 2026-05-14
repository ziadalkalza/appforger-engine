# Team Operations Backend

The Team Operations Backend is an optional state/control backend for live team visibility. It is not a document store and it is not the canonical source of project truth.

Canonical artifacts remain in `project-control/`, code repositories, Figma, docs storage, exports, or approved cloud storage. The operations backend stores structured, queryable state and metadata links back to those canonical artifacts.

## Purpose
Use this backend when a project needs live visibility into tasks, approvals, handoffs, conflicts, agent runs, job runs, release blockers, and role assignments.

## Non-goals
- Do not store full documents, full meeting notes, source code, design files, or secret values.
- Do not replace GitHub/project-control as canonical truth.
- Do not bypass team PRs, approval gates, release blockers, or automation policies.
