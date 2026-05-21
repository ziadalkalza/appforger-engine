# GitHub Branch Protection Setup

Recommended manual setup:
- protect `main` in project-control repo
- require pull request before merge
- require at least one approval
- require specific approvers for high-risk files if possible
- block force pushes
- require status checks where available

Appforger can warn if this is not configured but cannot enforce it without GitHub settings.
