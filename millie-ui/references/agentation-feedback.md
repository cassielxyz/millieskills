# Agentation / Visual Feedback

If Agentation (or equivalent structured visual annotation tooling) is available, use it to shorten the
feedback loop between rendered UI and source.

Useful annotation evidence can include:
- CSS selector;
- source file/path;
- React component hierarchy;
- computed styles;
- user note;
- intent/priority.

## Workflow
1. collect annotations;
2. group duplicate/root-cause notes;
3. map to source;
4. fix as a batch;
5. re-render once;
6. resolve/confirm annotations.

Do not patch each annotation independently if one token/component/root layout bug explains many.

## Motion feedback
When tooling allows freezing/pausing animation, inspect meaningful frames: start, overshoot, settled,
mid-scroll, reversed state. Fix temporal issues using the motion source, not static CSS symptoms.
