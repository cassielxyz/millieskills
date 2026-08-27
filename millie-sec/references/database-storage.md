# Database & Storage Security

## Query safety

Use parameterized/bound queries.
Use allowlists for structural identifiers that cannot be parameterized.

## Authorization at data layer

For multi-tenant systems:
- scope every query by trusted tenant context;
- consider row-level security where appropriate;
- test cross-tenant denial.

Do not retrieve global rows then filter in application memory for sensitive boundaries unless there
is a strong, verified reason.

## Constraints

Security can depend on:
- uniqueness;
- foreign keys;
- check constraints;
- non-null;
- atomic transitions.

Use database constraints as defense-in-depth for business invariants.

## Credentials

- least-privilege DB identity;
- separate migration/admin identity where practical;
- rotate/store secrets safely;
- no production credentials in developer files.

## Sensitive data

Define:
- whether storage is necessary;
- encryption requirement;
- retention;
- access logging;
- deletion;
- backups;
- replicas/analytics copies.

## Backups

Security review includes:
- encryption;
- access;
- retention;
- restore process;
- deletion expectations.

## Migrations

Review:
- accidental public exposure;
- insecure defaults;
- privilege changes;
- data backfills/logging;
- destructive fallback behavior.

## Cache/search/object storage

Authorization must cover secondary data stores too.
Avoid sensitive cache keys/values leaking across tenants.
