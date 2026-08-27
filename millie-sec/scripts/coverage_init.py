#!/usr/bin/env python3
"""Create an initial Millie Security coverage ledger from an inventory."""
from __future__ import annotations
import argparse,json
from pathlib import Path

BASE=[
 ("authn","Authentication"),("authz","Authorization / tenancy"),
 ("input","Injection / parsing"),("secrets","Secrets / cryptography"),
 ("supply-chain","Dependencies / supply chain"),("privacy","Privacy / logging / errors"),
 ("ci","CI/CD / release")
]
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("inventory")
    args=ap.parse_args()
    inv=json.loads(Path(args.inventory).read_text(encoding="utf-8"))
    domains=list(BASE)
    if inv.get("package_signals") or any("javascript"==x for x in inv.get("languages",[])):
        domains += [("web","Web / browser")]
    if any(x in str(inv.get("package_signals",{})).lower() for x in ("express","fastify","graphql","nestjs")):
        domains += [("api","API"),("logic","Business logic"),("network","SSRF / egress")]
    if inv.get("iac_container_files"): domains += [("cloud","Cloud / IaC / containers")]
    if inv.get("mobile_signals"): domains += [("mobile","Mobile")]
    if inv.get("ai_agent_signals"): domains += [("ai","AI / agentic")]
    out={"schema_version":1,"domains":[]}
    seen=set()
    for did,name in domains:
        if did in seen: continue
        seen.add(did)
        out["domains"].append({"domain":did,"name":name,"applicable":True,
                               "method":[],"status":"planned","limitations":[]})
    print(json.dumps(out,indent=2))

if __name__=="__main__":
    main()
