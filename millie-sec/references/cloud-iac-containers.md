# Cloud, IaC, Containers & Kubernetes

Only inspect/test cloud accounts with authorization.

## Cloud identity

Review:
- least privilege;
- wildcard permissions;
- trust policies;
- service-account impersonation;
- long-lived keys;
- workload identity;
- admin paths.

## Network exposure

Map:
- public endpoints;
- security groups/firewalls;
- load balancers;
- private services;
- database exposure;
- management ports;
- egress.

## Object storage

Check:
- public ACL/policy;
- cross-account access;
- encryption;
- versioning/retention needs;
- sensitive logs/backups.

## Secrets

Use cloud-native secret management/KMS/workload identity where appropriate.
Do not bake secrets into images/IaC state.

## Containers

Prefer:
- minimal trusted base;
- pinned digest/version policy;
- non-root;
- read-only filesystem where feasible;
- dropped capabilities;
- no privileged mode;
- no host Docker socket;
- bounded resources;
- image vulnerability scanning.

## Dockerfile

Review:
- remote unverified downloads;
- package pinning;
- secret layers;
- copying excessive context;
- unsafe permissions;
- shell injection in build args.

## Kubernetes

Review:
- RBAC;
- service accounts;
- privileged pods;
- hostPath/host network/PID;
- capabilities;
- seccomp;
- security contexts;
- network policy;
- secrets;
- admission/policy;
- image pinning;
- resource limits.

## IaC

Static scan Terraform/CloudFormation/K8s/Helm and review actual intent.
Avoid automatically applying fixes to production infrastructure.

## CI/cloud bridge

Protect OIDC/trust conditions and deployment roles.
A pull request should not automatically gain production credentials.
