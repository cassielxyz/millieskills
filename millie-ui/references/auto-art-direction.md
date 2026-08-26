# Auto Art Direction & Design Fingerprints

Use when the user provides no meaningful visual direction or asks for options.

## Candidate construction

Create three candidates from genuinely different design families.

Each candidate:

```yaml
style:
secondary_influence:
composition:
type_character:
palette_character:
neutral_temperature:
material:
image_icon_language:
motion:
signature:
density:
theme:
immersion:
```

Bad:
- three glass designs with different accent colors.

Good:
- refined editorial;
- tactile contemporary;
- dark spatial.

## Fit score

Use a consistency rubric:

```text
product/task fit      22
audience fit          12
surface-mode fit      12
content fit           10
platform fit          10
trust/error-cost       8
brand fit              8
accessibility           7
performance             5
originality             3
implementation          3
                     ----
                      100
```

Hard-gate failures disqualify a candidate.

## Diversity

Fingerprint axes:
- style;
- composition;
- typography;
- dominant hue family;
- neutral temperature;
- material;
- motion;
- signature;
- theme;
- density;
- immersion.

If 5+ match an unrelated recent fingerprint, change the weakest-fit repeated axes.

## Dynamic dials

Set:
- DESIGN_VARIANCE;
- MOTION_INTENSITY;
- VISUAL_DENSITY;
- IMMERSION.

Do not use a universal default.

## Style-fit hints

High trust:
- refined minimal;
- Swiss;
- editorial;
- monochrome precision;
- data precision.

Friendly:
- organic;
- soft graphic;
- tactile;
- clay accents.

Distinctive:
- neobrutalism;
- maximalist;
- anti-grid;
- retro-futurist;
- immersive.

Luxury:
- luxury minimal;
- editorial luxe;
- dark cinematic;
- heritage;
- restrained geometric/Art-Deco influence.

Spatial/product:
- layered spatial;
- 3D showcase;
- DOM + WebGL.

## Project-derived fallback

If no persistent history:
derive variation from:
- project name;
- category;
- audience;
- primary task;
- platform.

Use `scripts/fingerprint.py` when convenient.

Never let a deterministic seed override fitness.
