# Authentication, Sessions & Authorization

Identity and authorization are separate questions.

## Authentication

Review:
- password storage and reset;
- MFA/recovery;
- OAuth/OIDC validation;
- redirect URI handling;
- PKCE where appropriate;
- JWT signature/algorithm/audience/issuer/expiry;
- token rotation/revocation;
- session fixation;
- credential stuffing/rate controls;
- login enumeration;
- magic links/one-time tokens;
- service-to-service identity.

Never store reusable credentials in client bundles.

## Sessions

Check:
- unpredictable IDs;
- secure cookie flags where cookies are used;
- appropriate SameSite;
- session rotation after privilege/auth changes;
- logout/revocation;
- idle/absolute expiry where required;
- CSRF controls for credential-bearing browser requests;
- no sensitive session material in URLs/logs.

## Authorization

Enforce server-side.

Test:
- object-level;
- function-level;
- field/property-level;
- tenant isolation;
- ownership;
- role transitions;
- admin-only actions;
- background jobs/workers;
- exports/downloads;
- GraphQL resolvers;
- websocket/subscription channels.

## Authorization matrix testing

For each sensitive operation include negative cases:
- anonymous;
- wrong role;
- wrong tenant;
- wrong owner;
- stale/revoked identity;
- guessed/alternate object identifier.

The UI hiding an action is not authorization.

## Centralization

Prefer centralized policy/guard/middleware when it preserves object-specific checks.

Avoid:
- duplicated ad-hoc role string checks;
- client-side-only policy;
- default-allow on missing context;
- trusting caller-supplied tenant/user IDs;
- checking ownership after side effects.

## Multi-tenancy

Tenant identity should come from trusted authenticated context.
Database queries should scope tenant/owner at the query/control layer, not filter after fetching.
