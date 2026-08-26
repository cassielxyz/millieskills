#!/usr/bin/env python3
import argparse,json
RULES={
 'hover':['css'], 'press':['css','motion','reanimated'], 'gesture':['motion','reanimated','gsap-observer'],
 'shared-layout':['motion','gsap-flip','reanimated-layout'], 'scroll-simple':['css-scroll-timeline'],
 'scroll-complex':['gsap-scrolltrigger'], 'cinematic':['theatre','gsap'], '3d-scroll':['gsap-scrolltrigger','theatre','three'],
 'react-native':['reanimated'], 'svelte-3d':['threlte'], '3d-authoring':['spline'], 'shader':['three','r3f','threlte']}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('need',choices=RULES); ap.add_argument('--stack',default='web')
    a=ap.parse_args(); choices=RULES[a.need]
    if a.stack=='react-native': choices=['reanimated']
    elif a.stack=='svelte' and any(x in a.need for x in ['3d','shader']): choices=['threlte','theatre']
    print(json.dumps({'need':a.need,'stack':a.stack,'recommended_order':choices},indent=2))
if __name__=='__main__': main()
