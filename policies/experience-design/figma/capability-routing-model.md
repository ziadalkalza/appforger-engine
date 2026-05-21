# Capability Routing Model

Appforger routes by capabilities:

| Capability | Typical provider types |
|---|---|
| product_planning | reasoning/planning model |
| architecture_reasoning | reasoning/planning model |
| document_generation | reasoning/planning model |
| repo_inspection | code agent |
| code_editing | code agent |
| command_execution | code agent/local shell |
| test_execution | code agent/CI/local shell |
| visual_generation | image generation provider |
| high_fidelity_design | design tool/Figma-like tool |
| prototype_iteration | design tool/sandbox/code agent |
| context_retrieval | project-control/context backend/RAG |
| release_review | planning model + validators |

Providers can satisfy multiple capabilities, but no provider should be assumed to satisfy all capabilities.
