# Risk Prioritization

Severity is contextual.

## Inputs

Consider:
- confirmed runtime exploitation;
- confidence;
- external exposure;
- authentication prerequisite;
- privilege gained;
- tenant crossing;
- sensitive data;
- persistence/integrity impact;
- availability impact;
- affected asset criticality;
- vulnerable dependency reachability;
- known exploitation;
- exploit likelihood;
- compensating controls.

## Millie Priority Score

A transparent project-priority helper, not a standard replacement.

Example 0–100 weighting:

```text
Technical impact              0–25
Exploit/reproduction evidence 0–20
Exposure/reachability         0–15
Privilege/tenant crossing     0–15
Sensitive data/business       0–10
Known exploitation / KEV      0–8
Exploit likelihood / EPSS     0–4
Confidence                    0–3
```

Then adjust down only for a **verified** compensating control.

Never let the formula override obvious reality.

## CVSS

Use vendor/NVD CVSS as one technical severity input for CVEs.
Do not copy CVSS directly as the project's business risk.

## CISA KEV

Known-exploited status is a strong prioritization input when the vulnerable component is actually
present/reachable.

## EPSS

EPSS estimates exploitation probability for a CVE over a time horizon.
It does not capture:
- project exposure;
- data impact;
- tenant architecture;
- compensating controls;
- business criticality.

Use it as one input.

## Priority classes

```text
P0 — immediate/block release
P1 — fix before release / urgent
P2 — planned near-term
P3 — hardening/backlog
P4 — informational
```

A confirmed cross-tenant auth bypass usually outranks a higher-CVSS unreachable library issue.
