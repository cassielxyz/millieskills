# Mobile Security Workflow

## Inventory

Record:
- Android/iOS;
- framework/native/Flutter/React Native;
- app identifiers;
- build variants;
- API endpoints;
- local storage;
- deep links;
- webviews;
- native plugins;
- SDKs;
- permissions.

## Standards

Use MASVS/MASTG/MASWE coverage.

## Static pass

Review:
- manifest/entitlements;
- exported components;
- cleartext/network config;
- secrets;
- hard-coded endpoints;
- WebView settings;
- local storage;
- crypto;
- debug/release flags;
- third-party SDKs;
- dependency vulnerabilities.

## Dynamic pass

When build/emulator/test device exists:
- install release-like build;
- proxy authorized traffic;
- inspect runtime storage/logs;
- exercise deep links/inter-app paths;
- verify server authorization;
- inspect sensitive data leakage.

Optional MobSF/Frida-class tooling based on environment.

## Server boundary

Mobile app is untrusted from the server's perspective.
Repeat API authorization/security tests independently.

## Exit

Document which MASVS control groups were covered and which dynamic tests were blocked.
