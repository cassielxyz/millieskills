#!/usr/bin/env python3
"""Lightweight structural validation for Millie Fix project/function graph JSON."""

from __future__ import annotations
import argparse, json
from pathlib import Path

def load(p):
    try: return json.loads(p.read_text(encoding="utf-8"))
    except Exception as e: raise SystemExit(f"{p}: invalid JSON: {e}")

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("graph_dir"); a=ap.parse_args()
    g=Path(a.graph_dir); errors=[]
    pg=g/"project-graph.json"; fg=g/"function-graph.json"

    if not pg.exists(): errors.append(f"missing {pg}")
    else:
        d=load(pg)
        for k in ("schema_version","generated_at","files","edges","entry_points"):
            if k not in d: errors.append(f"project-graph missing {k}")

    if not fg.exists(): errors.append(f"missing {fg}")
    else:
        d=load(fg)
        for k in ("schema_version","generated_at","functions","edges"):
            if k not in d: errors.append(f"function-graph missing {k}")
        ids=set()
        for i,f in enumerate(d.get("functions",[])):
            for k in ("id","name","kind","file","language","calls","called_by","tests","side_effects",
                      "dynamic_reference_risk","confidence","status"):
                if k not in f: errors.append(f"function[{i}] missing {k}")
            fid=f.get("id")
            if fid in ids: errors.append(f"duplicate function id: {fid}")
            ids.add(fid)
            c=f.get("confidence")
            if isinstance(c,(int,float)) and not 0 <= c <= 1:
                errors.append(f"{fid}: confidence out of range")

    if errors:
        print("Millie graph validation failed:")
        for e in errors: print(" -",e)
        raise SystemExit(1)
    print("Millie graph validation passed.")

if __name__=="__main__":
    main()
