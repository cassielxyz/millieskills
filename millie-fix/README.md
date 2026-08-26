# Millie Fix

**Understand first. Repair second. Prove the result.**

`millie-fix` is a portable Agent Skill for repository repair, debugging, code cleanup, dead-code
removal, spaghetti-code refactoring, architecture recovery, dependency hygiene, security review,
performance work, documentation, and verification.

## Core behavior

Millie Fix:

1. leaves the original repository untouched by default;
2. creates an isolated repair clone;
3. records a baseline;
4. understands project structure and entry points;
5. builds file/symbol/function relationships;
6. writes machine-readable JSON graphs;
7. writes durable project memory;
8. identifies root causes and technical debt;
9. repairs in small verified batches;
10. updates documentation at meaningful checkpoints;
11. produces a final analysis and verification report.

## Required project docs

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

## Package

```text
millie-fix/
├── SKILL.md
├── README.md
├── references/
├── schemas/
├── scripts/
└── templates/
```

## Helpers

Create isolated repair clone:

```bash
python scripts/init_workspace.py /path/to/repo
```

Validate generated graph structure:

```bash
python scripts/validate_graphs.py /path/to/repair-clone/docs/millie-fix/graphs
```

The helpers are optional; equivalent host-agent tools may be used.
