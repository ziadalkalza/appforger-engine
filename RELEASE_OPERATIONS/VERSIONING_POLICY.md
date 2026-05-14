# Versioning Policy

AppForge defaults to semantic versioning:

```text
MAJOR.MINOR.PATCH
1.0.0
1.1.0
1.1.1
```

Release candidates use:

```text
1.0.0-rc.1
1.0.0-rc.2
```

## Product and platform versions

Major product releases are grouped:

```text
Product Release 1.0.0
  backend: 1.0.0
  iOS: 1.0.0
  Android: 1.0.0
  web: 1.0.0
```

Smaller platform-specific changes may update only that platform:

```text
Product release: 1.2.0
iOS release: 1.2.1
Android release: 1.2.0
Web release: 1.2.0
Backend release: 1.2.0
```

App store build numbers may be tracked separately from semantic version.
