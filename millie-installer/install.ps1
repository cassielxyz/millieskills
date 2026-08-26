param(
    [string]$Repository = "cassielxyz/millieskill",
    [string]$Branch = "main",
    [string]$Skill,
    [string]$Platform,
    [switch]$AllSkills,
    [switch]$AllPlatforms,
    [switch]$Force,
    [switch]$NoBanner
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version 2.0

$Script:InstallerVersion = "0.1.0"
$Script:RegistryPath = Join-Path $HOME ".millie/installed.json"

# ------------------------------------------------------------
# Console / visual helpers
# ------------------------------------------------------------

function Write-Center {
    param(
        [string]$Text,
        [ConsoleColor]$Color = [ConsoleColor]::White
    )

    $width = 80
    try {
        if ($Host.UI.RawUI.WindowSize.Width -gt 20) {
            $width = $Host.UI.RawUI.WindowSize.Width
        }
    } catch {}

    $pad = [Math]::Max(0, [Math]::Floor(($width - $Text.Length) / 2))
    Write-Host ((" " * $pad) + $Text) -ForegroundColor $Color
}

function Show-MillieBanner {
    if ($NoBanner) { return }

    Clear-Host

    $banner = @(
        @{ Text = "███╗   ███╗██╗██╗     ██╗     ██╗███████╗"; Color = "Magenta" },
        @{ Text = "████╗ ████║██║██║     ██║     ██║██╔════╝"; Color = "DarkMagenta" },
        @{ Text = "██╔████╔██║██║██║     ██║     ██║█████╗  "; Color = "Blue" },
        @{ Text = "██║╚██╔╝██║██║██║     ██║     ██║██╔══╝  "; Color = "Cyan" },
        @{ Text = "██║ ╚═╝ ██║██║███████╗███████╗██║███████╗"; Color = "Green" },
        @{ Text = "╚═╝     ╚═╝╚═╝╚══════╝╚══════╝╚═╝╚══════╝"; Color = "Yellow" }
    )

    foreach ($line in $banner) {
        Write-Center -Text $line.Text -Color ([ConsoleColor]$line.Color)
    }

    Write-Host ""
    Write-Center "UNIVERSAL AGENT SKILLS INSTALLER" Cyan
    Write-Center "Build smarter agents. Keep the skill everywhere." DarkGray
    Write-Center "Installer v$($Script:InstallerVersion)" DarkGray
    Write-Host ""
}

function Write-Section {
    param([string]$Title)
    Write-Host ""
    Write-Host ("  " + ("─" * 70)) -ForegroundColor DarkGray
    Write-Host ("  " + $Title) -ForegroundColor Cyan
    Write-Host ("  " + ("─" * 70)) -ForegroundColor DarkGray
}

function Write-Success {
    param([string]$Text)
    Write-Host "  [OK] " -ForegroundColor Green -NoNewline
    Write-Host $Text -ForegroundColor White
}

function Write-WarningLine {
    param([string]$Text)
    Write-Host "  [!]  " -ForegroundColor Yellow -NoNewline
    Write-Host $Text -ForegroundColor DarkYellow
}

function Write-ErrorLine {
    param([string]$Text)
    Write-Host "  [X]  " -ForegroundColor Red -NoNewline
    Write-Host $Text -ForegroundColor White
}

function Pause-Millie {
    Write-Host ""
    [void](Read-Host "  Press Enter to continue")
}

# ------------------------------------------------------------
# Repository / manifest
# ------------------------------------------------------------

function Assert-RepositoryConfigured {
    if ($Repository -match "YOUR_GITHUB_USERNAME|YOUR_REPOSITORY") {
        Write-ErrorLine "The installer repository is not configured yet."
        Write-Host ""
        Write-Host "  Edit install.ps1 and replace:" -ForegroundColor White
        Write-Host '    YOUR_GITHUB_USERNAME/YOUR_REPOSITORY' -ForegroundColor Yellow
        Write-Host ""
        Write-Host "  Example:" -ForegroundColor White
        Write-Host '    jesowin/millie' -ForegroundColor Cyan
        throw "Millie repository has not been configured."
    }
}

function Get-RawBaseUrl {
    return "https://raw.githubusercontent.com/$Repository/$Branch"
}

function Get-MillieManifest {
    Assert-RepositoryConfigured

    $url = "$(Get-RawBaseUrl)/skills.json"

    Write-Host "  Fetching skill catalog..." -ForegroundColor DarkGray

    try {
        $manifest = Invoke-RestMethod -Uri $url
        if (-not $manifest.skills) {
            throw "Manifest has no skills array."
        }
        return $manifest
    }
    catch {
        Write-ErrorLine "Could not load skills.json"
        Write-Host "  $url" -ForegroundColor DarkGray
        throw
    }
}

# ------------------------------------------------------------
# Platform definitions
# ------------------------------------------------------------

function Get-PlatformDefinitions {
    $definitions = @(
        [pscustomobject]@{
            Id = "claude"
            Name = "Claude Code"
            Path = Join-Path $HOME ".claude/skills"
            Commands = @("claude")
            Notes = "Personal skills available across Claude Code projects."
        },
        [pscustomobject]@{
            Id = "antigravity"
            Name = "Google Antigravity"
            Path = Join-Path $HOME ".gemini/config/skills"
            Commands = @("antigravity")
            Notes = "Global Antigravity IDE skills."
        },
        [pscustomobject]@{
            Id = "antigravity-cli"
            Name = "Antigravity CLI"
            Path = Join-Path $HOME ".gemini/antigravity-cli/skills"
            Commands = @("agy")
            Notes = "Global Antigravity CLI skills."
        },
        [pscustomobject]@{
            Id = "vscode"
            Name = "VS Code / GitHub Copilot"
            Path = Join-Path $HOME ".copilot/skills"
            Commands = @("code", "copilot")
            Notes = "Personal Agent Skills used by VS Code/Copilot."
        },
        [pscustomobject]@{
            Id = "cursor"
            Name = "Cursor"
            Path = Join-Path $HOME ".cursor/skills"
            Commands = @("cursor")
            Notes = "Personal Cursor skills."
        },
        [pscustomobject]@{
            Id = "codex"
            Name = "OpenAI Codex"
            Path = Join-Path $HOME ".agents/skills"
            Commands = @("codex")
            Notes = "User Agent Skills scanned by Codex."
        },
        [pscustomobject]@{
            Id = "gemini"
            Name = "Gemini CLI"
            Path = Join-Path $HOME ".gemini/skills"
            Commands = @("gemini")
            Notes = "Global Gemini CLI skills."
        }
    )

    return $definitions
}

function Test-AnyCommand {
    param([string[]]$Names)

    foreach ($name in $Names) {
        if (Get-Command $name -ErrorAction SilentlyContinue) {
            return $true
        }
    }
    return $false
}

function Get-DetectedPlatforms {
    $detected = @()

    foreach ($p in (Get-PlatformDefinitions)) {
        $commandDetected = Test-AnyCommand $p.Commands
        $pathDetected = Test-Path (Split-Path $p.Path -Parent)

        if ($commandDetected -or $pathDetected) {
            $detected += $p
        }
    }

    return $detected
}

# ------------------------------------------------------------
# Interactive selectors
# ------------------------------------------------------------

function Select-SkillsInteractive {
    param($Manifest)

    Write-Section "SELECT SKILL"

    $skills = @($Manifest.skills)

    for ($i = 0; $i -lt $skills.Count; $i++) {
        $s = $skills[$i]
        $number = $i + 1

        if ($s.status -eq "available") {
            Write-Host ("  [{0,2}] " -f $number) -ForegroundColor Cyan -NoNewline
            Write-Host $s.name -ForegroundColor White -NoNewline
            Write-Host ("  — " + $s.short) -ForegroundColor DarkGray
        }
        else {
            Write-Host ("  [{0,2}] " -f $number) -ForegroundColor DarkGray -NoNewline
            Write-Host $s.name -ForegroundColor DarkGray -NoNewline
            Write-Host "  [COMING SOON]" -ForegroundColor DarkYellow
        }
    }

    Write-Host ""
    Write-Host "  [ A] Install ALL available skills" -ForegroundColor Green
    Write-Host "  [ Q] Quit" -ForegroundColor DarkGray
    Write-Host ""

    while ($true) {
        $choice = (Read-Host "  Choose a skill").Trim()

        if ($choice -match '^[Qq]$') {
            return @()
        }

        if ($choice -match '^[Aa]$') {
            return @($skills | Where-Object { $_.status -eq "available" })
        }

        $n = 0
        if ([int]::TryParse($choice, [ref]$n)) {
            if ($n -ge 1 -and $n -le $skills.Count) {
                $selected = $skills[$n - 1]

                if ($selected.status -ne "available") {
                    Write-WarningLine "$($selected.name) is not published yet."
                    continue
                }

                return @($selected)
            }
        }

        Write-WarningLine "Invalid selection."
    }
}

function Select-PlatformsInteractive {
    $platforms = @(Get-PlatformDefinitions)

    Write-Section "SELECT PLATFORM"

    for ($i = 0; $i -lt $platforms.Count; $i++) {
        $p = $platforms[$i]
        $detected = Test-AnyCommand $p.Commands

        Write-Host ("  [{0,2}] " -f ($i + 1)) -ForegroundColor Cyan -NoNewline
        Write-Host $p.Name -ForegroundColor White -NoNewline

        if ($detected) {
            Write-Host "  [DETECTED]" -ForegroundColor Green
        }
        else {
            Write-Host ""
        }

        Write-Host ("       " + $p.Path) -ForegroundColor DarkGray
    }

    Write-Host ""
    Write-Host "  [ D] Auto-detect installed platforms" -ForegroundColor Yellow
    Write-Host "  [ A] Install to ALL supported platforms" -ForegroundColor Green
    Write-Host "  [ Q] Quit" -ForegroundColor DarkGray
    Write-Host ""

    while ($true) {
        $choice = (Read-Host "  Choose a platform").Trim()

        if ($choice -match '^[Qq]$') {
            return @()
        }

        if ($choice -match '^[Aa]$') {
            return $platforms
        }

        if ($choice -match '^[Dd]$') {
            $detected = @(Get-DetectedPlatforms)
            if ($detected.Count -eq 0) {
                Write-WarningLine "No supported platform was confidently detected."
                Write-Host "  Select a platform manually; Millie can create its global skill directory." -ForegroundColor DarkGray
                continue
            }

            Write-Success ("Detected: " + (($detected | ForEach-Object { $_.Name }) -join ", "))
            return $detected
        }

        $n = 0
        if ([int]::TryParse($choice, [ref]$n)) {
            if ($n -ge 1 -and $n -le $platforms.Count) {
                return @($platforms[$n - 1])
            }
        }

        Write-WarningLine "Invalid selection."
    }
}

# ------------------------------------------------------------
# Download
# ------------------------------------------------------------

function Get-RepositoryArchive {
    param([string]$TempRoot)

    $zipPath = Join-Path $TempRoot "millie-repository.zip"
    $extractPath = Join-Path $TempRoot "repository"

    $url = "https://codeload.github.com/$Repository/zip/refs/heads/$Branch"

    Write-Section "DOWNLOAD"
    Write-Host "  Repository: " -ForegroundColor DarkGray -NoNewline
    Write-Host $Repository -ForegroundColor White
    Write-Host "  Branch:     " -ForegroundColor DarkGray -NoNewline
    Write-Host $Branch -ForegroundColor White

    Write-Host ""
    Write-Host "  Downloading repository archive..." -ForegroundColor Cyan

    Invoke-WebRequest -Uri $url -OutFile $zipPath -UseBasicParsing

    Write-Host "  Extracting..." -ForegroundColor Cyan
    Expand-Archive -Path $zipPath -DestinationPath $extractPath -Force

    $repoRoot = Get-ChildItem $extractPath -Directory | Select-Object -First 1

    if (-not $repoRoot) {
        throw "Could not locate extracted repository root."
    }

    Write-Success "Repository downloaded."
    return $repoRoot.FullName
}

# ------------------------------------------------------------
# Registry
# ------------------------------------------------------------

function Get-Registry {
    if (-not (Test-Path $Script:RegistryPath)) {
        return [pscustomobject]@{
            schema_version = 1
            installations = @()
        }
    }

    try {
        return (Get-Content $Script:RegistryPath -Raw | ConvertFrom-Json)
    }
    catch {
        Write-WarningLine "Existing Millie install registry is invalid; rebuilding it."
        return [pscustomobject]@{
            schema_version = 1
            installations = @()
        }
    }
}

function Save-Registry {
    param($Registry)

    $dir = Split-Path $Script:RegistryPath -Parent
    New-Item -ItemType Directory -Force -Path $dir | Out-Null
    $Registry | ConvertTo-Json -Depth 8 | Set-Content -Path $Script:RegistryPath -Encoding UTF8
}

function Record-Installation {
    param(
        [string]$SkillId,
        [string]$SkillName,
        [string]$PlatformId,
        [string]$PlatformName,
        [string]$Destination
    )

    $registry = Get-Registry
    $items = @($registry.installations)

    $items = @($items | Where-Object {
        -not (($_.skill -eq $SkillId) -and ($_.platform -eq $PlatformId))
    })

    $items += [pscustomobject]@{
        skill = $SkillId
        skill_name = $SkillName
        platform = $PlatformId
        platform_name = $PlatformName
        path = $Destination
        repository = $Repository
        branch = $Branch
        installed_at = (Get-Date).ToString("o")
        installer_version = $Script:InstallerVersion
    }

    $registry.installations = $items
    Save-Registry $registry
}

# ------------------------------------------------------------
# Installation
# ------------------------------------------------------------

function Confirm-ReplaceExisting {
    param(
        [string]$SkillName,
        [string]$Path
    )

    if ($Force) {
        return "replace"
    }

    Write-WarningLine "$SkillName is already installed:"
    Write-Host "       $Path" -ForegroundColor DarkGray
    Write-Host ""
    Write-Host "       [R] Replace / update" -ForegroundColor Yellow
    Write-Host "       [B] Backup existing, then update" -ForegroundColor Cyan
    Write-Host "       [S] Skip" -ForegroundColor DarkGray

    while ($true) {
        $choice = (Read-Host "       Choice").Trim().ToLowerInvariant()

        switch ($choice) {
            "r" { return "replace" }
            "b" { return "backup" }
            "s" { return "skip" }
            default { Write-WarningLine "Choose R, B, or S." }
        }
    }
}

function Install-OneSkill {
    param(
        $SkillDefinition,
        $PlatformDefinition,
        [string]$RepositoryRoot
    )

    $source = Join-Path $RepositoryRoot ($SkillDefinition.path -replace '/', [IO.Path]::DirectorySeparatorChar)
    $skillFile = Join-Path $source "SKILL.md"

    if (-not (Test-Path $skillFile)) {
        Write-ErrorLine "$($SkillDefinition.name): SKILL.md was not found at $($SkillDefinition.path)"
        return $false
    }

    $platformRoot = $PlatformDefinition.Path
    New-Item -ItemType Directory -Force -Path $platformRoot | Out-Null

    $destination = Join-Path $platformRoot $SkillDefinition.id

    if (Test-Path $destination) {
        $action = Confirm-ReplaceExisting -SkillName $SkillDefinition.name -Path $destination

        if ($action -eq "skip") {
            Write-WarningLine "Skipped $($SkillDefinition.name) for $($PlatformDefinition.Name)."
            return $true
        }

        if ($action -eq "backup") {
            $stamp = Get-Date -Format "yyyyMMdd-HHmmss"
            $backup = "$destination.__backup_$stamp"
            Move-Item -Path $destination -Destination $backup
            Write-Success "Existing skill backed up to $backup"
        }
        elseif ($action -eq "replace") {
            Remove-Item -Path $destination -Recurse -Force
        }
    }

    Copy-Item -Path $source -Destination $destination -Recurse -Force

    if (-not (Test-Path (Join-Path $destination "SKILL.md"))) {
        Write-ErrorLine "Installation verification failed: $destination"
        return $false
    }

    Record-Installation `
        -SkillId $SkillDefinition.id `
        -SkillName $SkillDefinition.name `
        -PlatformId $PlatformDefinition.Id `
        -PlatformName $PlatformDefinition.Name `
        -Destination $destination

    Write-Success "$($SkillDefinition.name) -> $($PlatformDefinition.Name)"
    Write-Host "       $destination" -ForegroundColor DarkGray
    return $true
}

function Install-Selections {
    param(
        [array]$Skills,
        [array]$Platforms,
        [string]$RepositoryRoot
    )

    Write-Section "INSTALL"

    $success = 0
    $failed = 0

    foreach ($platform in $Platforms) {
        Write-Host ""
        Write-Host ("  " + $platform.Name) -ForegroundColor Magenta
        Write-Host ("  " + $platform.Notes) -ForegroundColor DarkGray

        foreach ($skill in $Skills) {
            try {
                if (Install-OneSkill -SkillDefinition $skill -PlatformDefinition $platform -RepositoryRoot $RepositoryRoot) {
                    $success++
                }
                else {
                    $failed++
                }
            }
            catch {
                $failed++
                Write-ErrorLine "$($skill.name) -> $($platform.Name): $($_.Exception.Message)"
            }
        }
    }

    Write-Section "RESULT"
    Write-Success "$success installation(s) completed."

    if ($failed -gt 0) {
        Write-ErrorLine "$failed installation(s) failed."
    }

    Write-Host ""
    Write-Host "  Registry:" -ForegroundColor DarkGray
    Write-Host "  $Script:RegistryPath" -ForegroundColor DarkGray

    Write-Host ""
    Write-Host "  Some agents discover new skills immediately; if a skill does not appear," -ForegroundColor DarkGray
    Write-Host "  restart that agent/editor and try again." -ForegroundColor DarkGray
}

# ------------------------------------------------------------
# Non-interactive resolution
# ------------------------------------------------------------

function Resolve-SkillsFromParameters {
    param($Manifest)

    $available = @($Manifest.skills | Where-Object { $_.status -eq "available" })

    if ($AllSkills) {
        return $available
    }

    if ([string]::IsNullOrWhiteSpace($Skill)) {
        return Select-SkillsInteractive $Manifest
    }

    $ids = @($Skill -split ',' | ForEach-Object { $_.Trim() } | Where-Object { $_ })

    $selected = @()
    foreach ($id in $ids) {
        $match = $Manifest.skills | Where-Object { $_.id -eq $id } | Select-Object -First 1

        if (-not $match) {
            throw "Unknown skill '$id'."
        }
        if ($match.status -ne "available") {
            throw "Skill '$id' is not available yet."
        }

        $selected += $match
    }

    return $selected
}

function Resolve-PlatformsFromParameters {
    if ($AllPlatforms) {
        return @(Get-PlatformDefinitions)
    }

    if ([string]::IsNullOrWhiteSpace($Platform)) {
        return @(Select-PlatformsInteractive)
    }

    if ($Platform -eq "detected") {
        return @(Get-DetectedPlatforms)
    }

    $ids = @($Platform -split ',' | ForEach-Object { $_.Trim() } | Where-Object { $_ })
    $defs = @(Get-PlatformDefinitions)
    $selected = @()

    foreach ($id in $ids) {
        $match = $defs | Where-Object { $_.Id -eq $id } | Select-Object -First 1
        if (-not $match) {
            throw "Unknown platform '$id'."
        }
        $selected += $match
    }

    return $selected
}

# ------------------------------------------------------------
# Main
# ------------------------------------------------------------

$TempRoot = $null

try {
    Show-MillieBanner

    $manifest = Get-MillieManifest
    $skills = @(Resolve-SkillsFromParameters $manifest)

    if ($skills.Count -eq 0) {
        Write-Host ""
        Write-Host "  No skill selected. Goodbye." -ForegroundColor DarkGray
        return
    }

    $platforms = @(Resolve-PlatformsFromParameters)

    if ($platforms.Count -eq 0) {
        Write-Host ""
        Write-Host "  No platform selected. Goodbye." -ForegroundColor DarkGray
        return
    }

    Write-Section "CONFIRM"

    Write-Host "  Skills:" -ForegroundColor DarkGray
    foreach ($s in $skills) {
        Write-Host ("    • " + $s.name) -ForegroundColor White
    }

    Write-Host ""
    Write-Host "  Platforms:" -ForegroundColor DarkGray
    foreach ($p in $platforms) {
        Write-Host ("    • " + $p.Name + " -> " + $p.Path) -ForegroundColor White
    }

    if (-not $Force) {
        Write-Host ""
        $confirm = (Read-Host "  Continue? [Y/n]").Trim()
        if ($confirm -match '^[Nn]$') {
            Write-Host "  Cancelled." -ForegroundColor Yellow
            return
        }
    }

    $TempRoot = Join-Path ([IO.Path]::GetTempPath()) ("millie-" + [Guid]::NewGuid().ToString("N"))
    New-Item -ItemType Directory -Force -Path $TempRoot | Out-Null

    $repositoryRoot = Get-RepositoryArchive -TempRoot $TempRoot
    Install-Selections -Skills $skills -Platforms $platforms -RepositoryRoot $repositoryRoot

    Write-Host ""
    Write-Center "MILLIE IS READY." Green
    Write-Center "Open your agent and start building." Cyan
    Write-Host ""
}
catch {
    Write-Host ""
    Write-ErrorLine $_.Exception.Message
    Write-Host ""
    Write-Host "  Installer stopped without intentionally deleting existing skill backups." -ForegroundColor DarkGray
}
finally {
    if ($TempRoot -and (Test-Path $TempRoot)) {
        Remove-Item -Path $TempRoot -Recurse -Force -ErrorAction SilentlyContinue
    }
}
