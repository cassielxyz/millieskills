# Millie Repository Integration

Place the complete skill at:

```text
millieskills/
└── millie-sec/
    ├── SKILL.md
    └── ...
```

The main repository already has a planned `millie-sec` manifest entry in typical Millie layouts.
When publishing v1.0.0, update `millie-installer/skills.json` so the entry is:

```json
{
  "id": "millie-sec",
  "name": "Millie Security",
  "short": "Autonomous secure-by-design, AppSec audit, authorized pentest, remediation and verification pipeline.",
  "path": "millie-sec",
  "status": "available"
}
```

A machine-readable copy is provided in `skills-manifest-entry.json`.

After pushing both the `millie-sec/` folder and updated manifest to `main`, the existing Millie
installer should show **Millie Security** as an available skill without requiring a new installer
architecture.
