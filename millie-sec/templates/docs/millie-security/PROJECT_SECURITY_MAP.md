# Project Security Map

## Assessment identity
- Repository/workspace:
- Baseline commit:
- Security workspace:
- Assessment date:
- Runtime/environment:

## Architecture
Describe services/packages and security-critical boundaries.

## Actors and roles
| Actor | Authentication | Privileges | Notes |
|---|---|---|---|

## Sensitive assets/data
| Asset/data | Classification | Storage | Authorized actors |
|---|---|---|---|

## External interfaces
| Interface | Protocol | Auth | Exposure | Handler/module |
|---|---|---|---|---|

## Security-critical modules
- Authentication:
- Authorization:
- Secrets/config:
- Parsing/uploads:
- Network clients:
- Data access:
- Admin/privileged:
- CI/release:

## Trust boundaries
See `graphs/trust-boundaries.json`.

## Known dynamic/uncertain behavior
Document framework magic, reflection, plugins, generated routes, native bridges, runtime policy, etc.
