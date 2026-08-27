# CI/CD Security Workflow

## Review existing pipeline

Map:
- triggers;
- PR/fork behavior;
- permissions;
- secrets;
- third-party actions;
- build artifacts;
- deploy environments;
- release signing;
- caches;
- package publishing.

## Fast PR gate

Target useful feedback:
- secret scan;
- diff-aware SAST;
- dependency audit;
- focused security regression;
- IaC/container checks for changed assets.

## Deep gate

Scheduled or release:
- full SAST;
- full SCA/SBOM;
- image scan;
- full authorized dynamic test;
- provenance/signing verification.

## Credentials

Prefer OIDC/workload identity and environment-scoped credentials.
Minimize token permissions.

## Untrusted PRs

Do not expose secrets to untrusted fork code.
Review risky trigger modes and shell interpolation.

## Third-party actions/plugins

Prefer trusted/pinned versions/digests according to platform policy.

## Failure semantics

Decide:
- advisory;
- block merge;
- block release.

Do not accidentally convert intended blockers into `continue-on-error` informational jobs.

## Evidence

Store SARIF/reports/artifacts according to repository policy without leaking sensitive proof data.
