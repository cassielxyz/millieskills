# Anti-AI-Slop

This is not an AI detector.
It detects generic design decisions that reduce specificity and credibility.

## Five axes

Every meaningful design must make deliberate choices for:

1. color;
2. typography;
3. composition;
4. copy/content treatment;
5. motion/material.

If several axes are left on model defaults, the result will look generic.

## High-risk combinations

Watch for clusters such as:
- purple/indigo gradient + centered hero + dual CTA + three cards;
- cream + high-contrast serif + terracotta regardless of subject;
- near-black + acid accent regardless of subject;
- broadsheet/editorial grid regardless of subject;
- glass + glow + huge rounded cards;
- cyber product + Matrix/terminal/neon;
- dashboard + four stat cards + generic line chart;
- feature sections with icon tile + heading + one-line copy repeated six times.

Even once-distinctive design styles can become AI defaults when repeated without subject grounding.

## Component tells

Hero:
- generic promise;
- logo cloud without real logos;
- stats with invented numbers.

Cards:
- container for every grouping;
- nested cards;
- same radius/elevation everywhere.

Typography:
- same fashionable display font across unrelated projects;
- oversized heading as substitute for hierarchy.

Copy:
- "supercharge", "revolutionize", "seamless", "unlock the power" with no product-specific meaning.

Motion:
- every section fades up;
- repeated parallax;
- ambient loops everywhere.

Icons:
- every heading preceded by icon in colored rounded tile.

## Product-specificity check

Ask:
- What visual motif comes from the product itself?
- What content structure is unique to its job?
- What interaction could only make sense here?
- Does the palette/type/material connect to the subject?

## Repetition check

Compare recent fingerprint.

Do not swap purple for orange while keeping the same entire composition.

## v2: Library Slop

A polished registry component can still create generic output if pasted without product adaptation.
Detect:
- recognizable demo copy/data retained;
- multiple unrelated registry aesthetics mixed;
- trendy interaction chosen before task hierarchy;
- component API dictating product IA;
- default shadcn radius/palette left untouched when a distinct brand exists;
- every creative site using the same marquee, magnetic button, spotlight and text reveal quartet.

The cure is not "never use libraries"; it is **source the primitive, redesign the experience**.
