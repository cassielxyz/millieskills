# Finding Triage & Independent Verification

Normalize candidate findings before fixing.

## Unified record

Capture:
- ID;
- title;
- weakness/CWE when known;
- affected component;
- source tool/method;
- evidence;
- confidence;
- severity;
- exploitability prerequisites;
- impact;
- status;
- related variants;
- remediation;
- verification.

## Confidence

```text
CONFIRMED
Runtime/proof and code cause align.

HIGH-CONFIDENCE
Strong code/data-flow evidence; runtime validation unavailable or unnecessary.

PLAUSIBLE
Evidence suggests a weakness but key assumptions remain.

UNVERIFIED
Tool signal lacks enough context.

FALSE-POSITIVE
Evidence disproves applicability/exploitability.

NOT-APPLICABLE
Rule/domain does not apply to this system.
```

## Verification panel

For high/critical candidates use independent lenses when practical.

### Lens A — Code/data flow
Can attacker-controlled or wrong-tenant state reach the security-sensitive decision/sink?

### Lens B — Runtime
Can a safe test reproduce the violated security property?

### Lens C — Refutation
What assumption would make the finding false?
Check it explicitly.

## Duplicate normalization

Merge findings that share:
- same root cause;
- same sink;
- same affected policy.

Keep distinct instances when remediation/impact differs.

## Scanner disagreement

Do not vote by tool count.

Prefer:
- semantic evidence;
- runtime evidence;
- actual reachable configuration.

## Suppression

A suppression requires:
- why false/not-applicable;
- evidence;
- scope;
- owner;
- re-evaluation trigger if architecture changes.

Never suppress to get a green dashboard.
