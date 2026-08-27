# Full Security Pipeline

Millie Security is an evidence pipeline, not a scanner wrapper.

## State machine

```text
TARGET
  ↓
AUTHORIZATION / SCOPE
  ↓
ISOLATE / TRUST GATE
  ↓
BASELINE
  ↓
SECURITY CONTEXT
  ↓
THREAT MODEL
  ↓
COVERAGE PLAN
  ↓
STATIC / SCA / SECRETS / IAC
  ↓
MANUAL DATA-FLOW + VARIANT ANALYSIS
  ↓
ISOLATED RUNTIME
  ↓
AUTHORIZED DYNAMIC VALIDATION
  ↓
DOMAIN PASSES
  ↓
VERIFY FINDINGS
  ↓
PRIORITIZE
  ↓
REMEDIATE ROOT CAUSES
  ↓
SECURITY REGRESSION TESTS
  ↓
REPLAY / RESCAN / FULL REGRESSION
  ↓
CI / SBOM / SECURE DEFAULTS
  ↓
RESIDUAL RISK + HANDOFF
```

## Phase 0 — Authorization and target classification

Classify:
- local user-provided source;
- user's own local service;
- owned staging;
- production;
- third-party/external target;
- cloud account;
- mobile application;
- AI/agent system.

Local source review is normally safe to proceed.
Dynamic or intrusive testing of an external target requires explicit authorization.

Write scope:
- in-scope repos/services;
- excluded systems;
- test accounts;
- allowed environments;
- destructive-test restrictions;
- data handling limits.

## Phase 1 — Isolation and repository trust

Existing project:
- create independent sibling clone/copy;
- preserve legitimate uncommitted state;
- do not copy ignored secrets by default;
- disable accidental pushes;
- inspect executable setup before running it.

Output:
`docs/millie-security/BASELINE_REPORT.md` trust section.

## Phase 2 — Inventory and baseline

Detect:
- languages/frameworks;
- package managers/lockfiles;
- services/workspaces;
- tests/build;
- authentication/authorization;
- databases;
- containers/IaC;
- CI/CD;
- mobile;
- AI/agent/RAG;
- public interfaces.

Only after trust gate:
- establish build/test baseline;
- record pre-existing failures.

Security fixes must not be blamed for failures that already existed.

## Phase 3 — Security context

Build:
- assets;
- sensitive data classes;
- actors/roles;
- tenants;
- external interfaces;
- privilege boundaries;
- trust boundaries;
- data flows;
- administrative paths;
- secrets/configuration boundaries;
- third-party services.

## Phase 4 — Threat model

Create abuse cases around:
- identity;
- authorization;
- data exposure;
- injection/parsing;
- workflow/state abuse;
- resource exhaustion;
- supply chain;
- cloud/build boundaries;
- AI tool/model boundaries.

Map controls to likely threats.

## Phase 5 — Coverage plan

Create a machine-readable coverage ledger:

```json
{
  "domain": "dependency-risk",
  "applicable": true,
  "method": ["osv-scanner", "manual-lockfile-review"],
  "status": "planned",
  "limitations": []
}
```

Every applicable domain finishes as:
- covered;
- partially-covered;
- blocked;
- not-applicable.

Never silently omit a domain.

## Phase 6 — Broad automated passes

Run applicable:
- SAST/data-flow;
- dependency/SCA;
- secret scanning;
- license/SBOM;
- IaC/container/Kubernetes;
- CI workflow/security configuration;
- language-native security checks.

Preserve raw results in artifacts when useful.
Normalize findings before triage.

## Phase 7 — Manual audit and variant analysis

Automated scans do not replace reasoning.

Trace:
- source → transformations → validation → sink;
- identity → authorization decision → object;
- untrusted file/data → parser/interpreter;
- external URL → resolver/client → network destination;
- user-controlled workflow → state transition;
- secret → build/log/client/storage.

For a confirmed pattern, search for variants across the codebase.

## Phase 8 — Runtime preparation

Prefer local isolated runtime:
- test database;
- non-production credentials;
- local containers;
- seeded synthetic data;
- test tenant/user roles;
- outbound network restrictions when practical.

Do not point tests at production data by default.

## Phase 9 — Authorized dynamic validation

Use the least disruptive method that can prove or refute a serious issue.

Potential engines:
- existing integration/E2E tests;
- targeted HTTP/API tests;
- Strix;
- ZAP-class DAST;
- framework test clients;
- mobile dynamic tools.

Dynamic validation should not become indiscriminate destructive fuzzing.

## Phase 10 — Domain passes

Load applicable specialized references.

A web API with cloud deployment may need:
- auth/access;
- API;
- web;
- business logic;
- SSRF/network;
- files/parsers;
- database;
- supply chain;
- cloud/IaC;
- logging/privacy.

A mobile app adds MASVS/MASTG-oriented review.
An AI agent adds model/tool/RAG boundaries.

## Phase 11 — Finding verification

Normalize duplicates.
Use independent evidence.
Try to disprove high/critical findings.
Classify confidence and applicability.

## Phase 12 — Remediation

Patch:
- root cause;
- related variants;
- secure default;
- tests;
- documentation.

Keep business behavior intact unless insecure behavior itself is the requirement being removed.

## Phase 13 — Re-test

For every confirmed high/critical:
- run focused regression;
- replay original safe proof;
- re-run relevant scanner;
- re-run adjacent variant search.

Then run broader tests/build/scans.

## Phase 14 — Continuous controls

Add only useful gates:
- SAST;
- SCA;
- secrets;
- SBOM;
- IaC/container;
- security regression;
- PR diff scans;
- scheduled deep scan.

The pipeline should fail clearly, not silently fail open.

## Phase 15 — Handoff

Produce:
- secured working project;
- changed-files summary;
- confirmed/closed findings;
- residual findings;
- untested/blocked areas;
- coverage ledger;
- verification evidence;
- security gate verdict.

## Recovery behavior

If a tool is unavailable:
1. do not stop the entire pipeline;
2. record the gap;
3. choose a credible substitute;
4. use manual analysis where possible;
5. lower assurance only for the affected coverage.

If build/runtime cannot start:
- continue source/SCA/secrets/IaC/manual review;
- document DAST/runtime gap;
- do not fabricate dynamic validation.
