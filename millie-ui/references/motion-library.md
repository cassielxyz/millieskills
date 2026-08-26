# Millie UI — Motion & Creative Interaction Library

Motion is selected by product frequency, art direction, input mode, accessibility, and performance.

---

## Base Timing Heuristics

Approximate starting ranges:
- press feedback: 80–140ms
- hover/focus: 120–220ms
- small state transition: 160–280ms
- panel/modal: 220–400ms
- occasional scene: 350–700ms

Tune based on distance and physical character.

High-frequency actions should feel faster than rare storytelling moments.

Prefer transforms/opacity for routine motion.
Avoid `transition: all`.

---

## 1. Press / Tactile Feedback

Use:
- scale 0.97–0.99
- 1–2px translation
- shadow compression
- spring release

Best:
- buttons
- cards
- controls

Avoid:
- large page regions

---

## 2. Card Flip

Use when front/back is a meaningful model.

Implementation:
- perspective container
- `transform-style: preserve-3d`
- front/back faces
- `backface-visibility: hidden`
- rotateY/rotateX

Accessibility:
- explicit button/tap trigger
- keyboard operable
- content not hover-only
- reduced-motion fallback to crossfade

---

## 3. Perspective Tilt

Pointer maps to small rotateX/rotateY.
Add optional translated highlight.

Rules:
- keep angle small
- damp pointer values
- stable clickable bounds
- disable/simplify on touch/reduced motion

---

## 4. Gradient Reflection / Glare

Recipe:
- pseudo-element
- radial/linear/conic gradient
- mask to surface
- low opacity
- transform/position based on pointer
- clip overflow

Use:
- premium card
- metallic product
- media tile
- rare CTA

Do not loop constantly across many cards.

---

## 5. Chrome / Holographic Sheen

Use layered:
- conic gradient
- blend mode
- subtle noise
- specular highlight

Optional WebGL shader for hero object.

Avoid:
- body text over moving spectral surface

---

## 6. Magnetic Button

Desktop fine-pointer enhancement.

Move inner visual layer toward pointer.
Keep actual hit target stable.

Use only on rare expressive CTA.

---

## 7. Text Mask Reveal

Options:
- clip-path
- overflow-hidden line wrappers
- CSS mask
- SplitText or equivalent for complex choreography

Preserve semantic text.
Avoid blocking content for long durations.

---

## 8. Kinetic Typography

Use:
- variable font axis interpolation
- scale/weight/width response
- scroll progress
- controlled stagger

Best:
- campaign
- editorial
- agency
- music/fashion

Avoid:
- dashboards
- long body text

---

## 9. Shared Layout Morph

Use when one object persists between states:
- card -> detail
- thumbnail -> viewer
- tab indicator
- selected item -> drawer header

Motion should explain continuity.

---

## 10. Page Transition

Use:
- fade/slide
- shared image
- mask/wipe
- color field
- spatial transition

Critical rule:
- do not delay navigation for spectacle
- preserve browser/history behavior

Modern View Transitions API may be suitable when supported.

---

## 11. Sticky Storytelling

Keep media/object fixed while textual beats progress.

Use:
- product explanation
- case study
- process
- timeline

Mobile:
- reduce pinned duration
- convert to stacked scenes if necessary

---

## 12. Scroll Scrub

Map scroll progress to:
- transform
- opacity
- clip
- camera
- object rotation
- shader uniform

Use GSAP ScrollTrigger or native scroll-driven animations where appropriate.

Never make the page unscrollable without good reason.

---

## 13. 3D Image Rotation on Scroll

Place images along a spatial path.
Map viewport/scroll progress to:
- Y
- Z
- rotateX/Y
- opacity

Use for galleries and creative storytelling.

Do not use on product data tables.

---

## 14. Image Sequence

Use compressed frames/video alternative for:
- product disassembly
- physical transformation
- cinematic object rotation

Lazy load frames.
Provide static fallback.

---

## 15. DOM + WebGL Sync

DOM:
- semantic content
- headings
- controls
- links

WebGL:
- spatial imagery
- distortion
- 3D objects
- particles

Use one scroll source and map DOM measurements into canvas coordinates.

---

## 16. Particle Field

Use:
- hero atmosphere
- scientific/spatial data
- game/entertainment

Prefer canvas/WebGL over thousands of DOM nodes.

Pause offscreen.
Reduce count on weak devices.

---

## 17. Fluid / Shader Distortion

Use:
- image transitions
- hero background
- creative portfolio

Keep controls/text outside distortion layer when possible.

---

## 18. Image Trail / Cursor Trail

Use:
- portfolio
- fashion
- gallery

Rules:
- fine pointer only
- throttle
- cap object count
- never cover important controls

---

## 19. Spotlight / Radial Follow

Pointer position drives subtle radial light.

Use:
- dark premium surface
- card highlight
- interactive hero

Do not make it the only indicator of hover/focus.

---

## 20. Marquee / Ticker

Use:
- logos
- culture/event
- tags
- market/media ticker when real data

Rules:
- pause/reduce motion support
- no essential info only in moving ticker

---

## 21. SVG Draw

Use:
- route
- diagram
- signature
- topology
- process

Animate `stroke-dasharray` / `stroke-dashoffset` or path progress.

---

## 22. Topology / Data Flow

Great for networking/security products.

Use actual structure when data exists.
For decorative motif, keep it clearly non-data.

Animate:
- path trace
- packet pulse
- node activation

Do not fabricate operational status.

---

## 23. Parallax

Use few depth layers.
Small amplitude.
Disable/reduce for motion-sensitive users.

Avoid whole-page parallax.

---

## 24. Morphing Material / Liquid Control

Use:
- current native system APIs when platform supports
- shape interpolation
- highlight/refraction response

Keep primary content stable.

---

## 25. Scroll-Cinematic 3D

Use only for immersive category.

Stack:
- Three.js/R3F
- GSAP ScrollTrigger or equivalent
- compressed assets
- adaptive DPR
- reduced mobile scene
- fallback media

Build the story before building the scene.
