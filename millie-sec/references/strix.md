# Strix Dynamic Validation

Strix is an optional high-value dynamic validation engine for authorized targets.

## Preferred targets

- local project clone;
- local isolated running service;
- user's owned staging environment;
- explicitly authorized API/URL.

Do not point Strix at third-party infrastructure without explicit authorization.

## Why use it

Strix workflows emphasize:
- dynamic execution;
- validated findings;
- proof/reproduction artifacts;
- remediation;
- re-scan;
- CI integration.

This makes it complementary to static analysis.

## Before run

Record:
- target;
- scope;
- auth/test accounts;
- excluded destructive actions;
- runtime/data isolation;
- repository commit;
- Strix version/config.

Prefer synthetic/test data.

## Artifacts

Depending on Strix version/mode, inspect:
- `penetration_test_report.md`;
- `vulnerabilities/*.md`;
- `vulnerabilities.json`;
- SARIF output;
- run metadata.

Do not copy sensitive proof material into public reports.

## Completion check

A successful process exit is not enough.

Verify:
- run reached intended completion;
- target stayed reachable;
- budget/turn/time limits did not truncate coverage;
- authentication worked;
- applicable routes were exercised;
- run metadata does not indicate stopped/partial state.

If partial:
- mark `PARTIAL`;
- retain findings;
- do not interpret missing findings as clean coverage.

## Finding workflow

For each serious Strix finding:
1. read affected code and proof;
2. safely reproduce in isolated/authorized environment when practical;
3. confirm impact;
4. locate root cause;
5. search variants;
6. patch root cause;
7. add regression test;
8. replay original proof;
9. re-run relevant Strix scope.

## CI

Where appropriate:
- diff-scoped PR scan;
- SARIF/code-scanning integration;
- deeper scheduled/merge scan;
- clear fail behavior.

Do not put production secrets directly in workflow files.
