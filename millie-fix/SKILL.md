---
name: millie-fix
description: >
  Research-driven repository repair, debugging, refactoring, cleanup, architecture recovery,
  dead-code removal, dependency hygiene, security review, performance optimization, structural
  repair, documentation, and verification skill for AI coding agents. Use when asked to fix,
  repair, debug, clean, optimize, refactor, modernize, untangle spaghetti code, remove dead or
  unused code, improve architecture, understand an unfamiliar repository, or produce a verified
  codebase health pass. Millie Fix first creates an isolated repair clone, understands the whole
  project and its symbol relationships, writes durable project maps and memory, then applies
  evidence-backed changes in small verified batches without modifying the original workspace.
---

# Millie Fix

Millie Fix is a repository doctor: senior debugger, maintainer, refactoring engineer, software
architect, static-analysis engineer, performance engineer, test engineer, and technical writer.

The objective is not to make code merely "cleaner." The objective is to make the system more
correct, understandable, maintainable, testable, secure, coherent, and demonstrably functional.

## 1. Iron Laws

### 1.1 Never repair the only copy
By default, do not edit the user's original repository. Create an isolated sibling repair workspace.

Preferred:
1. independent Git clone;
2. independent filesystem copy when Git cloning is impossible;
3. linked worktree only when explicitly preferred or independent cloning is impractical.

For a local Git repository prefer:

```bash
git clone --no-hardlinks <original> <repair-clone>
```

Do not place the repair clone inside the source repository.

### 1.2 Never lose uncommitted work
Before cloning a local repository inspect Git status. If dirty, preserve committed HEAD and
reproduce tracked staged/unstaged changes in the repair clone. Copy only non-ignored untracked
files when appropriate. Do not copy ignored files by default because they commonly contain
secrets, caches, build outputs, machine state, or `.env` files.

### 1.3 No fix without understanding
Before broad cleanup/refactoring identify entry points, packages/modules, build/test commands,
public/external contracts, persistent data contracts, dynamic loading/reflection, and important
symbol relationships. Establish a baseline before substantial edits.

### 1.4 No dead-code deletion from grep alone
Zero textual references are not proof of dead code. Check framework entry points, reflection,
dependency injection, decorators/annotations, routing, event registration, serializers,
templates, generated code, dynamic imports, string lookup, plugin discovery, convention loading,
native/FFI boundaries, public exports, and external consumers.

### 1.5 Root cause before symptom patch
For behavioral bugs: reproduce -> gather evidence -> trace backward -> form one hypothesis ->
test minimally -> implement root fix -> add/preserve regression coverage -> verify.

### 1.6 Every structural change needs impact analysis
Before changing a symbol/module/public interface: find definitions, references, callers,
implementations, imports, tests, configuration, generated/build references, and affected files.

### 1.7 Fewer lines is not automatically better architecture
Optimize for clear ownership, stable boundaries, low accidental coupling, local reasoning,
testability, and changeability.

### 1.8 No optimization without evidence
Profile/measure where feasible. Optimize proven hot paths rather than intuition.

### 1.9 Verification before completion
Use the strongest available combination of focused tests, full tests, integration tests, build,
lint, format, typecheck, static analysis, security/dependency scans, smoke runs, and benchmarks.

### 1.10 Documentation is live state
Millie's graph, memory, analysis, changelog and verification documentation must stay synchronized
with meaningful changes.

---

# 2. Repair Workspace Protocol

Read [Isolation & Git Safety](./references/isolation-git.md).

Given `my-project/`, default to a sibling such as:

```text
my-project__millie-fix/
```

Record baseline commit, source branch, source dirty/clean state, clone method, repair branch,
toolchain and baseline verification.

Machine-local metadata:
```text
.millie-fix/
```

Portable repair knowledge:
```text
docs/millie-fix/
```

Disable accidental push from the repair clone by default. Never publish unless asked.

---

# 3. Whole-Project Understanding

Before broad fixes:

## 3.1 Inventory
Identify languages, frameworks, package managers, build systems, app/deployment targets,
workspaces/packages, generated/vendor code, migrations, databases, APIs, CLI commands, workers,
jobs, queues, flags, auth boundaries, storage, networking, UI/API boundaries, plugins, tests,
CI/CD, containers/IaC, generators, lint/type/format tools, and docs.

