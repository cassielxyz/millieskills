# Recommended Millie Repository Structure

```text
millie/
├── README.md
├── LICENSE
├── install.ps1
├── skills.json
│
├── assets/
│   └── repository-level branding
│
└── skills/
    ├── millie-ui/
    │   ├── SKILL.md
    │   ├── README.md
    │   ├── references/
    │   ├── scripts/
    │   └── assets/
    │
    ├── millie-fix/
    │   ├── SKILL.md
    │   ├── README.md
    │   ├── references/
    │   ├── schemas/
    │   ├── scripts/
    │   ├── templates/
    │   └── assets/
    │
    └── future skills...
```

The installer uses `skills.json` as the catalog and the `path` field as the source of truth.
