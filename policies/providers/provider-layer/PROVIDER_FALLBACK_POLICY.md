# Provider Fallback Policy

If the preferred provider is unavailable:

1. Check approved fallback provider in ACTIVE_PROVIDER_REGISTRY.
2. If none exists, recommend generic packet output.
3. If provider-specific facts are unknown, enter plan mode.
4. Do not silently switch to a provider with weaker security/privacy/tool access.
5. Record the fallback decision when it affects execution.
