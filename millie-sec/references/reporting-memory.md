# Reporting & Durable Security Memory

Security work should survive chat-session loss.

## Project security docs

Keep concise but evidence-bearing documents under:

```text
docs/millie-security/
```

## PROJECT_SECURITY_MAP.md

Record:
- architecture;
- services;
- trust boundaries;
- auth model;
- sensitive data;
- external interfaces;
- security-critical modules.

## THREAT_MODEL.md

Record:
- assets;
- actors;
- threats/abuse cases;
- controls;
- assumptions;
- unresolved items.

## ATTACK_SURFACE.md

Inventory reachable interfaces and privilege boundaries.

## CONTROL_MATRIX.md

Map standard/control → implementation → test/evidence → status.

## FINDINGS.md

One canonical normalized list.
Do not paste thousands of raw scanner lines; link artifacts.

## REMEDIATION_LOG.md

For each fix:
- finding;
- root cause;
- files;
- test;
- proof/re-scan;
- residual considerations.

## VERIFICATION_REPORT.md

Record what actually ran:
- command/tool/version;
- result;
- coverage;
- date;
- limitations.

## RESIDUAL_RISK.md

Must include:
- unresolved findings;
- accepted/deferred;
- blocked testing;
- environment assumptions;
- unsupported coverage;
- external risks not controlled by code.

## Memory

`memory/*.md` is concise operational context:
- auth model;
- data classes;
- security assumptions;
- known risk;
- useful commands.

Never store:
- passwords;
- tokens;
- private keys;
- secret values;
- production customer data;
- full exploit credentials.

## Evidence language

Say:

```text
"No confirmed high/critical findings remained within tested coverage."
```

Not:

```text
"The project has no vulnerabilities."
```
