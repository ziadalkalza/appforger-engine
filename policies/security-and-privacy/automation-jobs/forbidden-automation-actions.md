# Forbidden Automation Actions

File-based Appforger must not automatically:

- read or index `.env` files, tokens, private keys, or secret values
- approve baselines without explicit approval
- merge PRs without approval
- publish to app stores
- deploy production web apps
- delete production data
- rotate production secrets
- activate paid services
- use live payment mode
- bypass security/privacy/release gates silently
- convert draft/sandbox artifacts into approved baselines without review
