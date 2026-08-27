#!/usr/bin/env python3
"""
Evaluate normalized findings + coverage ledger into a Millie Security gate verdict.

This does not prove security. It enforces honest completion criteria.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path

OPEN_STATUSES={"CONFIRMED","HIGH-CONFIDENCE","PLAUSIBLE","UNVERIFIED"}
CLOSED_STATUSES={"FIXED","FALSE-POSITIVE","NOT-APPLICABLE","ACCEPTED"}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("findings")
    ap.add_argument("--coverage")
    args=ap.parse_args()
    d=json.loads(Path(args.findings).read_text(encoding="utf-8"))
    fs=d.get("findings",d if isinstance(d,list) else [])
    blockers=[]
    residual=[]
    for f in fs:
        status=str(f.get("status","UNVERIFIED")).upper()
        severity=str(f.get("severity","unknown")).lower()
        if status in CLOSED_STATUSES: continue
        if severity in {"critical","high"} and status in OPEN_STATUSES:
            blockers.append({"id":f.get("id") or f.get("rule_id"),"severity":severity,"status":status})
        else:
            residual.append({"id":f.get("id") or f.get("rule_id"),"severity":severity,"status":status})
    coverage_gaps=[]
    if args.coverage:
        c=json.loads(Path(args.coverage).read_text(encoding="utf-8"))
        for x in c.get("domains",[]):
            if x.get("applicable") and x.get("status") in {"blocked","partially-covered","not-tested","planned"}:
                coverage_gaps.append({"domain":x.get("domain"),"status":x.get("status"),
                                      "limitations":x.get("limitations",[])})
    if blockers:
        verdict="SECURITY GATE: FAIL"
    elif residual or coverage_gaps:
        verdict="SECURITY GATE: PASS WITH RESIDUAL RISK"
    else:
        verdict="SECURITY GATE: PASS"
    print(json.dumps({
        "verdict":verdict,
        "blocking_findings":blockers,
        "residual_findings":residual,
        "coverage_gaps":coverage_gaps,
        "assurance_note":"A PASS means no blocking finding remained within recorded coverage; it is not a claim of perfect security."
    },indent=2))

if __name__=="__main__":
    main()
