# Millie Fix — Isolation & Git Safety

## Default
Create a sibling repair clone and do all writes there.

For local Git:
```bash
git clone --no-hardlinks <source> <destination>
```

A worktree gives a separate directory but shares repository metadata/object storage. Use it only
when explicitly preferred or when clone isolation is impractical.

## Dirty source
A normal clone only captures committed history.

Before cloning inspect:
```bash
git status --porcelain
git diff --stat
git diff --cached --stat
```

To preserve tracked working state without editing source, stream:
```text
git diff --binary HEAD
        |
        v
git -C <clone> apply --binary -
```

Then copy only non-ignored untracked files when appropriate. Do not copy ignored files by default.

Ignored files frequently contain:
- `.env`
- secrets
- credentials
- node_modules/vendor caches
- build output
- IDE state
- local databases

## Push safety
Keep fetch capability but disable push in the repair clone by default. Publish only when asked.

## Original repo — read only
Do not run in the original:
- formatters
- code generators
- package installs that mutate lockfiles
- reset/clean
- refactor tools
- deletion
- branch switching that overwrites files

Read-only status/log/diff/search is allowed.

## Non-Git source
Create a sibling copy, preserve source exactly, exclude only clearly disposable caches/build
outputs, and optionally initialize Git inside the copy.

## Nested repos / submodules
Detect and preserve boundaries. Do not flatten or silently rewrite them.
