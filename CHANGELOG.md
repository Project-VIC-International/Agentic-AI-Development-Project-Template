# Changelog

This project follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and semantic versioning once development begins.

## [Unreleased]

Use this section to record user-facing changes as the project evolves. Move entries into a versioned section when a release is tagged.

### Added

- `START-HERE.md` entry point and `prompts/START-AGENT-HERE.md` bootstrap prompt for any AI coding agent.
- Course integration guide, beginner student-mode policy, student lab issue template, and NCCC mini-project example.
- Optional GitHub Codespaces/devcontainer configuration for conference and classroom setup.
- Agent-neutral development policies in `policies/` (25 policies adapted from the Project VIC International development policy corpus), covering human review, privacy and tiered test data, data contracts, persistence, dependencies and supply chain, MCP and agent safety, model governance, observability, testing, documentation, and rule authoring in addition to the earlier rule set.
- `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, and `.github/copilot-instructions.md` so Cursor, Claude Code, Codex, GitHub Copilot, Gemini CLI, OpenCode, Zed, Warp, and other agents load the same policies.
- `scripts/sync_agent_rules.py` (standard-library Python) to regenerate `.cursor/rules/` and the agent file policy sections from `policies/`, with a `--check` mode.
- `docs/agent-setup.md`, `docs/test-data-handling.md`, `docs/manual-test-checklist.md`, `docs/templates/` (test data handling plan and release test annex), and `.github/pull_request_template.md`.
- `.gitignore` entries for local-only test data (`demo-data/local/`, `testdata/local/`).

### Changed

- Elevated the student golden path in `README.md`, `QUICKSTART.md`, and agent guidance so the template is clearly the primary hands-on workspace.
- Renamed `prompts/cursor-prompts.md` to `prompts/agent-prompts.md` and replaced Cursor-only instructions with agent-neutral wording throughout the docs.
- `.cursor/rules/` is now generated from `policies/`; edit the policies, not the `.mdc` files.
- Security guidance is now jurisdiction-aware: agents ask which country's and agency's rules apply instead of assuming one framework.
- Spec Kit guidance updated for current Spec Kit (`specify init --integration`, per-agent command spelling, and the `converge` step).

### Removed

- Organization-specific brand references from the visible-surface policy; projects now use the design system their own organization designates.
- `release-management` and `specify-rules` Cursor rules, replaced by `policies/versioning-release-management.md` and `policies/project-context.md`.

## [v0.1.0] - 2026-04-25

### Added

- Initial Project VIC Agentic AI Development project template.
- Beginner quickstart, GitHub/Cursor setup guidance, permissions troubleshooting, and development workflow documentation.
- Project intake, milestone planning, release roadmap, GitHub issue, and Cursor prompt templates.
- Project VIC Cursor rules for spec-kit, four-interface architecture, security, CASE/UCO/CAC alignment, no-stubs implementation, cross-platform support, release management, and autoresearch.
- Optional setup scripts for Ubuntu 24.04, macOS, and Windows 11.
- Synthetic CASE/UCO/CAC-style JSONC teaching example.
- Security guidance for synthetic data and sensitive mission-data boundaries.


