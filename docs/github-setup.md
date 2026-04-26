# GitHub Setup

GitHub is where your project repository, milestones, issues, pull requests, and releases live.

## Create a Private Repository

For most student and mission-support projects, create a new private repository under your own GitHub account.

1. Sign in to GitHub.
2. Select **New repository**.
3. Choose a short project name.
4. Select **Private**.
5. Do not add a README if you are pushing this template as the starting point.

## Install GitHub CLI

GitHub CLI lets you and your Cursor agent work with GitHub from the terminal.

Check whether it is installed:

```bash
gh --version
```

If it is not installed, follow the official instructions for your operating system: <https://cli.github.com/>

## Authenticate GitHub CLI

Run:

```bash
gh auth login
```

Recommended beginner choices:

- GitHub.com
- HTTPS
- Authenticate with your browser
- Allow GitHub CLI to manage Git credentials

Check your status:

```bash
gh auth status
```

## Connect This Template to Your Repository

After creating a private GitHub repository, connect this local project:

```bash
git remote add origin https://github.com/YOUR-ACCOUNT/YOUR-REPO.git
git branch -M main
git push -u origin main
```

Ask Cursor to explain the commands if you are unsure.

## Development Loop

Use this general process:

1. Develop a small change.
2. Test it locally with synthetic data.
3. Commit the change.
4. Push to GitHub.
5. Let GitHub Actions run if a workflow exists.
6. Fix failures.
7. Test again.
8. Release when the milestone is complete.

## GitHub Actions Cost Guidance

Private repositories on free GitHub accounts have limits. Ask the agent to plan minimal workflows based on your actual requirements.

Avoid unnecessary scheduled jobs, large artifacts, long-running workflows, large dependency caches, and Git LFS unless you understand the cost and storage implications.

