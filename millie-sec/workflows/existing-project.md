# Existing Project — Full Security Hardening

## 1. Clone first

Create independent sibling clone/copy.
Preserve legitimate dirty work.
Do not run setup before trust gate.

## 2. Baseline

Record:
- commit/branch;
- dirty-state reproduction;
- project stack;
- existing test/build status;
- existing security tooling;
- public interfaces.

## 3. Context

Map:
- assets;
- roles;
- tenants;
- auth;
- sensitive data;
- APIs;
- admin flows;
- data flows;
- cloud/build boundaries.

## 4. Discover

Run applicable automated scanners and manual audit.

Do not fix immediately after first scanner output if whole-system context is not complete.

## 5. Validate

Normalize and independently verify serious findings.
Dynamic validation stays local/owned/authorized.

## 6. Repair

Fix in priority batches:
- P0;
- P1;
- systemic P2.

Each batch:
- root cause;
- variants;
- regression test;
- focused verification;
- broader regression.

## 7. Harden

Add:
- secure defaults;
- security CI;
- SBOM/provenance where appropriate;
- documentation;
- monitoring/logging controls.

## 8. Handoff

Original remains untouched.
Secured clone contains code and `docs/millie-security/`.

Do not merge/push unless separately requested.
