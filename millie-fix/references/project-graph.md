# Millie Fix — Project Graph & Function Relationships

The graph is durable repository memory.

It must answer:
- what defines this symbol?
- who calls it?
- what does it call?
- what imports this file?
- what route/job/event reaches it?
- what data/state does it touch?
- what tests exercise it?
- what breaks if it changes?
- can it be safely removed?

## Files
```text
docs/millie-fix/graphs/
├── project-graph.json
├── function-graph.json
├── dependency-graph.json
├── data-flow.json
└── dead-code-evidence.json
```

## Stable IDs
Prefer:
```text
relative/path.ext::Qualified.Owner.symbol
```

Overloads may append a normalized signature. Important anonymous callbacks may use:
```text
path::anonymous@line:column:role
```

## Function node
Useful fields:
- id/name/kind/file/language
- owner/visibility/exported
- entry_point/framework_entry
- signature/params/return type
- calls/called_by/references
- reads/writes
- emits/consumes
- routes
- external_calls
- DB tables/queries
- tests
- side effects
- exceptions
- complexity/lines
- dynamic-reference risk
- confidence
- status

## Edge vocabulary
- imports
- calls
- references
- implements
- extends
- registers
- routes_to
- emits
- consumes
- reads
- writes
- queries
- mutates
- serializes
- deserializes
- constructs
- injects
- configures
- tests
- generates
- loads_dynamic
- ffi_calls

## Evidence
Uncertain edges record:
```json
{
  "kind": "loads_dynamic",
  "from": "plugin-registry",
  "to": "plugins/foo.py::activate",
  "evidence": "framework-convention",
  "confidence": 0.72,
  "dynamic": true
}
```

Evidence sources:
compiler/LSP, AST, import graph, static call graph, framework config, explicit registration,
tests, runtime trace, manual inspection, convention, inferred.

Unknown is not absent.

## Large repos
Shard by package/module:
```text
function-graph.index.json
functions/package-a.json
functions/package-b.json
```
The index records shards and summary counts.

## Centrality hints
When practical record:
- caller count
- dependent count
- entry-point reachability
- package centrality
- Git change frequency
- test coverage

Use this to prioritize context after agent/session resets.

## Regenerate
After onboarding, symbol moves/renames, dead-code deletion, dependency changes, architecture changes
and before final verification.
