#!/usr/bin/env python3
"""Route a repository inventory to a minimal high-value security tool plan."""
from __future__ import annotations
import argparse,json
from pathlib import Path

def add(plan, tool, reason, priority):
    if not any(x["tool"]==tool for x in plan):
        plan.append({"tool":tool,"priority":priority,"reason":reason})

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("inventory")
    ap.add_argument("--registry", default=str(Path(__file__).resolve().parents[1]/"data/tool-registry.json"))
    args=ap.parse_args()
    inv=json.loads(Path(args.inventory).read_text(encoding="utf-8"))
    registry=json.loads(Path(args.registry).read_text(encoding="utf-8"))
    known={x["id"] for x in registry["tools"]}
    plan=[]

    add(plan,"semgrep","Cross-language SAST/taint baseline",10)
    if inv.get("manifests"):
        add(plan,"osv-scanner","Dependency vulnerability coverage",9)
    if inv.get("has_git"):
        add(plan,"gitleaks","Repository/history secret coverage",9)
    if inv.get("iac_container_files"):
        add(plan,"trivy","IaC/container/dependency/secret cross-check",9)

    langs=set(inv.get("languages",[]))
    if "javascript" in langs:
        add(plan,"dependency-native","Use the detected JS package manager audit in addition to OSV",7)
    if "python" in langs:
        add(plan,"bandit","Python-specific security pattern pass",6)
    if "go" in langs:
        add(plan,"govulncheck","Go vulnerability/reachability analysis",9)
    if "rust" in langs:
        add(plan,"cargo-audit","Rust dependency advisories",8)
        add(plan,"cargo-clippy","Rust static diagnostics",6)
    if "ruby" in langs:
        add(plan,"brakeman","Rails/Ruby web security if Rails is detected",8)
        add(plan,"bundler-audit","Ruby dependency advisories",7)
    if "php" in langs:
        add(plan,"composer-audit","PHP dependency advisories",7)
    if "dotnet" in langs:
        add(plan,"dotnet-audit",".NET dependency vulnerability coverage",7)

    if inv.get("mobile_signals"):
        add(plan,"mobSF","Mobile-specific static/dynamic review if a build is available",8)
    if inv.get("iac_container_files"):
        add(plan,"syft","Generate SBOM for release/container surface when useful",8)
    if inv.get("auth_access_signals") or inv.get("ai_agent_signals"):
        add(plan,"codeql","Semantic/data-flow second lens when language/database support exists",9)

    plan.sort(key=lambda x:(-x["priority"],x["tool"]))
    result={
        "schema_version":1,
        "policy":"Plan only. The agent verifies availability/applicability and does not mass-install.",
        "selected":[x for x in plan if x["tool"] in known],
        "dynamic_phase":[
            {"tool":"strix","condition":"Local/owned/explicitly authorized target and useful runtime/source scope"},
            {"tool":"zap","condition":"Authorized web runtime when an independent DAST lens adds value"}
        ]
    }
    print(json.dumps(result,indent=2))

if __name__=="__main__":
    main()
