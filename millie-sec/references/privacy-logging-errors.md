# Privacy, Logging & Exceptional Conditions

## Data minimization

Collect/store only what the product needs.

For sensitive data define:
- purpose;
- access;
- retention;
- deletion;
- export;
- backup implications;
- third parties.

## Logs

Never log:
- passwords;
- raw session tokens;
- private keys;
- full auth headers;
- unnecessary payment/identity data.

Use structured redaction and test it.

## Audit logs

Security-relevant events may include:
- authentication;
- privilege change;
- sensitive admin action;
- key/secret management;
- critical configuration change;
- suspicious authorization denial patterns.

Protect audit log integrity/access.

## Error behavior

Exceptional conditions are attack surfaces.

Review:
- default-allow fallback;
- skipped authorization after exception;
- transaction partial completion;
- retry duplicate side effect;
- queue poison loops;
- sensitive stack trace;
- malformed input panic/resource leak.

Fail securely.

## User-facing errors

Provide enough information for recovery without exposing:
- stack;
- SQL;
- internal path;
- token;
- secret;
- detailed auth oracle.

## Alerts

Logs without actionable alerting may not satisfy critical detection needs.
Define thresholds/context for meaningful security events.
