# Perceived Performance

Perceived latency is a design problem only after real performance is treated seriously.

## Very fast operations

Avoid flashing spinners for operations that normally complete almost instantly.

If a loader appears, prevent a 50–100ms flicker that reads as a glitch.

## Skeletons

Use when:
- content shape is predictable;
- wait is meaningful;
- layout stability matters.

Skeleton geometry should resemble final content.

Do not use three gray text bars as a placeholder for a card grid.

## Optimistic UI

Use for:
- reversible;
- low-risk;
- high-confidence actions.

Must have:
- failure rollback;
- visible failure explanation;
- restored state.

Do not optimistically pretend a payment or irreversible server action succeeded.

## Images

- reserve dimensions/aspect ratio;
- responsive source size;
- dominant-color or blur placeholder when useful;
- lazy load below-the-fold media;
- do not lazy-load likely LCP imagery blindly.

## Prefetch

Prefetch on strong intent where:
- resource cost is acceptable;
- privacy/security constraints allow;
- user benefit is meaningful.

## Progress

Use determinate progress when real progress can be measured.
Use indeterminate state when duration is unknown.

For long operations, explain:
- what is happening;
- whether the user can leave;
- whether work continues;
- cancellation/retry when supported.
