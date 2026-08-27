# Audit Context & Threat Model

Build understanding before naming vulnerabilities.

## Asset inventory

Identify:
- identities/accounts;
- tokens/credentials;
- user content;
- PII;
- payment/financial data;
- health/sensitive records if present;
- intellectual property;
- administrative capability;
- infrastructure credentials;
- build/release keys;
- model prompts/vector data for AI systems.

Classify:

```text
PUBLIC
INTERNAL
CONFIDENTIAL
HIGHLY_SENSITIVE
```

## Actors

Map:
- unauthenticated;
- normal user;
- privileged user;
- admin/operator;
- service identity;
- CI/release identity;
- third party;
- attacker-controlled external service;
- tenant A / tenant B.

## Trust boundaries

Common boundaries:
- browser ↔ server;
- mobile app ↔ API;
- API ↔ database;
- service ↔ service;
- app ↔ third-party API;
- parser ↔ uploaded file;
- CI ↔ artifact registry;
- cloud account ↔ workload;
- model ↔ tools;
- RAG retriever ↔ untrusted documents.

## Data-flow record

For important flow capture:

```text
source
actor
authentication state
authorization requirement
transformations
validation
storage
sink
external boundary
sensitive data
failure behavior
```

## Authorization matrix

Create one when object/function access matters:

| Operation | Anonymous | User | Manager | Admin | Tenant boundary |
|---|---:|---:|---:|---:|---|
| Read own object | No | Yes | Yes | Yes | Own only |
| Read other user | No | No | Policy | Yes | Enforced |
| Delete | No | Own | Policy | Yes | Enforced |

Test the matrix server-side, not just UI visibility.

## Threat modeling

Use a pragmatic STRIDE-like pass where useful:
- spoofing → identity/authentication;
- tampering → integrity;
- repudiation → auditability;
- information disclosure → confidentiality;
- denial of service → availability/resource control;
- elevation → authorization/privilege.

Then add product-specific abuse cases.

## Abuse cases

Examples of categories:
- bypass intended workflow;
- perform action as wrong tenant/role;
- replay an operation;
- race two state changes;
- force high-cost resource consumption;
- submit malicious structured content;
- cause server to reach internal network;
- trick AI tool into exposing protected data;
- poison build/dependency resolution.

Document hypotheses; do not label them vulnerabilities until evidence supports the claim.

## Security assumptions

Every important assumption should have:
- statement;
- owner/enforcer;
- evidence;
- consequence if false.

Bad assumption:

```text
Only admins know this URL.
```

Good:

```text
Every admin operation passes centralized server-side role authorization;
tests exercise a non-admin request and expect denial.
```
