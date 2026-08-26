#!/usr/bin/env python3
"""
Millie UI OKLCH palette helper.

Outputs a small CSS-variable palette and approximate WCAG contrast checks after
converting OKLCH to sRGB. Values are starting points; final UI contrast must be
checked against actual rendered foreground/background pairs.
"""

from __future__ import annotations
import argparse, math

def oklch_to_srgb(L, C, h_deg):
    h = math.radians(h_deg)
    a = C * math.cos(h)
    b = C * math.sin(h)

    l_ = L + 0.3963377774*a + 0.2158037573*b
    m_ = L - 0.1055613458*a - 0.0638541728*b
    s_ = L - 0.0894841775*a - 1.2914855480*b

    l, m, s = l_**3, m_**3, s_**3

    r_lin = +4.0767416621*l - 3.3077115913*m + 0.2309699292*s
    g_lin = -1.2684380046*l + 2.6097574011*m - 0.3413193965*s
    b_lin = -0.0041960863*l - 0.7034186147*m + 1.7076147010*s

    def gamma(x):
        x = max(0.0, min(1.0, x))
        return 12.92*x if x <= 0.0031308 else 1.055*(x**(1/2.4)) - 0.055

    return tuple(gamma(x) for x in (r_lin,g_lin,b_lin))

def hexrgb(rgb):
    vals = [round(max(0,min(1,x))*255) for x in rgb]
    return "#" + "".join(f"{v:02X}" for v in vals)

def rel_lum(rgb):
    def lin(c):
        return c/12.92 if c <= 0.04045 else ((c+0.055)/1.055)**2.4
    r,g,b = (lin(x) for x in rgb)
    return 0.2126*r + 0.7152*g + 0.0722*b

def contrast(a,b):
    l1,l2 = sorted([rel_lum(a), rel_lum(b)], reverse=True)
    return (l1+0.05)/(l2+0.05)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hue", type=float, default=28.0)
    ap.add_argument("--mode", choices=["light","dark"], default="light")
    ap.add_argument("--chroma", type=float, default=0.16)
    args = ap.parse_args()

    h=args.hue%360
    c=max(0,min(.35,args.chroma))

    if args.mode=="light":
        stops = {
            "canvas": (.985,.008,h),
            "surface": (.965,.010,h),
            "text-primary": (.22,.025,h),
            "text-secondary": (.42,.025,h),
            "primary": (.58,c,h),
            "primary-hover": (.52,min(.35,c+.01),h),
            "primary-soft": (.92,min(.08,c*.45),h),
            "border": (.86,.018,h),
        }
    else:
        stops = {
            "canvas": (.15,.015,h),
            "surface": (.20,.018,h),
            "text-primary": (.94,.012,h),
            "text-secondary": (.76,.018,h),
            "primary": (.72,min(.24,c),h),
            "primary-hover": (.78,min(.24,c+.01),h),
            "primary-soft": (.28,min(.08,c*.40),h),
            "border": (.34,.025,h),
        }

    rgb={}
    print(":root {")
    for name,(L,C,H) in stops.items():
        rgb[name]=oklch_to_srgb(L,C,H)
        print(f"  --color-{name}: oklch({L:.3f} {C:.3f} {H:.1f}); /* {hexrgb(rgb[name])} */")
    print("}")

    print("\nContrast checks (approx sRGB):")
    for fg,bg in [("text-primary","canvas"),("text-secondary","canvas"),("primary","canvas")]:
        print(f"  {fg} on {bg}: {contrast(rgb[fg],rgb[bg]):.2f}:1")

if __name__ == "__main__":
    main()
