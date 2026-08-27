# Dependencies & Software Supply Chain

## Dependency review

Inspect:
- manifest;
- lockfile;
- direct vs transitive dependencies;
- source/registry;
- version pinning;
- integrity hashes;
- lifecycle scripts;
- native binaries;
- abandoned/deprecated packages;
- duplicate vulnerable versions;
- dependency confusion/namespace risk.

## SCA

Use project-native audit plus OSV/Trivy-class scanning where useful.

A CVE finding needs context:
- affected version;
- vulnerable functionality;
- reachability;
- exposure;
- exploit status;
- compensating controls;
- fixed version/migration cost.

Do not auto-upgrade a major dependency without regression analysis.

## Known exploitation and probability

For CVEs, use inputs such as:
- CISA KEV;
- EPSS;
- vendor advisory;
- exploitability prerequisites;
- actual project reachability.

EPSS alone is not a project risk score.

## SBOM

Generate a CycloneDX/SPDX SBOM where useful for release/operations.

Record:
- artifact/commit;
- generator/version;
- timestamp.

## Build provenance

Where supported:
- reproducible/hosted builds;
- provenance attestation;
- artifact signing;
- signature verification;
- trusted builders.

Use SLSA concepts proportionally.

## Open-source posture

OpenSSF Scorecard-style signals can help assess:
- branch protection;
- pinned dependencies/actions;
- vulnerability disclosure;
- dangerous workflows;
- release practices.

They are supplier signals, not proof that a dependency is vulnerability-free.

## CI dependencies

Review:
- GitHub Actions pinning;
- third-party actions;
- reusable workflow trust;
- package publishing credentials;
- provenance/signing;
- fork PR secret exposure.
