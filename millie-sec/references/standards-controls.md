# Standards & Control Matrix

Standards are coverage references, not check-box substitutes for reasoning.

## Web/application baseline

### OWASP ASVS 5.0

Use as the primary detailed application-control catalog when relevant.

Map applicable controls across areas such as:
- architecture;
- authentication;
- session;
- authorization;
- validation;
- cryptography;
- error/logging;
- data protection;
- communication;
- malicious code;
- business logic;
- files/resources;
- API/web services;
- configuration.

Do not claim ASVS conformance unless the project was actually assessed against the selected level
and evidence exists.

### OWASP Top 10:2025

Awareness categories:
1. Broken Access Control
2. Security Misconfiguration
3. Software Supply Chain Failures
4. Cryptographic Failures
5. Injection
6. Insecure Design
7. Authentication Failures
8. Software or Data Integrity Failures
9. Security Logging and Alerting Failures
10. Mishandling of Exceptional Conditions

Use it as broad risk coverage, not a complete test plan.

### OWASP WSTG

Use for authorized web dynamic/manual test planning.

## APIs

OWASP API Security Top 10 2023:
- object-level authorization;
- authentication;
- object-property authorization;
- resource consumption;
- function-level authorization;
- sensitive business flows;
- SSRF;
- misconfiguration;
- inventory;
- unsafe consumption of APIs.

Authorization deserves dedicated tests per role/object/tenant.

## Mobile

Use:
- OWASP MASVS;
- OWASP MASTG;
- OWASP MASWE.

Review storage, crypto, authentication, network, platform, code quality, resilience and privacy as
applicable.

## AI / agentic systems

Use OWASP GenAI/LLM and Agentic AI guidance for:
- prompt injection;
- unsafe output handling;
- excessive agency;
- sensitive disclosure;
- poisoning;
- insecure tool/action boundaries;
- unbounded resource use;
- system-prompt/secret handling;
- agent identity/authorization.

## Weakness catalog

Use CWE Top 25 as a useful common-weakness coverage lens, not a severity ranking for a specific
project.

## Secure development

Use NIST SSDF for practices such as:
- prepare organization/project;
- protect software;
- produce well-secured software;
- respond to vulnerabilities.

## Supply chain

Use:
- SBOM (CycloneDX/SPDX where applicable);
- SLSA provenance concepts;
- OpenSSF Scorecard signals;
- dependency pinning/lockfile integrity;
- artifact signing/verification where supported.

## Control evidence

For each control:

```text
CONTROL ID
APPLICABLE?
IMPLEMENTATION
TEST/EVIDENCE
STATUS
GAP
OWNER/LOCATION
```

Status:
- PASS
- PARTIAL
- FAIL
- NOT_APPLICABLE
- NOT_TESTED
