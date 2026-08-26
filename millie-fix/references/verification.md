# Millie Fix — Verification

## Baseline
Before broad changes run feasible install/restore, build, typecheck, lint, tests and smoke run.
Record pre-existing failures separately.

## Per batch
Behavior fix:
- focused regression
- relevant suite
- compile/type

Dead code:
- relevant tests
- build/type
- dead-code scan again
- graph update

Refactor:
- last-green baseline
- relevant tests after
- contract drift check
- graph update

Architecture:
- package/module tests
- full build
- dependency rules
- integration tests
- graph update

Dependency:
- install/lock consistency
- build/test
- advisory/security check
- runtime smoke if relevant

Performance:
- before/after benchmark
- correctness
- resource/memory checks if relevant

## Final record
For each command:
- command
- tool/version
- scope
- result
- duration if useful
- notes

Statuses:
`PASS`, `FAIL`, `SKIPPED`, `UNAVAILABLE`, `NOT_APPLICABLE`.

## Diff check
Inspect status, diff stat and meaningful diffs. Ensure no cache/generated/secret file entered
accidentally and the original workspace was not modified.

## Claim discipline
Never claim all tests passed when only a subset ran, zero vulnerabilities from one scanner,
safe dead-code deletion while dynamic uncertainty remains, or performance improvement without
measurement when measurement was feasible.
