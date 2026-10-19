# Changelog

This project follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and semantic versioning once development begins.

## [Unreleased]

Use this section to record user-facing changes as the project evolves. Move entries into a versioned section when a release is tagged.

### Added

- Conference-focused `START-HERE.md` entry point and `prompts/START-CURSOR-HERE.md` bootstrap prompt.
- Course integration guide, beginner `student-mode` Cursor rule, student lab issue template, and NCCC mini-project example.
- Optional GitHub Codespaces/devcontainer configuration for conference and classroom setup.

### Changed

- Replaced the local Cursor rules with mandatory policy corpus `0.1.0` at commit `57bfea65f7f97769446d62a3b7cc07ead09d2649`, and installed the Cursor, Claude Code, GitHub Copilot, Gemini CLI, Hermes, OpenCode, Zed, Codex, and Warp adapters.
- Removed `.cursor/rules/student-mode.mdc` because it is not part of the mandatory corpus.
- Replaced the NCCC-specific start guide with `START-HERE.md` for a general conference or workshop audience.
- Elevated the student golden path in `README.md`, `QUICKSTART.md`, and agent guidance so the template is clearly the primary hands-on workspace.

## [v0.1.0] - 2026-04-25

### Added

- Initial Project VIC Agentic AI Development project template.
- Beginner quickstart, GitHub/Cursor setup guidance, permissions troubleshooting, and development workflow documentation.
- Project intake, milestone planning, release roadmap, GitHub issue, and Cursor prompt templates.
- Project VIC Cursor rules for spec-kit, four-interface architecture, security, CASE/UCO/CAC alignment, no-stubs implementation, cross-platform support, release management, and autoresearch.
- Optional setup scripts for Ubuntu 24.04, macOS, and Windows 11.
- Synthetic CASE/UCO/CAC-style JSONC teaching example.
- Security guidance for synthetic data and sensitive mission-data boundaries.


