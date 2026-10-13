# Course Integration

The Project VIC course teaches the method. This template is the student workspace where the method gets applied.

## Golden Path

1. Create a private repository from this template.
2. Open it in your AI coding agent (see `docs/agent-setup.md`).
3. Paste `prompts/START-AGENT-HERE.md`.
4. Complete `intake/problem-intake.md`.
5. Ask your agent to review the intake, not build yet.
6. Ask your agent to draft a milestone plan.
7. Approve one small `v0.1.0` milestone.
8. Create or update one issue.
9. Use spec-kit: specify, plan, tasks, implement, analyze.
10. Test with synthetic data.
11. Commit and push.

## Course-to-Template Crosswalk

| Course concept | Course location | Template location | Student action |
| --- | --- | --- | --- |
| Environment setup | `part-2-lab/exercises/00-environment-setup/` | `QUICKSTART.md`, `docs/tooling-setup.md`, `scripts/`, `.devcontainer/devcontainer.json` | Verify tools, run a setup script, or use Codespaces |
| First agent conversation | `part-2-lab/exercises/02-cursor-first-steps/` | `START-HERE.md`, `prompts/START-AGENT-HERE.md`, `AGENTS.md` | Ask the agent to explain the template before editing |
| Spec-driven development | `part-2-lab/exercises/03-spec-driven-dev/` | `docs/spec-kit-workflow.md`, `policies/speckit-workflow.md` | Use `specify -> clarify -> plan -> tasks -> analyze -> implement -> converge` |
| CASE/UCO/CAC alignment | `part-2-lab/exercises/04-case-uco-introduction/`, `part-2-lab/exercises/05-cac-ontology-modeling/` | `docs/case-uco-cac-guidance.md`, `policies/ontology-alignment.md` | Reuse ontology concepts where practical |
| Prototype build | `part-2-lab/exercises/06-build-a-prototype/` | `intake/`, `planning/`, `.github/ISSUE_TEMPLATE/`, `examples/` | Build one reviewed issue at a time with synthetic data |

## Safety Reminder

Do not paste real case data into your AI agent, GitHub, issues, logs, screenshots, test files, or sample data. Use synthetic data only.
