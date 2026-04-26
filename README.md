# Project VIC Agentic AI Development Template

This repository is a quick-start template for investigators, digital forensic examiners, analysts, and supporting technologists who want to build mission tools using the Project VIC International agentic AI development approach.

It is a companion to the [Project VIC International Agentic AI Development Course](https://github.com/Project-VIC-International/Agentic-AI-Development-Course.git). The course teaches the approach; this repository helps you start applying it in your own private project with Cursor, GitHub, spec-kit, synthetic test data, and CASE/UCO/CAC interoperability guidance.

## Student Path: Do These 7 Things

1. Create a private repository from this template.
2. Open your private repository in Cursor.
3. Read `START-HERE-NCCC.md`.
4. Paste the prompt in `prompts/START-CURSOR-HERE.md`.
5. Complete `intake/problem-intake.md`.
6. Ask Cursor to review the intake and draft a milestone plan.
7. Build only the first small milestone with synthetic data.

## Who This Is For

This template assumes you are a beginner with GitHub, Cursor, and Python, or that you have at least read or attended the Phase 1 lecture from the course.

You do not need to be a professional software developer. You do need to move carefully, test what the agent creates, and avoid putting sensitive investigative data into development tools.

## What This Template Provides

- Beginner-friendly setup guidance for GitHub, Cursor, Python, GitHub CLI, and local development.
- Optional setup scripts for Ubuntu 24.04, macOS, and Windows 11.
- Cursor rules that guide the agent toward Project VIC's development practices.
- A problem intake form that helps you describe the mission problem, proposed solution, constraints, data, and timeline.
- Planning templates for milestone plans, GitHub issues, and release roadmaps.
- Example prompts you can give to Cursor while using spec-kit.
- Guidance for using CASE, UCO, and CAC Ontology concepts to improve interoperability.
- Security guidance for synthetic development data and production mission data boundaries.

## Recommended Workflow

1. Read `QUICKSTART.md`.
2. Complete `intake/problem-intake.md`.
3. Ask Cursor to create a milestone plan from your intake form.
4. Review and edit the plan before allowing the agent to create GitHub milestones or issues.
5. Use the spec-kit flow: specify, plan, tasks, implement, analyze.
6. Test every result with synthetic data that is representative of your mission data.
7. Commit, push, run GitHub Actions if configured, fix failures, test again, and release when ready.

## Important Safety Rules

Do not use real case data, CSAM, victim data, suspect data, investigative leads, credentials, private agency information, or sensitive operational details while building and testing. Use synthetic data that represents the structure and workflow of your mission data without exposing actual mission content.

Applications should be designed so they can later process real mission data in a properly approved, controlled production environment.

## Getting Started

Start with:

- `START-HERE-NCCC.md` for the NCCC lab path.
- `QUICKSTART.md` for the first-session path.
- `docs/tooling-setup.md` for optional setup scripts and tool installation.
- `docs/github-setup.md` for GitHub and GitHub CLI.
- `docs/cursor-setup.md` for Cursor setup and permissions.
- `intake/problem-intake.md` for your project description.
- `prompts/START-CURSOR-HERE.md` for the first agent prompt.
- `prompts/cursor-prompts.md` for prompts you can give to the agent.

## Documentation Map

- Workflow: `docs/spec-kit-workflow.md`, `docs/development-workflow.md`, and `.cursor/rules/`.
- Course integration: `docs/course-integration.md`, `START-HERE-NCCC.md`, and `prompts/START-CURSOR-HERE.md`.
- Agent guidance: `docs/agent-expectations.md` and `.cursor/rules/`.
- Planning: `planning/milestone-plan-template.md`, `planning/issue-template.md`, `planning/release-roadmap-template.md`, and `examples/sample-milestone-plan.md`.
- Data and interoperability: `docs/synthetic-test-data.md`, `docs/case-uco-cac-guidance.md`, `examples/README.md`, and `examples/synthetic-data/README.md`.
- Security and permissions: `SECURITY.md`, `docs/permissions-troubleshooting.md`, `docs/github-setup.md`, and `docs/cursor-setup.md`.
- Automation and setup: `docs/tooling-setup.md`, `scripts/`, and `.github/workflows/README.md`.

The `.cursor/rules/` folder encodes the Project VIC expectations that the user's agent should follow. Ask the agent to summarize those rules before starting a real project.

