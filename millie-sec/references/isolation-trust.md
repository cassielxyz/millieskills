# Isolation & Repository Trust

## Existing-project isolation

Default destination:

```text
<project>__millie-sec/
```

Prefer an independent clone.

For a local Git repository:

```bash
git clone --no-hardlinks <source> <destination>
```

Do not create the security clone inside the source repository.

Disable accidental push from the clone:

```bash
git -C <destination> remote set-url --push origin no_push://millie-sec
```

If there is no `origin`, record that instead of inventing one.

## Dirty working tree

Before cloning:
- record `git status --porcelain=v1`;
- record HEAD/branch;
- distinguish tracked staged/unstaged changes from untracked;
- never discard user work.

For tracked changes, a binary-capable patch can reproduce state:

```bash
git diff --binary HEAD
```

Apply to the clone.

For non-ignored untracked files:
- copy only when needed for the project;
- preserve relative paths;
- do not copy ignored files by default.

Ignored files often include:
- `.env`;
- credentials;
- local databases;
- build outputs;
- caches;
- vendor directories.

If the project cannot run without local secrets, ask for an isolated test credential or let the
user provision it directly in the clone without echoing it into chat/reports.

## Non-Git project

Create an independent copy excluding common:
- VCS data;
- caches;
- build outputs;
- dependency directories;
- secret files;
- local databases unless explicitly needed.

Record exclusion decisions.

## Repository trust gate

Before package install, build, test or project script execution, inspect:
- package manager lifecycle hooks;
- shell/bootstrap scripts;
- Makefiles/task runners;
- build hooks;
- Git hooks;
- CI workflow scripts;
- dev-container bootstrap;
- Docker entrypoints;
- editor/agent instructions;
- MCP/tool configuration;
- native binaries/download steps;
- `curl|sh`, `irm|iex`, remote script execution;
- post-install binary fetchers;
- symlinks escaping the project.

Look for unexpected:
- credential file reads;
- SSH/token access;
- browser credential access;
- clipboard access;
- home-directory scanning;
- network exfiltration;
- persistence;
- privilege elevation;
- destructive filesystem actions.

## Trust levels

```text
TRUSTED
No suspicious setup behavior found; execute baseline normally.

CONSTRAINED
Some setup/network behavior is expected but should run in an isolated container/sandbox.

UNTRUSTED
Suspicious or unexplained behavior. Do not run project code outside a hardened sandbox.

UNKNOWN
Not enough evidence. Treat as constrained.
```

## Sandbox preference

For untrusted/unknown code:
- isolated container/VM;
- no host secrets mounted;
- no Docker socket;
- minimal filesystem mounts;
- non-root user;
- restricted outbound network where practical;
- disposable test data.

## Original repository

Millie Security does not:
- modify;
- delete;
- commit;
- push;
- install packages into

the original project by default.

The secured clone is the handoff.
Merge-back is a separate user decision.
