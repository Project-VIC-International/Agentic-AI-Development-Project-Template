# Cursor Setup

The instructor uses Cursor in the workshop, so this page has Cursor-specific tips. The template works with any AI coding agent; see `docs/agent-setup.md` for the others.

Cursor reads two things from this repository automatically:

- `.cursor/rules/*.mdc`: one rule per policy, generated from `policies/` by `scripts/sync_agent_rules.py`. Core policies are always on; the others attach when you work on matching files or when the agent decides they are relevant. Do not edit these files directly; edit `policies/` and re-run the script.
- `AGENTS.md`: the shared instructions for every agent.

## Open the Repository

1. Clone your private GitHub repository.
2. Open the folder in Cursor.
3. Read `README.md`, `QUICKSTART.md`, and `SECURITY.md`.
4. Paste `prompts/START-AGENT-HERE.md` into the Agent chat and let Cursor explain the repository before making changes.

## Recommended First Prompt

```text
Read AGENTS.md, the core policies it lists in policies/, README.md, QUICKSTART.md, SECURITY.md, and the files in docs/. Then explain how I should use this template for my project. Do not make changes yet.
```

## Cursor Settings Worth Checking

- **Rules:** open Cursor Settings and look at the Rules section to confirm the project rules from `.cursor/rules/` are listed.
- **Command approval:** keep terminal commands set to ask for approval. Do not turn on auto-run for commands during the course.
- **Privacy:** turn on Privacy Mode if your agency requires that prompts and code are not stored or used for training.
- **MCP servers:** review each MCP server before enabling it (`policies/mcp-agent-safety.md`).
- **Spec Kit:** after the intake is complete, run `specify init --here --integration cursor-agent` in the terminal, then reload Cursor so the Spec Kit commands appear when you type `/speckit` in chat.

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

