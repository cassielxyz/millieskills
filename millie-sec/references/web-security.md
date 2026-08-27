# Web Security

Apply based on architecture.

## Browser/server boundary

Review:
- cookies/session;
- CSRF;
- CORS;
- XSS;
- CSP;
- clickjacking;
- open redirect;
- cache behavior;
- host/header trust;
- security headers;
- sensitive data in URLs;
- mixed content/TLS.

## CORS

Do not use permissive origins with credentials.
Validate exact trusted origins.
Treat origin reflection carefully.
Remember CORS is a browser policy, not API authorization.

## CSRF

State-changing cookie-authenticated requests need appropriate CSRF defense unless architecture
provides an equivalent property.

## CSP

Use CSP as defense-in-depth.
Avoid policies so permissive they provide little value.
Test application behavior before tightening.

## Headers

Consider:
- HSTS where HTTPS is mandatory;
- frame restrictions;
- MIME sniffing protection;
- referrer policy;
- permissions policy;
- secure cache policy for sensitive responses.

## Redirects

Allowlist/normalize destinations.
Do not redirect to arbitrary user-supplied schemes/hosts.

## Cache

Ensure personalized/sensitive responses are not cached/shared incorrectly.
Review CDN/cache-key assumptions and authorization interactions.

## WebSockets/realtime

Authenticate connection and authorize each sensitive channel/action.
Handle token expiry/revocation and origin expectations.

## File/download endpoints

Enforce authorization before content retrieval.
Set safe content disposition/type.
Do not trust client filename/path.
