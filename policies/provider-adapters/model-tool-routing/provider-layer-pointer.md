# Provider Layer Pointer

The older model/tool routing layer now defers provider-agnostic execution decisions to:

```text
policies/providers/provider-layer/
templates/packets/execution-packets/
```

Use routing by capability first. Provider-specific terms such as execution packet are allowed only as adapters of a generic execution packet.
