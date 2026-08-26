# Image -> 3D -> Website Pipeline

A single image is incomplete 3D evidence. Be explicit about inference.

## 1. Suitability / rights

Check:
- user owns/has permission for the image or use is otherwise appropriate;
- object is sufficiently visible;
- silhouette/materials can be inferred;
- hidden sides will require approximation;
- reflective/transparent/organic objects may be harder.

## 2. Reconstruction route

Preferred when `img2threejs` is available:
- delegate the object reconstruction to that specialized skill;
- keep its assessment/spec/quality gates;
- generate an animation-ready procedural `THREE.Group`/factory;
- compare reference beside render through passes.

If unavailable:
- simple geometry -> procedural Three.js;
- complex asset -> use user-supplied GLTF/GLB or suitable modeling route;
- do not promise 1:1 geometry from a single photo.

## 3. Web integration

Choose:
- Three.js for vanilla/framework neutral;
- R3F/Drei for React;
- Threlte for Svelte;
- Spline when a visually authored scene is desired and compatible.

Build:
- deterministic asset/component API;
- camera + lighting matching product identity;
- loading placeholder/poster;
- orbit/drag only when useful;
- hotspots/labels in accessible DOM where possible;
- scroll choreography only when the story benefits.

## 4. Animation readiness

Separate logical parts/pivots/material controls needed for later animation. Keep camera/object state
controllable from the chosen motion system (GSAP, Theatre, R3F, etc.).

## 5. Quality gates

- silhouette/proportion;
- camera/perspective;
- major color/material;
- recognizable details;
- interaction pivots;
- mobile framing;
- performance;
- static/reduced-motion fallback.
