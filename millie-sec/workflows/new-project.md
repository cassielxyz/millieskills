# New Project — Secure by Design

Use when Millie Security is invoked before or during creation of a new project.

## Goal

Security controls should be architectural defaults, not a patch sprint before launch.

## Phase A — Product security context

Before implementation identify:
- user/actor classes;
- sensitive data;
- high-value operations;
- trust boundaries;
- external services;
- deployment environment;
- auth requirements;
- compliance/business constraints if explicitly known.

Do not invent regulatory obligations.

## Phase B — Security architecture

Define:
- authentication provider/mechanism;
- session/token strategy;
- authorization model;
- tenant/ownership model;
- secrets strategy;
- database identities;
- network boundaries;
- file/upload policy;
- logging/redaction;
- dependency policy;
- cloud identity;
- AI tool permissions if applicable.

## Phase C — Secure scaffolding

Prefer framework defaults:
- CSRF/secure cookies where applicable;
- template auto-escaping;
- ORM parameterization;
- schema validation;
- central authz guard/policy;
- standard password/token libraries;
- TLS verification;
- safe error handler;
- security headers where relevant.

## Phase D — Security tests before release

Add negative tests for:
- unauthenticated access;
- wrong role;
- wrong tenant/owner;
- malformed input;
- dangerous parser/file conditions;
- rate/resource limits;
- replay/idempotency;
- secret redaction.

## Phase E — Tool baseline

Choose applicable:
- SAST;
- SCA;
- secret scan;
- SBOM;
- IaC/container scan;
- dynamic/local validation.

## Phase F — CI

Add fast PR checks plus deeper scheduled/release checks.

## Release gate

Do not release with:
- confirmed critical/high vulnerability;
- missing server-side authorization for sensitive operations;
- known live secret exposure;
- broken TLS validation;
- unbounded high-cost public operation without accepted risk;
- unsupported/untested high-risk path without explicit residual risk.

End with the normal Millie Security gate verdict.
