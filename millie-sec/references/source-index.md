# Research Source Index

Research refresh: 2026-08-27.

Millie Security is an original synthesis. It does not copy third-party skills verbatim.

## High-weight sources

### Strix
- Repository: https://github.com/usestrix/strix
- Skills: `penetration-testing-with-strix`, `api-security-testing`,
  `fix-security-vulnerabilities-with-strix`, `ci-security-scanning-with-strix`
- Influence: authorized dynamic pentesting, validated findings, root-cause remediation, re-scan,
  CI/SARIF.
- License: inspect upstream repository/skill license before redistributing any upstream content.

### Trail of Bits Skills
- Repository: https://github.com/trailofbits/skills
- Key skills: audit-context-building, variant-analysis, static-analysis, testing/sanitizer/fuzzer
  workflows, supply-chain review.
- Influence: understand before hunting; root-cause-based variant analysis; evidence and
  rationalization resistance.

### Anthropic Security
- Official plugin repository:
  https://github.com/anthropics/claude-plugins-official
- Relevant security plugin/workflows: security scan/patch/verifier patterns.
- Influence: scratch-copy patching and independent verification/refutation.

### Semgrep Skills
- https://github.com/semgrep/skills
- Influence: code-security guidance, SAST/taint, test-driven security rule development.

### OWASP
- ASVS: https://owasp.org/www-project-application-security-verification-standard/
- Top 10: https://owasp.org/Top10/
- WSTG: https://owasp.org/www-project-web-security-testing-guide/
- API Security: https://owasp.org/www-project-api-security/
- MASVS: https://mas.owasp.org/MASVS/
- MASTG: https://mas.owasp.org/MASTG/
- GenAI Security: https://genai.owasp.org/

### NIST
- SSDF SP 800-218:
  https://csrc.nist.gov/pubs/sp/800/218/final

### OpenSSF / SLSA
- Scorecard: https://github.com/ossf/scorecard
- SLSA: https://slsa.dev/

### Vulnerability prioritization
- CISA KEV: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- FIRST EPSS: https://www.first.org/epss/
- CWE Top 25: https://cwe.mitre.org/top25/

### Dependency / SBOM tooling
- OSV-Scanner: https://google.github.io/osv-scanner/
- Trivy: https://trivy.dev/
- Syft: https://github.com/anchore/syft
- Grype: https://github.com/anchore/grype
- Gitleaks: https://github.com/gitleaks/gitleaks

### Broad skill collections
- Antigravity Awesome Skills:
  https://github.com/sickn33/antigravity-awesome-skills
- Only the security engineer/security developer/backend/auth/API subsets are relevant.
- Millie deliberately does not load the whole collection.

### Workflow/orchestration
- Superpowers: https://github.com/obra/superpowers
- gstack: https://github.com/garrytan/gstack
- Ruflo: https://github.com/ruvnet/ruflo
- Influence is process/orchestration, not primary vulnerability knowledge.

## Source-use rules

1. Prefer primary standards and official project documentation.
2. Verify version-sensitive claims before publishing.
3. Never copy paid/proprietary security content.
4. Do not redistribute third-party rules/tools unless their license permits it.
5. Link/reference upstream instead of embedding large upstream bodies.
6. Re-evaluate resource weights as projects evolve.
