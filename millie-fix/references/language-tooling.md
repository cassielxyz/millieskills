# Millie Fix — Language & Tooling Matrix

Use tools already pinned/configured by the repository first. Do not install every tool in this list.

## Cross-language
Semantic/relationship:
- LSP/IDE references
- compiler/type checker
- AST/tree-sitter tooling
- Serena when available
- repository map tools

Security/static analysis:
- Semgrep
- CodeQL when available/appropriate

Duplication:
- jscpd

History/diagnosis:
- Git diff/log/blame/bisect

## JavaScript / TypeScript
Core:
- TypeScript compiler
- ESLint
- framework build/tests
- package-manager audit

Dead/dependency:
- Knip
- dependency-cruiser

Refactor:
- language-service rename
- ast-grep
- OpenRewrite JS recipes where suitable

Duplication:
- jscpd

Important: Knip depends on correct entry points. Teach it framework/plugin entries before deleting
reported files/exports/dependencies.

## Python
Core:
- pytest/unittest
- Ruff
- mypy or Pyright

Dead:
- Vulture
- semantic/reference analysis

Dependency:
- deptry/package tooling where appropriate

Security:
- Semgrep
- Bandit where project uses/accepts it

Refactor:
- LSP
- LibCST/AST-based tooling where available

Vulture's non-100% confidence findings are heuristic and dynamic attribute access can produce false
positives.

## Java / Kotlin
- Gradle/Maven build
- JUnit/Kotest
- compiler
- Detekt/ktlint
- SpotBugs/Error Prone when configured
- OpenRewrite for semantic migrations/refactors
- architecture tests such as ArchUnit where appropriate
- Semgrep/CodeQL/dependency scanning

## Go
- gofmt
- go test
- go vet
- Staticcheck
- golangci-lint when configured
- deadcode analysis
- govulncheck when available
- `go mod tidy` only after understanding the expected dependency diff

## Rust
- cargo fmt
- cargo check
- cargo clippy
- cargo test
- cargo audit
- cargo deny
- cargo udeps when appropriate

Do not treat an externally consumable public library item as dead solely because local callers are
zero.

## C / C++
- compiler warnings
- unit/integration tests
- clang-format
- clang-tidy
- cppcheck
- ASan/UBSan/TSan when supported
- compiler/IDE semantic refactors
- platform profiler

## C# / .NET
- dotnet build/test
- analyzers
- nullable analysis
- dotnet format
- Roslyn/IDE refactors
- Semgrep/CodeQL where suitable

## PHP
- PHPUnit/Pest
- PHPStan/Psalm
- PHPCS/Pint
- Composer audit
- Rector
- Semgrep

## Ruby
- tests
- RuboCop
- Brakeman
- reek/complexity tooling where used
- Bundler audit

## Swift / Apple
- Xcode build/test
- Swift compiler
- SwiftLint
- Xcode static analyzer
- Instruments for performance

## Android
- Gradle
- unit/instrumented tests
- Android Lint
- Detekt/ktlint
- dependency checks
- performance tools where relevant

## Dart / Flutter
- dart format
- dart analyze
- flutter test
- package tooling
- DevTools profiler

## Shell / IaC / CI
- shellcheck/shfmt
- Terraform validate/plan + project lint/security checks
- Dockerfile linting
- YAML/schema validation
- CI workflow validation

## Tool rules
1. Prefer project-pinned tools.
2. Prefer read-only analysis before auto-fix.
3. Keep formatter-only changes separate from behavior changes when practical.
4. Use auto-fix in focused batches.
5. Record tool versions/commands/results.
6. No single scanner proves the codebase is clean.
