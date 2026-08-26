# Millie Fix — Documentation & Durable Memory

`docs/millie-fix/` is the portable source of repair knowledge.

## Memory
`memory/core.md` — project purpose, key modules, repair state, references to other memories.
`memory/architecture.md` — layers, ownership, dependency direction, invariants, flows.
`memory/commands.md` — install/build/test/lint/typecheck/run/package/analysis.
`memory/constraints.md` — public contracts, persistence, compatibility, generated/vendor boundaries.
`memory/hotspots.md` — fragile, dynamic, highly central, high-complexity areas.
`memory/decisions.md` — accepted decisions and rationale.

Update after onboarding, meaningful architecture/public-contract discoveries, dead-code decisions
that depend on dynamic behavior, before agent/session handoff, and at finalization.

Do not update memory for every trivial edit.

## Reports
`PROJECT_MAP.md` — human-readable repo map.
`ANALYSIS_REPORT.md` — full health analysis.
`CHANGELOG.md` — repair ledger.
`DECISIONS.md` — architecture/refactor decisions.
`VERIFICATION_REPORT.md` — actual verification evidence.

## Normal project docs
If behavior, config, public API, setup, deployment or examples changed, also update the repository's
normal README/API/architecture/ADR/deployment/example/env/migration docs. Do not hide all
knowledge inside Millie-specific docs.

## Privacy
Do not persist secrets, tokens, credentials, personal data, production dumps, or unnecessary source
copies.
