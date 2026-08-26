# Typography

## Roles

- display
- heading
- body
- label
- numeric/data
- mono/code

## Character families

- rational grotesk
- humanist sans
- geometric sans
- neo-grotesk
- transitional serif
- editorial serif
- high-contrast serif
- condensed display
- wide display
- rounded friendly
- technical mono
- expressive variable

## Pairing

Pair on contrast:
- serif + sans;
- geometric + humanist;
- display + neutral text.

Or use one flexible superfamily.

Avoid two similar sans families with no meaningful distinction.

## Scale

Typical starting ratios:
- compact pro UI: ~1.125
- general product/read: ~1.20
- editorial/marketing: ~1.25
- dramatic display: up to ~1.333

Tune to copy length and viewport.

## Measure

Sustained body reading:
roughly 60–75 characters per line.

## Line height

- body ~1.45–1.65 depending on font/size;
- headings tighter;
- dense data labels tighter but still legible.

## Display text

Use `text-wrap: balance`/equivalent where supported for short headings.
Do not force headings to one line if localization makes that fragile.

## Numeric UI

Use tabular numerals for aligned changing numbers when the typeface supports them.

## Font loading

- preload only critical fonts;
- avoid excessive families/weights;
- use `font-display` thoughtfully;
- set fallback metrics where practical to reduce layout shift;
- use real italic/bold faces/axes.

## Anti-default

Do not ban common fonts.
Do not use them by reflex.

A familiar system font is often correct in dense native/pro UI.
A brand surface may deserve stronger display character.
