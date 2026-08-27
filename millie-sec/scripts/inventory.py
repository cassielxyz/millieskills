#!/usr/bin/env python3
"""
Read-only repository security inventory.

Does not execute project code, install packages, or read secret-like files.
"""
from __future__ import annotations
import argparse, json, os
from pathlib import Path

SKIP = {".git","node_modules",".next",".nuxt","dist","build","out","target",".cache",
        ".turbo",".venv","venv","__pycache__","Pods","DerivedData","vendor"}
SECRET = {".env",".env.local",".env.production","credentials.json","secrets.json"}
MANIFESTS = {
    "package.json":"javascript","pnpm-lock.yaml":"javascript","yarn.lock":"javascript",
    "package-lock.json":"javascript","pyproject.toml":"python","requirements.txt":"python",
    "Pipfile":"python","poetry.lock":"python","go.mod":"go","go.sum":"go",
    "Cargo.toml":"rust","Cargo.lock":"rust","pom.xml":"java","build.gradle":"java",
    "build.gradle.kts":"kotlin","composer.json":"php","Gemfile":"ruby",
    "*.csproj":"dotnet","Package.swift":"swift","pubspec.yaml":"dart-flutter"
}
IAC_NAMES = {"main.tf","terraform.tfvars.example","template.yaml","serverless.yml",
             "docker-compose.yml","docker-compose.yaml","Dockerfile","Chart.yaml"}
CI_PARTS = {".github/workflows",".gitlab-ci.yml","azure-pipelines.yml","Jenkinsfile"}

def walk(root):
    for base, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP]
        b=Path(base)
        for f in files:
            p=b/f
            if f in SECRET or f.startswith(".env."):
                continue
            yield p

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("root", nargs="?", default=".")
    ap.add_argument("-o","--output")
    args=ap.parse_args()
    root=Path(args.root).expanduser().resolve()

    files=list(walk(root))
    rel=[p.relative_to(root).as_posix() for p in files]
    names={p.name for p in files}
    langs=set()
    manifests=[]
    for p in files:
        n=p.name
        for pattern,lang in MANIFESTS.items():
            if (pattern.startswith("*.") and n.endswith(pattern[1:])) or n==pattern:
                langs.add(lang); manifests.append(p.relative_to(root).as_posix())

    package_signals={}
    pkg=root/"package.json"
    lifecycle={}
    if pkg.exists():
        try:
            d=json.loads(pkg.read_text(encoding="utf-8"))
            deps={}
            for section in ("dependencies","devDependencies"):
                deps.update(d.get(section,{}) or {})
            signals=["express","fastify","next","react","vue","nuxt","svelte","@sveltejs/kit",
                     "nestjs","passport","jsonwebtoken","next-auth","@auth/core","prisma",
                     "drizzle-orm","sequelize","typeorm","mongoose","graphql","apollo-server",
                     "openai","@anthropic-ai/sdk","langchain","@langchain/core"]
            package_signals={x:deps[x] for x in signals if x in deps}
            scripts=d.get("scripts",{}) or {}
            lifecycle={k:v for k,v in scripts.items()
                       if k in {"preinstall","install","postinstall","prepare","prepublish","postpublish"}}
        except Exception as exc:
            package_signals={"parse_error":str(exc)}

    ci=[x for x in rel if any(part in x for part in CI_PARTS)]
    iac=[x for x in rel if Path(x).name in IAC_NAMES or x.endswith(".tf")
         or "/k8s/" in f"/{x}" or "/kubernetes/" in f"/{x}"]
    mobile=[x for x in rel if x.endswith("AndroidManifest.xml") or x.endswith("Info.plist")
            or x.endswith("pubspec.yaml") or "/ios/" in f"/{x}" or "/android/" in f"/{x}"]
    auth_hint=[x for x in rel if any(t in x.lower() for t in
               ("auth","session","oauth","oidc","jwt","permission","rbac","policy"))][:80]
    ai_hint=[x for x in rel if any(t in x.lower() for t in
             ("prompt","rag","embedding","agent","llm","model","tool_call"))][:80]

    result={
        "schema_version":1,
        "root":str(root),
        "file_count_scanned":len(files),
        "languages":sorted(langs),
        "manifests":sorted(set(manifests)),
        "package_signals":package_signals,
        "lifecycle_hooks":lifecycle,
        "ci_files":ci[:100],
        "iac_container_files":iac[:150],
        "mobile_signals":mobile[:100],
        "auth_access_signals":auth_hint,
        "ai_agent_signals":ai_hint,
        "has_git":(root/".git").exists(),
        "notes":[
            "Read-only evidence index; not a vulnerability scan.",
            "Secret-like files and common dependency/build/cache directories are skipped."
        ]
    }
    text=json.dumps(result, indent=2)+"\n"
    if args.output:
        Path(args.output).write_text(text,encoding="utf-8")
    else:
        print(text,end="")

if __name__=="__main__":
    main()
