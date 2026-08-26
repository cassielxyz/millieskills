#!/usr/bin/env python3
"""
Millie UI repository context scanner.

Produces a compact JSON evidence index for frontend/UI design work.
It does NOT read .env files or secret-like files and is not a substitute for
semantic inspection by the agent.
"""

from __future__ import annotations
import argparse, json, os, re
from pathlib import Path

SKIP_DIRS = {
    ".git", "node_modules", ".next", "dist", "build", "out", ".cache",
    ".turbo", ".venv", "venv", "__pycache__", "Pods", "DerivedData",
}
SECRET_NAMES = {
    ".env", ".env.local", ".env.production", ".env.development",
    "credentials.json", "secrets.json",
}
IMPORTANT_NAMES = {
    "package.json", "pnpm-workspace.yaml", "yarn.lock", "package-lock.json",
    "pnpm-lock.yaml", "vite.config.ts", "vite.config.js", "next.config.js",
    "next.config.mjs", "next.config.ts", "tailwind.config.js", "tailwind.config.ts",
    "DESIGN.md", "AGENTS.md", "CLAUDE.md", "README.md", "pubspec.yaml",
    "build.gradle", "build.gradle.kts", "settings.gradle", "settings.gradle.kts",
    "Package.swift", "project.pbxproj",
}
STYLE_SUFFIXES = {".css", ".scss", ".sass", ".less"}
CODE_SUFFIXES = {".tsx", ".jsx", ".vue", ".svelte", ".swift", ".kt", ".kts", ".dart"}

def safe_walk(root: Path):
    for base, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".millie")]
        b = Path(base)
        for f in files:
            p = b / f
            if f in SECRET_NAMES or f.startswith(".env"):
                continue
            yield p

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root", nargs="?", default=".")
    args = ap.parse_args()
    root = Path(args.root).expanduser().resolve()

    result = {
        "root": str(root),
        "important_files": [],
        "style_files": [],
        "ui_code_files": [],
        "asset_dirs": [],
        "candidate_component_dirs": [],
        "candidate_route_dirs": [],
        "design_docs": [],
        "package_signals": {},
    }

    for p in safe_walk(root):
        rel = p.relative_to(root).as_posix()
        if p.name in IMPORTANT_NAMES:
            result["important_files"].append(rel)
        if p.suffix.lower() in STYLE_SUFFIXES:
            result["style_files"].append(rel)
        if p.suffix.lower() in CODE_SUFFIXES:
            result["ui_code_files"].append(rel)
        if p.name.lower() in {"design.md", "brand.md", "styleguide.md"}:
            result["design_docs"].append(rel)

    for candidate in [
        "src/components", "components", "app/components", "src/ui", "ui",
        "src/pages", "pages", "app", "src/routes", "routes",
        "public", "assets", "src/assets",
    ]:
        p = root / candidate
        if p.is_dir():
            key = "asset_dirs" if "asset" in candidate or candidate == "public" else (
                "candidate_route_dirs" if candidate in {"src/pages","pages","app","src/routes","routes"} else
                "candidate_component_dirs"
            )
            result[key].append(candidate)

    pkg = root / "package.json"
    if pkg.exists():
        try:
            data = json.loads(pkg.read_text(encoding="utf-8"))
            deps = {}
            for section in ("dependencies", "devDependencies"):
                deps.update(data.get(section, {}) or {})
            signals = [
                "react", "next", "vue", "nuxt", "svelte", "@sveltejs/kit",
                "tailwindcss", "@mui/material", "@chakra-ui/react",
                "@radix-ui/react-dialog", "lucide-react", "framer-motion",
                "motion", "gsap", "three", "@react-three/fiber", "@react-three/drei",
                "styled-components", "@emotion/react",
            ]
            result["package_signals"] = {s: deps[s] for s in signals if s in deps}
        except Exception as exc:
            result["package_signals_error"] = str(exc)

    # Keep output compact.
    for key in ("style_files", "ui_code_files"):
        result[key] = result[key][:200]

    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
