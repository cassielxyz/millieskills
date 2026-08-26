# Millie Fix — Spaghetti & Architecture Repair

## Diagnose first
Map responsibilities, state ownership, control flow, data flow, I/O, public contracts,
callers/callees and test boundaries.

## Common transformations

### God function
Separate only coherent responsibilities such as validation, pure domain decision, side effects,
persistence, output mapping. Do not extract every few lines.

### God class/module
Split by stable reasons-to-change and ownership, not arbitrary size.

### Circular dependency
Possible fixes:
- move shared contract/type to a stable lower layer;
- invert one dependency behind a real interface/port;
- move orchestration to a higher layer;
- merge falsely-separated modules;
- remove bidirectional state access.

### Shared global state
Identify a clear owner/lifecycle and controlled mutation. Do not automatically add a DI framework.

### Duplicate rules
Choose one canonical implementation, route callers to it, verify, then remove duplicates.

### Deep conditional
Consider guard clauses, explicit state machines, table-driven mapping, policy/mechanism split, or
polymorphism only when behavior families are stable.

### Long parameters
Create a value/object only when parameters form a real domain concept.

### Utility dumping ground
Move behavior near its owner. Keep genuinely cross-cutting pure utilities small.

## Proposal format
```text
Problem
Evidence
Current dependency path
Target dependency path
Contracts preserved
Migration steps
Verification
Rollback
```

## Enforce architecture
When practical add machine-checkable dependency rules to prevent regression.

## Rewrite threshold
Prefer incremental repair. Consider rewrite only when behavior/contracts are sufficiently mapped,
tests/characterization can protect behavior, incremental change is blocked, and migration/rollback
exists.
