# Millie Fix — Detailed Repair Catalog

Use this as a diagnostic checklist, not a command to rewrite everything.

## Correctness & Logic
- syntax/build failure
- type mismatch
- unreachable branch
- impossible/contradictory condition
- duplicated branch logic
- missing default case
- invalid state transition
- off-by-one / bounds
- null/undefined handling
- mutation while iterating
- aliasing surprise
- stale closure/state/cache
- bad cache invalidation
- swallowed error
- wrong exception/status
- accidental fallthrough
- partial update / missing rollback
- broken idempotency
- wrong retry classification
- timeout without cancellation
- cancellation without cleanup
- duplicate job execution
- race condition / deadlock / lock-order problem
- shared mutable state
- async/sync blocking mismatch
- task/thread/goroutine/coroutine/resource leak
- timezone/DST/local-vs-UTC bug
- precision/rounding/overflow
- float equality misuse
- encoding/Unicode/locale bug
- serialization/parser/schema/default drift

## Dead / Unused
- unused import/variable/parameter
- unused private symbol
- unused export/class/type
- orphan file/package
- orphan route/command/job/worker
- stale feature flag
- obsolete compatibility code
- stale migration helper
- unreachable asset
- unused config/environment key
- unused/dead dependency
- stale generated code
- dead test fixture

## Duplication
- exact clone
- near clone
- repeated validation/transformation/mapping
- repeated error handling
- repeated query/API client/auth rule
- duplicate schema/type/model/constants/config
- repeated test fixture/setup
- repeated UI/controller/service behavior

## Spaghetti / Maintainability
- god function/class/module
- utility dumping ground
- deep nesting
- callback/promise pyramid
- high branching
- long parameter list
- boolean flag explosion
- primitive obsession
- magic constants
- implicit state machine
- temporal coupling / order-dependent init
- hidden global state / singleton abuse
- service locator
- feature envy
- shotgun surgery
- divergent change
- inappropriate intimacy
- message chain / wrapper chain
- speculative/dead abstraction
- inconsistent abstraction levels
- leaky abstraction
- side-effectful helper/getter
- huge constructor
- cyclic initialization
- unnecessary inheritance
- fragile base class
- interface-segregation problems
- unclear ownership
- duplicated business rules

## Architecture
- circular imports/packages
- wrong dependency direction
- domain depends on infrastructure
- controller/UI owns domain logic
- persistence spread across layers
- transport DTO used as domain model everywhere
- duplicate domain representations
- cross-package internal access
- monorepo boundary violations
- shared folder as global dumping ground
- no external-integration boundary
- untestable static/global dependencies
- configuration read everywhere
- duplicated configuration parsing
- unclear lifecycle ownership
- event bus as hidden control flow
- over-centralized orchestration
- over-fragmented micro-modules
- accidental distributed transaction
- wrong service boundary
- excessive public API surface
- unstable dependency direction
- missing architecture tests/rules

## APIs & Integrations
- inconsistent validation
- inconsistent errors/statuses
- request/response schema drift
- accidental breaking change
- undocumented endpoint
- duplicated endpoint logic
- missing pagination/bounds
- timeout/retry/cancellation gaps
- wrong content type
- webhook signature bug
- event schema drift
- message duplicate handling
- non-idempotent consumer
- poisoned-message loop
- API client version drift
- authn/authz inconsistency

## Database / Persistence
- N+1 query
- too many round trips
- missing/incorrect transaction
- transaction too broad
- unsafe migration ordering
- destructive migration without rollout
- missing/contradictory constraints
- nullable drift
- stale column/model field
- missing index where profiling/query evidence supports it
- write amplification
- unbounded query
- connection leak
- isolation-level assumption
- ORM cascade surprise
- serialization drift
- duplicated query logic
- missing persistence boundary where useful

## Performance
- avoidable O(n²+) hot path
- repeated sort/parse/regex compile/serialize
- unnecessary allocation/copy
- N+1 / repeated DB/network call
- missing batch operation
- unbounded result set
- inappropriate cache / missing cache on proven hot path
- unbounded cache
- no connection reuse
- oversized payload/bundle/asset
- heavy startup initialization
- blocking I/O in async/event loop
- sync crypto/compression on hot event loop
- unnecessary render/recomposition
- retained observer/listener
- wasteful polling
- excessive log volume
- lock contention
- redundant work across requests/jobs

## Dependencies / Supply Chain
- unused direct dependency
- missing direct dependency
- transitive dependency relied on implicitly
- duplicate versions
- deprecated/unmaintained package
- vulnerable version
- oversized dependency for trivial feature
- runtime/dev scope mismatch
- invalid peer dependency
- lockfile/config drift
- package-manager mismatch
- license concern
- suspicious/malicious dependency indicators
- native binary portability issue

## Security
- hardcoded secret/token
- secret/sensitive data in logs
- missing authn/authz
- object-level authorization gap
- SQL/command/template injection
- XSS / unsafe HTML
- CSRF
- open redirect
- SSRF-like untrusted outbound request
- path traversal
- unsafe upload/extraction/temp file
- unsafe deserialization
- prototype pollution pattern
- insecure randomness
- weak/deprecated crypto
- disabled TLS verification
- dangerous CORS
- insecure cookie/session
- JWT validation mistakes
- missing rate/bounds controls
- ReDoS / DoS amplification
- unsafe XML parser
- excessive IAM/cloud permissions
- debug/admin endpoint exposure
- insecure defaults
- reachable vulnerable dependency

## Reliability
- infinite/unbounded retry
- retry storm / no backoff or jitter
- retrying non-idempotent work
- missing timeout
- arbitrary timeout masking state
- partial failure unhandled
- no graceful shutdown
- signal/cancellation handling bug
- cleanup skipped on failure
- fragile startup order
- dependency outage causes unnecessary total failure
- poor readiness/health separation
- non-atomic file write
- duplicate scheduled execution
- weak fallback/degradation path

## Observability
- swallowed stack trace
- low-context/misleading error
- duplicate/noisy logging
- sensitive logging
- missing correlation/request/job context
- inconsistent structured fields
- missing metric for critical queue/path
- misleading health check
- no timing around expensive boundary
- debug logging permanently enabled

## Tests
- failing/flaky test
- arbitrary sleep/timing test
- shared mutable fixture
- order-dependent suite
- excessive mocking
- implementation-detail mock
- test-only production API
- weak/no assertion
- snapshot abuse
- duplicated fixture setup
- slow accidental integration
- orphan/stale test
- missing regression coverage
- critical branch untested
- external contract untested

## Build / CI / Release
- stale/broken build script
- duplicate CI logic
- deprecated action/plugin
- missing CI timeout
- missing useful cache
- environment-specific build
- stale generated source
- lockfile mismatch
- warnings ignored
- formatter/linter mismatch
- undeclared globally installed tool
- dead CI job
- obsolete deployment config
- release script risk
- missing artifact verification
- unreproducible build

## Documentation
- README command does not work
- wrong prerequisites
- stale screenshot/config/example
- missing environment description
- missing public API docs
- stale architecture diagram
- stale module description
- stale migration/deployment instruction
- misleading code comment
- completed/obsolete TODO
- missing ADR/decision rationale
- missing runbook
- docs contradict source