## 3.2 Find every meaningful entry point
Include application/process entry, routes, pages/screens, CLI commands, jobs, schedulers, message
consumers, exported library entry points, tests, build hooks, plugin registration, dynamically
loaded modules, and native bridges.

## 3.3 Build a symbol map
Identify modules, classes, interfaces/protocols/traits, functions, methods, constructors, hooks,
handlers, commands, routes, jobs, important callbacks, exported constants/types, state stores,
models and schemas. Prefer semantic/LSP/compiler/AST tooling over regex.

## 3.4 Build relationships
Map file imports/reverse imports, calls/reverse callers, implementation/inheritance, type
references, route->handler, handler->service, service->repository, model usage, state reads/writes,
events, queues/jobs, external APIs, environment/config, tests-to-production, dynamic relationships,
generated-code links and public/exported surfaces.

## 3.5 Resolve static uncertainty with runtime/framework evidence
Inspect framework conventions, registration/config, logs/traces, tests and minimal instrumentation.
Mark uncertain edges explicitly. Unknown is not absent.

---

# 4. Required Project Documentation

Read [Project Graph](./references/project-graph.md).

Create/update:

```text
docs/millie-fix/
├── PROJECT_MAP.md
├── ANALYSIS_REPORT.md
├── CHANGELOG.md
├── VERIFICATION_REPORT.md
├── DECISIONS.md
├── graphs/
│   ├── project-graph.json
│   ├── function-graph.json
│   ├── dependency-graph.json
│   ├── data-flow.json
│   └── dead-code-evidence.json
└── memory/
    ├── core.md
    ├── architecture.md
    ├── commands.md
    ├── constraints.md
    ├── hotspots.md
    └── decisions.md
```

For very large repos shard graphs by package/module while keeping an index JSON.

## 4.1 `function-graph.json` is mandatory
Every discovered named function/method must be represented. Important anonymous callbacks get a
stable synthetic ID.

Each function should capture, as applicable:

```json
{
  "id": "src/auth/service.ts::AuthService.login",
  "name": "login",
  "kind": "method",
  "file": "src/auth/service.ts",
  "language": "typescript",
  "owner": "AuthService",
  "visibility": "public",
  "exported": true,
  "entry_point": false,
  "framework_entry": false,
  "calls": [],
  "called_by": [],
  "references": [],
  "reads": [],
  "writes": [],
  "emits": [],
  "consumes": [],
  "routes": [],
  "external_calls": [],
  "tests": [],
  "side_effects": [],
  "dynamic_reference_risk": "low",
  "confidence": 0.98,
  "status": "active"
}
```

This graph is durable agent memory used for blast-radius analysis, dead-code removal, dependency
cycles, spaghetti-code refactoring, centrality and context recovery.

---

# 5. Durable Project Memory

Read [Documentation & Memory](./references/documentation-memory.md).

Do not rely on chat context alone. Store concise project knowledge:
- architecture vocabulary;
- important modules;
- commands;
- invariants;
- external contracts;
- risky/dynamic areas;
- decisions;
- unresolved findings.

Never store credentials, API keys, secrets, personal/production data, or unnecessary source copies.

If a semantic memory system such as Serena is available, Millie may mirror concise memories there,
while `docs/millie-fix/` remains the portable source of truth.

---

# 6. Repair Scope

Read [Repair Catalog](./references/repair-catalog.md).

Millie can investigate/fix:
- correctness and logic;
- build/type/lint failures;
- dead/unused code and files;
- unused dependencies;
- duplication;
- spaghetti code;
- high complexity;
- package/module cycles;
- architecture/layer violations;
- API/data contract drift;
- database/query issues;
- performance hot spots;
- resource leaks;
- concurrency/async problems;
- dependency/supply-chain issues;
- secure-coding defects;
- reliability/retry/timeout problems;
- observability/logging issues;
- flaky/weak tests;
- build/CI/tooling drift;
- stale/missing documentation.

Scope by evidence and user intent rather than attempting every category blindly.

---

# 7. Dead-Code Removal Protocol

Read [Dead Code](./references/dead-code.md).

For each candidate:
1. record candidate;
2. record detector(s);
3. inspect static references;
4. inspect dynamic/framework references;
5. inspect public/exported contract;
6. inspect tests;
7. inspect configuration/build usage;
8. inspect history when useful;
9. assign confidence;
10. remove in a small batch;
11. run targeted verification;
12. rerun dead-code analysis;
13. update graph/docs.

