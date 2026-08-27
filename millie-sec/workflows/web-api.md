# Web / API Security Workflow

## Coverage

Load:
- auth-access;
- web-security;
- api-security;
- input-output;
- business-logic;
- network-ssrf;
- files-parsers;
- database-storage;
- privacy/logging.

## Route inventory

Map every:
- route;
- method;
- auth requirement;
- role;
- object/tenant;
- request schema;
- response/sensitive fields;
- rate/cost profile.

## Negative authorization matrix

Exercise:
- anonymous;
- wrong role;
- wrong owner;
- wrong tenant;
- stale/revoked identity.

## Input/sink tracing

Trace:
- query/body/header/cookie/file;
- validation;
- authz;
- SQL/template/shell/path/URL/parser sinks.

## Runtime

Use:
- framework test clients;
- integration tests;
- Strix or another authorized DAST engine where valuable.

Avoid destructive state corruption; use test accounts/data.

## API-specific

Check:
- BOLA/BFLA/property auth;
- inventory/version drift;
- GraphQL cost/depth;
- webhooks;
- resource consumption;
- unsafe upstream consumption.

## Web-specific

Check:
- XSS/CSRF/CORS/CSP;
- cookies/session;
- redirect;
- headers;
- sensitive caching;
- websockets.

## Exit

All serious auth findings need explicit negative tests.
