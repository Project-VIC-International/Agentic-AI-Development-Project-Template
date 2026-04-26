# Quickstart

Use this guide when you have just cloned this template into Cursor and want to begin a new Project VIC style agentic AI development project.

## 0. Read the Safety Rules

Before creating issues, writing specs, or running setup scripts, read `SECURITY.md` and the "Important Safety Rules" section in `README.md`.

Use synthetic data only while building and testing. Do not put real case data, CSAM, suspected CSAM, credentials, agency-private information, or sensitive operational details into prompts, repositories, issues, logs, screenshots, or fixtures.

## 1. Create Your Own GitHub Repository

Create a new private GitHub repository under your own account or organization. Keep it private unless you have explicit approval to make the work public.

You can create the repository in the GitHub website, or you can install and use GitHub CLI as described in `docs/github-setup.md`.

After creating the repository, connect this local template to it:

```bash
git remote add origin https://github.com/YOUR-ACCOUNT/YOUR-REPO.git
git branch -M main
git push -u origin main
```

If you are not sure whether this is safe to run, ask Cursor to explain each command before running it.

## 2. Install Tools

If you are using Ubuntu 24.04, start with:

```bash
bash scripts/setup-ubuntu-24.04.sh
```

For macOS or Windows 11, see:

- `scripts/setup-macos.sh`
- `scripts/setup-windows-11.ps1`

The setup scripts should ask before installing tools. When there is a choice, prefer the lowest-risk local option, such as a Python virtual environment inside the project. See `docs/tooling-setup.md` for more detail.

## 3. Complete the Intake Form

Copy or edit `intake/problem-intake.md`. Use `docs/synthetic-test-data.md` and `docs/case-uco-cac-guidance.md` while answering. Describe:

- The mission problem you are trying to solve.
- How you think the solution should work.
- Constraints, approvals, timeline, and expected users.
- What synthetic data can safely represent your mission data.
- Whether CASE, UCO, or CAC Ontology concepts are relevant.

## 4. Ask Cursor to Plan

Use the prompts in `prompts/cursor-prompts.md`. The usual path is:

1. Ask Cursor to review the intake form.
2. Ask Cursor to create a milestone plan from `v0.1.0` through `v1.0.0`.
3. Save the reviewed plan as a project-specific planning file, such as `planning/my-milestone-plan.md`.
4. Ask Cursor to create GitHub milestones and issues only after you approve the plan.

## 5. Use the Spec-Kit Flow

Use the opinionated spec-kit flow:

1. Specify the behavior.
2. Plan the technical approach.
3. Break work into tasks.
4. Implement one task at a time.
5. Analyze consistency across the spec, plan, tasks, code, tests, and docs.
6. Test and give feedback.

Use `docs/spec-kit-workflow.md` for more detail. Testing and feedback are crucial. The agent will not know whether it solved your mission problem unless you test the result and explain what is right or wrong.

## 6. Develop, Test, Commit, Push

Use this loop:

1. Develop a small change.
2. Test it locally with synthetic data.
3. Commit the change.
4. Push to GitHub.
5. Run GitHub Actions if configured.
6. Fix failures.
7. Test again.
8. Release when the milestone is complete.

See `docs/development-workflow.md` for the day-to-day loop. Keep GitHub Actions small and inexpensive. Free private repositories have limits for Actions minutes, storage, artifacts, and related features.

