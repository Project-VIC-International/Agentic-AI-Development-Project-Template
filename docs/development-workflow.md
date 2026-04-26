# Development Workflow

This template encourages small, reviewable steps.

## Standard Loop

1. Choose one issue.
2. Ask Cursor to inspect the relevant files and propose a plan. Significant changes must go through `docs/spec-kit-workflow.md`.
3. Review the plan.
4. Let Cursor implement the change.
5. Test locally with synthetic data.
6. Ask Cursor to fix clear failures.
7. Use Karpathy's autoresearch to improve areas of the application with measured performance criteria. Create a measurement benchmark, then let autoresearch ratchet the performance up using the scientific method.
8. Commit the working change.
9. Push to GitHub.
10. Check GitHub Actions if configured.
11. Repeat.

## Beginner Rule

If you do not understand a command, ask Cursor:

```text
Explain this command in plain language before I run it. Tell me what files, settings, or remote services it may change.
```

## Commits

Commit when a small unit of work is complete and tested.

Good commit messages explain why the change matters:

```text
Add intake template for milestone planning
```

Avoid committing credentials, datasets, generated artifacts, or unrelated experiments.

## Releases

Use releases when a milestone is complete enough that another person could install, test, or use the project.

For this template, the default milestone path is:

- `v0.1.0`: first working project skeleton.
- `v0.2.0` through `v0.9.0`: incremental capabilities and hardening.
- `v1.0.0`: first major release that satisfies the original mission goal.

The user may choose a different milestone plan after reviewing the intake.

## See Also

- `QUICKSTART.md` for the first-session setup path.
- `docs/spec-kit-workflow.md` for specification, planning, tasks, implementation, and analysis.
- `docs/github-setup.md` for GitHub CLI and repository setup.
- `docs/synthetic-test-data.md` for safe test data guidance.

