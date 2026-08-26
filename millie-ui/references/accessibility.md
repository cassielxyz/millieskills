# Accessibility

Target WCAG 2.2 for web unless project requirements specify otherwise.

## Core

- semantic HTML/native roles;
- accessible names;
- visible labels;
- keyboard support;
- logical focus order;
- visible focus;
- focus not obscured;
- reflow/zoom;
- contrast;
- target size/spacing;
- reduced motion;
- drag alternative;
- no hover-only critical content;
- no color-only status.

## Contrast

AA:
- normal text 4.5:1;
- qualifying large text 3:1;
- important non-text UI 3:1.

Do not round failing values.

## Target size

WCAG 2.2 minimum target criterion is 24x24 CSS px with documented exceptions/spacing behavior.
Prefer larger comfortable targets for touch.

Android:
- aim at least 48dp interactive target.

Apple:
- follow current platform recommended/default control sizes.

## Focus

Do not `outline: none` without a visible replacement.
Ensure sticky headers/sheets do not hide the focused item.

## Forms

- explicit labels;
- instructions;
- fieldset/legend for related sets;
- programmatic error relation;
- concise correction guidance;
- dynamic overall errors announced appropriately.

Placeholder is not a label.

## Drag

If functionality depends on dragging and drag is not essential, provide a single-pointer
non-drag alternative.

## Motion

Honor reduced motion.
Avoid sustained/repetitive motion, rapid flashing, unnecessary zoom/depth.

## Native

Use built-in accessible components and semantics before custom controls.

Test actual screen reader/keyboard behavior when tooling/device access allows.
