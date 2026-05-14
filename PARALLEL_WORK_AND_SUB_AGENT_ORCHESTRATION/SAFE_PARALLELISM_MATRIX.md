# Safe Parallelism Matrix

Safe:
- QA creates draft tests while design/backend work continues.
- iOS and Android implement separate native screens from the same approved visual baseline.
- Web frontend uses mock API while backend builds the real API.
- Documentation drafts are created from approved stories.

Needs caution:
- Two agents work in the same repo on separate branches.
- Frontend agents use a mock contract while backend API is changing.
- Different brand families work on related implementation chains.

High risk:
- Two agents edit the same files.
- Agents change API/design baselines while implementation is active.
- Security/auth/payment work is split across brand families without reconciliation.

Avoid or require override:
- Parallel production release changes.
- Parallel database migrations.
- Parallel secret/config changes.

All parallel execution in this matrix assumes an approved parallel work plan. Any detected conflict must be recorded before continuing.
