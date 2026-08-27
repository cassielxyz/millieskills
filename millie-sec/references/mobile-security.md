# Mobile Security

Use OWASP MASVS/MASTG/MASWE as the primary mobile lens.

## Storage

Review:
- tokens;
- PII;
- local databases;
- files/cache;
- logs;
- backups;
- clipboard;
- screenshots;
- keychain/keystore usage.

Do not hard-code server secrets into a mobile app. A distributed client cannot keep a shared secret
confidential from its owner.

## Cryptography

Use platform keystore/keychain and vetted crypto.
Review key lifecycle and device backup behavior.

## Authentication

The server is authoritative.
Biometrics generally unlock local credentials/session; they should not substitute for server-side
authorization.

## Network

Review:
- TLS validation;
- cleartext exceptions;
- certificate pinning only where the product can operate it safely;
- proxy/debug config;
- sensitive data in URLs/logs.

Never disable TLS verification to make development easier in a release build.

## Platform

Review:
- exported Android components;
- intents/deep links;
- WebViews;
- custom URL schemes/universal/app links;
- iOS entitlements;
- pasteboard;
- file providers;
- notifications;
- inter-app communication.

## Code integrity/resilience

Apply proportionally to threat model:
- debug flags;
- signing;
- tamper/root/jailbreak detection;
- obfuscation;
- anti-debugging.

Resilience does not replace server authorization.

## Privacy

Review permissions, tracking, SDK collection, retention, purpose limitation.

## Dynamic analysis

When authorized and tooling exists:
- emulator/test device;
- MobSF-class static/dynamic analysis;
- Frida-class runtime inspection;
- proxy testing.

Use test accounts/data and record device/build/version.
