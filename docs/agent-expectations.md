# Agent Expectations

This template includes Cursor rules in `.cursor/rules/`. Those rules are the persistent guidance that the user's agent should follow while turning the intake form into specs, milestones, issues, code, tests, docs, and releases.

Ask the agent to summarize these rules before starting a real project:

```text
Read .cursor/rules/ and explain the development expectations in plain language. Focus on how they affect planning, GitHub issues, spec-kit, security, synthetic data, CASE/UCO/CAC alignment, and releases.
```

## Key Rule Areas

- Beginner workflow and safer pacing: `.cursor/rules/student-mode.mdc`.
- Spec-kit first: `.cursor/rules/speckit-workflow.mdc`.
- Four data interfaces: `.cursor/rules/four-surface-review.mdc`.
- CASE/UCO/CAC alignment: `.cursor/rules/ontology-alignment.mdc`.
- Security defaults: `.cursor/rules/security-compliance.mdc`.
- No stubs: `.cursor/rules/no-stubs.mdc`.
- Cross-platform support: `.cursor/rules/cross-platform.mdc`.
- Release discipline: `.cursor/rules/release-management.mdc`.
- Measured improvement: `.cursor/rules/auto-research.mdc`.
- Visible-surface design guidance: `.cursor/rules/brand-design-system.mdc`.

## How This Connects

- `START-HERE-NCCC.md` gives students the shortest safe path through the template.
- `prompts/START-CURSOR-HERE.md` gives the agent a predictable first instruction.
- `intake/problem-intake.md` gives the agent the project context.
- `planning/milestone-plan-template.md` turns the intake into a reviewed roadmap.
- `.github/ISSUE_TEMPLATE/project_issue.md` turns roadmap items into issue-level spec-kit inputs.
- `docs/spec-kit-workflow.md` explains the workflow behind the rules.
- `docs/development-workflow.md` explains the day-to-day build and test loop.