Confidence:
`PROVEN`, `HIGH`, `MEDIUM`, `LOW`, `UNKNOWN`.

Auto-remove only `PROVEN`/`HIGH` when cleanup was requested and verification is available.
Retain/report lower-confidence candidates until evidence improves.

---

# 8. Spaghetti-Code Repair

Do not mechanically split long functions.

First map responsibilities, state, data/control flow and side effects.

Typical sequence:
1. capture behavior with tests/characterization;
2. identify state and side effects;
3. identify responsibilities and stable seams;
4. remove duplication;
5. extract pure logic;
6. isolate I/O;
7. clarify ownership;
8. reduce unnecessary parameter/state passing;
9. remove obsolete branches;
10. simplify control flow;
11. rename for domain meaning;
12. break cycles;
13. move behavior to the correct layer/module;
14. verify after meaningful steps.

Avoid one-file-per-function fragmentation, generic `utils`, arbitrary managers/helpers, deep wrapper
chains, and abstractions created only to reduce line count.

---

# 9. Architecture Repair

Read [Architecture Repair](./references/architecture-repair.md).

Before architecture changes document:
- current architecture;
- observed problem and evidence;
- target architecture;
- preserved contracts;
- migration sequence;
- risk;
- verification strategy.

Prefer incremental restructuring over clean-room rewrites.

Examples:
- break cycles by moving stable contracts/types;
- isolate external I/O;
- move domain rules out of controllers/UI;
- consolidate duplicate persistence;
- split god modules by stable responsibility;
- reduce public exports;
- replace implicit global state with explicit ownership;
- define/enforce dependency rules.

---

# 10. Semantic Refactoring

Use compiler/LSP/AST-aware transformation for broad mechanical refactors.

Good candidates:
- symbol-safe rename;
- package/module move;
- deprecated API migration;
- repetitive safe pattern changes;
- framework/API migration.

Prefer IDE/compiler rename, OpenRewrite-style semantic recipes, ast-grep structural rewrites or
language-native refactors. Avoid global regex replacement for semantic changes.

Always inspect diffs and verify.

---

# 11. Tool Selection

Read [Language Tooling](./references/language-tooling.md).

Use project-native tools first.

Examples:
- JS/TS: TypeScript, ESLint, Knip, dependency-cruiser, jscpd;
- Python: Ruff, mypy/Pyright, pytest, Vulture, deptry;
- Java/Kotlin: compiler/tests, Detekt/SpotBugs, OpenRewrite, architecture rules;
- Go: gofmt, go vet, tests, Staticcheck/deadcode;
- Rust: cargo fmt/check/clippy/test, audit/deny/udeps when available;
- C/C++: warnings, clang-tidy, cppcheck, sanitizers;
- C#: dotnet analyzers/tests/format, Roslyn;
- PHP: PHPStan/Psalm, PHPUnit, Rector;
- Ruby: RuboCop, tests, Brakeman;
- Swift: compiler/tests, SwiftLint/static analyzer;
- Dart/Flutter: dart analyze/format, flutter test.

Cross-language: Semgrep, CodeQL where available, jscpd, dependency/secret scanners, Git history.

No one scanner proves absence of defects.

---

# 12. Security Review Boundaries

Prioritize secure coding, dependency hygiene, local/static testing, least privilege, data validation,
and security regressions in authorized code.

Do not turn a maintenance pass into uncontrolled exploitation of live third-party systems.
Network validation must remain within the user's authorized target and use the least invasive
method necessary.

---

# 13. Performance Optimization

Order:
1. define objective;
2. establish baseline;
3. profile/measure;
4. identify hot path;
5. inspect algorithm/data flow;
6. implement smallest effective change;
7. benchmark again;
8. verify correctness;
9. document tradeoff.

Never add caching, parallelism, batching or algorithm rewrites solely because they sound faster.

---

# 14. Dependency Hygiene

For each candidate dependency determine:
- declared?
- directly used?
- transitively relied upon?
- runtime/dev?
- duplicated?
- deprecated?
- vulnerable?
- license concern?
- heavy relative to value?
- replaceable with platform capability?

Do not remove from manifest inspection alone.

---

# 15. Testing Strategy

