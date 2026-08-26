# Responsive Layout & Proportion

## General

Design to the app/window, not the hardware label.

Inputs:
- width;
- height;
- aspect ratio;
- orientation;
- safe area;
- pointer type;
- hover;
- touch;
- keyboard;
- text scaling;
- zoom;
- fold posture;
- split-screen.

## Web

Use:
- media queries for macro;
- container queries for components;
- Grid/Flexbox;
- `minmax`;
- `auto-fit/auto-fill` when appropriate;
- `clamp`;
- logical properties;
- `aspect-ratio`;
- `srcset/sizes`;
- safe areas.

Breakpoints happen where content/layout fails.

## Density

- 1–3 gallery
- 4–7 general product
- 8–10 cockpit/pro data

Dense UI should reduce decorative containers, not merely shrink everything.

## Proportion

Priority:
- P0 primary task/content
- P1 frequent support
- P2 context
- P3 decoration

P3 never dominates P0.

## Responsive grid

Do not choose columns by device name.

```text
candidate = floor(usable_width / minimum_useful_item_width)
```

Then cap for comprehension.

## Mobile recomposition

Possible transformations:
- columns -> stacked;
- persistent sidebar -> drawer/bottom nav;
- master-detail -> separate routes/sheets;
- inline controls -> bottom sheet/menu;
- dense toolbar -> primary actions + overflow;
- hover preview -> tap disclosure.

Do not merely shrink type and spacing.

## Android current width classes

When using current adaptive APIs:
- compact <600dp
- medium 600–839dp
- expanded 840–1199dp
- large 1200–1599dp
- extra-large >=1600dp

Treat width/height classes as runtime state.

## Touch

Desktop precision can use smaller visual controls, but touch targets remain comfortable and
platform-appropriate.
