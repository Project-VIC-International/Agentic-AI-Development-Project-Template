# Changelog

This project follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and semantic versioning once development begins.

## [Unreleased]

Use this section to record user-facing changes as the project evolves. Move entries into a versioned section when a release is tagged.

## [v0.2.0] - 2026-10-19

### Added

- Conference and workshop start path in `START-HERE.md`, with the first-agent prompt in `prompts/START-CURSOR-HERE.md`.
- Course integration guide, student lab issue template, and NCCC mini-project example.
- Optional GitHub Codespaces and devcontainer configuration for conference and classroom setup.
- Pinned Project VIC mandatory policy corpus `0.1.0` at commit `57bfea65f7f97769446d62a3b7cc07ead09d2649`, installed for Cursor, Claude Code, GitHub Copilot, Gemini CLI, Hermes, OpenCode, Zed, Codex, and Warp. The pin record is `docs/mandatory-policy-corpus.md`.

### Changed

- Replaced the template's local Cursor rules with the mandatory policy corpus.
- Elevated the student golden path in `README.md`, `QUICKSTART.md`, and agent guidance so the template is clearly the primary hands-on workspace.

### Removed

- `START-HERE-NCCC.md`. Use `START-HERE.md` for conference, workshop, classroom, and follow-up work.
- `.cursor/rules/student-mode.mdc`, because it is not part of the mandatory policy corpus.

## [v0.1.0] - 2026-04-25

### Added

- Initial Project VIC Agentic AI Development project template.
- Beginner quickstart, GitHub/Cursor setup guidance, permissions troubleshooting, and development workflow documentation.
- Project intake, milestone planning, release roadmap, GitHub issue, and Cursor prompt templates.
- Project VIC Cursor rules for spec-kit, four-interface architecture, security, CASE/UCO/CAC alignment, no-stubs implementation, cross-platform support, release management, and autoresearch.
- Optional setup scripts for Ubuntu 24.04, macOS, and Windows 11.
- Synthetic CASE/UCO/CAC-style JSONC teaching example.
- Security guidance for synthetic data and sensitive mission-data boundaries.


