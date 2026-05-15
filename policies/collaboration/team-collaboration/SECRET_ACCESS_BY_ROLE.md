# Secret Access By Role

AppForge stores secret metadata only, not secret values.

Secret classes:
- public_config
- developer_local_secret
- staging_secret
- production_secret
- admin_only_secret
- ci_secret

Normal users use integrations through app workflows, test accounts, staging environments, and frontend-safe public config. They do not need raw secrets.
