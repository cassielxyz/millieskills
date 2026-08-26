#!/usr/bin/env python3
"""
Millie UI design fingerprint helper.

Commands:
  suggest "project|category|platform"
  record path/to/fingerprint.json
  list

History contains non-sensitive design metadata only.
"""

from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

HISTORY = Path.home() / ".millie-ui" / "history.json"

AXES = {
    "style": [
        "refined-minimal","luxury-minimal","swiss","editorial","industrial",
        "data-precision","glass","tactile","neobrutalism","bauhaus","organic",
        "dark-cinematic","retro-futurist","heritage","layered-spatial","fashion-editorial"
    ],
    "composition": [
        "asymmetric-columns","editorial-grid","split-stage","edge-media","layered-canvas",
        "cardless-flow","modular-grid","sticky-story","top-nav-workspace","sidebar-workspace"
    ],
    "type_character": [
        "rational-grotesk","humanist","geometric","editorial-serif",
        "high-contrast-serif","condensed-display","wide-display","rounded-friendly","mono-technical"
    ],
    "palette": [
        "warm-refined","cool-refined","monochrome-accent","earth-material","jewel-luxury",
        "muted-editorial","saturated-graphic","pastel-friendly","dark-cinematic","technical-high-vis"
    ],
    "material": [
        "flat-ink","hairline","soft-elevation","glass","tactile","hard-shadow","paper","chrome","spatial"
    ],
    "motion": [
        "near-static","precise-functional","soft-spring","editorial-mask",
        "kinetic-type","tactile-physical","cinematic-depth","scroll-story"
    ],
    "signature": [
        "reflection-sweep","image-mask","custom-rule-system","topology-trace","art-directed-crop",
        "tactile-press","focus-spotlight","object-morph","page-transition","editorial-numbering",
        "dynamic-artwork-color"
    ],
}

def load_history():
    if not HISTORY.exists():
        return {"schema_version": 1, "recent": []}
    try:
        return json.loads(HISTORY.read_text(encoding="utf-8"))
    except Exception:
        return {"schema_version": 1, "recent": []}

def pick(values, digest, offset):
    return values[digest[offset % len(digest)] % len(values)]

def suggest(identity: str):
    d = hashlib.sha256(identity.encode("utf-8")).digest()
    out = {"identity_hash": hashlib.sha256(identity.encode()).hexdigest()[:12]}
    offsets = [0,3,7,11,17,23,29]
    for (key, values), off in zip(AXES.items(), offsets):
        out[key] = pick(values, d, off)
    return out

def record(path: Path):
    data = json.loads(path.read_text(encoding="utf-8"))
    allowed = {"style","composition","type_character","palette","material","motion","signature",
               "theme","density","immersion","identity_hash"}
    clean = {k: data[k] for k in allowed if k in data}
    hist = load_history()
    hist["recent"] = ([clean] + hist.get("recent", []))[:30]
    HISTORY.parent.mkdir(parents=True, exist_ok=True)
    HISTORY.write_text(json.dumps(hist, indent=2)+"\n", encoding="utf-8")
    print(HISTORY)

def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("suggest"); s.add_argument("identity")
    r = sub.add_parser("record"); r.add_argument("file")
    sub.add_parser("list")
    args = ap.parse_args()

    if args.cmd == "suggest":
        print(json.dumps(suggest(args.identity), indent=2))
    elif args.cmd == "record":
        record(Path(args.file))
    else:
        print(json.dumps(load_history(), indent=2))

if __name__ == "__main__":
    main()
