<div align="center">

<img src="./assets/brand/millie-logo.svg" width="520" alt="Millie UI/UX" />

# Millie UI/UX v2

**Research-first product UX + creative frontend + motion direction + adaptive UI + 3D/WebGL.**

</div>

Millie UI is a portable Agent Skill for designing and implementing product interfaces without falling
back to one AI-generated aesthetic. It routes each task to only the design knowledge it needs.

## v2 highlights

- automatic product-specific art direction when no design is supplied;
- UX/task-flow reasoning before decoration;
- shadcn project detection and registry-safe component composition;
- SmoothUI / Unlumen / Animata / ThreeUI-aware source selection;
- CSS -> Motion -> GSAP -> Theatre -> WebGL motion routing;
- deep ScrollTrigger/Flip/Observer/ScrollSmoother guidance;
- React Native Reanimated 4 motion guidance;
- image -> img2threejs-style reconstruction -> 3D website integration;
- Three.js / R3F / Threlte / Theatre.js / Spline routing;
- optional Stitch, Agentation, brain.md, Ruflo and Superpowers interoperability;
- security/backend-state-aware UI design;
- persistent non-sensitive design fingerprints;
- research locks, living DESIGN.md and bounded visual verification.
- searchable catalog with 40 style families, 43 motion patterns, 33 source/tool routes, and 33 product archetypes;

## Package

```text
millie-ui/
├── SKILL.md
├── README.md
├── VERSION
├── RESEARCH_REPORT.md
├── assets/
├── data/
│   └── catalog.json
├── references/
├── scripts/
├── schemas/
├── templates/
└── evaluations/
```

## Useful helpers

```bash
python scripts/scan_project.py /path/to/project
python scripts/query_catalog.py "cybersecurity dashboard motion"
python scripts/query_catalog.py "scroll product launch" --domain motion_patterns
python scripts/motion_router.py scroll-complex --stack react
python scripts/palette.py --hue 28 --mode light
python scripts/fingerprint.py suggest "project|category|platform"
python scripts/validate.py .
```

Helpers provide evidence and deterministic lookups; they do not replace design judgement.

## Example prompts

```text
Use Millie UI to design this product. I have no visual direction; choose a distinctive premium
art direction automatically and avoid repeating designs from unrelated projects.
```

```text
Use Millie UI. This is an existing shadcn project: preserve the current design system, add a polished
settings workflow, and use Motion only where it improves state continuity.
```

```text
Use Millie UI to build a creative product story with GSAP scroll choreography and a Three.js object.
Keep normal document scrolling, provide reduced-motion/static fallback, and verify mobile performance.
```

```text
Use Millie UI with the supplied object image. If img2threejs is available, reconstruct an animation-
ready Three.js object and integrate it into a responsive product page with accessible DOM content.
```

## Research

See [`RESEARCH_REPORT.md`](./RESEARCH_REPORT.md) for the source-by-source comparison used in v2.
