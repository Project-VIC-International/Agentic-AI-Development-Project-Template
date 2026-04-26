# Cursor Setup

Cursor is the agentic AI development environment used with this template. If you give this template repository to Claude Code, OpenCode, Google Antigravity or other future agentic AI development tool it can adapt what it needs from this repository.

## Open the Repository

1. Clone your private GitHub repository.
2. Open the folder in Cursor.
3. Read `README.md`, `QUICKSTART.md`, and `SECURITY.md`.
4. Ask Cursor to explain the repository structure before making changes.

## Recommended First Prompt

```text
Read README.md, QUICKSTART.md, SECURITY.md, the files in docs/, and the rules in .cursor/rules/. Then explain how I should use this template for my project. Do not make changes yet.
```

## GitHub Permissions

Cursor and its terminal can use the same GitHub credentials that you configure with GitHub CLI.

Check access:

```bash
gh auth status
git remote -v
git status
```

If `gh auth status` fails, run:

```bash
gh auth login
```

If `git push` fails, confirm:

- You are signed in to the correct GitHub account.
- The repository exists.
- The repository is private if required.
- Your account has write access.
- The `origin` remote points to the correct repository.

For more detailed help, see `docs/permissions-troubleshooting.md`.

## Agent Permissions

Before allowing the agent to create milestones, issues, workflows, or releases:

1. Ask it to show the plan.
2. Review the plan.
3. Edit anything that is wrong.
4. Explicitly approve the action.

Do not allow an agent to upload sensitive data, create broad access tokens, disable security controls, or make a repository public unless you fully understand and approve the change.

