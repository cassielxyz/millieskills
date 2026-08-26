# Production Hardening, UX Copy & i18n

## Reachable states

Test:
- first load;
- loading;
- empty;
- partial data;
- error;
- permission denied;
- offline/slow network if relevant;
- success;
- destructive undo/recovery;
- expired session;
- long content;
- large data;
- zero/one/many items.

## UX copy

Use product vocabulary.

Error:
- what happened;
- what user can do;
- preserve work.

Button:
- action-specific label;
- avoid vague "Submit" when "Create invoice" is clearer.

Destructive:
- name the consequence.

## Localization

Test:
- 30–50% text expansion;
- long German/Finnish-like compounds;
- CJK density;
- RTL;
- dates;
- times;
- currency;
- decimal/grouping separators;
- plural rules.

Use logical CSS properties where possible.

Avoid:
- concatenating translated fragments;
- icons whose direction is wrong in RTL;
- fixed-width labels that clip.

## Content resilience

Do not rely on:
- exactly 2-line titles;
- short usernames;
- all images loading;
- every data field existing.

## Accessibility hardening

- live updates announced where needed;
- focus placed/restored around dialogs/routes appropriately;
- modal traps only when semantics require;
- no inaccessible custom select when native/established primitive works.
