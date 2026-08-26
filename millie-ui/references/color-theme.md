# Color & Theme

## Semantic roles

```text
canvas
surface
surface_elevated
surface_interactive
text_primary
text_secondary
text_muted
border
border_strong
primary
primary_hover
primary_active
primary_soft
focus
success
warning
error
info
```

## Palette algorithm

1. Preserve verified brand color if present.
2. Choose neutral temperature.
3. Choose dominant hue family.
4. Choose color relationship:
   - monochrome
   - analogous
   - complementary
   - split complementary
   - triadic
   - image-derived
5. Generate tones.
6. Assign semantic roles.
7. Validate actual contrast pairs.
8. Build dark theme separately.
9. Test states, disabled, charts and overlays.
10. Compare with recent unrelated project palette.

## OKLCH

Use OKLCH for perceptual tonal manipulation where the stack/browser support is appropriate.

Do not just add/subtract RGB values.

Low-chroma tinted neutrals can create cohesion without obvious color cast.

## Contrast

Web AA target:
- 4.5:1 normal text;
- 3:1 qualifying large text;
- 3:1 important non-text UI boundaries/states.

Focus and target rules have separate accessibility requirements.

## Dark theme

Do not invert.
Re-evaluate:
- surface hierarchy;
- borders;
- elevation;
- saturated accents;
- imagery;
- semantic status colors.

Avoid pure black by reflex, but allow it if product/platform/context genuinely benefits.

## Gradients

Use for:
- material;
- atmosphere;
- light;
- brand field;
- depth;
- spatial path.

Never use gradient solely because flat color feels "not premium."
