#!/usr/bin/env python3
"""
Millie UI deterministic diversity helper.

This script does NOT design the interface.
It only generates a stable combination of design-axis suggestions from a
non-sensitive project identity so separate projects are less likely to converge
on the same default aesthetic.

Usage:
    python design_seed.py "project-name|category|platform"

Do not pass secrets, customer data, source code, or private content.
"""

from __future__ import annotations

import hashlib
import json
import sys

STYLES = [
    "refined-minimal", "luxury-minimal", "swiss", "editorial",
    "monochrome-precision", "industrial", "glass", "tactile-hybrid",
    "neobrutalism", "bauhaus", "organic", "dark-cinematic",
    "retro-futurist", "heritage", "layered-spatial", "fashion-editorial",
]

COMPOSITIONS = [
    "asymmetric-columns", "editorial-grid", "split-stage", "edge-to-edge-media",
    "layered-canvas", "cardless-flow", "modular-grid", "sticky-story",
    "top-nav-workspace", "sidebar-workspace",
]

TYPE = [
    "rational-grotesk", "humanist", "geometric", "editorial-serif",
    "high-contrast-serif", "condensed-display", "wide-display",
    "rounded-friendly", "mono-technical",
]

PALETTES = [
    "warm-refined", "cool-refined", "monochrome-accent", "earth-material",
    "jewel-luxury", "muted-editorial", "saturated-graphic", "pastel-friendly",
    "dark-cinematic", "technical-high-vis",
]

MATERIALS = [
    "flat-ink", "hairline-surface", "soft-elevation", "glass",
    "tactile", "hard-shadow", "paper", "chrome", "spatial",
]

MOTION = [
    "near-static", "precise-functional", "soft-spring", "editorial-mask",
    "kinetic-type", "tactile-physical", "cinematic-depth", "scroll-story",
]

SIGNATURES = [
    "reflection-sweep", "image-mask", "custom-rule-system", "topology-trace",
    "art-directed-crop", "tactile-press", "focus-spotlight", "object-morph",
    "page-transition", "editorial-numbering", "dynamic-artwork-color",
]


def pick(values: list[str], digest: bytes, offset: int) -> str:
    return values[digest[offset % len(digest)] % len(values)]


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: design_seed.py 'project-name|category|platform'", file=sys.stderr)
        raise SystemExit(2)

    identity = sys.argv[1].strip()
    digest = hashlib.sha256(identity.encode("utf-8")).digest()

    result = {
        "note": "Diversity suggestion only; Millie must reject choices that do not fit the product.",
        "style": pick(STYLES, digest, 0),
        "composition": pick(COMPOSITIONS, digest, 3),
        "type_character": pick(TYPE, digest, 7),
        "palette_family": pick(PALETTES, digest, 11),
        "material": pick(MATERIALS, digest, 17),
        "motion": pick(MOTION, digest, 23),
        "signature_detail": pick(SIGNATURES, digest, 29),
    }

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
