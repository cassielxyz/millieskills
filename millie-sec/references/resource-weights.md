# Research Resource Weights

Weights indicate how much a source should influence **Millie Security**, not how good the source is
in its own domain.

```text
10 = foundational security input
 8 = strong specialist/security workflow input
 6 = useful supporting process/orchestration
 4 = situational intelligence
 2 = tiny overlap
 0 = intentionally excluded from security core
```

## Security-core sources

| Resource | Weight | Use in Millie Security |
|---|---:|---|
| Strix + Strix security skills | 10.0 | Authorized dynamic validation, validated findings, remediation/re-test, CI |
| Trail of Bits Agent Skills | 10.0 | Audit context, variant analysis, static analysis, testing discipline, rationalization resistance |
| OWASP ASVS / WSTG / Top 10 / API / MASVS / GenAI | 10.0 | Security control and test coverage |
| Anthropic Claude Security workflows | 9.5 | Independent finding verification, scratch-copy patching, adversarial refutation |
| Semgrep Skills | 9.0 | SAST, taint/data-flow, secure coding, test-driven custom rules |
| NIST SSDF | 8.5 | Secure software-development lifecycle |
| Antigravity Awesome Skills — Security Engineer/Developer subset | 8.5 | Auth/API/backend/pentest coverage vocabulary |
| Backend/auth/API security skills | 8.5 | Server-side auth, API and secure implementation patterns |
| OpenSSF / SLSA / SBOM ecosystem | 8.0 | Supply-chain/release security |
| Claude Superpowers / Superpowers | 8.0 | Evidence, TDD, systematic debugging/review discipline |
| gstack | 7.5 | Adversarial second-opinion / attacker-style review pattern |
| Ruflo | 6.5 | Optional multi-agent orchestration, security specialist routing |
| BRAIN.md-style durable memory | 5.0 | Persistent rationale/assumptions without secrets |
| FreeBuf | 4.0 | Situational threat-intel/community research only; verify independently |

## User-listed resources intentionally excluded from core

| Resource | Weight | Why |
|---|---:|---|
| shadcn/ui | 1.5 | Only frontend implementation context; not a security methodology |
| UI/UX Pro skill | 1.0 | Design knowledge, minimal security overlap |
| Impeccable | 1.0 | Design workflow, not security assurance |
| Agentation | 0.5 | UI feedback workflow |
| GSAP | 0 | Animation library |
| styles.refero.design | 0 | Design inspiration |
| ThreeUI | 0 | 3D UI components |
| img2three.js | 0 | Image-to-3D |
| React Native Reanimated | 0 | Motion runtime; mobile security uses MASVS/MASTG instead |
| Stitch integration | 0 | UI generation |
| Taste skill | 0 | Visual critique |
| Awesome Claude Design | 0 | UI/design |
| DESIGN.md Chrome/design tools | 0 | Visual design-system tooling |
| Unlumen UI | 0 | UI component/design |
| Smooth UI | 0 | UI animation/components |
| AnimMaster | 0 | Motion |
| Threlte | 0 | 3D runtime |
| PeachWeb | 0 | Creative web |
| Theatre.js | 0 | Animation authoring |
| Spline | 0 | 3D authoring |

## Filtering rule

Do not import a source just because it appeared in the user's broader Millie research list.

A source enters Millie Security only if it materially improves:
- threat modeling;
- vulnerability discovery;
- exploit validation;
- secure implementation;
- remediation;
- verification;
- secure SDLC;
- security reporting;
- authorized orchestration.

This keeps the skill deep instead of bloated.
