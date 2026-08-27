# Business Logic & Abuse

Business-logic vulnerabilities often pass static scanners.

## Build state machine

For high-value workflows map:

```text
states
allowed transition
actor
precondition
side effect
idempotency
rollback
```

Examples:
- order/payment;
- subscription;
- invite;
- password reset;
- account recovery;
- role approval;
- coupon/reward;
- resource provisioning;
- file publishing.

## Abuse questions

Can a user:
- skip a required state;
- repeat a one-time operation;
- reorder steps;
- submit stale data;
- modify price/quantity/owner/tenant fields;
- race two requests;
- trigger side effect twice;
- consume unlimited resources;
- create negative/overflow values;
- use an expired approval/token;
- perform operation on another tenant?

## Race / TOCTOU

Sensitive read-check-write sequences may need:
- transaction;
- atomic update;
- lock;
- unique constraint;
- idempotency key;
- version/compare-and-swap.

## Idempotency

For retry-prone high-impact operations:
- use stable request identity;
- persist result;
- return consistent response;
- avoid duplicate side effects.

## Rate / quota

Rate limits should be:
- identity-aware;
- endpoint/operation-aware;
- distributed consistently;
- bounded under attacker-controlled keys.

Do not rely solely on client-side debounce.

## Financial/value flows

Use server-authoritative values.
Never trust client price/discount/role/entitlement fields.
