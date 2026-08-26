<div align="center">

# Millie Skills

### Universal Agent Skills for modern AI coding agents

Research-driven, portable skills for **UI/UX, repository repair, security, testing, architecture, backend/API, databases, mobile, DevOps, documentation, planning, auditing, and more.**

<br />

[**Install Millie**](#quick-install) ·
[**Available Skills**](#available-skills) ·
[**Platform Guides**](#platform-specific-guides) ·
[**How to Use**](#how-to-use-millie) ·
[**Troubleshooting**](#troubleshooting)

<br />

```text
One repository
      ↓
Multiple specialist skills
      ↓
Install once
      ↓
Use across your projects
```

</div>

---

# What is Millie?

**Millie** is a collection of reusable Agent Skills for AI coding tools.

Each Millie skill is a self-contained folder containing a `SKILL.md` entry point and, when needed, supporting:

```text
references/
scripts/
templates/
schemas/
assets/
data/
evaluations/
```

Instead of repeatedly pasting large prompts into an AI coding agent, you install Millie once and let the agent load the relevant specialist instructions when the task calls for them.

Millie is designed around the open **Agent Skills** model used by multiple coding-agent ecosystems.

---

# Available Skills

## Millie UI/UX

```text
millie-ui
```

A research-driven UI/UX and creative frontend skill covering:

- product and UX reasoning;
- automatic art direction;
- design systems;
- responsive/adaptive interfaces;
- accessibility;
- typography and color;
- shadcn-aware implementation;
- advanced animation;
- GSAP/scroll storytelling;
- React Native Reanimated;
- Three.js / R3F / Threlte / Spline;
- image → 3D → website workflows;
- visual auditing and rendered verification.

Directory:

```text
millie-ui/
```

Documentation:

```text
millie-ui/README.md
```

---

## Millie Fix

```text
millie-fix
```

A repository doctor for:

- root-cause debugging;
- whole-project understanding;
- safe refactoring;
- dead-code analysis;
- spaghetti-code repair;
- architecture recovery;
- dependency cleanup;
- performance analysis;
- project graphs;
- durable project memory;
- testing and verification;
- documentation synchronization.

Directory:

```text
millie-fix/
```

Documentation:

```text
millie-fix/README.md
```

---

## Planned Millie Skills

The repository is designed to grow into a broader specialist family.

Examples include:

```text
millie-sec
millie-qa
millie-arch
millie-api
millie-db
millie-mobile
millie-devops
millie-docs
millie-plan
millie-audit
```

Only skills marked **available** by the installer should be treated as released.

---

# Quick Install

## Windows — PowerShell

Open **PowerShell** and paste:

```powershell
irm https://raw.githubusercontent.com/cassielxyz/millieskills/main/millie-installer/install.ps1 | iex
```

Press **Enter**.

The interactive Millie installer will open.

You will first choose a skill:

```text
SELECT SKILL

[1] Millie UI/UX
[2] Millie Fix
[3] Millie Security        [COMING SOON]
...

[A] Install ALL available skills
[Q] Quit
```

Then choose where to install it:

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

The installer copies the **entire skill folder**, not only `SKILL.md`.

---

# Do Not Be Afraid of the Terminal Command

This command:

```powershell
irm https://raw.githubusercontent.com/cassielxyz/millieskills/main/millie-installer/install.ps1 | iex
```

looks more complicated than what it actually does.

Conceptually it means:

```text
Download Millie's public PowerShell installer
                  ↓
Run that installer
                  ↓
Choose skill
                  ↓
Choose coding agent
                  ↓
Copy skill into that agent's user skills directory
```

`irm` is PowerShell's `Invoke-RestMethod`.

`iex` is `Invoke-Expression`.

Because running any internet-delivered script deserves caution, the installer source is public:

```text
millie-installer/install.ps1
```

You can inspect it before running it.

---

# Inspect Before Running

If you prefer to download and inspect the installer first:

```powershell
$u="https://raw.githubusercontent.com/cassielxyz/millieskills/main/millie-installer/install.ps1"
$f="$env:TEMP\millie-install.ps1"
Invoke-WebRequest $u -OutFile $f
notepad $f
```

After reviewing it:

```powershell
& "$env:TEMP\millie-install.ps1"
```

This performs the same installation without piping the remote script directly into execution.

---

# What the Installer Does

The installer is designed to:

1. load the Millie skill catalog;
2. show available and planned skills;
3. let you choose one or all released skills;
4. let you choose one, detected, or all supported platforms;
5. temporarily download this repository;
6. copy each complete selected skill directory;
7. verify that `SKILL.md` exists after installation;
8. record installed skills in the Millie registry;
9. remove the temporary repository download.

The local registry is stored at:

```text
~/.millie/installed.json
```

On Windows, `~` normally resolves to:

```text
C:\Users\<YOUR_USERNAME>
```

---

# Global vs Project Installation

There are two common ways to use Agent Skills.

## Global / Personal

Install once into your user profile.

The skill becomes available across many projects.

This is the default Millie installer behavior.

Example:

```text
C:\Users\Alice\.claude\skills\millie-ui\
```

Advantages:

- install once;
- works across projects;
- easy to update centrally;
- ideal for general-purpose skills such as Millie UI and Millie Fix.

---

## Project / Workspace

Copy the skill into a project's supported skills directory.

Example:

```text
my-project/
└── .agents/
    └── skills/
        └── millie-ui/
            └── SKILL.md
```

Advantages:

- project can pin a particular skill version;
- team members can share it through Git;
- project-specific rules travel with the repository.

Use a project-local install when a team explicitly wants Millie versioned with that project.

---

# Platform-Specific Guides

The following paths are the locations Millie currently targets for personal/global installation.

> [!NOTE]
> Agent-skill ecosystems are evolving quickly. The installer is kept separate so platform paths can be updated without restructuring every Millie skill.

---

# Google Antigravity IDE

Antigravity supports workspace and global skills.

## Global installation

Millie installs to:

```text
~/.gemini/config/skills/
```

Example on Windows:

```text
C:\Users\Alice\.gemini\config\skills\millie-ui\
```

Expected structure:

```text
~/.gemini/config/skills/
├── millie-ui/
│   ├── SKILL.md
│   ├── references/
│   ├── scripts/
│   ├── assets/
│   └── ...
└── millie-fix/
    ├── SKILL.md
    └── ...
```

This makes the skill available across Antigravity workspaces.

---

## Workspace installation

Antigravity's current workspace skills directory is:

```text
<workspace>/.agents/skills/
```

Example:

```text
my-project/
└── .agents/
    └── skills/
        └── millie-ui/
            ├── SKILL.md
            └── ...
```

Workspace skills are useful when a project needs to pin or share a specific Millie configuration.

---

## How Antigravity discovers Millie

When a conversation begins, Antigravity sees the names and descriptions of available skills.

When a task matches a skill, the agent can load its `SKILL.md` and supporting resources.

You normally do not need to manually paste the Millie instructions.

---

## Using Millie UI in Antigravity

You can be explicit:

```text
Use millie-ui to redesign this application.

First understand the current product and existing design system.
Preserve functionality and choose the strongest design direction.
```

Or more naturally:

```text
Redesign this dashboard into a polished responsive product interface.
```

If the `millie-ui` description matches the request, Antigravity can select it automatically.

For a highly important task, explicitly naming the skill is recommended.

---

## Using Millie Fix in Antigravity

```text
Use millie-fix to analyze and repair this repository.

Do not modify the original repository.
Create the isolated repair workspace and follow the complete
analysis, repair, documentation, and verification workflow.
```

---

## Antigravity troubleshooting

Check that:

```text
~/.gemini/config/skills/millie-ui/SKILL.md
```

exists.

For a workspace skill, check:

```text
<project>/.agents/skills/millie-ui/SKILL.md
```

Also confirm:

- the folder contains `SKILL.md`;
- the frontmatter description exists;
- you installed the complete folder;
- the workspace is the one you intended;
- restarting Antigravity if the skill was added after the session began.

---

# Antigravity CLI

Antigravity CLI uses a different global location from the Antigravity IDE.

## Global installation

```text
~/.gemini/antigravity-cli/skills/
```

Example:

```text
~/.gemini/antigravity-cli/skills/millie-ui/
```

Workspace skills use:

```text
<workspace>/.agents/skills/
```

---

## Use

Start the CLI in your project and ask:

```text
Use millie-ui to implement the new frontend.
```

or:

```text
Use millie-fix to inspect this repository and repair the root causes.
```

The exact skill behavior is defined by each Millie `SKILL.md`.

---

# Claude Code

Claude Code supports personal and project Agent Skills.

## Global installation

Millie installs to:

```text
~/.claude/skills/
```

Example:

```text
~/.claude/skills/millie-ui/SKILL.md
```

On Windows:

```text
C:\Users\Alice\.claude\skills\millie-ui\SKILL.md
```

---

## Project installation

```text
<project>/.claude/skills/
```

Example:

```text
my-project/
└── .claude/
    └── skills/
        └── millie-ui/
            └── SKILL.md
```

---

## How to use Millie in Claude Code

Claude can invoke relevant skills automatically from their descriptions.

Claude Code also supports direct skill invocation.

For example:

```text
/millie-ui
```

or:

```text
/millie-fix
```

You can also add instructions after invoking it.

Example:

```text
/millie-ui Redesign the dashboard without changing existing functionality.
```

Natural-language usage also works:

```text
Use millie-ui to build a premium landing page with purposeful
scroll interaction and a responsive mobile composition.
```

---

## Verify Claude Code installation

Check:

```bash
ls ~/.claude/skills/millie-ui/SKILL.md
```

On Windows PowerShell:

```powershell
Test-Path "$HOME\.claude\skills\millie-ui\SKILL.md"
```

Expected:

```text
True
```

If the top-level `~/.claude/skills` directory did not exist when Claude Code started, restart Claude Code after creating it.

Claude Code can detect edits to existing watched skill directories during a session.

---

# VS Code / GitHub Copilot

GitHub Copilot supports Agent Skills in VS Code Agent Mode and other Copilot agent surfaces.

## Global installation

Millie installs to:

```text
~/.copilot/skills/
```

Example:

```text
~/.copilot/skills/millie-ui/SKILL.md
```

GitHub Copilot also supports:

```text
~/.agents/skills/
```

for personal Agent Skills.

Millie's installer uses the dedicated Copilot directory:

```text
~/.copilot/skills/
```

---

## Project installation

GitHub Copilot supports project skills in locations such as:

```text
.github/skills/
.claude/skills/
.agents/skills/
```

A portable option is:

```text
<repo>/.agents/skills/
```

Example:

```text
my-project/
└── .agents/
    └── skills/
        └── millie-ui/
            └── SKILL.md
```

---

## How to use Millie in VS Code

Open the repository in VS Code and switch Copilot to an agent-capable mode.

Then ask:

```text
Use millie-ui to redesign the current interface.
```

or:

```text
Use millie-fix to inspect this repository before changing anything.
```

Copilot can load matching Agent Skills automatically based on the task.

---

## Good VS Code prompt example

```text
Use millie-ui.

Review the existing app first.
Preserve its functionality and strong existing design patterns.

Then redesign the dashboard for desktop, tablet, and mobile.
Use purposeful motion only where it improves state communication.
Render and verify the result before considering the task complete.
```

---

## Verify installation

PowerShell:

```powershell
Test-Path "$HOME\.copilot\skills\millie-ui\SKILL.md"
```

Expected:

```text
True
```

If Copilot does not seem to use the skill:

- make sure you are using an agent surface that supports Agent Skills;
- restart/reload VS Code;
- explicitly say `Use millie-ui`;
- check that `SKILL.md` contains valid frontmatter;
- ensure the entire Millie directory was copied.

---

# Cursor

Cursor supports both Cursor-specific and common Agent Skills directories.

## Global installation

Millie installs to:

```text
~/.cursor/skills/
```

Example:

```text
~/.cursor/skills/millie-ui/SKILL.md
```

Cursor also supports the shared user-level location:

```text
~/.agents/skills/
```

and compatibility locations used by some other coding agents.

---

## Project installation

Cursor supports:

```text
.cursor/skills/
```

and:

```text
.agents/skills/
```

Example:

```text
my-project/
└── .cursor/
    └── skills/
        └── millie-ui/
            └── SKILL.md
```

A cross-agent project may prefer:

```text
my-project/.agents/skills/
```

---

## How to use Millie in Cursor

Open the project and use Cursor's agent workflow.

Ask explicitly:

```text
Use millie-ui to design and implement this frontend.
```

or:

```text
Use millie-fix to repair the repository.
```

Cursor can also discover relevant skills automatically.

---

## Nested project skills

Cursor supports skills in nested project directories.

This can be useful in monorepos.

Example:

```text
my-monorepo/
├── .agents/skills/
│   └── millie-fix/
│
└── apps/
    └── web/
        └── .agents/
            └── skills/
                └── millie-ui/
```

The UI skill can therefore be placed close to the frontend package while repository-wide skills remain at the root.

---

# OpenAI Codex

Current Codex builds use the common personal Agent Skills directory:

```text
~/.agents/skills/
```

Millie's installer therefore installs Codex skills there.

Example:

```text
~/.agents/skills/millie-ui/SKILL.md
```

---

## How to use Millie in Codex

Open Codex on the repository you want to work with.

Then ask:

```text
Use the millie-ui skill to redesign this interface.
```

or:

```text
Use millie-fix to analyze this repository and repair it safely.
```

If your Codex build exposes direct skill selection/invocation, choose the installed Millie skill there.

---

## Verify installation

PowerShell:

```powershell
Test-Path "$HOME\.agents\skills\millie-ui\SKILL.md"
```

Expected:

```text
True
```

If a skill is present on disk but not immediately visible in a picker, restart the Codex session and try an explicit request naming the skill.

The on-disk user-skill directory and the UI skill picker/index can evolve independently across Codex builds.

---

# Gemini CLI

Gemini CLI supports user and workspace Agent Skills.

## Global installation

```text
~/.gemini/skills/
```

Gemini CLI also recognizes the common alias:

```text
~/.agents/skills/
```

Millie's installer uses:

```text
~/.gemini/skills/
```

Example:

```text
~/.gemini/skills/millie-ui/SKILL.md
```

---

## Workspace installation

Gemini CLI supports:

```text
<workspace>/.gemini/skills/
```

and:

```text
<workspace>/.agents/skills/
```

---

## Verify Gemini CLI discovery

Inside an interactive Gemini CLI session:

```text
/skills list
```

You should see the installed Millie skills.

If you added a skill while the session is already running:

```text
/skills reload
```

For workspace skills, ensure the workspace is trusted if Gemini requests trust.

---

## Use Millie

Ask:

```text
Use millie-ui to redesign this app.
```

or:

```text
Use millie-fix to diagnose and repair this project.
```

Gemini selects skills from their names and descriptions and can ask for consent before activating them.

---

# Installation Path Reference

| Platform | Millie Global Install Path | Common Project Path |
|---|---|---|
| Google Antigravity IDE | `~/.gemini/config/skills/` | `.agents/skills/` |
| Antigravity CLI | `~/.gemini/antigravity-cli/skills/` | `.agents/skills/` |
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |
| VS Code / GitHub Copilot | `~/.copilot/skills/` | `.agents/skills/` or `.github/skills/` |
| Cursor | `~/.cursor/skills/` | `.cursor/skills/` or `.agents/skills/` |
| OpenAI Codex | `~/.agents/skills/` | `.agents/skills/` |
| Gemini CLI | `~/.gemini/skills/` | `.gemini/skills/` or `.agents/skills/` |

> [!TIP]
> For a personal installation used across projects, prefer the dedicated global directory selected by the Millie installer.
>
> For a repository shared by several different Agent Skills-compatible tools, `.agents/skills/` is often the cleanest project-local common location when all selected tools support it.

---

# How to Use Millie

You do not need to paste `SKILL.md` into the conversation.

The installed coding agent reads it when appropriate.

There are three practical ways to use a Millie skill.

---

## 1. Explicit Skill Request

Most reliable:

```text
Use millie-ui to redesign this application.
```

or:

```text
Use millie-fix to analyze and repair this repository.
```

This is recommended for important tasks.

---

## 2. Natural Trigger

Because each `SKILL.md` contains a detailed description, supported agents can automatically determine that Millie is relevant.

Example:

```text
Redesign this web app into a premium responsive interface with
purposeful animation and a proper design system.
```

The agent may recognize that `millie-ui` fits the task.

---

## 3. Platform-Specific Direct Invocation

Some agents expose installed skills through slash commands, skill pickers, or dedicated UI.

For example, Claude Code can invoke:

```text
/millie-ui
```

Gemini CLI lets you inspect skills with:

```text
/skills list
```

Other coding agents may expose skills automatically through their agent UI rather than a universal slash-command syntax.

---

# Using Millie UI

## Automatic Design Direction

```text
Use millie-ui to build this frontend.

I have no visual direction.
Understand the product and automatically choose the strongest
context-fit premium design.

Do not use generic AI UI patterns.
```

---

## Existing Project

```text
Use millie-ui.

Inspect the current project, its design tokens, components,
typography, interaction patterns, and responsive behavior first.

Improve the UI without breaking functionality or replacing strong
existing design decisions unnecessarily.
```

---

## Creative UI

```text
Use millie-ui to create a distinctive, highly creative frontend.

Research current high-quality references first.
Create a coherent visual direction specific to this product.
Use unusual composition and interaction only when they improve the experience.
```

---

## Scroll Animation

```text
Use millie-ui.

Create a scroll-driven product story.

Choose between native CSS scroll animation, Motion, GSAP/ScrollTrigger,
or WebGL based on actual complexity.

Do not hijack scrolling.
Provide responsive and reduced-motion behavior.
```

---

## shadcn Project

```text
Use millie-ui.

This project uses shadcn.

Inspect components.json and the existing component configuration first.
Use shadcn as the accessible component foundation, but create a
product-specific visual identity instead of a default shadcn dashboard.
```

---

## 3D Product Website

```text
Use millie-ui.

Create an interactive 3D product experience.

Choose the appropriate runtime from Three.js, R3F, Threlte, Spline,
or a simpler technique based on this project's stack.

Keep essential content semantic and provide mobile,
reduced-motion, and performance fallbacks.
```

---

## Image → 3D → Website

```text
Use millie-ui.

Use the supplied product image as reference for an image-to-3D
workflow, then integrate the resulting model into the website.

Use 3D only where it improves product understanding.
Design camera, lighting, materials, scroll behavior,
interaction, mobile quality, and fallback states deliberately.
```

---

## React Native

```text
Use millie-ui to redesign this React Native app.

Use platform-native behavior.
Use Reanimated where it materially improves gesture feedback,
continuity, scroll interaction, or layout transition.

Prioritize smooth release-mode performance and reduced-motion support.
```

---

# Using Millie Fix

## Full Repository Repair

```text
Use millie-fix.

Analyze this repository completely before changing it.
Create the isolated repair clone.
Build the project/function relationship maps.
Find root causes rather than patching symptoms.
Repair issues in verified batches.
Update documentation and produce the final verification report.
```

---

## Refactor Existing Project

```text
Use millie-fix to refactor this project.

Do not modify the original copy.
Preserve behavior.
Find dead code using semantic and runtime evidence rather than grep alone.
Untangle spaghetti code and improve architecture where justified.
```

---

## Performance Cleanup

```text
Use millie-fix.

Find evidence-backed performance problems.
Do not perform speculative optimization.
Measure where possible, fix the root issue, and verify the result.
```

---

# Combining Millie Skills

Multiple skills can complement each other.

Example:

```text
Use millie-fix first to understand and stabilize the repository.

After the project is structurally healthy, use millie-ui to redesign
the frontend without breaking the repaired architecture.
```

A future workflow might be:

```text
millie-plan
    ↓
millie-arch
    ↓
millie-api
    ↓
millie-ui
    ↓
millie-sec
    ↓
millie-qa
    ↓
millie-audit
```

The goal is specialist collaboration rather than one enormous universal prompt.

---

# Skill Folder Integrity

Do not copy only `SKILL.md` when a Millie skill includes other resources.

For example, Millie UI contains resources such as:

```text
millie-ui/
├── SKILL.md
├── README.md
├── references/
├── scripts/
├── schemas/
├── templates/
├── data/
├── evaluations/
└── assets/
```

The `SKILL.md` router references those resources.

Removing them reduces the skill's capabilities.

The Millie installer always copies the complete skill folder.

---

# Updating Millie

Until a dedicated Millie update command is released, the simplest update method is to run the installer again:

```powershell
irm https://raw.githubusercontent.com/cassielxyz/millieskills/main/millie-installer/install.ps1 | iex
```

Choose the same skill and platform.

When the installer detects an existing copy it can offer:

```text
[R] Replace / update
[B] Backup existing, then update
[S] Skip
```

Use **Backup** if you manually modified the installed copy and want to preserve it before upgrading.

---

# Manual Update

If you installed Millie manually:

1. download the latest skill folder;
2. back up your existing copy if it contains local changes;
3. replace the complete skill folder;
4. restart/reload the coding agent if needed.

Do not merge old and new reference directories blindly because obsolete files can remain and create contradictory instructions.

---

# Uninstalling a Skill

The current installer focuses on installation/update.

For a manual uninstall, remove the relevant skill directory.

Example for Claude Code:

```powershell
Remove-Item "$HOME\.claude\skills\millie-ui" -Recurse
```

Example for Cursor:

```powershell
Remove-Item "$HOME\.cursor\skills\millie-ui" -Recurse
```

Example for Codex:

```powershell
Remove-Item "$HOME\.agents\skills\millie-ui" -Recurse
```

Only remove the specific Millie skill directory—not the entire parent skills directory if it contains other skills.

---

# Verify a Millie Installation on Windows

## Claude Code

```powershell
Test-Path "$HOME\.claude\skills\millie-ui\SKILL.md"
```

## Antigravity IDE

```powershell
Test-Path "$HOME\.gemini\config\skills\millie-ui\SKILL.md"
```

## Antigravity CLI

```powershell
Test-Path "$HOME\.gemini\antigravity-cli\skills\millie-ui\SKILL.md"
```

## VS Code / Copilot

```powershell
Test-Path "$HOME\.copilot\skills\millie-ui\SKILL.md"
```

## Cursor

```powershell
Test-Path "$HOME\.cursor\skills\millie-ui\SKILL.md"
```

## Codex

```powershell
Test-Path "$HOME\.agents\skills\millie-ui\SKILL.md"
```

## Gemini CLI

```powershell
Test-Path "$HOME\.gemini\skills\millie-ui\SKILL.md"
```

If PowerShell prints:

```text
True
```

the expected `SKILL.md` exists at that location.

---

# Troubleshooting

## Installer opens but cannot load the catalog

Confirm the public manifest exists at:

```text
https://raw.githubusercontent.com/cassielxyz/millieskills/main/millie-installer/skills.json
```

and that the repository/branch names are correct.

---

## The skill is installed but the agent does not use it

Check:

```text
1. Is SKILL.md present?
2. Is it exactly named SKILL.md?
3. Is the full skill folder present?
4. Is YAML frontmatter valid?
5. Does the description clearly match the task?
6. Is the coding agent/version capable of Agent Skills?
7. Was the agent already running when the skill directory was first created?
8. Does the tool require workspace trust?
9. Are you using the correct global path for that platform?
```

Then try:

```text
Use millie-ui for this task.
```

Explicit naming is the easiest diagnostic.

---

## Gemini CLI does not show the skill

Run:

```text
/skills list
```

If you installed the skill during the current session:

```text
/skills reload
```

For workspace skills, check workspace trust.

---

## Claude Code does not show the skill

Confirm:

```text
~/.claude/skills/millie-ui/SKILL.md
```

If the top-level skills directory was created after Claude Code started, restart Claude Code.

Try:

```text
/millie-ui
```

---

## Cursor does not use the skill

Confirm either:

```text
~/.cursor/skills/millie-ui/SKILL.md
```

or a supported shared location exists.

Then ask explicitly:

```text
Use millie-ui.
```

---

## Copilot does not use the skill

Confirm:

```text
~/.copilot/skills/millie-ui/SKILL.md
```

Use a Copilot agent surface that supports Agent Skills.

Then explicitly ask:

```text
Use millie-ui for this task.
```

---

## Codex has the file but does not show it in a picker

Confirm:

```text
~/.agents/skills/millie-ui/SKILL.md
```

Start a fresh Codex session and explicitly request:

```text
Use the millie-ui skill.
```

The user-skill filesystem location and a particular Codex UI picker/index may not always refresh at the same time.

---

# Repository Structure

```text
millieskills/
│
├── README.md
│
├── millie-installer/
│   ├── install.ps1
│   ├── skills.json
│   └── README.md
│
├── millie-ui/
│   ├── SKILL.md
│   ├── README.md
│   ├── VERSION
│   ├── CHANGELOG.md
│   ├── RESEARCH_REPORT.md
│   ├── references/
│   ├── scripts/
│   ├── schemas/
│   ├── templates/
│   ├── data/
│   ├── evaluations/
│   └── assets/
│
├── millie-fix/
│   ├── SKILL.md
│   ├── README.md
│   ├── references/
│   ├── scripts/
│   ├── schemas/
│   ├── templates/
│   └── assets/
│
└── future Millie skills...
```

---

# Installer Repository Layout

The Millie installer reads:

```text
millie-installer/skills.json
```

to determine which skills are:

```text
available
planned
```

This lets future Millie skills appear in the installer without rewriting the entire installation workflow.

---

# Why Millie Uses Separate Skills

A single giant instruction file for every software-engineering task would:

- consume unnecessary context;
- mix unrelated workflows;
- create conflicting priorities;
- make maintenance difficult;
- make evaluation difficult;
- reduce specialist depth.

Millie instead uses:

```text
small top-level specialist router
              ↓
task-specific references
              ↓
scripts/data/templates only when needed
```

This gives each skill deeper capabilities without forcing every piece of knowledge into every request.

---

# Recommended Usage Pattern

For most people:

```text
1. Install Millie globally.
2. Open your normal project.
3. Start your preferred coding agent.
4. Tell the agent which Millie skill to use for important work.
5. Let the skill inspect the project before acting.
6. Review major plans when appropriate.
7. Let Millie execute and verify according to the skill workflow.
```

You do **not** need to copy Millie into every repository unless you intentionally want a project-local pinned version.

---

# Example — Antigravity

```text
Use millie-ui.

Analyze the existing frontend and determine the current design authority.

Then redesign the interface into a premium, responsive experience
specific to this product.

Use creative interaction and animation where meaningful.
Do not use generic AI landing-page patterns.
Do not break existing functionality.
Verify the rendered result.
```

---

# Example — Claude Code

```text
/millie-fix

Analyze this repository completely.
Create an isolated repair workspace.
Find root causes, dead code, architectural drift,
dependency problems, and maintainability issues.
Repair in verified batches and update documentation.
```

---

# Example — VS Code / GitHub Copilot

```text
Use millie-ui.

This project already uses shadcn.
Inspect the project configuration before changing components.

Preserve accessible primitives but create a distinct
product-specific visual system and responsive layout.
```

---

# Example — Cursor

```text
Use millie-fix to understand the repository first.

After stabilization, use millie-ui to improve the frontend.
Keep architecture and UI work separated and verify both.
```

---

# Example — Codex

```text
Use millie-ui.

Build a responsive product showcase with a real design system.
If 3D improves product understanding, choose the lightest suitable
Three.js/R3F workflow and provide a static/reduced-motion fallback.
```

---

# Example — Gemini CLI

First check:

```text
/skills list
```

Then:

```text
Use millie-ui to audit and improve this interface.
```

If the skill was just installed:

```text
/skills reload
```

---

# Contributing

When adding a Millie skill:

```text
1. create its own directory;
2. add a valid SKILL.md;
3. keep the main SKILL.md focused;
4. move deeper knowledge into references;
5. add scripts/templates only when they have real value;
6. add evaluation cases;
7. document important upstream research;
8. avoid copying third-party proprietary content;
9. update millie-installer/skills.json;
10. validate installation from a clean environment.
```

---

# Security

Millie skills can contain instructions and executable helper scripts.

Treat third-party Agent Skills the same way you treat development tooling:

- inspect unfamiliar code;
- understand what scripts do;
- do not run untrusted installers;
- avoid committing secrets;
- review network/system operations;
- use appropriate coding-agent permission controls.

The Millie repository keeps its installer and skill source visible so users can review what they install.

---

# License and Third-Party Sources

Millie is an original synthesis.

Individual skills may research or interoperate with external frameworks, component ecosystems, design references, and open-source projects.

That does **not** mean third-party code, logos, paid components, or proprietary designs are automatically redistributable.

Check each skill's:

```text
README.md
RESEARCH_REPORT.md
references/source-index.md
assets/THIRD_PARTY_NOTICES.md
```

where applicable.

---

# Official Platform References

The current installation guidance in this README follows the documented Agent Skills locations for the supported platforms.

Useful upstream documentation includes:

- Claude Code — Agent Skills / personal and project skill directories
- Google Antigravity — global `~/.gemini/config/skills/` and workspace `.agents/skills/`
- Antigravity CLI — global `~/.gemini/antigravity-cli/skills/`
- GitHub Copilot — personal `~/.copilot/skills/` / `~/.agents/skills/`
- Cursor — global `~/.cursor/skills/` / `~/.agents/skills/`
- Gemini CLI — user `~/.gemini/skills/` / `~/.agents/skills/`
- Codex — current personal Agent Skills convention under `~/.agents/skills/`

Because coding-agent products evolve rapidly, check current platform documentation if a future release stops discovering an installed skill.

---

# Quick Reference

## Install

```powershell
irm https://raw.githubusercontent.com/cassielxyz/millieskills/main/millie-installer/install.ps1 | iex
```

## Use UI Skill

```text
Use millie-ui to design and implement this interface.
```

## Use Fix Skill

```text
Use millie-fix to analyze and repair this repository.
```

## Gemini Verification

```text
/skills list
```

## Claude Direct Invocation

```text
/millie-ui
```

## Repository

```text
https://github.com/cassielxyz/millieskills
```

---

<div align="center">

# Millie Skills

### Specialist intelligence for AI coding agents.

```text
Understand first.
Choose deliberately.
Build carefully.
Verify before claiming.
```

**One installer. Multiple skills. Multiple coding agents.**

</div>
