# Verification & Audit

## Bounded visual verification

Preferred:
1. complete implementation pass;
2. render representative environments in one batch;
3. collect all defects;
4. one consolidated fix;
5. one confirmation pass;
6. stop.

## Web matrix

As relevant:
- 360-ish narrow phone;
- 390–430 phone;
- tablet/narrow window;
- laptop;
- wide desktop;
- intermediate breakpoint boundaries;
- 200% zoom / reflow;
- reduced motion;
- coarse pointer;
- keyboard-only.

## States

- default
- hover
- focus-visible
- pressed
- selected
- disabled
- loading
- success
- error
- empty
- long content
- missing image
- slow response

## Technical checks

- build;
- lint;
- typecheck;
- tests;
- console errors;
- failed network requests;
- accessibility tooling;
- performance tooling where relevant.

## Visual checks

- primary task visible;
- hierarchy;
- alignment;
- spacing rhythm;
- typography;
- contrast;
- component state distinction;
- mobile recomposition;
- no accidental overflow;
- visual originality;
- design-system consistency;
- meaningful signature detail.

## Audit format

```text
[BLOCKER] src/path:123 — Accessibility
Problem:
Why it matters:
Fix:
```

Severity:
- BLOCKER
- HIGH
- MEDIUM
- LOW
- INFO

End verdict:
- SHIP
- SHIP WITH KNOWN ISSUES
- DO NOT SHIP

## No false evidence

Never claim:
- rendered;
- tested;
- audited;
- passed;
unless the corresponding action occurred.

## v2 creative verification

For motion/scroll/3D additionally inspect:
- initial/mid/final/reverse state;
- interruption and repeated interaction;
- resize/orientation after initialization;
- reduced motion;
- touch vs pointer;
- nested scroll/focus behavior;
- FPS/jank on representative hardware when possible;
- scene/asset load failure and fallback;
- memory/listener/timeline cleanup on navigation.

For third-party components, verify license/source provenance and remove unused demo assets/dependencies.
