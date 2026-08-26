# Scroll & Interactive Storytelling

Scroll can be navigation, reading progression, animation input or scene time. Decide which.

## Native-first
Use normal document scroll for most sites. CSS scroll/view timelines can handle many progress-linked
effects without JS.

## GSAP ScrollTrigger
Choose when you need coordinated timelines, scrub, pin, snap, responsive trigger logic or complex
multi-element choreography beyond CSS.

Good patterns:
- product assembly/exploded view;
- pinned media with changing narrative copy;
- controlled image sequence;
- timeline/progress story;
- horizontal visual track inside a vertically understandable page;
- camera/object animation tied to story progress.

## Flip
Use for continuity across DOM/layout changes: grid -> detail, filter/reorder, dock/morph, card expand.

## Observer
Use for explicit gesture-driven experiences (wheel/touch/pointer) only with clear navigation and a
keyboard/touch-accessible alternate path.

## ScrollSmoother
Use only if smoothing materially improves the intended atmosphere. It should retain native scrolling
semantics; touch smoothing should be conservative. Never add it to a productivity/transaction surface
just to feel "premium."

## Anti-scroll-jacking
Avoid:
- blocking normal scrollbar behavior;
- mandatory full-screen section snapping for ordinary content;
- endless pinned sequences;
- sideways content with no obvious progress;
- stealing wheel events from nested controls;
- fixed-height stories that break zoom/text expansion.

## Implementation discipline
- establish DOM content and reading order first;
- mark start/end triggers visually during development when useful;
- use responsive setup/matchMedia;
- clean up timelines/listeners in SPA lifecycle;
- refresh positions after fonts/media/layout changes if the engine requires it;
- pause expensive offscreen animation;
- reduced motion replaces scrub/camera travel with readable static states.
