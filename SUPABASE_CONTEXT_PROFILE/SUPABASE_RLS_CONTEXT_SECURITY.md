# Supabase RLS Context Security

If multiple people use the context backend, enable RLS.

At minimum, scope records by:

- project_id
- organization_id if applicable
- role/permission later

v16 does not implement full multi-user management, but schemas should not block it later.
