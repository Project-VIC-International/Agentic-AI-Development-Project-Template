# Agent Expectations

This template includes development policies in `policies/`. They are the persistent guidance that your AI coding agent follows while turning the intake form into specs, milestones, issues, code, tests, docs, and releases. `AGENTS.md` summarizes the most important rules and lists every policy. See `docs/agent-setup.md` for how each agent loads them.

`.project-vic/` keeps the pinned upstream Project VIC mandatory policy corpus from v0.2.0. It is provenance. Agents follow `policies/`, not the files under `.project-vic/`.

Ask the agent to summarize these policies before starting a real project:

```text
Read AGENTS.md and the core policies it lists in policies/. Explain the development expectations in plain language. Focus on how they affect planning, GitHub issues, Spec Kit, security, synthetic data, CASE/UCO/CAC alignment, and releases.
```

## Key Policy Areas

Core policies (apply to every task):

- Policy index and precedence: `policies/rule-index.md`.
- Beginner workflow and safer pacing: `policies/student-mode.md`.
- Project context: `policies/project-context.md`.
- Security and jurisdiction-aware compliance: `policies/security-compliance.md`.
- Privacy and test data tiers: `policies/privacy-redaction-and-synthetic-data.md`.
- No stubs: `policies/no-stubs.md`.
- Spec Kit first: `policies/speckit-workflow.md`.
- Human review: `policies/human-review-and-risk-gates.md`.

Conditional policies (apply when the task touches their area):

- Four data interfaces: `policies/four-surface-review.md`.
- CASE/UCO/CAC alignment: `policies/ontology-alignment.md`.
- Architecture boundaries: `policies/architecture-boundaries.md`.
- Cross-platform support: `policies/cross-platform.md`.
- Testing: `policies/testing-quality.md` and `policies/testing-program.md`.
- Release discipline: `policies/versioning-release-management.md`.
- Measured improvement: `policies/auto-research.md`.
- Visible surfaces and documentation: `policies/brand-design-system.md` and `policies/documentation-standards.md`.
- MCP and agent tools: `policies/mcp-agent-safety.md`.
- Models, data contracts, persistence, dependencies, and logging: see the index in `AGENTS.md`.

## How This Connects

- `START-HERE.md` gives workshop, conference, and course participants the shortest safe path through the template.
- `prompts/START-AGENT-HERE.md` gives any agent a predictable first instruction.
- `intake/problem-intake.md` gives the agent the project context.
- `planning/milestone-plan-template.md` turns the intake into a reviewed roadmap.
- `.github/ISSUE_TEMPLATE/project_issue.md` turns roadmap items into issue-level Spec Kit inputs.
- `docs/spec-kit-workflow.md` explains the workflow behind the policies.
- `docs/development-workflow.md` explains the day-to-day build and test loop.

## Remember

Instruction files guide an agent; they do not force it. An agent can misread or ignore a rule. You are still responsible for reviewing what it does, approving risky actions, and testing the result.
