# Project VIC Agentic AI Development Template

This repository is a quick-start template for investigators, digital forensic examiners, analysts, and supporting technologists who want to build mission tools using the Project VIC International agentic AI development approach.

It is a companion to the [Project VIC International Agentic AI Development Course](https://github.com/Project-VIC-International/Agentic-AI-Development-Course.git). The course teaches the approach; this repository helps you start applying it in your own private project with the AI coding agent of your choice, GitHub, Spec Kit, synthetic test data, and CASE/UCO/CAC interoperability guidance.

## Student Path: Do These 7 Things

1. Create a private repository from this template.
2. Open your private repository in your AI coding agent (Cursor, Claude Code, Codex, GitHub Copilot, Gemini CLI, or another). See `docs/agent-setup.md`.
3. Read `START-HERE.md`.
4. Paste the prompt in `prompts/START-AGENT-HERE.md` into your agent.
5. Complete `intake/problem-intake.md`.
6. Ask your agent to review the intake and draft a milestone plan.
7. Build only the first small milestone with synthetic data.

## Who This Is For

This template assumes you are a beginner with GitHub, AI coding agents, and Python, or that you have at least read or attended the Phase 1 lecture from the course.

You do not need to be a professional software developer. You do need to move carefully, test what the agent creates, and avoid putting sensitive investigative data into development tools.

## What This Template Provides

- Development policies in `policies/` that any AI coding agent can follow: data safety, evidence integrity, honest results, Spec Kit planning, interoperability, testing, and human review.
- Agent instruction files generated from those policies: `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, and `.cursor/rules/`.
- Beginner-friendly setup guidance for GitHub, Python, GitHub CLI, and local development.
- Optional setup scripts for Ubuntu 24.04, macOS, and Windows 11.
- A problem intake form that helps you describe the mission problem, proposed solution, constraints, data, and timeline.
- Planning templates for milestone plans, GitHub issues, and release roadmaps.
- Example prompts you can give to your agent while using Spec Kit.
- Guidance for using CASE, UCO, and CAC Ontology concepts to improve interoperability.
- Tiered test data guidance and manual test checklists.
- Jurisdiction-aware security guidance: the agent asks which country's and agency's rules apply instead of assuming one.

## Recommended Workflow

1. Read `QUICKSTART.md`.
2. Complete `intake/problem-intake.md`.
3. Ask your agent to create a milestone plan from your intake form.
4. Review and edit the plan before allowing the agent to create GitHub milestones or issues.
5. Use the Spec Kit flow: specify, clarify, plan, tasks, analyze, implement, converge.
6. Test every result with synthetic data that is representative of your mission data.
7. Commit, push, run GitHub Actions if configured, fix failures, test again, and release when ready.

## Important Safety Rules

Do not use real case data, CSAM, victim data, suspect data, investigative leads, credentials, private agency information, or sensitive operational details while building and testing. Use synthetic data that represents the structure and workflow of your mission data without exposing actual mission content.

Anything you give a cloud AI agent may leave your computer. Treat the agent like any other external service.

Applications should be designed so they can later process real mission data in a properly approved, controlled production environment.

## Getting Started

Start with:

- `START-HERE.md` for the conference, workshop, and lab path.
- `QUICKSTART.md` for the first-session path.
- `docs/agent-setup.md` for setting up your AI coding agent.
- `docs/tooling-setup.md` for optional setup scripts and tool installation.
- `docs/github-setup.md` for GitHub and GitHub CLI.
- `docs/cursor-setup.md` for Cursor-specific tips (the instructor's tool in the workshop).
- `intake/problem-intake.md` for your project description.
- `prompts/START-AGENT-HERE.md` for the first agent prompt.
- `prompts/agent-prompts.md` for prompts you can give to the agent.

## Documentation Map

- Policies: `policies/README.md`, `AGENTS.md`, and `docs/agent-expectations.md`.
- Workflow: `docs/spec-kit-workflow.md` and `docs/development-workflow.md`.
- Course integration: `docs/course-integration.md`, `START-HERE.md`, and `prompts/START-AGENT-HERE.md`.
- Upstream policy pin: `docs/mandatory-policy-corpus.md` and `.project-vic/`. Live agent rules come from `policies/`.
- Planning: `planning/milestone-plan-template.md`, `planning/issue-template.md`, `planning/release-roadmap-template.md`, and `examples/sample-milestone-plan.md`.
- Data and interoperability: `docs/test-data-handling.md`, `docs/synthetic-test-data.md`, `docs/case-uco-cac-guidance.md`, `examples/README.md`, and `examples/synthetic-data/README.md`.
- Testing: `docs/manual-test-checklist.md` and `docs/templates/`.
- Security and permissions: `SECURITY.md`, `docs/permissions-troubleshooting.md`, `docs/github-setup.md`, and `docs/agent-setup.md`.
- Automation and setup: `docs/tooling-setup.md`, `scripts/`, and `.github/workflows/README.md`.

## How the Policies Work

`policies/` is the single source of truth for how agents should work in this repository. `AGENTS.md` is the entry point most agents read automatically; it lists every policy and when it applies. If you change a policy, run `python3 scripts/sync_agent_rules.py` to update the agent-specific copies. Ask your agent to summarize the policies before starting a real project.

The policies are guidance for safe development. Following them does not by itself demonstrate compliance with any law, regulation, or security framework; your agency remains responsible for its own requirements.
