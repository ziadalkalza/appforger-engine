# Model and Tool Agnostic Provider Layer

This layer makes Appforger route work by **capability**, not by a hardcoded model or brand.

Appforger must decide what capability a task needs, then recommend an appropriate provider/tool. The user may continue in the current tool, but the output mode must match the risk:

- planning-only
- draft-only
- packet-generation-only
- untested patch proposal
- provider-executed task

This layer does not remove ChatGPT, Codex, Figma, or image generation. It makes them provider profiles inside a larger routing system.
