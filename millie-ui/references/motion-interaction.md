# Motion & Interaction

## Five-question motion read

Before choosing motion for a described interaction:

1. Verb — what semantic action happened?
2. Reversibility — does opposite action exist?
3. Initiator — click/tap/key/system/scroll?
4. Spatial source — where does the new state come from?
5. Affordance load — frequency and stakes?

## Intensity

1–3:
- hover/focus/press only;
- minimal automatic motion.

4–6:
- functional transitions;
- shared-layout;
- restrained entrance sequences.

7–8:
- scroll choreography;
- kinetic type;
- richer gestures.

9–10:
- cinematic/immersive;
- only for surfaces whose job supports it.

## Timing

Starting ranges, tune by distance/context:
- press: 80–140ms
- hover/focus: 120–220ms
- small state: 160–280ms
- panel/dialog: 220–400ms
- scene: 350–700ms

Avoid slow motion on frequent controls.

## Easing

Enter/settle often uses strong ease-out or spring.
Exit is commonly slightly faster.
Opening/closing should feel like inverse states, not unrelated animations.

Avoid `ease-in` for most direct UI feedback where it makes the UI feel delayed.

## Properties

Routine motion:
- transform;
- opacity;
- filter only with care.

Avoid layout-triggering animation of width/height/top/left when a transform or modern platform
primitive can express the same behavior.

## Modern primitives

Consider:
- `@starting-style`;
- `transition-behavior: allow-discrete`;
- `interpolate-size`;
- `@property`;
- View Transitions API;
- scroll/view timelines;
- Web Animations API.

## Reduced motion

Preserve comprehension, remove unnecessary movement:
- replace travel/scale/depth with crossfade/instant;
- remove repetitive ambient loops;
- reduce parallax and camera motion;
- avoid blur-in/out for sensitive settings.

## Advanced vocabulary

- card flip
- perspective tilt
- glare/reflection
- magnetic attraction
- text/image masks
- variable-font axes
- shared layout
- image trail
- spotlight
- SVG line draw
- sticky narrative
- scroll scrub
- image sequence
- object morph
- shader transition
- particle field

Use only when earned.
