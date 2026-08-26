# Living Design Memory

## Root DESIGN.md

For a long-lived project, `DESIGN.md` is a compact execution contract.

Suggested sections:

```text
Design thesis
Product/surface modes
Design dials
Typography
Color
Spacing/layout
Shape/elevation/material
Icons/imagery
Motion
Interaction states
Responsive behavior
Accessibility
Performance budgets
Signature motifs
Explicit anti-patterns
Exceptions
Per-surface checklist
```

## Evidence mode

Existing repo:
- cite actual file paths;
- name actual tokens;
- name actual components;
- document what polished surfaces actually do.

Do not invent a rule because it sounds good.

## Merge mode

If design docs already exist:
- preserve unique rules;
- deduplicate;
- flag contradictions;
- leave one source of truth.

## New project

Once Millie selects the direction:
- write the chosen system;
- include explicit budgets;
- do not include all rejected candidates.

## Surface brief

For very complex products, optional per-surface brief:

```text
docs/millie-ui/surfaces/<surface>.md
```

Include:
- mode;
- primary job;
- density;
- special interaction;
- departures from DESIGN.md.

Do not create surface briefs for every trivial screen.

## Cross-project history

`~/.millie-ui/history.json` stores only non-sensitive fingerprints.
Never store source code, customer data, prompts, credentials, or product secrets.
