# Millie Security v1.0 — Research & Design Report

Research refresh: 2026-08-27.

## Objective

Build a portable security Agent Skill where the user can say:

```text
Use millie-sec to secure this project.
```

and the coding agent follows a complete autonomous security-hardening pipeline without the user
manually requesting every scanner/test/remediation phase.

The skill must:
- protect the original project;
- support existing and new projects;
- understand before scanning;
- combine multiple evidence sources;
- dynamically validate only in authorized scope;
- fix root causes;
- re-test fixes;
- add durable guardrails;
- document coverage and residual risk;
- never claim absolute security.

## Filtering the user's resource list

The user's broader Millie research list contains excellent UI, animation, 3D, agent and engineering
resources. A security skill should not absorb unrelated material.

The central architectural decision was therefore:

```text
RELEVANCE FILTER
      ↓
SECURITY WEIGHTS
      ↓
PROGRESSIVE DISCLOSURE
```

rather than:

```text
LOAD EVERYTHING
```

### Weight 10.0 — foundational

#### Strix
Why:
- autonomous/dynamic security validation;
- validated findings/proof;
- remediation workflow;
- re-scan;
- CI/SARIF;
- source/app/API modes.

Millie adaptation:
- optional dynamic specialist;
- local/owned/authorized targets only;
- run-completion verification;
- root-cause remediation + proof replay;
- never treat process exit alone as coverage.

#### Trail of Bits Agent Skills
Why:
- audit-context building before bug hunting;
- variant analysis;
- semantic/static analysis;
- testing/fuzzing/sanitizer mindset;
- supply-chain thinking;
- strong anti-rationalization discipline.

Millie adaptation:
- context before verdict;
- pattern-family search after a confirmed issue;
- evidence over tool output;
- progressive reference loading.

#### OWASP
Primary sources:
- ASVS 5.0;
- Top 10:2025;
- WSTG;
- API Security Top 10 2023;
- MASVS/MASTG/MASWE;
- GenAI/Agentic AI security.

Millie adaptation:
- standards/control router;
- web/API/mobile/AI domain references;
- control evidence matrix.

### Weight 9.5 — Anthropic Claude Security workflows

Useful ideas:
- independent verification;
- patching/security repair in a scratch copy;
- attempts to refute serious findings;
- separation between scan, patch, verify.

Millie adaptation:
- isolated project;
- verification lenses;
- do not trust candidate finding merely because a scanner produced it.

### Weight 9.0 — Semgrep Skills

Useful ideas:
- cross-language code security;
- taint/data-flow;
- OWASP/CWE-oriented rules;
- custom rule development;
- test-driven rules;
- CI diff scanning.

Millie adaptation:
- Semgrep as a high-value SAST option;
- taint for source→sink classes;
- custom rules after a known vulnerability pattern.

### Weight 8.5 — NIST SSDF

Useful for:
- secure development lifecycle;
- secure software production;
- protection of software;
- vulnerability response.

Millie adaptation:
- new-project secure-by-design mode;
- CI/release/handoff model.

### Weight 8.5 — Antigravity Awesome Skills security subsets

The very large skill collection is useful only when filtered.

Relevant bundles:
- Security Engineer;
- Security Developer;
- API security;
- authentication;
- backend security;
- security auditor;
- vulnerability scanning;
- cloud penetration/security.

Millie deliberately rejects loading the whole 1,400+ collection.

### Weight 8.5 — Backend/Auth/API skills

Security depends heavily on server-side behavior, especially:
- authentication;
- session/token handling;
- authorization;
- multi-tenancy;
- API validation;
- DB query scoping;
- webhooks;
- business logic.

These belong in Millie Security because UI security alone cannot enforce them.

### Weight 8.0 — OpenSSF / SLSA / SBOM ecosystem

Influence:
- dependency/supplier posture;
- provenance;
- SBOM;
- artifact/release integrity;
- CI trust.

### Weight 8.0 — Superpowers / Claude Superpower

Influence:
- test-driven changes;
- evidence before completion;
- systematic debugging;
- structured review.

Not used as a security knowledge base.

### Weight 7.5 — gstack

Useful pattern:
- adversarial independent second opinion;
- security-specialist review for relevant changes.

Millie adaptation:
- independent finding-refutation lens;
- optional second-agent challenge.

### Weight 6.5 — Ruflo

Useful only as optional orchestration:
- multi-agent security specialist routing;
- parallel domain work for very large repos.

Not required for ordinary Millie operation.

### Weight 5.0 — BRAIN.md-style memory

Useful concept:
- durable assumptions/rationale/project security context.

Millie stores only non-secret concise memory under `docs/millie-security/memory/`.

### Weight 4.0 — FreeBuf

Potentially useful for situational threat intelligence/community awareness.

Not authoritative enough to drive fixes without primary-source verification.

## Low or excluded user-list resources

These resources are intentionally not imported into the security core:

- GSAP;
- Refero styles;
- ThreeUI;
- img2three.js;
- React Native Reanimated;
- Stitch UI integration;
- Taste;
- Awesome Claude Design;
- visual DESIGN.md Chrome tools;
- Unlumen;
- Smooth UI;
- AnimMaster;
- Threlte;
- PeachWeb;
- Theatre.js;
- Spline.

Reason:
they are UI/motion/3D/design tools, not application-security methodologies.

shadcn/UI/UX Pro/Impeccable/Agentation have only incidental security overlap.

The correct Millie architecture is:
- `millie-ui` owns those resources;
- `millie-sec` owns security;
- future `millie-api` owns deep backend architecture;
- skills cooperate without duplicating the entire universe.

## Security-method synthesis

The strongest shared pattern across the high-weight sources is:

```text
UNDERSTAND
    ↓
COVER BROADLY
    ↓
VALIDATE
    ↓
REFUTE
    ↓
FIX ROOT CAUSE
    ↓
SEARCH VARIANTS
    ↓
RE-TEST
    ↓
KEEP AUTOMATED GUARDRAILS
```

This became the central Millie pipeline.

## Key improvements beyond a traditional security skill

### 1. Repository trust before build

Security agents frequently execute the target project.
That creates a security paradox: malicious repo setup can attack the auditor.

Millie introduces an explicit repository trust gate before install/build/test.

### 2. Clone-first remediation

The original workspace is not the repair target.
The secured clone is an independent output.

### 3. Coverage ledger

Missing tools/runtime do not silently disappear.
Coverage is explicit and machine-readable.

### 4. Finding verification panel

High/critical candidates are challenged from:
- code/data-flow;
- runtime;
- refutation.

### 5. Variant analysis

A confirmed vulnerability is treated as a pattern family, not a one-line patch.

### 6. Dynamic scan completion evidence

A tool exit status cannot substitute for run completion/coverage.

### 7. Root-cause remediation

Examples:
- auth policy, not UI hiding;
- parameterization, not payload blocklist;
- correct URL/egress design, not one SSRF hostname block;
- secret rotation + manager, not line deletion.

### 8. Security regression tests

Every serious fix should become a durable denial/invariant test when practical.

### 9. New-project mode

Millie can secure architecture before vulnerable code is written.

### 10. Residual-risk honesty

Millie never promises perfect security.

## Source index

See `references/source-index.md`.

## Machine-readable resource weights

See `data/source-weights.json`.

## Validation philosophy

Package validation checks:
- required files;
- relative links;
- JSON syntax;
- Python compilation;
- SKILL router size.

Behavioral correctness requires running evaluation cases against each target coding agent.
