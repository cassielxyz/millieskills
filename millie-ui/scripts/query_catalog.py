#!/usr/bin/env python3
import argparse,json,re
from pathlib import Path

def tokens(s): return set(re.findall(r"[a-z0-9]+", s.lower()))
def flatten(x):
    if isinstance(x,dict): return ' '.join(flatten(v) for v in x.values())
    if isinstance(x,list): return ' '.join(flatten(v) for v in x)
    return str(x)

def main():
    ap=argparse.ArgumentParser(description='Search Millie UI compact design catalog')
    ap.add_argument('query')
    ap.add_argument('--domain', choices=['styles','motion_patterns','sources','product_archetypes'])
    ap.add_argument('--limit',type=int,default=8)
    args=ap.parse_args()
    data=json.loads((Path(__file__).resolve().parents[1]/'data/catalog.json').read_text())
    q=tokens(args.query)
    domains=[args.domain] if args.domain else ['styles','motion_patterns','sources','product_archetypes']
    hits=[]
    for d in domains:
        for item in data.get(d,[]):
            t=tokens(flatten(item)); score=len(q&t)*3 + sum(1 for x in q if any(y.startswith(x) for y in t))
            if score: hits.append((score,d,item))
    hits.sort(key=lambda x:(-x[0],x[1],str(x[2].get('id',''))))
    print(json.dumps([{'score':s,'domain':d,**i} for s,d,i in hits[:args.limit]],indent=2))
if __name__=='__main__': main()
