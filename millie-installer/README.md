# Millie — One-Line Installer

> Replace `cassielxyz/millieskills` once in `install.ps1` and `skills.json`
> before publishing.

## Quick Install — PowerShell

```powershell
irm https://raw.githubusercontent.com/cassielxyz/millieskills/main/millie-installer/install.ps1 | iex
```

The installer opens an interactive terminal UI:

```text
          ███╗   ███╗██╗██╗     ██╗     ██╗███████╗
          ████╗ ████║██║██║     ██║     ██║██╔════╝
          ██╔████╔██║██║██║     ██║     ██║█████╗
          ██║╚██╔╝██║██║██║     ██║     ██║██╔══╝
          ██║ ╚═╝ ██║██║███████╗███████╗██║███████╗
          ╚═╝     ╚═╝╚═╝╚══════╝╚══════╝╚═╝╚══════╝

                   UNIVERSAL AGENT SKILLS INSTALLER

  ────────────────────────────────────────────────────────────────
  SELECT SKILL
  ────────────────────────────────────────────────────────────────

  [ 1] Millie UI/UX
  [ 2] Millie Fix
  [ 3] Millie Security          [COMING SOON]
  [ 4] Millie QA                [COMING SOON]
  [ 5] Millie Architecture      [COMING SOON]
  ...
  [ A] Install ALL available skills
```

After selecting a skill:

```text
  SELECT PLATFORM

  [ 1] Claude Code
       ~/.claude/skills

  [ 2] Google Antigravity
       ~/.gemini/config/skills

  [ 3] Antigravity CLI
       ~/.gemini/antigravity-cli/skills

  [ 4] VS Code / GitHub Copilot
       ~/.copilot/skills

  [ 5] Cursor
       ~/.cursor/skills

  [ 6] OpenAI Codex
       ~/.agents/skills

  [ 7] Gemini CLI
       ~/.gemini/skills

  [ D] Auto-detect installed platforms
  [ A] Install to ALL supported platforms
```

## What the installer does

1. Downloads `skills.json`.
2. Shows only published skills as installable.
3. Downloads the current repository archive to a temporary folder.
4. Copies the full skill folder — `SKILL.md`, references, scripts, assets, schemas, etc.
5. Installs it into the selected platform's **global/personal** skills directory.
6. Verifies that `SKILL.md` exists after installation.
7. Keeps an installation registry at:

```text
~/.millie/installed.json
```

8. Deletes the temporary repository archive.

## Existing installation

If a skill already exists, the installer offers:

```text
[R] Replace / update
[B] Backup existing, then update
[S] Skip
```

Backups are saved next to the skill:

```text
millie-ui.__backup_20260826-104500/
```

## Non-interactive examples

Install Millie UI into Claude Code:

```powershell
& ([scriptblock]::Create((irm "https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY/main/install.ps1"))) -Skill millie-ui -Platform claude -Force
```

Install UI + Fix into Cursor:

```powershell
& ([scriptblock]::Create((irm "https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY/main/install.ps1"))) -Skill "millie-ui,millie-fix" -Platform cursor -Force
```

Install all currently available skills into all supported platform directories:

```powershell
& ([scriptblock]::Create((irm "https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY/main/install.ps1"))) -AllSkills -AllPlatforms -Force
```

Install all available skills only into detected platforms:

```powershell
& ([scriptblock]::Create((irm "https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY/main/install.ps1"))) -AllSkills -Platform detected -Force
```

## Safer download-first alternative

Users who prefer to inspect the installer before executing it can use:

```powershell
$u="https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY/main/install.ps1"; $f="$env:TEMP\millie-install.ps1"; iwr $u -OutFile $f; notepad $f
```

Then run:

```powershell
& "$env:TEMP\millie-install.ps1"
```

## Recommended repository layout

```text
millie/
├── README.md
├── install.ps1
├── skills.json
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
    ├── millie-sec/
    ├── millie-qa/
    └── ...
```

## Adding a future skill

You do **not** need to modify `install.ps1`.

Add the skill folder:

```text
skills/millie-sec/
```

Then update `skills.json`:

```json
{
  "id": "millie-sec",
  "name": "Millie Security",
  "short": "Secure-code review, vulnerability analysis and remediation.",
  "path": "skills/millie-sec",
  "status": "available"
}
```

The installer menu automatically makes it selectable.

## Current global installation targets

| Platform | Millie installs to |
|---|---|
| Claude Code | `~/.claude/skills/` |
| Google Antigravity IDE | `~/.gemini/config/skills/` |
| Antigravity CLI | `~/.gemini/antigravity-cli/skills/` |
| VS Code / GitHub Copilot | `~/.copilot/skills/` |
| Cursor | `~/.cursor/skills/` |
| OpenAI Codex | `~/.agents/skills/` |
| Gemini CLI | `~/.gemini/skills/` |

These are personal/global locations so the installed Millie skills can be discovered from projects across the user's machine.
