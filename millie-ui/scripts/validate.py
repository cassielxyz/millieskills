#!/usr/bin/env python3
from pathlib import Path
import json,re,sys,py_compile
root=Path(sys.argv[1] if len(sys.argv)>1 else Path(__file__).resolve().parents[1]).resolve()
errors=[]
required=['SKILL.md','README.md','VERSION','RESEARCH_REPORT.md','data/catalog.json','evaluations/cases.json']
for rel in required:
    if not (root/rel).exists(): errors.append(f'missing {rel}')
skill=(root/'SKILL.md').read_text(encoding='utf-8') if (root/'SKILL.md').exists() else ''
if not skill.startswith('---\nname: millie-ui\n'): errors.append('invalid SKILL frontmatter/name')
# Keep the router compact enough for progressive disclosure.
if len(skill.splitlines())>500: errors.append(f'SKILL.md too long: {len(skill.splitlines())} lines (>500)')
for md in root.rglob('*.md'):
    text=md.read_text(encoding='utf-8')
    for target in re.findall(r'\]\((\.?\.?/[^)#]+)', text):
        p=(md.parent/target).resolve()
        if not p.exists(): errors.append(f'broken link {md.relative_to(root)} -> {target}')
for rel in ['data/catalog.json','evaluations/cases.json','schemas/design-fingerprint.schema.json','schemas/research-lock.schema.json']:
    p=root/rel
    if p.exists():
        try: json.loads(p.read_text(encoding='utf-8'))
        except Exception as e: errors.append(f'invalid json {rel}: {e}')
for py in (root/'scripts').glob('*.py'):
    try: py_compile.compile(str(py),doraise=True)
    except Exception as e: errors.append(f'python compile {py.name}: {e}')
assets=list((root/'assets').rglob('*.svg')) if (root/'assets').exists() else []
if len(assets)<50: errors.append(f'expected full vector assets pack, found {len(assets)} SVGs')
if errors:
    print('\n'.join('ERROR: '+e for e in errors)); raise SystemExit(1)
print(f'OK Millie UI { (root/"VERSION").read_text().strip() }: {len(skill.splitlines())} SKILL lines, {len(list((root/"references").glob("*.md")))} refs, {len(assets)} SVG assets')
print('Structural validation only; behavioral cases require an agent runtime.')