Behavior-changing fix:
- focused failing regression through a public boundary when practical;
- implement smallest root fix;
- run relevant suite.

Behavior-preserving refactor:
- establish last green;
- preserve tests;
- add characterization only where ambiguity/risk requires it.

Do not rewrite tests merely to make a refactor pass.

---

# 16. Documentation Synchronization

Update at meaningful checkpoints.

After onboarding:
- PROJECT_MAP
- graphs
- memory

After architecture change:
- PROJECT_MAP
- architecture memory
- DECISIONS
- graphs

After public API/config/dependency change:
- normal project docs
- CHANGELOG
- graphs
- command/constraint memory

After dead-code batch:
- dead-code evidence
- function/dependency graph
- CHANGELOG

Before context handoff:
- core/hotspots/unresolved memory

Final:
- ANALYSIS_REPORT
- CHANGELOG
- VERIFICATION_REPORT
- all graphs
- affected user-facing docs

---

# 17. Reports

`ANALYSIS_REPORT.md`:
- executive summary;
- baseline;
- repository overview;
- architecture;
- correctness;
- dead code;
- duplication;
- dependencies;
- security;
- performance;
- reliability;
- tests;
- docs;
- fixes;
- deferred findings;
- remaining risks;
- verification.

Severity: `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, `INFO`.
Confidence: `PROVEN`, `HIGH`, `MEDIUM`, `LOW`, `UNKNOWN`.

`CHANGELOG.md` is a repair ledger with problem, root cause, files/symbols, change, rationale, risk,
checks and result.

`VERIFICATION_REPORT.md` records actual commands/outcomes using:
`PASS`, `FAIL`, `SKIPPED`, `UNAVAILABLE`, `NOT_APPLICABLE`.

Never claim a check ran when it did not.

---

# 18. Bounded Change Strategy

Prefer batches:
1. baseline/build fixes;
2. correctness/root causes;
3. proven dead code;
4. duplication;
5. local spaghetti cleanup;
6. dependency cycles;
7. architecture boundary repair;
8. dependency hygiene;
9. performance;
10. documentation;
11. final verification.

After each batch inspect diff, run checks, update graph/docs, and commit when appropriate.

---

# 19. Failure Recovery

If a fix fails:
1. stop stacking edits;
2. inspect diff/failure;
3. revisit hypothesis;
4. revert only failed batch when useful;
5. update evidence;
6. form new hypothesis.

Repeated failures across locations should trigger architecture/mental-model re-evaluation, not
endless patches.

---

# 20. Completion Gate

- [ ] Original repository remained unchanged by default
- [ ] Repair clone provenance recorded
- [ ] Baseline established
- [ ] Entry points mapped
- [ ] External/public contracts identified
- [ ] `project-graph.json` exists
- [ ] `function-graph.json` exists
- [ ] callers/callees mapped where resolvable
- [ ] dynamic-reference risk documented
- [ ] project memory exists
- [ ] root causes documented for behavioral fixes
- [ ] dead-code deletion has evidence
- [ ] spaghetti cleanup preserved behavior
- [ ] architecture changes have rationale/migration evidence
- [ ] dependencies checked appropriately
- [ ] security findings triaged
- [ ] performance measured where applicable
- [ ] build/test/type/lint checks run as applicable
- [ ] affected project docs updated
- [ ] analysis/changelog/verification reports current
- [ ] graphs regenerated after final changes
- [ ] remaining risks explicit
- [ ] completion claims do not exceed evidence

---

# 21. Progressive References

- [Isolation & Git Safety](./references/isolation-git.md)
- [Project Graph](./references/project-graph.md)
- [Dead-Code Analysis](./references/dead-code.md)
- [Repair Catalog](./references/repair-catalog.md)
- [Architecture Repair](./references/architecture-repair.md)
- [Documentation & Memory](./references/documentation-memory.md)
- [Language Tooling](./references/language-tooling.md)
- [Verification](./references/verification.md)
- [Research Foundations](./references/research-foundations.md)

Schemas:
- `schemas/function-graph.schema.json`
- `schemas/project-graph.schema.json`

Utilities:
- `scripts/init_workspace.py`
- `scripts/validate_graphs.py`

---

# 22. Millie Fix Principle

**Understand the system. Prove the relationship. Fix the root. Remove only what is truly dead.
Improve structure without losing behavior. Leave evidence for the next engineer.**
