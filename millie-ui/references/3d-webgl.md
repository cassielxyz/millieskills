# 3D / WebGL / Spatial

## Decision

3D earns its cost when it improves:
- product understanding;
- spatial understanding;
- storytelling;
- identity;
- exploration.

## Complexity ladder

1. CSS 3D
2. SVG/Canvas
3. authored embed
4. Three.js
5. React Three Fiber/Drei
6. shaders/post processing

## Product showcase

Possible:
- orbit;
- material/color configurator;
- exploded view;
- hotspots;
- camera dolly;
- scroll-linked rotation.

## DOM + WebGL

Prefer:
- DOM for semantic text, links, controls;
- WebGL for atmosphere, spatial media, 3D objects.

Keep one coherent scroll/input source.

## Performance

- lazy load after critical content;
- compressed GLTF/textures;
- reuse geometry/material;
- instancing;
- adaptive DPR;
- reduced lights/shadows;
- on-demand rendering;
- lower-quality mobile mode;
- poster/2D fallback.

## Accessibility

- essential content outside canvas;
- keyboard-accessible controls;
- descriptive fallback;
- reduced camera motion;
- no required interaction only through drag/3D manipulation.

## Weak use cases

Do not add a 3D scene to:
- login;
- standard settings;
- CRUD table;
- checkout;
- docs;
just to make it "premium."

## v2 stack routing

For framework/tool-specific implementation also read:
- `creative-3d-stack.md`
- `image-to-3d-web.md`
- `scroll-storytelling.md`

Do not force React Three Fiber into Svelte (prefer Threlte) or hand-code a complex 3D editor scene
when a supplied Spline workflow is the user's chosen source of truth.
