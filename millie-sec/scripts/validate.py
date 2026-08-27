#!/usr/bin/env python3
"""Validate the Millie Security skill package."""
from __future__ import annotations
import json,re,sys
from pathlib import Path

root=Path(sys.argv[1] if len(sys.argv)>1 else Path(__file__).resolve().parents[1])
errors=[]
required=["SKILL.md","README.md","VERSION","RESEARCH_REPORT.md","references/pipeline.md",
          "data/tool-registry.json","schemas/finding.schema.json","evaluations/cases.json"]
for rel in required:
    if not (root/rel).exists(): errors.append(f"missing: {rel}")

skill=root/"SKILL.md"
if skill.exists():
    text=skill.read_text(encoding="utf-8")
    if not text.startswith("---\nname: millie-sec\n"): errors.append("invalid SKILL.md frontmatter/name")
    links=re.findall(r'\]\(\./([^)#]+)',text)
    for link in links:
        if not (root/link).exists(): errors.append(f"broken SKILL link: {link}")
    lines=len(text.splitlines())
    if lines>500: errors.append(f"SKILL.md should remain <=500 lines for progressive disclosure; got {lines}")

for p in root.rglob("*.json"):
    try: json.loads(p.read_text(encoding="utf-8"))
    except Exception as exc: errors.append(f"invalid JSON {p.relative_to(root)}: {exc}")

for p in root.rglob("*.md"):
    if p.stat().st_size==0: errors.append(f"empty markdown: {p.relative_to(root)}")

if errors:
    print("\n".join(errors),file=sys.stderr)
    raise SystemExit(1)
print(f"Millie Security valid. SKILL lines={len(skill.read_text(encoding='utf-8').splitlines())}; "
      f"references={len(list((root/'references').glob('*.md')))}; "
      f"JSON files={len(list(root.rglob('*.json')))}")
