# Provider Layer Pointer

The older model/tool routing layer now defers provider-agnostic execution decisions to:

```text
MODEL_AND_TOOL_AGNOSTIC_PROVIDER_LAYER/
EXECUTION_PACKETS/
```

Use routing by capability first. Provider-specific terms such as execution packet are allowed only as adapters of a generic execution packet.
