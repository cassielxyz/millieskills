# Millie UI — 3D / WebGL Engineering Reference

## Decision

3D is justified when it adds:
- product understanding
- spatial comprehension
- storytelling
- brand identity
- immersive exploration

3D is weak when added to:
- login
- settings
- CRUD admin
- checkout
- basic docs
- dense forms

## Complexity Ladder

1. CSS transforms/perspective
2. SVG/Canvas 2D
3. authored embed/Spline
4. Three.js
5. React Three Fiber/Drei
6. custom shader/post-processing

## Responsive Canvas

On resize:
- update camera aspect
- update projection
- resize renderer to display size
- cap/adapt DPR
- account for orientation/container changes

## Performance

- lazy load
- compress textures/models
- KTX2/Basis where appropriate
- Draco/Meshopt where appropriate
- instance repeated geometry
- reuse materials/geometries
- avoid allocations in render loop
- avoid React state per frame
- reduce dynamic shadows/lights
- bake when possible
- use on-demand rendering for static scenes
- reduce post processing during motion/on weak devices
- provide poster/video/2D fallback

## Accessibility

- semantic content outside canvas when possible
- keyboard-accessible controls
- reduced-motion camera path
- no essential information only in 3D
- clear fallback
