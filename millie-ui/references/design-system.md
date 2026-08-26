# Design System

## Tokens

Prefer semantic tokens:

```text
color.*
space.*
type.*
radius.*
border.*
elevation.*
motion.*
layer.*
size.*
```

Use aliases:
- `color.text.primary`
- `color.action.primary`
rather than component-specific raw values wherever maintainable.

## Spacing

Start with a controlled progression (4/8 based or project-native).
Rhythm matters more than blind grid obedience.

## Radius

Use a small intentional radius family.
Do not use the same huge radius on buttons, cards, dialogs, images and inputs by reflex.

## Elevation

Elevation should communicate stacking/interaction hierarchy.
Use dividers, grouping and whitespace before cards/shadows.

## Layer scale

Define:
- base;
- sticky;
- dropdown/popover;
- modal/sheet;
- toast;
- tooltip;
- critical overlay.

Avoid random `z-index: 9999`.

## Icons

Use one primary icon family for functional icons.
Use official product marks where applicable.
Custom icons must share geometry/stroke/fill language.

Do not put every icon inside a decorative rounded square.

## Imagery

Define:
- photography style;
- crop behavior;
- aspect ratios;
- illustration style;
- empty-state imagery;
- product screenshots;
- texture/grain rules.

## Component policy

Create reusable components where:
- behavior repeats;
- visual contract repeats;
- accessibility behavior repeats.

Do not componentize every wrapper solely to reduce file length.

## DESIGN.md

A good design contract names explicit budgets:
- number of accent families;
- type families;
- radius families;
- elevation levels;
- expressive moments per surface;
- motion intensity;
- glass usage;
- 3D usage.
