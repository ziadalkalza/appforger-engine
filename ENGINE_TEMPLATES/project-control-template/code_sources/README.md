# Code Sources

This folder stores generated metadata about registered code sources. It must not store secret values.

Code sources may be local, remote Git, uploaded snapshot, CI-generated context, or summary-only. A source is canonical only when marked `canonical: true`.

Do not edit generated files blindly. Update the single private config file or approved source registry, then regenerate metadata.
