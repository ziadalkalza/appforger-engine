# Custom Code Iteration Policy

Custom integration code may require iteration just like any software feature.

The decision packet must warn that custom code may need testing and adjustment for:

- authentication specifics;
- pagination;
- rate limits;
- API versions;
- schemas and field names;
- permission failures;
- network errors;
- retries and backoff;
- data normalization;
- sensitive-field exclusions;
- source-specific edge cases.

The acting model must not promise that custom code will work perfectly on the first try. It should create a test plan, mock/sample input path, dry-run command, and validation checklist.
