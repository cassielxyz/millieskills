# Motion Engine Selection

Pick the simplest engine that can faithfully express the interaction.

| Need | Preferred first choice |
|---|---|
| hover/focus/press | CSS |
| entry/exit simple web state | CSS / View Transitions / Motion |
| React spring/gesture/shared layout | Motion |
| complex authored web timeline | GSAP |
| scroll scrub/pin/snap choreography | GSAP ScrollTrigger when CSS is insufficient |
| DOM layout morph across states | Motion layout / GSAP Flip |
| wheel/touch/pointer directional experience | GSAP Observer with fallback |
| browser art-directed cinematic/keyframes | Theatre.js |
| React Native gestures/layout/scroll | Reanimated 4 + Gesture Handler |
| Svelte 3D | Threlte + Three.js |
| 3D visual authoring/embed | Spline |
| 3D code scene | Three.js / R3F / Threlte |

## CSS-first modern primitives

Consider before libraries:
- transitions for specific properties (not blanket `all`);
- `@starting-style`;
- discrete transition behavior;
- keyframes;
- `@property`;
- View Transitions;
- scroll/view timelines;
- Web Animations API.

## Cost test

Add a library only if it materially reduces complexity or enables a capability the current stack
cannot express clearly.

## Motion coherence

One product should feel like one physical/temporal world. Align spring character, easing, distance,
duration, stagger, blur/depth behavior and interruption handling.
