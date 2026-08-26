# Native Platform Guidance

## Android

Design for dynamic windows:
- phone;
- tablet;
- foldable;
- desktop windowing;
- connected displays.

Use current adaptive APIs when project stack supports them.

Window-width classes:
- compact <600dp
- medium 600–839dp
- expanded 840–1199dp
- large 1200–1599dp
- extra-large >=1600dp

Navigation can adapt:
- bottom bar
- rail
- drawer/persistent pane
based on current adaptive information.

Canonical relationships:
- list-detail;
- supporting pane;
- feed.

Use current Android/Compose guidance rather than outdated resource-qualifier-only thinking for a
new Compose app.

Touch target:
- at least 48dp for interactive targets.

Respect:
- TalkBack semantics;
- keyboard/mouse;
- large text;
- orientation;
- split-screen;
- fold posture.

## Apple

Respect:
- safe areas;
- Dynamic Type;
- standard gestures;
- system navigation;
- pointer/keyboard on iPad/macOS;
- Reduce Motion;
- Reduce Transparency;
- Increase Contrast.

Current Liquid Glass:
- system controls/navigation adopt it automatically on current SDK/platform versions;
- it is a distinct functional layer above content;
- standard materials remain useful in content;
- custom glass should be sparse;
- clear glass belongs over visually rich content when appropriate.

Use native components before recreating platform behavior.

## Desktop

Professional desktop UI may need:
- menu/command structure;
- keyboard shortcuts;
- resizable panes;
- denser controls;
- context menus;
- multi-window/state persistence.

Do not use mobile-sized empty spacing everywhere.

## Wearable / spatial

Wearable:
- glanceable;
- low interaction burden;
- platform-native.

Spatial:
- comfort first;
- limited peripheral motion;
- avoid forced head/body gestures;
- keep controls in comfortable field of view;
- provide alternate input.
