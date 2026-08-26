# Millie UI — Auto Art Direction & Uniqueness Engine

Use when the user did not give a meaningful UI direction.

## Goal

Produce a premium design automatically while preventing repeated AI aesthetics across projects.

## 1. Build Project Signature

Create:

```text
identity = [
  project_name,
  product_category,
  primary_user,
  primary_job,
  platform,
  brand_seed_if_any
]
```

## 2. Derive Design Axes

Select independently but coherently:

### Composition families
- centered-monument
- asymmetric-columns
- editorial-grid
- modular-grid
- edge-to-edge-media
- split-stage
- layered-canvas
- sidebar-workspace
- top-nav-workspace
- command-surface
- cardless-flow
- masonry/editorial
- sticky-story
- scene-based

### Type characters
- rational-grotesk
- humanist
- geometric
- neo-grotesk
- editorial-serif
- high-contrast-serif
- condensed-display
- wide-display
- rounded-friendly
- mono-technical
- expressive-variable

### Material languages
- flat-ink
- hairline-surface
- soft-elevation
- glass
- liquid-glass-inspired
- tactile
- clay
- hard-shadow
- paper
- chrome
- spatial
- cinematic

### Palette families
- ivory-ink-accent
- stone-jewel
- warm-earth
- cool-mineral
- midnight-pearl
- graphite-high-vis
- monochrome
- muted-editorial
- pastel-friendly
- saturated-graphic
- image-derived
- dynamic-material

### Motion languages
- near-static
- precise-functional
- soft-spring
- editorial-mask
- kinetic-type
- tactile-physical
- cinematic-depth
- scroll-story
- spatial-3d

### Signature details
- reflection-sweep
- image-mask
- custom-rule-system
- split-type
- topology-trace
- art-directed-crop
- tactile-press
- focus-spotlight
- object-morph
- page-transition
- 3d-object
- shader-field
- editorial-numbering
- asymmetric-navigation
- dynamic-artwork-color

## 3. Candidate Generation

Generate 3 candidates from different primary style families.

Bad:
- glass + glass + glass with different accent colors

Good:
- refined editorial
- tactile contemporary
- dark spatial

## 4. Fit Checks

For each candidate ask:

- Does it fit trust expectations?
- Does it fit content density?
- Does it fit interaction frequency?
- Does it fit audience?
- Does it fit platform conventions?
- Does it fit available assets?
- Can it remain accessible?
- Can it remain performant?
- Is it too close to a category cliché?
- Is it too close to a recent design?

## 5. Novelty Control

Set novelty level:

```text
0 = conservative institutional
1 = refined product
2 = distinctive premium
3 = expressive creative
4 = experimental experience
```

Default:
- government/critical finance/medical -> 0–1
- enterprise/SaaS/productivity -> 1–2
- consumer/commerce -> 1–2
- agency/portfolio/fashion/music -> 2–4
- campaign/experimental -> 3–4

Novelty changes composition and motion more than basic usability conventions.

## 6. Premium Palette Autogeneration

If no brand palette:

1. choose neutral temperature;
2. choose dominant hue family from project fingerprint;
3. choose relationship (monochrome/analogous/complementary/split/triadic);
4. generate semantic tonal roles;
5. reserve strongest chroma for primary focus;
6. validate contrast;
7. derive dark mode separately if needed;
8. reject generic purple-blue unless product context genuinely fits it;
9. compare dominant hue to recent projects and reroll when unnecessarily repeated.

### Example refined families

These are examples, not templates:
- warm ivory + espresso + oxblood
- bone + deep forest + muted brass
- pearl + midnight blue + cobalt
- fog + graphite + vermilion
- sand + dark cocoa + terracotta
- cool gray + deep teal + coral
- charcoal + off-white + electric chartreuse
- cream + ink + ultramarine

Do not reuse these exact palettes constantly.

## 7. Layout Diversity

If recent project was:
- centered hero -> prefer asymmetric/split/editorial where fit
- bento -> avoid bento
- sidebar -> consider top-nav/multi-pane
- dark -> consider light/mixed
- glass -> prefer flat/tactile/editorial
- serif luxury -> prefer modern grotesk or vice versa

## 8. Persistent History

If the environment allows writing user-level state, store only non-sensitive design fingerprints:

`~/.millie-ui/history.json`

Example:

```json
{
  "recent": [
    {
      "project": "hashed-or-generic-id",
      "primary_style": "editorial-luxury",
      "composition": "asymmetric-columns",
      "type": "high-contrast-serif",
      "palette": "warm-refined",
      "material": "flat-ink",
      "motion": "editorial-mask"
    }
  ]
}
```

Do not store user secrets, source code, customer data, or project contents.

If global state is not appropriate/available, do not create it.
Use deterministic project-derived variation instead.

## 9. Deterministic Fallback

The included `scripts/design_seed.py` produces stable style-axis suggestions from a non-sensitive
project identity string. It is a diversity aid, not a substitute for design judgment.

## 10. Never Let the Seed Override Fitness

If the seed selects claymorphism for a bank transaction console, reject it.
The seed introduces variation only inside the acceptable candidate set.
