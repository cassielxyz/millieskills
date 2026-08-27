# Cloud / Infrastructure Security Workflow

Only access accounts/environments that are explicitly authorized.

## Source-first

Review IaC before touching live cloud:
- Terraform;
- CloudFormation;
- Helm/Kubernetes;
- Docker;
- CI deployment workflows.

## Inventory

Map:
- accounts/subscriptions/projects;
- identities/roles;
- workloads;
- networks;
- public endpoints;
- databases/storage;
- secrets/KMS;
- registries;
- build/deploy roles.

## Automated

Use applicable:
- IaC scanning;
- image/container scanning;
- Kubernetes posture;
- secret scanning;
- SBOM.

## Manual

Prioritize:
- wildcard IAM;
- dangerous trust relationships;
- public storage;
- public admin/databases;
- metadata/SSRF impact;
- privileged containers;
- host mounts/socket;
- CI-to-cloud trust;
- production credentials.

## Live validation

Do not modify production resources just to "prove" a misconfiguration.
Prefer configuration evidence and read-only validation.

## Remediation

Change IaC/source of truth, not only live console state, unless the user explicitly needs emergency
containment.

## Exit

Re-plan/re-scan IaC and verify expected diff.
