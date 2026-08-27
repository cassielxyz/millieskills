#!/usr/bin/env python3
"""Compute the transparent Millie Priority Score (project priority helper, not a standard)."""
from __future__ import annotations
import argparse,json
from pathlib import Path

MAX = {
 "technical_impact":25,
 "exploit_evidence":20,
 "exposure_reachability":15,
 "privilege_tenant_crossing":15,
 "sensitive_data_business":10,
 "known_exploitation_kev":8,
 "exploit_likelihood_epss":4,
 "confidence":3
}
def priority(score):
    if score>=80: return "P0"
    if score>=60: return "P1"
    if score>=40: return "P2"
    if score>=20: return "P3"
    return "P4"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("json_file", help="JSON object containing 0..max factor values")
    args=ap.parse_args()
    d=json.loads(Path(args.json_file).read_text(encoding="utf-8"))
    factors=d.get("factors",d)
    clean={}
    for k,m in MAX.items():
        v=float(factors.get(k,0))
        clean[k]=max(0,min(m,v))
    score=round(sum(clean.values()),2)
    print(json.dumps({"score":score,"priority":priority(score),"max":100,
      "factors":clean,"note":"Contextual project-priority helper; do not treat as CVSS/EPSS replacement."},indent=2))

if __name__=="__main__":
    main()
