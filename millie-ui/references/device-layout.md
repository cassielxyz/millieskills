# Millie UI — Device, Proportion, Size & Placement Reference

## Principle

Design to the available window and interaction capabilities, not only a physical device label.

Consider:
- width/height
- aspect ratio
- orientation
- safe area
- touch vs pointer
- hover
- keyboard
- dynamic text/zoom
- reduced motion
- contrast/transparency settings
- fold/hinge posture

## Web

Macro layout:
- viewport media queries

Component layout:
- container queries

Use:
- CSS Grid/Flexbox
- `minmax()`
- `auto-fit`
- `clamp()`
- `min()`/`max()`
- logical properties
- `aspect-ratio`
- safe-area environment variables

Breakpoints belong where layout/content fails.

## Android Adaptive Width

- Compact `<600dp`
- Medium `600–839dp`
- Expanded `840–1199dp`
- Large `1200–1599dp`
- Extra-large `>=1600dp`

Height:
- Compact `<480dp`
- Medium `480–899dp`
- Expanded `>=900dp`

Adapt at runtime.

## Apple Platforms

Respect:
- safe areas
- Dynamic Type
- resizable iPad/Mac windows
- keyboard/system overlays
- platform navigation
- current material behavior
- accessibility settings

## Touch Targets

Prefer comfortable targets beyond bare minimums.
Web WCAG 2.2 minimum target size has a 24x24 CSS-pixel criterion with exceptions/spacing rules.
Native mobile commonly benefits from larger platform-standard targets.

## Reading

For sustained body copy:
- roughly 60–75 characters per line

## Placement

Rank:
- P0 task-critical
- P1 frequent support
- P2 context
- P3 decoration

Never let P3 move, obscure, or overpower P0.

## Form Proportion

Avoid full-width inputs on very wide screens unless the content demands it.
Keep label, field, help, and error visually connected.

## Data Layout

Allow tables/data regions more width than prose.
Use horizontal strategies locally instead of making the whole page overflow.
