# Millie Fix — Dead / Unused Code Analysis

Static "unused" results are hypotheses until reachability is understood.

## Candidates
Unreachable statement, unused local/import/parameter/private symbol/export/class/type, orphan
file/package/route/command/job/asset/config/feature flag/dependency/compatibility layer.

## Evidence ladder

### Strong static evidence
- compiler proves unreachable;
- private symbol has no references in a closed-world app;
- entry-point reachability excludes a file after framework loading is understood;
- language-specific tool reports high certainty.

### Cross-check
Use multiple:
- LSP references
- AST/call graph
- dependency graph
- repository search
- build/config
- route/plugin registry
- tests
- runtime trace

### Dynamic-risk review
Check:
- reflection/getattr
- DI/service loaders
- annotations/decorators
- string event names
- templates
- XML/YAML config
- framework route discovery
- filename conventions
- code generation
- plugin entry points
- dynamic import/require
- FFI/JNI/native calls

## Public exports
Zero internal callers may still mean external API. Inspect package exports, API docs, semver,
published interfaces, CLI/API entry points and known external consumers.

## History
Git history can provide intent/context but is not absolute proof.

## Removal loop
Remove a small coherent batch -> build/type/tests -> dead-code scan again -> graph update.

## Confidence
`PROVEN`, `HIGH`, `MEDIUM`, `LOW`, `UNKNOWN`.

Only high-confidence candidates should be auto-removed during a requested cleanup.
