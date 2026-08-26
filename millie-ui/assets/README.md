# Millie UI/UX Assets

This folder contains the standalone SVG assets referenced by the Millie UI/UX README.

## Structure

```text
assets/
├── brand/
│   ├── millie-logo.svg
│   ├── millie-mark.svg
│   └── millie-ui.svg
├── banners/
├── icons/
└── brands/
```

## Design language

Millie custom assets use a shared spectrum:

```text
pink → orange → amber → green → cyan → violet
```

Functional icons use a lightweight geometric stroke style.

## Brand compatibility assets

The files in `assets/brands/` are deliberately neutral compatibility badges rather than copies of
vendor logos. This avoids implying official endorsement or bundling trademark artwork without
separate licensing review.

You may replace them with appropriately licensed official marks while preserving the filenames
used by your README.

## Usage

```html
<img src="./assets/icons/palette.svg" width="27" align="center" alt="" />
```

All assets are standalone SVG files and do not require external fonts, CSS, images, or JavaScript.
