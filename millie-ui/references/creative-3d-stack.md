# Creative 3D Stack

## Framework routing

### Vanilla / framework-neutral
Three.js.

### React
React Three Fiber + Drei when React integration benefits the project. ThreeUI Community can provide
editable React/Three/WebGL starting points when a component actually fits.

### Svelte
Threlte is the natural declarative Three.js layer. It supports the Three.js feature set and provides
integrations such as Rapier, Theatre.js and GLTF helpers.

### Browser-authored motion
Theatre.js changes JS values through a dope sheet/graph editor. Use it for camera, light, shader,
object and complex UI sequencing when visual fine-tuning is valuable. It complements code; it is not
needed for normal button motion.

### Visual scene authoring
Spline is appropriate when the user wants/already has a visually authored interactive scene. Web
Code API can update variables/properties, trigger transitions and listen for events in React/Next/
Vanilla. Spline Viewer can react to page-level pointer/scroll interactions.

### No/low-code 3D inspiration
PeachWeb demonstrates keyframe + scroll-triggered WebGL storytelling and responsive 3D page patterns.
Treat it as an authoring/reference option, not a mandatory runtime dependency.

## Scene design
Define:
- semantic purpose;
- camera/framing;
- lighting;
- material palette;
- interaction mapping;
- scroll relationship;
- loading strategy;
- mobile quality tier;
- reduced-motion/static fallback.

## Performance
- compressed models/textures;
- adaptive DPR;
- instancing/reuse;
- on-demand rendering when scene is static;
- limited dynamic lights/shadows/post-processing;
- pause offscreen;
- lazy load after critical content unless 3D is the critical content;
- profile on representative mobile hardware.

## DOM + WebGL
Keep headings, copy, links, forms and critical actions in semantic DOM/native UI whenever possible.
Use WebGL for spatial imagery, product representation, atmosphere and interaction.
