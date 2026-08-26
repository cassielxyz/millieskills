# Secure UI & Backend Contracts

Millie is not a replacement for a security/backend skill. This reference prevents frontends from
creating unsafe or dishonest UX around backend/security behavior.

## Authorization
- client-side hiding is not authorization;
- UI may hide unavailable actions for clarity, but server must enforce permissions;
- render 401/403/session-expired/reauth states deliberately;
- never expose admin/internal credentials to make a UI demo work.

## Auth UX
- do not reveal whether an account exists when the security model requires generic auth errors;
- keep recovery/support paths humane;
- represent MFA/passkey/device approval states accurately;
- never claim "encrypted/secure" without product evidence.

## Untrusted content / XSS
- prefer framework escaping and safe text sinks;
- avoid raw HTML escape hatches (`dangerouslySetInnerHTML`, unsafe HTML directives) unless content is
  appropriately sanitized for the context;
- validate dynamic URLs/protocols;
- treat rich-text renderers and third-party embeds as security boundaries.

## State-changing web actions
- UI methods/links must align with backend semantics;
- no destructive side effect on simple GET/navigation;
- do not assume SameSite alone solves every CSRF model; backend security owns the defense.

## Backend state model
Design for realistic outcomes:

```text
idle, pending, success,
400 validation, 401 unauthenticated, 403 forbidden,
404 missing, 409 conflict, 422 semantic validation,
429 rate limit, 5xx, timeout, offline, partial/realtime stale
```

Only include states relevant to the actual API.

## Optimistic UI
Use for reversible/low-risk actions with rollback. Do not optimistically display irreversible
payment/account/security success before backend confirmation.

## Sensitive data
- minimize displayed secrets/PII;
- mask/reveal with explicit user action where appropriate;
- clear copied-secret feedback; do not log secret values;
- avoid putting sensitive values in URLs.

## Uploads/downloads/external links
Represent scanning/processing/failure states if backend has them. Use safe target/rel practices for
external web links and do not render a filename as trusted HTML.
