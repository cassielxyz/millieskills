# API Security

API security is authorization-heavy.

## Inventory

Map:
- versioned routes;
- undocumented routes;
- deprecated routes;
- GraphQL;
- gRPC;
- websocket;
- webhooks;
- internal/admin APIs.

## Object-level authorization

Every endpoint receiving an object identifier should be checked for:
- owner;
- tenant;
- role;
- relationship;
- action.

Query-time scoping is stronger than filtering after retrieval.

## Function-level authorization

Admin/operator routes must enforce policy server-side even if not linked by the UI.

## Property-level authorization

Do not mass-assign arbitrary request fields into privileged model properties.
Define explicit writable/readable schemas by role/context.

## Authentication

Validate tokens fully:
- signature;
- issuer;
- audience;
- expiry;
- intended token type;
- revocation/rotation where applicable.

## Resource consumption

Bound:
- pagination;
- body size;
- upload size;
- query complexity;
- GraphQL depth/cost;
- expensive search;
- batch operations;
- concurrency.

## Business flows

Protect high-value flows from automated abuse:
- signup/invites;
- password reset;
- checkout;
- coupon/reward;
- reservation;
- export;
- expensive AI/job execution.

## Webhooks

Verify signature and replay/freshness where provider supports it.
Do not trust source IP alone when a cryptographic mechanism exists.

## Third-party API consumption

Validate:
- TLS;
- response schema;
- size;
- redirects;
- error handling;
- untrusted content passed to sinks/models.

## Errors

Do not leak stack traces/secrets/internal topology.
Keep machine-readable error semantics without exposing internals.
