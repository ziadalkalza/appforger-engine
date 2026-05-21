# Agent Brand-Family Policy

Provider-agnostic does not mean brand-family consistency is irrelevant.

Brand family examples:
- OpenAI: ChatGPT, Codex, OpenAI image generation
- Anthropic: Claude, Claude Code
- Google: Gemini-related tools
- Local: local LLMs/code agents
- External: non-model third-party tools

Dependent reasoning chains should preferably stay in the same brand family.

Cross-brand work is allowed, but Appforger must strengthen handoff controls with:
- explicit source-of-truth baselines
- execution packets
- output contracts
- acceptance criteria
- done reports
- reconciliation records when needed

Low/medium-risk cross-brand work gets a warning. High-risk dependent cross-brand work requires reconciliation before completion or approval.

High-risk dependent work includes:
- authentication/security
- payments/subscriptions
- production backend architecture
- database schema/migrations
- privacy-sensitive features
- release blockers
- API contract changes
- cross-platform shared logic
