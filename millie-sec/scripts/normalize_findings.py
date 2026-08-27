#!/usr/bin/env python3
"""
Normalize selected security scanner output formats into a simple Millie finding list.

Supported:
- SARIF 2.x
- Semgrep JSON (`results`)
- Trivy JSON (`Results`)
- Gitleaks JSON list

No secret values are intentionally copied; common secret fields are redacted.
"""
from __future__ import annotations
import argparse,json,re
from pathlib import Path

SECRET_KEYS={"secret","match","token","password","private_key","apikey","api_key"}

def redact_obj(x):
    if isinstance(x,dict):
        return {k:("[REDACTED]" if k.lower() in SECRET_KEYS else redact_obj(v)) for k,v in x.items()}
    if isinstance(x,list): return [redact_obj(v) for v in x]
    return x

def sev(s):
    s=(s or "unknown").lower()
    m={"error":"high","warning":"medium","note":"low","critical":"critical",
       "high":"high","medium":"medium","low":"low","info":"info","unknown":"unknown"}
    return m.get(s,s)

def sarif(d):
    out=[]
    for run in d.get("runs",[]):
        rules={r.get("id"):r for r in run.get("tool",{}).get("driver",{}).get("rules",[])}
        for r in run.get("results",[]):
            loc=(r.get("locations") or [{}])[0].get("physicalLocation",{})
            art=loc.get("artifactLocation",{}).get("uri")
            line=loc.get("region",{}).get("startLine")
            rid=r.get("ruleId")
            rule=rules.get(rid,{})
            out.append({"source":"sarif","rule_id":rid,"title":rule.get("shortDescription",{}).get("text") or rid,
                        "severity":sev(r.get("level")),"path":art,"line":line,
                        "message":r.get("message",{}).get("text"),"status":"UNVERIFIED"})
    return out

def semgrep(d):
    out=[]
    for r in d.get("results",[]):
        extra=r.get("extra",{})
        out.append({"source":"semgrep","rule_id":r.get("check_id"),"title":r.get("check_id"),
                    "severity":sev(extra.get("severity")),"path":r.get("path"),
                    "line":r.get("start",{}).get("line"),"message":extra.get("message"),
                    "status":"UNVERIFIED"})
    return out

def trivy(d):
    out=[]
    for result in d.get("Results",[]):
        target=result.get("Target")
        for v in result.get("Vulnerabilities") or []:
            out.append({"source":"trivy","rule_id":v.get("VulnerabilityID"),"title":v.get("Title") or v.get("VulnerabilityID"),
                        "severity":sev(v.get("Severity")),"path":target,
                        "component":v.get("PkgName"),"installed_version":v.get("InstalledVersion"),
                        "fixed_version":v.get("FixedVersion"),"status":"UNVERIFIED"})
        for m in result.get("Misconfigurations") or []:
            out.append({"source":"trivy","rule_id":m.get("ID"),"title":m.get("Title") or m.get("ID"),
                        "severity":sev(m.get("Severity")),"path":target,
                        "message":m.get("Message"),"status":"UNVERIFIED"})
    return out

def gitleaks(d):
    out=[]
    if not isinstance(d,list): return out
    for r in d:
        out.append({"source":"gitleaks","rule_id":r.get("RuleID"),"title":r.get("Description") or r.get("RuleID"),
                    "severity":"high","path":r.get("File"),"line":r.get("StartLine"),
                    "message":"Potential secret detected; value redacted. Verify and rotate if live.",
                    "status":"UNVERIFIED"})
    return out

def detect(d):
    if isinstance(d,dict) and "runs" in d: return sarif(d)
    if isinstance(d,dict) and "results" in d: return semgrep(d)
    if isinstance(d,dict) and "Results" in d: return trivy(d)
    if isinstance(d,list): return gitleaks(d)
    raise ValueError("Unrecognized supported finding format")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("-o","--output")
    args=ap.parse_args()
    d=redact_obj(json.loads(Path(args.input).read_text(encoding="utf-8")))
    findings=detect(d)
    payload={"schema_version":1,"findings":findings}
    text=json.dumps(payload,indent=2)+"\n"
    if args.output: Path(args.output).write_text(text,encoding="utf-8")
    else: print(text,end="")

if __name__=="__main__":
    main()
