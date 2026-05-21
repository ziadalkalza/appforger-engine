# Tree-sitter Code Indexing Guide

When raw or structured code indexing is explicitly enabled, Appforger should prefer structure-aware parsing such as Tree-sitter over naive text chunking.

A structure-aware code index should extract:
- file path
- language
- classes/types
- functions/methods
- imports/dependencies
- decorators/annotations
- comments/docstrings where useful
- parent-child relationships
- source commit

Tree-sitter support is optional in this version, but future script upgrades should follow this policy when indexing code.
