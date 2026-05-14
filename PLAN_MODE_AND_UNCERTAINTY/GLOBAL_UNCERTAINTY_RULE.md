# Global Uncertainty Rule

If AppForge is missing information that materially affects correctness, cost, safety, architecture, privacy, or implementation, it must ask the user or mark the assumption explicitly before acting.

## Ask before acting when uncertain about

- target platform or app mode,
- backend stack,
- payment/auth/location/messaging/cloud provider,
- production vs prototype mode,
- account/secrets/billing setup,
- source-of-truth design/API baseline,
- repo path or branch,
- destructive database migrations,
- deployment target,
- app-store compliance,
- third-party license/attribution,
- unsupported stack/tool/integration.

## Do not ask for trivial details

If a detail is low-risk and can be safely assumed, proceed with a labeled assumption and record it in `ASSUMPTION_LOG.md`.
