# Millie UI — Color System & Palette Algorithm

## Goal

Create context-fit semantic palettes algorithmically without repeating the same AI-default colors.

## Inputs

Priority:
1. explicit user/brand colors
2. existing production tokens
3. logo/identity
4. imagery
5. platform dynamic colors
6. Auto Premium palette engine

## Semantic Roles

At minimum:
- canvas
- surface
- surfaceElevated
- surfaceInteractive
- textPrimary
- textSecondary
- textMuted
- border
- borderStrong
- primary
- primaryHover
- primaryActive
- primarySoft
- focus
- success
- warning
- error
- info

Components consume roles, not raw palette values.

## Auto Palette Algorithm

### Step 1 — Neutral temperature
Choose:
- warm
- neutral
- cool

Match product and style.

### Step 2 — Dominant hue
Choose from context/fingerprint.
Do not default to purple/blue.

### Step 3 — Relationship
Choose:
- monochrome
- analogous
- complementary
- split complementary
- triadic
- image-derived

### Step 4 — Tone generation

For modern web projects, OKLCH is preferred when support permits:

`oklch(L C H)`

Control:
- L = perceived lightness
- C = chroma
- H = hue

Keep hue fairly stable across a tonal family.
Reduce chroma near extreme light/dark tones when necessary.

Example tone lightness ladder:
`97, 94, 88, 80, 70, 60, 50, 40, 30, 22, 15`

This is a starting family, not a law.

### Step 5 — Tinted neutrals
For refined UI, neutrals can borrow a very low chroma from the dominant hue.

### Step 6 — Semantic states
Success/warning/error/info need distinct meaning and adequate contrast.
Do not force all states to match brand hue.

### Step 7 — Interaction states
Primary hover/active states must visibly change without creating contrast failure.

### Step 8 — Dark mode
Design independently.
Do not invert light theme mechanically.

### Step 9 — Validate
Check actual foreground/background pairs.

Web AA minimum:
- 4.5:1 normal text
- 3:1 qualifying large text
- 3:1 important non-text boundaries/states

### Step 10 — Diversity
If previous unrelated project used the same dominant hue + material + theme mode, reroll one axis.

## Gradient Algorithm

Use gradients for:
- material/reflection
- atmosphere
- brand field
- depth
- visual path

Prefer perceptually smooth interpolation when available.

Do not use the generic purple-to-blue gradient unless art direction specifically supports it.

## Brand Color Accessibility

Preserve exact brand color for brand expression if needed.
Derive accessible action/container roles around it rather than forcing inaccessible text pairs.
