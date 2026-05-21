# DOCX and PDF Summary Policy

DOCX and PDF files are not indexed directly by default.

Default flow:

```text
original file -> stored in docs/imports/ or external storage
summary/extraction -> stored in docs/summaries/*.summary.md
context backend -> indexes summary/extraction only
```

Summaries must include:
- original source path or URL
- document ID
- extraction date
- summary confidence/limitations
- sensitivity classification
- related Appforger entities

Original files remain untouched.
