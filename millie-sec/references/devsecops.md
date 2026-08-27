# DevSecOps & Continuous Security

The final secured codebase should resist regression.

## PR gates

Potential controls:
- diff-aware SAST;
- secret scan;
- dependency/SCA;
- security regression tests;
- IaC/container scan;
- Strix/dynamic diff scan where environment supports it.

Fast gates should finish quickly enough that developers do not bypass them.

## Scheduled/deep

Run broader:
- full SAST;
- dependency inventory;
- container images;
- full authorized DAST/pentest;
- SBOM;
- provenance posture;
- mobile deep testing.

## SBOM

Generate per release/artifact where useful.
Store/attach to release system, not necessarily source repo if policy differs.

## Provenance/signing

Where supported:
- trusted build identity;
- attestation;
- signature;
- verification in deploy path.

## CI secrets

Use:
- environment/repo secret store;
- OIDC/workload identity;
- minimal permissions;
- environment approval for production.

Never put long-lived deployment credentials in workflow YAML.

## GitHub Actions-style review

Check:
- explicit permissions;
- third-party action pinning policy;
- untrusted PR input used in shell;
- `pull_request_target` risks;
- artifact/script trust;
- cache poisoning assumptions;
- fork secret exposure.

## Fail-open risk

A security job that says:

```text
continue-on-error: true
```

or swallows scanner failures may be informational rather than a gate.

Make intended enforcement explicit.

## Exceptions

Security exceptions need:
- reason;
- scope;
- expiry/review;
- compensating control;
- owner;
- test/evidence.
