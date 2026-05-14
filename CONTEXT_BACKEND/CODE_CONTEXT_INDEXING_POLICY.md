# Code Context Indexing Policy

Default behavior:
- index generated code summaries only
- do not index raw source code by default

Raw source code indexing requires explicit approval and must respect repository source-of-truth rules.

If raw code indexing is enabled:
- exclude secrets, generated files, build artifacts, vendored packages, and binaries
- preserve file path, language, symbols, classes/functions, imports, and source commit metadata
- prefer structure-aware parsing over blind text chunking
- retrieved code chunks must never replace the code repo as source of truth
