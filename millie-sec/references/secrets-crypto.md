# Secrets & Cryptography

## Secrets

A secret should not live in:
- source;
- committed config;
- frontend/mobile bundle when confidentiality is required;
- logs;
- error messages;
- analytics;
- test fixtures copied from production;
- screenshots/docs.

Use:
- environment injection;
- secret manager/vault/KMS;
- workload identity;
- short-lived credentials.

## Secret finding response

If a real secret was exposed:
1. do not repeat its value;
2. identify scope;
3. rotate/revoke;
4. remove from current code/config;
5. consider Git/history/artifact/cache exposure;
6. update documentation/tests to prevent recurrence.

Deleting the line without rotation may be insufficient.

## Cryptography

Prefer established library/platform primitives.

Review:
- algorithm suitability;
- key length;
- mode/nonces;
- randomness;
- key storage;
- key rotation;
- signature verification;
- certificate/TLS verification;
- password hashing;
- encryption-at-rest requirements;
- authenticated encryption where confidentiality + integrity are needed.

Do not:
- invent cryptographic algorithms;
- use deterministic/plain hashes for passwords;
- disable certificate validation;
- reuse nonces where the mode forbids it;
- hard-code encryption keys.

## Passwords

Use a modern password-hashing function with appropriate cost:
- Argon2id where supported;
- scrypt/bcrypt/PBKDF2 where platform policy dictates.

Never use reversible encryption as password storage.

## Tokens

Generate with a cryptographically secure RNG.
Bind purpose and expiry where relevant.
Avoid sensitive tokens in URLs when referrers/history/logging can expose them.
