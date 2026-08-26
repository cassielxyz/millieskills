# Research First

Research is mandatory for substantial unfamiliar/brand-critical/creative work when tools permit; it
is intentionally skipped for trivial edits.

## Three evidence layers

1. **Style** — art direction, typography, color, material, composition.
2. **Screen** — concrete pattern/layout decisions.
3. **Flow** — journey sequence, states, transitions, recovery.

This mirrors the useful separation found in research-first systems such as Refero without making any
single external service mandatory.

## Reference locks

Before major implementation, lock 2–5 references:

```yaml
- url_or_source:
  layer: style|screen|flow|motion|3d
  decisions_to_borrow:
  decisions_to_avoid:
  relevance:
```

Do not average ten unrelated references into generic middle-of-the-road UI.

## Preferred research sequence

1. user references / brand assets;
2. existing project;
3. direct competitors and category leaders;
4. real product flows;
5. current design showcases / Refero styles / curated DESIGN.md examples;
6. current platform docs;
7. open-source implementation references;
8. community criticism for failure modes.

## Decision ledger

For large work record 5–12 decisions, e.g.:

```text
D01 — Product list remains cardless because comparison is primary.
Evidence: competitor flow A + existing table conventions.
D02 — One image-led scroll sequence only; all product actions stay normal flow.
Evidence: campaign reference B + performance budget.
```

## Copyright / originality

Extract principles: rhythm, density, transition topology, content hierarchy, material logic.
Do not clone trademarks, logos, exact copy, proprietary imagery, or highly distinctive protected
compositions when an original solution can satisfy the brief.
