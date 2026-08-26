param(
    [string]$Repository = "cassielxyz/millieskills",
    [string]$Branch = "main",
    [string]$ManifestPath = "millie-installer/skills.json",
    [string]$Skill,
    [string]$Platform,
    [switch]$AllSkills,
    [switch]$AllPlatforms,
    [switch]$Force,
    [switch]$NoBanner
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version 2.0

$Script:InstallerVersion = "0.2.0"
$Script:RegistryPath = Join-Path $HOME ".millie\installed.json"

function Get-TerminalWidth {
    $width = 80
    try {
        if ($Host.UI.RawUI.WindowSize.Width -gt 20) {
            $width = $Host.UI.RawUI.WindowSize.Width
        }
    } catch {}
    return $width
}

function Get-CenteredText {
    param([string]$Text)
    $width = Get-TerminalWidth
    $padding = [Math]::Max(0, [Math]::Floor(($width - $Text.Length) / 2))
    return ((" " * $padding) + $Text)
}

function Write-Center {
    param(
        [string]$Text,
        [ConsoleColor]$Color = [ConsoleColor]::White
    )
    Write-Host (Get-CenteredText $Text) -ForegroundColor $Color
}

function Test-AnsiColor {
    if (-not [string]::IsNullOrWhiteSpace($env:WT_SESSION)) { return $true }
    try {
        $prop = $Host.UI.PSObject.Properties["SupportsVirtualTerminal"]
        if ($null -ne $prop -and $Host.UI.SupportsVirtualTerminal) { return $true }
    } catch {}
    if ($env:TERM_PROGRAM -or $env:ConEmuANSI -eq "ON" -or $env:ANSICON) { return $true }
    return $false
}

function Get-GradientRgb {
    param([double]$Position)

    # Three-stop warm gradient:
    # RED #FF3B30 -> ORANGE #FF9500 -> YELLOW #FFD60A
    $red    = @(255, 59, 48)
    $orange = @(255, 149, 0)
    $yellow = @(255, 214, 10)

    if ($Position -le 0.5) {
        $local = $Position / 0.5
        $a = $red
        $b = $orange
    } else {
        $local = ($Position - 0.5) / 0.5
        $a = $orange
        $b = $yellow
    }

    return @(
        [int][Math]::Round($a[0] + (($b[0] - $a[0]) * $local)),
        [int][Math]::Round($a[1] + (($b[1] - $a[1]) * $local)),
        [int][Math]::Round($a[2] + (($b[2] - $a[2]) * $local))
    )
}

function Write-GradientText {
    param([string]$Text)

    $centered = Get-CenteredText $Text

    if (-not (Test-AnsiColor)) {
        $leading = $centered.Length - $centered.TrimStart().Length
        if ($leading -gt 0) { Write-Host (" " * $leading) -NoNewline }

        $visible = $centered.TrimStart()
        $n = $visible.Length
        $a = [Math]::Max(1, [Math]::Floor($n / 3))
        $b = [Math]::Min($n, $a * 2)

        Write-Host $visible.Substring(0, $a) -ForegroundColor Red -NoNewline
        Write-Host $visible.Substring($a, $b - $a) -ForegroundColor DarkYellow -NoNewline
        Write-Host $visible.Substring($b) -ForegroundColor Yellow
        return
    }

    $esc = [char]27
    $reset = "$esc[0m"
    $leadingSpaces = $centered.Length - $centered.TrimStart().Length

    if ($leadingSpaces -gt 0) {
        Write-Host (" " * $leadingSpaces) -NoNewline
    }

    $visible = $centered.TrimStart()
    $count = $visible.Length

    for ($i = 0; $i -lt $count; $i++) {
        $position = if ($count -le 1) { 1.0 } else { $i / ($count - 1.0) }
        $rgb = Get-GradientRgb -Position $position
        Write-Host "$esc[38;2;$($rgb[0]);$($rgb[1]);$($rgb[2])m$($visible[$i])" -NoNewline
    }

    Write-Host $reset
}

function Show-MillieBanner {
    if ($NoBanner) { return }
    try { Clear-Host } catch {}

    $banner = @(
        "███╗   ███╗██╗██╗     ██╗     ██╗███████╗",
        "████╗ ████║██║██║     ██║     ██║██╔════╝",
        "██╔████╔██║██║██║     ██║     ██║█████╗  ",
        "██║╚██╔╝██║██║██║     ██║     ██║██╔══╝  ",
        "██║ ╚═╝ ██║██║███████╗███████╗██║███████╗",
        "╚═╝     ╚═╝╚═╝╚══════╝╚══════╝╚═╝╚══════╝"
    )

    Write-Host ""
    foreach ($line in $banner) { Write-GradientText $line }
    Write-Host ""
    Write-Center "UNIVERSAL AGENT SKILLS INSTALLER" Yellow
    Write-Center "Build smarter agents. Keep the skill everywhere." DarkGray
    Write-Center "Installer v$($Script:InstallerVersion)" DarkGray
    Write-Host ""
}

function Write-Section {
    param([string]$Title)
    Write-Host ""
    Write-Host ("  " + ("─" * 70)) -ForegroundColor DarkGray
    Write-Host ("  " + $Title) -ForegroundColor DarkYellow
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

function Get-RawBaseUrl {
    return "https://raw.githubusercontent.com/$Repository/$Branch"
}

function Get-MillieManifest {
    $url = "$(Get-RawBaseUrl)/$ManifestPath"

    Write-Host "  Fetching Millie skill catalog..." -ForegroundColor DarkGray
    Write-Host "  $url" -ForegroundColor DarkGray

    try {
        $manifest = Invoke-RestMethod -Uri $url
        if ($null -eq $manifest) { throw "The manifest response was empty." }
        if (-not $manifest.skills) { throw "The manifest does not contain a skills array." }
        Write-Success "Skill catalog loaded."
        return $manifest
    }
    catch {
        Write-ErrorLine "Could not load the Millie skill catalog."
        Write-Host ""
        Write-Host "  Expected manifest:" -ForegroundColor DarkGray
        Write-Host "  $url" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "  Ensure millie-installer/skills.json exists on branch '$Branch'." -ForegroundColor DarkGray
        throw
    }
}

function Get-PlatformDefinitions {
    return @(
        [pscustomobject]@{
            Id="claude"; Name="Claude Code"; Path=(Join-Path $HOME ".claude\skills");
            Commands=@("claude"); Notes="Personal Claude Code skills."
        },
        [pscustomobject]@{
            Id="antigravity"; Name="Google Antigravity"; Path=(Join-Path $HOME ".gemini\config\skills");
            Commands=@("antigravity"); Notes="Global Antigravity IDE skills."
        },
        [pscustomobject]@{
            Id="antigravity-cli"; Name="Antigravity CLI"; Path=(Join-Path $HOME ".gemini\antigravity-cli\skills");
            Commands=@("agy"); Notes="Global Antigravity CLI skills."
        },
        [pscustomobject]@{
            Id="vscode"; Name="VS Code / GitHub Copilot"; Path=(Join-Path $HOME ".copilot\skills");
            Commands=@("code","copilot"); Notes="Personal VS Code / Copilot Agent Skills."
        },
        [pscustomobject]@{
            Id="cursor"; Name="Cursor"; Path=(Join-Path $HOME ".cursor\skills");
            Commands=@("cursor"); Notes="Personal Cursor skills."
        },
        [pscustomobject]@{
            Id="codex"; Name="OpenAI Codex"; Path=(Join-Path $HOME ".agents\skills");
            Commands=@("codex"); Notes="Personal Codex Agent Skills."
        },
        [pscustomobject]@{
            Id="gemini"; Name="Gemini CLI"; Path=(Join-Path $HOME ".gemini\skills");
            Commands=@("gemini"); Notes="Global Gemini CLI skills."
        }
    )
}

function Test-AnyCommand {
    param([string[]]$Names)
    foreach ($name in $Names) {
        if (Get-Command $name -ErrorAction SilentlyContinue) { return $true }
    }
    return $false
}

function Test-PlatformDetected {
    param($PlatformDefinition)
    if (Test-AnyCommand $PlatformDefinition.Commands) { return $true }
    $parent = Split-Path $PlatformDefinition.Path -Parent
    return (Test-Path $parent)
}

function Get-DetectedPlatforms {
    $found = @()
    foreach ($p in (Get-PlatformDefinitions)) {
        if (Test-PlatformDetected $p) { $found += $p }
    }
    return $found
}

function Select-SkillsInteractive {
    param($Manifest)

    Write-Section "SELECT SKILL"
    $skills = @($Manifest.skills)

    for ($i=0; $i -lt $skills.Count; $i++) {
        $s = $skills[$i]
        $number = $i + 1

        if ($s.status -eq "available") {
            Write-Host ("  [{0,2}] " -f $number) -ForegroundColor Yellow -NoNewline
            Write-Host $s.name -ForegroundColor White
            Write-Host ("       " + $s.short) -ForegroundColor DarkGray
        } else {
            Write-Host ("  [{0,2}] " -f $number) -ForegroundColor DarkGray -NoNewline
            Write-Host $s.name -ForegroundColor DarkGray -NoNewline
            Write-Host "  [COMING SOON]" -ForegroundColor DarkYellow
        }
        Write-Host ""
    }

    Write-Host "  [ A] Install ALL available skills" -ForegroundColor Green
    Write-Host "  [ Q] Quit" -ForegroundColor DarkGray
    Write-Host ""

    while ($true) {
        $choice = (Read-Host "  Choose a skill").Trim()

        if ($choice -match '^[Qq]$') { return @() }
        if ($choice -match '^[Aa]$') {
            return @($skills | Where-Object { $_.status -eq "available" })
        }

        $number = 0
        if ([int]::TryParse($choice, [ref]$number)) {
            if ($number -ge 1 -and $number -le $skills.Count) {
                $selected = $skills[$number-1]
                if ($selected.status -ne "available") {
                    Write-WarningLine "$($selected.name) is coming soon."
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

    for ($i=0; $i -lt $platforms.Count; $i++) {
        $p = $platforms[$i]
        $detected = Test-PlatformDetected $p

        Write-Host ("  [{0,2}] " -f ($i+1)) -ForegroundColor Yellow -NoNewline
        Write-Host $p.Name -ForegroundColor White -NoNewline

        if ($detected) { Write-Host "  [DETECTED]" -ForegroundColor Green }
        else { Write-Host "" }

        Write-Host ("       " + $p.Path) -ForegroundColor DarkGray
        Write-Host ""
    }

    Write-Host "  [ D] Auto-detect installed platforms" -ForegroundColor DarkYellow
    Write-Host "  [ A] Install to ALL supported platforms" -ForegroundColor Green
    Write-Host "  [ Q] Quit" -ForegroundColor DarkGray
    Write-Host ""

    while ($true) {
        $choice = (Read-Host "  Choose a platform").Trim()

        if ($choice -match '^[Qq]$') { return @() }
        if ($choice -match '^[Aa]$') { return $platforms }

        if ($choice -match '^[Dd]$') {
            $detected = @(Get-DetectedPlatforms)
            if ($detected.Count -eq 0) {
                Write-WarningLine "No supported platform could be confidently detected."
                Write-Host "  Choose a platform manually." -ForegroundColor DarkGray
                continue
            }
            Write-Success ("Detected: " + (($detected | ForEach-Object {$_.Name}) -join ", "))
            return $detected
        }

        $number = 0
        if ([int]::TryParse($choice, [ref]$number)) {
            if ($number -ge 1 -and $number -le $platforms.Count) {
                return @($platforms[$number-1])
            }
        }

        Write-WarningLine "Invalid selection."
    }
}

function Download-RepositoryArchive {
    param([string]$TempRoot)

    $zipPath = Join-Path $TempRoot "millieskills.zip"
    $extractPath = Join-Path $TempRoot "repository"
    $url = "https://codeload.github.com/$Repository/zip/refs/heads/$Branch"

    Write-Section "DOWNLOAD"
    Write-Host "  Repository : " -ForegroundColor DarkGray -NoNewline
    Write-Host $Repository -ForegroundColor White
    Write-Host "  Branch     : " -ForegroundColor DarkGray -NoNewline
    Write-Host $Branch -ForegroundColor White
    Write-Host ""
    Write-Host "  Downloading repository archive..." -ForegroundColor DarkYellow

    Invoke-WebRequest -Uri $url -OutFile $zipPath

    Write-Host "  Extracting repository..." -ForegroundColor DarkYellow
    New-Item -ItemType Directory -Force -Path $extractPath | Out-Null
    Expand-Archive -Path $zipPath -DestinationPath $extractPath -Force

    $repoRoot = Get-ChildItem -Path $extractPath -Directory | Select-Object -First 1
    if ($null -eq $repoRoot) { throw "Could not locate extracted repository root." }

    Write-Success "Repository downloaded."
    return $repoRoot.FullName
}

function Get-Registry {
    if (-not (Test-Path $Script:RegistryPath)) {
        return [pscustomobject]@{ schema_version=1; installations=@() }
    }

    try {
        $registry = Get-Content $Script:RegistryPath -Raw | ConvertFrom-Json
        if ($null -eq $registry.installations) {
            $registry | Add-Member -NotePropertyName installations -NotePropertyValue @()
        }
        return $registry
    }
    catch {
        Write-WarningLine "Existing Millie registry is invalid. Rebuilding it."
        return [pscustomobject]@{ schema_version=1; installations=@() }
    }
}

function Save-Registry {
    param($Registry)
    $dir = Split-Path $Script:RegistryPath -Parent
    New-Item -ItemType Directory -Force -Path $dir | Out-Null
    $Registry | ConvertTo-Json -Depth 10 | Set-Content -Path $Script:RegistryPath -Encoding UTF8
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
        skill=$SkillId
        skill_name=$SkillName
        platform=$PlatformId
        platform_name=$PlatformName
        path=$Destination
        repository=$Repository
        branch=$Branch
        installed_at=(Get-Date).ToString("o")
        installer_version=$Script:InstallerVersion
    }

    $registry.installations = $items
    Save-Registry $registry
}

function Confirm-ExistingInstallation {
    param([string]$SkillName,[string]$Destination)

    if ($Force) { return "replace" }

    Write-WarningLine "$SkillName is already installed:"
    Write-Host "       $Destination" -ForegroundColor DarkGray
    Write-Host ""
    Write-Host "       [R] Replace / update" -ForegroundColor Yellow
    Write-Host "       [B] Backup existing, then update" -ForegroundColor DarkYellow
    Write-Host "       [S] Skip" -ForegroundColor DarkGray

    while ($true) {
        $answer = (Read-Host "       Choice").Trim().ToLowerInvariant()
        switch ($answer) {
            "r" { return "replace" }
            "b" { return "backup" }
            "s" { return "skip" }
            default { Write-WarningLine "Choose R, B, or S." }
        }
    }
}

function Install-OneSkill {
    param($SkillDefinition,$PlatformDefinition,[string]$RepositoryRoot)

    $relativeSource = $SkillDefinition.path -replace '/', [IO.Path]::DirectorySeparatorChar
    $source = Join-Path $RepositoryRoot $relativeSource
    $skillFile = Join-Path $source "SKILL.md"

    if (-not (Test-Path $source)) {
        Write-ErrorLine "Skill source folder not found:"
        Write-Host "       $source" -ForegroundColor DarkGray
        return $false
    }

    if (-not (Test-Path $skillFile)) {
        Write-ErrorLine "$($SkillDefinition.name) does not contain SKILL.md."
        Write-Host "       $skillFile" -ForegroundColor DarkGray
        return $false
    }

    $platformRoot = $PlatformDefinition.Path
    New-Item -ItemType Directory -Force -Path $platformRoot | Out-Null
    $destination = Join-Path $platformRoot $SkillDefinition.id

    if (Test-Path $destination) {
        $action = Confirm-ExistingInstallation -SkillName $SkillDefinition.name -Destination $destination

        if ($action -eq "skip") {
            Write-WarningLine "Skipped $($SkillDefinition.name) for $($PlatformDefinition.Name)."
            return $true
        }

        if ($action -eq "backup") {
            $stamp = Get-Date -Format "yyyyMMdd-HHmmss"
            $backup = "$destination.__backup_$stamp"
            Move-Item -Path $destination -Destination $backup
            Write-Success "Backed up previous install:"
            Write-Host "       $backup" -ForegroundColor DarkGray
        }

        if ($action -eq "replace") {
            Remove-Item -Path $destination -Recurse -Force
        }
    }

    Copy-Item -Path $source -Destination $destination -Recurse -Force

    if (-not (Test-Path (Join-Path $destination "SKILL.md"))) {
        Write-ErrorLine "Installation verification failed."
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
    param([array]$Skills,[array]$Platforms,[string]$RepositoryRoot)

    Write-Section "INSTALL"
    $successCount = 0
    $failureCount = 0

    foreach ($platform in $Platforms) {
        Write-Host ""
        Write-Host ("  " + $platform.Name) -ForegroundColor Yellow
        Write-Host ("  " + $platform.Notes) -ForegroundColor DarkGray

        foreach ($skill in $Skills) {
            try {
                if (Install-OneSkill -SkillDefinition $skill -PlatformDefinition $platform -RepositoryRoot $RepositoryRoot) {
                    $successCount++
                } else {
                    $failureCount++
                }
            }
            catch {
                $failureCount++
                Write-ErrorLine "$($skill.name) -> $($platform.Name): $($_.Exception.Message)"
            }
        }
    }

    Write-Section "RESULT"
    Write-Success "$successCount installation(s) completed."
    if ($failureCount -gt 0) { Write-ErrorLine "$failureCount installation(s) failed." }

    Write-Host ""
    Write-Host "  Registry:" -ForegroundColor DarkGray
    Write-Host "  $Script:RegistryPath" -ForegroundColor DarkGray
    Write-Host ""
    Write-Host "  Restart an already-open editor/agent if it does not discover the new skill immediately." -ForegroundColor DarkGray
}

function Resolve-Skills {
    param($Manifest)

    if ($AllSkills) {
        return @($Manifest.skills | Where-Object {$_.status -eq "available"})
    }

    if ([string]::IsNullOrWhiteSpace($Skill)) {
        return @(Select-SkillsInteractive $Manifest)
    }

    $selected = @()
    foreach ($id in @($Skill -split ',' | ForEach-Object {$_.Trim()} | Where-Object {$_})) {
        $match = $Manifest.skills | Where-Object {$_.id -eq $id} | Select-Object -First 1
        if ($null -eq $match) { throw "Unknown skill '$id'." }
        if ($match.status -ne "available") { throw "Skill '$id' is not available yet." }
        $selected += $match
    }

    return $selected
}

function Resolve-Platforms {
    if ($AllPlatforms) { return @(Get-PlatformDefinitions) }
    if ([string]::IsNullOrWhiteSpace($Platform)) { return @(Select-PlatformsInteractive) }
    if ($Platform -eq "detected") { return @(Get-DetectedPlatforms) }

    $defs = @(Get-PlatformDefinitions)
    $selected = @()

    foreach ($id in @($Platform -split ',' | ForEach-Object {$_.Trim()} | Where-Object {$_})) {
        $match = $defs | Where-Object {$_.Id -eq $id} | Select-Object -First 1
        if ($null -eq $match) { throw "Unknown platform '$id'." }
        $selected += $match
    }

    return $selected
}

$tempRoot = $null

try {
    Show-MillieBanner

    $manifest = Get-MillieManifest
    $skills = @(Resolve-Skills $manifest)

    if ($skills.Count -eq 0) {
        Write-Host ""
        Write-Host "  No skill selected. Goodbye." -ForegroundColor DarkGray
        return
    }

    $platforms = @(Resolve-Platforms)

    if ($platforms.Count -eq 0) {
        Write-Host ""
        Write-Host "  No platform selected. Goodbye." -ForegroundColor DarkGray
        return
    }

    Write-Section "CONFIRM"

    Write-Host "  Skills:" -ForegroundColor DarkGray
    foreach ($s in $skills) { Write-Host ("    - " + $s.name) -ForegroundColor White }

    Write-Host ""
    Write-Host "  Platforms:" -ForegroundColor DarkGray
    foreach ($p in $platforms) { Write-Host ("    - " + $p.Name + " -> " + $p.Path) -ForegroundColor White }

    if (-not $Force) {
        Write-Host ""
        $confirmation = (Read-Host "  Continue? [Y/n]").Trim()
        if ($confirmation -match '^[Nn]$') {
            Write-Host "  Cancelled." -ForegroundColor Yellow
            return
        }
    }

    $tempRoot = Join-Path ([IO.Path]::GetTempPath()) ("millie-" + [Guid]::NewGuid().ToString("N"))
    New-Item -ItemType Directory -Force -Path $tempRoot | Out-Null

    $repositoryRoot = Download-RepositoryArchive -TempRoot $tempRoot
    Install-Selections -Skills $skills -Platforms $platforms -RepositoryRoot $repositoryRoot

    Write-Host ""
    Write-GradientText "MILLIE IS READY"
    Write-Center "Open your AI coding agent and start building." Yellow
    Write-Host ""
}
catch {
    Write-Host ""
    Write-ErrorLine $_.Exception.Message
    Write-Host ""
    Write-Host "  Installer stopped safely." -ForegroundColor DarkGray
}
finally {
    if ($null -ne $tempRoot -and (Test-Path $tempRoot)) {
        Remove-Item -Path $tempRoot -Recurse -Force -ErrorAction SilentlyContinue
    }
}
