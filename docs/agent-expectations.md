# Agent Expectations

Development agents follow the Project VIC mandatory policy corpus installed in this repository. The canonical record is `docs/mandatory-policy-corpus.md`. Generated adapter files must stay byte-for-byte equal to the pinned corpus. Do not edit them to add local exceptions.

Cursor loads `.cursor/rules/`. Other agents load their own entry points, listed in the pin record. The shared policy text is in `.project-vic/policies/`.

Ask the agent to summarize the active policies before starting a real project:

```text
Read .cursor/rules/project-vic-rule-index.mdc, .project-vic/manifest.json, and docs/mandatory-policy-corpus.md. Explain the development expectations in plain language. Focus on how they affect planning, GitHub issues, spec-kit, security, synthetic data, CASE/UCO/CAC alignment, and releases.
```

## How this connects

- `START-HERE.md` gives workshop and conference participants the shortest safe path through the template.
- `prompts/START-CURSOR-HERE.md` gives the agent a predictable first instruction.
- `intake/problem-intake.md` gives the agent the project context.
- `planning/milestone-plan-template.md` turns the intake into a reviewed roadmap.
- `.github/ISSUE_TEMPLATE/project_issue.md` turns roadmap items into issue-level spec-kit inputs.
- `docs/spec-kit-workflow.md` explains the workflow behind the policies.
- `docs/development-workflow.md` explains the day-to-day build and test loop.
