# Remediation & Verification

## Root-cause workflow

```text
evidence
  ↓
root cause
  ↓
blast radius / variants
  ↓
framework-native control
  ↓
minimal coherent patch
  ↓
negative regression test
  ↓
focused test
  ↓
replay original proof
  ↓
re-scan
  ↓
broader regression
```

## Remediation qualities

A good fix:
- closes the violated security property;
- covers variants;
- preserves legitimate behavior;
- is easy to understand;
- uses existing architecture;
- is centrally enforceable where appropriate;
- fails securely;
- is tested.

## Authorization

Bad:
- hide button;
- block known ID;
- special-case proof request.

Good:
- centralized server-side policy;
- query scoped to trusted identity/tenant;
- negative tests for wrong user/role/tenant.

## Injection

Bad:
- block a payload substring.

Good:
- parameterize/encode/sandbox at the sink;
- remove dynamic interpreter path if unnecessary.

## SSRF

Bad:
- block `localhost` string.

Good:
- allowlist destination where possible;
- parse/resolve;
- block disallowed networks;
- validate redirects;
- egress restrict.

## Secrets

Bad:
- delete secret from current file.

Good:
- revoke/rotate;
- remove from source/history/artifacts as required;
- migrate to secret manager;
- add secret scanning/prevention.

## Dependency

Bad:
- force latest major without test.

Good:
- identify fixed compatible version;
- understand behavioral/security change;
- update lockfile;
- run full relevant tests;
- verify SCA finding is closed.

## Re-test

Original proof should fail for the expected defensive reason.
A server crash or timeout is not a successful security fix.

## Regression

Security control should have a durable automated test whenever practical.
