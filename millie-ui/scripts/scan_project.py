#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,os
from pathlib import Path

SKIP={'.git','node_modules','.next','dist','build','out','.cache','.turbo','.venv','venv','__pycache__','Pods','DerivedData'}
SECRET={'.env','.env.local','.env.production','.env.development','credentials.json','secrets.json'}

def walk(root):
    for base,dirs,files in os.walk(root):
        dirs[:]=[d for d in dirs if d not in SKIP]
        for f in files:
            if f in SECRET or f.startswith('.env'): continue
            yield Path(base)/f

def read_json(p):
    try:return json.loads(p.read_text(encoding='utf-8'))
    except:return None

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('root',nargs='?',default='.')
    root=Path(ap.parse_args().root).expanduser().resolve()
    result={'root':str(root),'signals':{},'important_files':[],'ui_dirs':[],'assets':[]}
    important={'package.json','components.json','DESIGN.md','BRAIN.md','AGENTS.md','CLAUDE.md','pubspec.yaml','app.json','app.config.js','app.config.ts','Podfile','build.gradle','build.gradle.kts'}
    for p in walk(root):
        rel=p.relative_to(root).as_posix()
        if p.name in important or rel.startswith('.stitch/'):
            result['important_files'].append(rel)
    pkg=read_json(root/'package.json') if (root/'package.json').exists() else None
    if pkg:
        deps={}; deps.update(pkg.get('dependencies') or {}); deps.update(pkg.get('devDependencies') or {})
        probes={
          'react':['react'],'next':['next'],'vue':['vue'],'nuxt':['nuxt'],'svelte':['svelte'],'astro':['astro'],
          'tailwind':['tailwindcss'],'shadcn':['shadcn'],'motion':['motion','framer-motion'],'gsap':['gsap'],
          'three':['three'],'r3f':['@react-three/fiber'],'drei':['@react-three/drei'],'theatre':['@theatre/core','@theatre/studio'],
          'spline':['@splinetool/react-spline','@splinetool/runtime'],'agentation':['agentation'],
          'react-native':['react-native'],'reanimated':['react-native-reanimated'],'gesture-handler':['react-native-gesture-handler'],
          'expo':['expo'],'threlte':['@threlte/core']}
        result['signals']['packages']={k:{n:deps[n] for n in names if n in deps} for k,names in probes.items() if any(n in deps for n in names)}
    comp=root/'components.json'
    if comp.exists(): result['signals']['components_json']=read_json(comp)
    result['signals']['has_design_md']=(root/'DESIGN.md').exists()
    result['signals']['has_brain_md']=(root/'BRAIN.md').exists()
    result['signals']['has_stitch']=(root/'.stitch').exists()
    for cand in ['components','src/components','app','src/app','pages','src/pages','routes','src/routes','ui','src/ui']:
        if (root/cand).is_dir(): result['ui_dirs'].append(cand)
    for cand in ['public','assets','src/assets','static']:
        if (root/cand).is_dir(): result['assets'].append(cand)
    print(json.dumps(result,indent=2))
if __name__=='__main__': main()
