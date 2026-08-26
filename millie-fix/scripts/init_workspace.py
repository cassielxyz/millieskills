#!/usr/bin/env python3
"""Create an isolated Millie Fix repair clone without writing to the source repository."""

from __future__ import annotations
import argparse, datetime as dt, json, shutil, subprocess
from pathlib import Path

def run(cmd, *, cwd=None, check=True, input_bytes=None):
    return subprocess.run(cmd, cwd=cwd, check=check, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, input=input_bytes)

def out(cmd, cwd=None, check=True):
    return run(cmd, cwd=cwd, check=check).stdout.decode("utf-8", "replace").strip()

def default_dest(source: str) -> Path:
    p = Path(source).expanduser()
    if p.exists():
        p = p.resolve()
        return p.parent / f"{p.name}__millie-fix"
    name = source.rstrip("/").split("/")[-1].removesuffix(".git") or "repo"
    return Path.cwd() / f"{name}__millie-fix"

def overlay_dirty(src: Path, dst: Path):
    patch = run(["git","-C",str(src),"diff","--binary","HEAD","--"]).stdout
    if patch:
        p = run(["git","-C",str(dst),"apply","--binary","-"], check=False, input_bytes=patch)
        if p.returncode:
            raise RuntimeError(p.stderr.decode("utf-8","replace"))
    raw = run(["git","-C",str(src),"ls-files","--others","--exclude-standard","-z"]).stdout
    for b in raw.split(b"\0"):
        if not b:
            continue
        rel = Path(b.decode("utf-8","surrogateescape"))
        s, d = src/rel, dst/rel
        if s.is_file():
            d.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(s,d)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("--dest")
    ap.add_argument("--no-working-state", action="store_true")
    ap.add_argument("--allow-push", action="store_true")
    args = ap.parse_args()

    src_arg = args.source
    local = Path(src_arg).expanduser().exists()
    dest = Path(args.dest).expanduser().resolve() if args.dest else default_dest(src_arg).resolve()
    if dest.exists():
        raise SystemExit(f"Destination already exists: {dest}")

    meta = {"created_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()}

    if local:
        src = Path(src_arg).expanduser().resolve()
        top = Path(out(["git","-C",str(src),"rev-parse","--show-toplevel"])).resolve()
        src = top
        meta.update({
            "source_kind":"local-git",
            "source":str(src),
            "source_head":out(["git","-C",str(src),"rev-parse","HEAD"]),
            "source_branch":out(["git","-C",str(src),"branch","--show-current"], check=False) or "(detached)"
        })
        status = out(["git","-C",str(src),"status","--porcelain=v1"], check=False)
        meta["source_dirty"] = bool(status)
        p = run(["git","clone","--no-hardlinks",str(src),str(dest)], check=False)
    else:
        meta.update({"source_kind":"remote-git","source":src_arg})
        p = run(["git","clone",src_arg,str(dest)], check=False)

    if p.returncode:
        raise SystemExit(p.stderr.decode("utf-8","replace"))

    if local and meta["source_dirty"] and not args.no_working_state:
        overlay_dirty(src, dest)
        meta["working_state_overlaid"] = True
        meta["ignored_files_copied"] = False
    else:
        meta["working_state_overlaid"] = False

    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d-%H%M%S")
    branch = f"millie-fix/{stamp}"
    p = run(["git","-C",str(dest),"checkout","-b",branch], check=False)
    if p.returncode:
        branch = f"millie-fix-{stamp}"
        run(["git","-C",str(dest),"checkout","-b",branch])

    if not args.allow_push:
        run(["git","-C",str(dest),"remote","set-url","--push","origin","no_push://millie-fix"], check=False)

    local_meta = dest/".millie-fix"
    local_meta.mkdir(exist_ok=True)
    meta.update({
        "repair_clone":str(dest),
        "repair_head":out(["git","-C",str(dest),"rev-parse","HEAD"]),
        "repair_branch":branch,
        "push_disabled":not args.allow_push
    })
    (local_meta/"workspace.json").write_text(json.dumps(meta,indent=2)+"\n",encoding="utf-8")

    exclude = dest/".git"/"info"/"exclude"
    if exclude.exists():
        t = exclude.read_text(encoding="utf-8",errors="replace")
        if ".millie-fix/" not in t:
            exclude.write_text(t.rstrip()+"\n.millie-fix/\n",encoding="utf-8")

    print(json.dumps(meta, indent=2))

if __name__ == "__main__":
    main()
