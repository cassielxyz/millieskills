# Millie Fix — Research Foundations

Research refresh: August 26, 2026.

Millie Fix is an original synthesis, not a copy of a single public skill.

## Root-cause debugging
The Superpowers systematic-debugging skill strongly emphasizes root-cause investigation before
fixes, consistent reproduction/evidence, one hypothesis at a time, minimal changes and explicit
verification. Millie adopts this discipline and extends it to repository-wide repair.

## Codebase understanding and memory
Serena provides symbol-level semantic retrieval/refactoring and project memories. Its documented
memory model emphasizes human-readable, versionable, progressively disclosed project knowledge.
Millie mirrors that principle in portable `docs/millie-fix/memory/` files.

Aider's repository map models source relationships as a graph and ranks important code so an LLM
can understand large repositories under a context budget. Millie extends the idea with durable JSON
file/function graphs and reverse relationships.

## Dead-code analysis
Knip builds a graph from entry files and reachable imports. Its documentation warns that missing
entries/dynamic loading can make live code look unused and recommends addressing unused files
before exports/dependencies. It also recommends reviewing auto-fix changes.

Vulture reports Python unused-code candidates with confidence levels and documents dynamic-access
false positives. Millie therefore requires evidence/confidence before deletion.

## Dependency and architecture graphs
dependency-cruiser validates dependency rules and emits JSON, Mermaid, DOT and summarized
architecture views. Millie uses the same machine-readable relationship philosophy across languages
and requires project/function relationship JSON.

## Semantic refactoring
OpenRewrite uses lossless semantic trees and composable recipes for reviewable automated
refactoring/migration. ast-grep performs AST-based structural search/rewrite and can preview diffs.
Millie prefers semantic transformation over broad regex.

## Duplication
jscpd detects code duplication across hundreds of code/document formats and supports AI-oriented
reporting. Millie treats duplication as refactoring evidence, not proof that two blocks should
always share an abstraction.

## Security/static analysis
Semgrep supports pattern-based code scanning and data-flow/taint approaches; its own documentation
acknowledges analysis boundaries. CodeQL supports security, correctness, maintainability,
readability, data-flow and path queries. Millie treats scanners as evidence, not proof of absence.

## Git isolation
Git's worktree documentation describes linked worktrees sharing the same repository. Git's clone
documentation notes local clones can hardlink objects, while `--no-hardlinks` forces object copies.
Millie therefore prefers an independent no-hardlink local clone for repair isolation.

## Resulting design
Millie Fix combines:
- isolated repair clone
- whole-project onboarding
- symbol/function graph
- durable memory
- root-cause-first debugging
- confidence-based dead-code removal
- duplication detection
- semantic refactoring
- architecture repair/rules
- security/dependency analysis
- bounded verified changes
- continuous documentation
