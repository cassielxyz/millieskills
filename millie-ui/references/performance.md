# UI Performance

## Web experience metrics

Watch:
- LCP — important content appears quickly;
- CLS — layout remains stable;
- INP — interactions respond quickly.

## Images

- responsive `srcset`/`sizes`;
- correct transfer size;
- dimensions/aspect-ratio reserved;
- modern formats where supported;
- lazy load noncritical media;
- prioritize likely LCP media appropriately.

## CSS / rendering

Be cautious with:
- many backdrop filters;
- huge blur regions;
- fixed full-screen filters;
- animated filters;
- giant shadows;
- complex clipping on many elements.

`content-visibility: auto` can reduce offscreen rendering work for large regions when compatible
with the content and accessibility/measurement requirements.

## Motion

Prefer compositor-friendly transform/opacity for frequent animation.

Avoid JS scroll loops if CSS scroll timelines can express the effect cleanly.

## JS

Avoid installing heavy libraries for trivial effects.
Tree-shake/code-split when the stack supports it.

## Fonts

Minimize families/weights.
Prevent layout shift.

## Canvas/WebGL

- cap/adapt DPR;
- pause offscreen;
- use on-demand rendering for static scenes;
- avoid allocations in render loop;
- instance repeated objects;
- compress models/textures;
- reduce post processing on weak devices.

## Measurement

Optimization should be evidence-backed when profiling/lab tools are available.
