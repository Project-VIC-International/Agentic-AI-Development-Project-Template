Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$ProjectRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$VenvDir = Join-Path $ProjectRoot ".venv"
$ToolsDir = Join-Path $ProjectRoot "tools"

function Ask-YesNo {
    param(
        [Parameter(Mandatory = $true)][string]$Prompt,
        [ValidateSet("y", "n")][string]$Default = "n"
    )

    if ($Default -eq "y") {
        $answer = Read-Host "$Prompt [Y/n]"
        if ([string]::IsNullOrWhiteSpace($answer)) { $answer = "y" }
    } else {
        $answer = Read-Host "$Prompt [y/N]"
        if ([string]::IsNullOrWhiteSpace($answer)) { $answer = "n" }
    }

    return $answer -match "^[Yy]$"
}

Write-Host "Project VIC Agentic AI Development Template setup for Windows 11"
Write-Host "Project root: $ProjectRoot"
Write-Host ""
Write-Host "Default behavior: install Python tools into a local virtual environment at $VenvDir."
Write-Host ""

if (-not (Get-Command py -ErrorAction SilentlyContinue) -and -not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python was not found. Install Python 3.11+ before continuing."
    Write-Host "Recommended beginner option: install Python from https://www.python.org/downloads/windows/"
    exit 1
}

if (Ask-YesNo "Install recommended tools with winget if available?" "n") {
    if (Get-Command winget -ErrorAction SilentlyContinue) {
        winget install --id Git.Git -e
        winget install --id GitHub.cli -e
        winget install --id Python.Python.3.12 -e
    } else {
        Write-Host "winget was not found. Install Git, GitHub CLI, and Python manually."
    }
}

if (-not (Test-Path $VenvDir)) {
    if (Get-Command py -ErrorAction SilentlyContinue) {
        py -3 -m venv $VenvDir
    } else {
        python -m venv $VenvDir
    }
}

$Python = Join-Path $VenvDir "Scripts\python.exe"
& $Python -m pip install --upgrade pip

if (Ask-YesNo "Install uv into the local virtual environment?" "y") {
    & $Python -m pip install --upgrade uv
}

New-Item -ItemType Directory -Force -Path $ToolsDir | Out-Null

if (Ask-YesNo "Install GitHub spec-kit into the local virtual environment?" "y") {
    & $Python -m pip install "git+https://github.com/github/spec-kit.git"
    Write-Host "Verify with: .\.venv\Scripts\specify.exe version"
}

if (Ask-YesNo "Clone Karpathy AutoResearch into tools\autoresearch? This is optional and GPU-oriented." "n") {
    $AutoResearchDir = Join-Path $ToolsDir "autoresearch"
    if (-not (Test-Path $AutoResearchDir)) {
        git clone https://github.com/karpathy/autoresearch.git $AutoResearchDir
    } else {
        Write-Host "tools\autoresearch already exists; skipping clone."
    }
}

if (Ask-YesNo "Install CASE/UCO SDK Python package into the local virtual environment?" "y") {
    try {
        & $Python -m pip install --upgrade case-uco
    } catch {
        Write-Host "case-uco package install failed. You can still clone the SDK repository in the next step."
    }
}

if (Ask-YesNo "Clone CASE-UCO-SDK into tools\CASE-UCO-SDK for SDK and MCP server files?" "y") {
    $CaseSdkDir = Join-Path $ToolsDir "CASE-UCO-SDK"
    if (-not (Test-Path $CaseSdkDir)) {
        git clone https://github.com/vulnmaster/CASE-UCO-SDK.git $CaseSdkDir
    } else {
        Write-Host "tools\CASE-UCO-SDK already exists; skipping clone."
    }
}

if (Get-Command gh -ErrorAction SilentlyContinue) {
    gh --version
} else {
    Write-Host "GitHub CLI was not found. See docs/github-setup.md or https://cli.github.com/."
}

Write-Host ""
Write-Host "Setup complete."
Write-Host "Activate the local Python environment with:"
Write-Host ".\.venv\Scripts\Activate.ps1"

