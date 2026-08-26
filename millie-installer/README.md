# Millie Skills Installer

Install **Millie Agent Skills** globally for your AI coding tools with a simple interactive PowerShell installer.

The installer lets you choose:

* which Millie skill to install;
* which AI coding platform to install it for;
* one skill or all available skills;
* one platform, detected platforms, or all supported platforms.

---

## Quick Install

Open **PowerShell** and paste:

```powershell
irm https://raw.githubusercontent.com/cassielxyz/millieskills/main/millie-installer/install.ps1 | iex
```

Press **Enter**.

That's it.

The Millie installer will open automatically.

---

## Don't Be Afraid of the Terminal Command

If you are not familiar with PowerShell, the command may look complicated:

```powershell
irm https://raw.githubusercontent.com/cassielxyz/millieskills/main/millie-installer/install.ps1 | iex
```

It is simply a short way of doing this:

```text
Download Millie's install.ps1
            ↓
Run install.ps1 in PowerShell
            ↓
Open the Millie installer
```

In PowerShell:

```text
irm
```

means:

```text
Invoke-RestMethod
```

It downloads the installer from this GitHub repository.

And:

```text
iex
```

means:

```text
Invoke-Expression
```

It runs the downloaded PowerShell script.

So the command is essentially:

```text
Download Millie Installer
        +
Run Millie Installer
```

The installer source is public in this repository, so you can inspect it before running it:

`millie-installer/install.ps1`

---

## Prefer to Inspect It First?

You do not have to execute the one-line command directly.

Download the installer first:

```powershell
irm https://raw.githubusercontent.com/cassielxyz/millieskills/main/millie-installer/install.ps1 -OutFile "$env:TEMP\millie-install.ps1"
```

Open it:

```powershell
notepad "$env:TEMP\millie-install.ps1"
```

After reviewing it, run:

```powershell
& "$env:TEMP\millie-install.ps1"
```

This performs the same installation while allowing you to inspect the script first.

---

# How It Works

After running the installer, you will see the Millie terminal interface:

```text
███╗   ███╗██╗██╗     ██╗     ██╗███████╗
████╗ ████║██║██║     ██║     ██║██╔════╝
██╔████╔██║██║██║     ██║     ██║█████╗
██║╚██╔╝██║██║██║     ██║     ██║██╔══╝
██║ ╚═╝ ██║██║███████╗███████╗██║███████╗
╚═╝     ╚═╝╚═╝╚══════╝╚══════╝╚═╝╚══════╝

        UNIVERSAL AGENT SKILLS INSTALLER
```

The actual terminal banner uses Millie's:

```text
RED → ORANGE → YELLOW
```

gradient.

---

## Step 1 — Choose a Skill

Example:

```text
SELECT SKILL

[1] Millie UI/UX
[2] Millie Fix
[3] Millie Security          [COMING SOON]
[4] Millie QA                [COMING SOON]
[5] Millie Architecture      [COMING SOON]

[A] Install ALL available skills
[Q] Quit
```

Enter the number of the skill you want.

For example:

```text
1
```

installs:

```text
millie-ui
```

---

## Step 2 — Choose Your AI Coding Platform

The installer then asks where Millie should be installed.

Example:

```text
SELECT PLATFORM

[1] Claude Code

[2] Google Antigravity

[3] Antigravity CLI

[4] VS Code / GitHub Copilot

[5] Cursor

[6] OpenAI Codex

[7] Gemini CLI

[D] Auto-detect installed platforms

[A] Install to ALL supported platforms

[Q] Quit
```

Choose the platform you use.

---

# Supported Platforms

| Platform                 | Global Millie Skills Location       |
| ------------------------ | ----------------------------------- |
| Claude Code              | `~/.claude/skills/`                 |
| Google Antigravity       | `~/.gemini/config/skills/`          |
| Antigravity CLI          | `~/.gemini/antigravity-cli/skills/` |
| VS Code / GitHub Copilot | `~/.copilot/skills/`                |
| Cursor                   | `~/.cursor/skills/`                 |
| OpenAI Codex             | `~/.agents/skills/`                 |
| Gemini CLI               | `~/.gemini/skills/`                 |

Millie installs skills into the selected user's global/personal skill directory.

That means you do not need to manually copy the skill into every new project.

---

# Auto Detect

Instead of choosing manually, select:

```text
D
```

The installer attempts to detect supported AI coding tools already installed on your computer.

It will then install Millie into the detected platforms.

---

# Install Everywhere

Choose:

```text
A
```

from the platform menu to install the selected skill into every supported skill directory.

You can also select:

```text
A
```

from the skill menu to install all currently available Millie skills.

---

# What Gets Installed?

Millie does not install only `SKILL.md`.

The **complete skill directory** is copied.

For example:

```text
millie-ui/
├── SKILL.md
├── README.md
├── references/
├── scripts/
└── assets/
```

or:

```text
millie-fix/
├── SKILL.md
├── README.md
├── references/
├── schemas/
├── scripts/
├── templates/
└── assets/
```

This ensures all supporting instructions, references, scripts and resources remain available to the agent.

---

# Existing Installation

If Millie detects that the selected skill already exists, you can choose:

```text
[R] Replace / update

[B] Backup existing, then update

[S] Skip
```

Choosing **Backup** keeps the previous version before installing the new one.

Example:

```text
millie-ui.__backup_20260827-041500
```

---

# Installation Registry

Millie keeps a small local record of installed skills at:

```text
~/.millie/installed.json
```

It can contain information such as:

```text
skill
platform
installation path
repository
branch
installation time
installer version
```

This will also make future Millie update and uninstall tools easier to support.

---

# Temporary Files

The installer temporarily downloads the GitHub repository while installing a skill.

After installation completes, the temporary download is removed.

The actual Millie skill remains in the selected platform's global skills directory.

---

# Is It Safe?

The installer is intentionally kept public and readable.

You can inspect:

```text
millie-installer/install.ps1
```

before running it.

The installer is designed to:

```text
download Millie skills
create required skill directories
copy selected skill folders
update existing Millie installations when requested
maintain the Millie installation registry
remove its temporary download
```

You should still follow the same rule you should follow for **any** internet-delivered terminal command:

> If you do not trust the source, inspect the script before executing it.

The inspect-first method above is always available.

---

# No Administrator Required

For normal installation, Millie installs under your user profile:

```text
C:\Users\YOUR_NAME\
```

rather than modifying system-wide Windows directories.

In normal use you should therefore **not need to run PowerShell as Administrator**.

---

# After Installation

Restart your AI editor or coding agent if it was already running.

Then you can ask it to use the installed skill.

Example:

```text
Use Millie UI to redesign this application.
```

or:

```text
Use Millie Fix to analyze and repair this repository.
```

Compatible agents may also automatically discover the skill based on the task.

---

# Quick Start

```text
1. Open PowerShell

2. Paste:

   irm https://raw.githubusercontent.com/cassielxyz/millieskills/main/millie-installer/install.ps1 | iex

3. Press Enter

4. Select a Millie skill

5. Select your AI coding platform

6. Confirm installation

7. Restart your agent/editor if necessary

8. Use Millie
```

---

# Millie

**Universal skills for AI coding agents.**

One installer.

Multiple skills.

Multiple coding agents.

Available across your projects.

Repository:

```text
cassielxyz/millieskills
```

Installer:

```text
millie-installer/install.ps1
```
