# Tooling Setup

The setup scripts are helpers, not magic. Read them before running them, and ask Cursor to explain any command you do not understand.

## Supported Starter Environments

- Ubuntu 24.04: `scripts/setup-ubuntu-24.04.sh`
- macOS: `scripts/setup-macos.sh`
- Windows 11: `scripts/setup-windows-11.ps1`

## Default Install Location

The lowest-risk default is a local Python virtual environment:

```text
.venv/
```

This keeps Python tools inside the project instead of installing them globally. The setup scripts ask before installing system packages, cloning repositories, or installing optional tools.

## Optional Tools

The scripts can help install or clone:

- GitHub spec-kit from `https://github.com/github/spec-kit.git`.
- Karpathy AutoResearch from `https://github.com/karpathy/autoresearch.git`.
- CASE/UCO SDK from `https://github.com/vulnmaster/CASE-UCO-SDK.git`.
- GitHub CLI guidance for repository, issue, milestone, and release work.

AutoResearch is GPU-oriented and may not be useful on every student machine. It is optional.

## After Setup

Activate the environment:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Then continue with `intake/problem-intake.md` and `prompts/cursor-prompts.md`.

