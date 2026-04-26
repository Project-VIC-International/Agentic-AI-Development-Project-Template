# Permissions Troubleshooting

Use this guide when Cursor, Git, or GitHub CLI cannot access your repository.

## Check GitHub CLI

```bash
gh auth status
```

If you are not logged in:

```bash
gh auth login
```

If you are logged in as the wrong account:

```bash
gh auth logout
gh auth login
```

## Check Git Remotes

```bash
git remote -v
```

The `origin` remote should point to your GitHub repository.

If it points to the wrong repository, ask Cursor to help you update it. Do not guess if you are unfamiliar with Git.

## Check Repository Access

```bash
gh repo view
```

If this fails, common causes are:

- You are in the wrong folder.
- The repository has not been created on GitHub.
- You are signed in to the wrong GitHub account.
- Your account does not have permission.

## Check Push Access

```bash
git status
git push
```

If push fails:

- Read the error message carefully.
- Confirm the branch name is correct.
- Confirm you have write access.
- Confirm your authentication method is still valid.

## When to Ask for Help

Ask for help before deleting remotes, force-pushing, resetting branches, changing repository visibility, or changing organization permissions.

