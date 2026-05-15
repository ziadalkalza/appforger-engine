# Qdrant Cloud Setup

Manual user actions:

1. Create Qdrant Cloud account.
2. Create cluster.
3. Create API key.
4. Store environment variables:

```bash
QDRANT_URL="https://..."
QDRANT_API_KEY="..."
```

Do not paste API keys into Markdown registries. Store them in `.env.local`, local secret store, or CI secrets.
