#!/usr/bin/env python3
"""
Create an isolated Millie Security workspace without executing project code.

- Local Git repositories are independently cloned with --no-hardlinks.
- Tracked dirty changes are reproduced from `git diff --binary HEAD`.
- Non-ignored untracked files are copied except secret-like names.
- Ignored files are not copied by default.
- Push URLs are disabled in the clone.
- Non-Git projects are copied with conservative cache/secret exclusions.

This script performs filesystem/Git preparation only. It never runs the target project.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

SKIP_DIRS = {
    ".git", "node_modules", ".next", ".nuxt", "dist", "build", "out", "target",
    ".cache", ".turbo", ".venv", "venv", "__pycache__", "Pods", "DerivedData",
}
SECRET_NAMES = {
    ".env", ".env.local", ".env.production", ".env.development", ".env.test",
    "credentials.json", "secrets.json", "id_rsa", "id_ed25519",
}
SECRET_SUFFIXES = {".pem", ".p12", ".pfx", ".key", ".keystore", ".jks"}

def run(cmd, cwd=None, input_bytes=None, check=True):
    return subprocess.run(
        cmd, cwd=cwd, input=input_bytes, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        check=check
    )

def is_git_repo(p: Path) -> bool:
    try:
        r = run(["git", "-C", str(p), "rev-parse", "--is-inside-work-tree"], check=False)
        return r.returncode == 0 and r.stdout.strip() == b"true"
    except FileNotFoundError:
        return False

def secret_like(p: Path) -> bool:
    n = p.name.lower()
    return (
        n in SECRET_NAMES
        or n.startswith(".env.")
        or p.suffix.lower() in SECRET_SUFFIXES
        or "credential" in n
        or ("secret" in n and p.suffix.lower() in {".json",".yaml",".yml",".txt"})
    )

def default_destination(source: Path) -> Path:
    return source.parent / f"{source.name}__millie-sec"

def ensure_empty_destination(dest: Path):
    if dest.exists():
        raise SystemExit(f"Destination already exists; refusing to overwrite: {dest}")
    dest.parent.mkdir(parents=True, exist_ok=True)

def disable_pushes(dest: Path):
    remotes = run(["git","-C",str(dest),"remote"], check=False).stdout.decode().split()
    for remote in remotes:
        subprocess.run(
            ["git","-C",str(dest),"remote","set-url","--push",remote,"no_push://millie-sec"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False
        )
    return remotes

def copy_untracked(source: Path, dest: Path):
    r = run(["git","-C",str(source),"ls-files","--others","--exclude-standard","-z"], check=False)
    copied, skipped = [], []
    if r.returncode != 0:
        return copied, skipped
    for raw in r.stdout.split(b"\x00"):
        if not raw:
            continue
        rel = Path(raw.decode("utf-8", errors="surrogateescape"))
        src = source / rel
        if secret_like(rel):
            skipped.append(rel.as_posix())
            continue
        if src.is_symlink():
            # Reproduce symlink only if its link target text is available; do not dereference.
            target = os.readlink(src)
            out = dest / rel
            out.parent.mkdir(parents=True, exist_ok=True)
            try:
                out.symlink_to(target, target_is_directory=src.is_dir())
                copied.append(rel.as_posix())
            except OSError:
                skipped.append(rel.as_posix())
        elif src.is_file():
            out = dest / rel
            out.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, out)
            copied.append(rel.as_posix())
    return copied, skipped

def clone_local(source: Path, dest: Path):
    ensure_empty_destination(dest)
    run(["git","clone","--no-hardlinks",str(source),str(dest)])

    head = run(["git","-C",str(source),"rev-parse","HEAD"], check=False).stdout.decode().strip()
    branch = run(["git","-C",str(source),"branch","--show-current"], check=False).stdout.decode().strip()
    status = run(["git","-C",str(source),"status","--porcelain=v1"], check=False).stdout.decode(
        "utf-8", errors="replace"
    )

    patch = run(["git","-C",str(source),"diff","--binary","HEAD"], check=False).stdout
    patch_applied = False
    patch_error = ""
    if patch:
        apply = run(["git","-C",str(dest),"apply","--binary","-"], input_bytes=patch, check=False)
        patch_applied = apply.returncode == 0
        patch_error = apply.stderr.decode("utf-8", errors="replace")[:2000]
        if not patch_applied:
            raise SystemExit("Failed to reproduce tracked working-tree changes in clone: " + patch_error)

    copied, skipped = copy_untracked(source, dest)
    remotes = disable_pushes(dest)

    return {
        "mode":"local-git-clone",
        "source_head":head,
        "source_branch":branch,
        "source_was_dirty":bool(status.strip()),
        "tracked_patch_applied":patch_applied,
        "nonignored_untracked_copied":copied,
        "secretlike_untracked_skipped":skipped,
        "push_disabled_remotes":remotes,
    }

def clone_remote(source: str, dest: Path):
    ensure_empty_destination(dest)
    run(["git","clone",source,str(dest)])
    remotes = disable_pushes(dest)
    return {"mode":"remote-git-clone","push_disabled_remotes":remotes}

def ignore_copy(directory, names):
    ignored = set()
    for n in names:
        p = Path(n)
        if n in SKIP_DIRS or secret_like(p):
            ignored.add(n)
    return ignored

def copy_non_git(source: Path, dest: Path):
    ensure_empty_destination(dest)
    shutil.copytree(source, dest, symlinks=True, ignore=ignore_copy)
    return {"mode":"filesystem-copy","excluded_dirs":sorted(SKIP_DIRS),
            "secretlike_files_excluded":True}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source", help="Local project path or Git repository URL")
    ap.add_argument("destination", nargs="?", help="Sibling security workspace path")
    args = ap.parse_args()

    local = Path(args.source).expanduser()
    is_local = local.exists()
    if is_local:
        local = local.resolve()
        dest = Path(args.destination).expanduser().resolve() if args.destination else default_destination(local)
        meta = clone_local(local, dest) if is_git_repo(local) else copy_non_git(local, dest)
        source_display = str(local)
    else:
        if not args.destination:
            raise SystemExit("A destination is required for a remote Git URL.")
        dest = Path(args.destination).expanduser().resolve()
        meta = clone_remote(args.source, dest)
        source_display = args.source

    state_dir = dest / ".millie-sec"
    state_dir.mkdir(exist_ok=True)
    record = {
        "schema_version":1,
        "created_at":datetime.now(timezone.utc).isoformat(),
        "source":source_display,
        "workspace":str(dest),
        "project_code_executed":False,
        **meta,
    }
    (state_dir/"workspace.json").write_text(json.dumps(record, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(record, indent=2))

if __name__ == "__main__":
    main()
