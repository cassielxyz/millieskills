# Component & Effect Sourcing

Use external components to save implementation effort, not to outsource art direction.

## Source classes

### Foundation
shadcn/ui and project-native accessible primitives.

### Animated React source
SmoothUI, Unlumen UI, Animata/Animate UI and comparable registries can provide interaction patterns
and editable source. Adapt them to the product; do not preserve demo identity by default.

### Creative/WebGL source
ThreeUI Community can provide React/DOM/Canvas/WebGL/Three.js components and required assets. Prefer
official package/source paths; verify asset/license notices and version compatibility.

### Paid/pro catalogs
Examples such as Animmaster Pro or paid registry components may be used only when the user has
legitimate access. Public previews can inspire categories/patterns, not justify copying paid code.

## Selection score

```text
FIT 30
ACCESSIBILITY 15
MAINTAINABILITY 15
PERFORMANCE 12
STACK COMPATIBILITY 10
LICENSE/PROVENANCE 10
CUSTOMIZABILITY 8
```

Reject if a hard security/license/compatibility gate fails.

## Integration checklist

- install one primitive at a time when possible;
- remove demo data/copy/styles;
- map to local tokens;
- reuse local primitives;
- delete unused dependencies/assets;
- add reduced-motion behavior;
- test keyboard/touch;
- verify bundle/runtime cost;
- document non-obvious attribution/license needs.

## Anti-library soup

Do not combine five animation registries on one page. Prefer a small coherent source set and one
motion language.
