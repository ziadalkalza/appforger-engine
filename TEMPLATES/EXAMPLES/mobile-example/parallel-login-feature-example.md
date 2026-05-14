# Parallel Login Feature Example

This example shows how an existing mobile workflow can run parallel work safely.

## Parallel plan

Agents:
- Backend Agent: implement auth API in `backend/` using OpenAI-family code agent preference if backend architecture was planned by ChatGPT.
- iOS Agent: implement login UI in `ios/` against `MOCK_API_CONTRACT_V1`.
- Android Agent: implement login UI in `android/` against `MOCK_API_CONTRACT_V1`.
- QA Agent: generate and run auth test cases.

## Rules

- A parallel work plan is required before dispatch.
- Frontend agents may use mock contract until `API_BASELINE_V1` is approved.
- Backend and frontend outputs require reconciliation before real integration.
- If Claude Code implements frontend while ChatGPT/Codex handles backend, record brand-family boundaries and reconcile API expectations.
- No agent may approve baselines directly.

## Reconciliation example

After backend API is done:
1. Compare real API response with mock contract.
2. Update frontend packets if fields/errors differ.
3. Record `REC-AUTH-001` in the reconciliation registry.
4. Create follow-up frontend integration packet.
