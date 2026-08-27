# Tool Routing

Tool count is not assurance.

Choose tools based on independent coverage, project stack, runtime availability and evidence quality.

## Routing order

1. existing project-native tools;
2. language/framework-native checks;
3. high-signal general security tools;
4. dynamic tools when environment permits;
5. specialist tools for detected domains.

## Suggested families

| Need | Primary options | Notes |
|---|---|---|
| SAST | Semgrep, CodeQL | Use data-flow/taint where valuable |
| Language security | ecosystem compiler/analyzers | Stack-dependent |
| Dependencies | OSV-Scanner, ecosystem audit, Trivy | Consider reachability/context |
| Secrets | Gitleaks, Trivy | Never print live secret values |
| SBOM | Syft, Trivy, CycloneDX tooling | Preserve as artifact |
| Containers | Trivy, Grype | Image + config as applicable |
| IaC | Trivy config, Checkov-class | Terraform/K8s/cloud templates |
| K8s | Kubescape-class + manual RBAC/network | Only if Kubernetes exists |
| Web/API DAST | Strix, ZAP-class tools | Authorized/local only |
| Mobile | MobSF/Frida-class + MASTG | Isolated test device/emulator |
| Supply chain | OpenSSF Scorecard, provenance/signature tools | Contextualize |
| Fuzzing | native fuzzers/property tests | High-value parsers/protocols |

## Install policy

Do not auto-install every tool.

Before installing:
- confirm it applies;
- prefer pinned/trusted package-manager or official releases;
- record version;
- avoid unreviewed remote shell installers where a safer channel exists;
- do not require privileged host installation when a container can isolate it.

## Coverage diversity

For a critical auth issue, useful independent lenses can be:
- manual data-flow review;
- targeted integration test;
- dynamic authorized validation.

Three similar regex scanners are not independent evidence.

## Fallbacks

If CodeQL unavailable:
- Semgrep + compiler/LSP + manual data-flow.

If Strix unavailable:
- framework test client + targeted DAST/manual authorized tests.

If SBOM generator unavailable:
- preserve lockfile inventory and record SBOM gap.

If mobile dynamic tooling unavailable:
- static MASVS/MASWE pass + emulator/build tests where possible.

## Tool result handling

Keep:
- command;
- version;
- target;
- timestamp;
- exit/result status;
- whether scan completed;
- limitations;
- raw artifact path.

Do not assume exit code zero means:
- no vulnerabilities;
- scan completion;
- coverage completeness.
