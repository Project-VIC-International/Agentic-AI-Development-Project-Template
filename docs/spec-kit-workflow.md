# Spec-Kit Workflow

Use spec-kit to keep the agent focused on explicit requirements before implementation.

## Opinionated Flow

The recommended flow is:

1. Specify the user-facing behavior and mission outcome.
2. Plan the architecture and technical approach.
3. Generate tasks.
4. Implement tasks one at a time.
5. Analyze consistency across the spec, plan, tasks, code, tests, and docs.
6. Test and provide feedback.

Do not skip testing. The agent can produce plausible code that does not actually solve your problem.

## Before Specifying

Complete `intake/problem-intake.md` first. The intake form gives the agent context about:

- The mission problem.
- Expected users.
- Data types and workflows.
- Constraints and approvals.
- Timeline.
- Interoperability needs.
- Synthetic test data.

## During Planning

Ask the agent to identify:

- What can be built safely with synthetic data.
- What needs future production approval.
- How the four data interfaces apply: human UI, command-line/power-user, application/API/MCP, and interoperable export.
- What CASE/UCO/CAC concepts apply.
- What risks and assumptions need review.
- What GitHub Actions are truly needed.

## During Implementation

Ask the agent to work issue by issue. Keep each implementation step small enough to test.

Example:

```text
Work only on the first task for milestone v0.1.0. Inspect the code first, explain your plan, implement the smallest useful change, and tell me how to test it with synthetic data.
```

## See Also

- `.cursor/rules/speckit-workflow.mdc` for the binding agent rule.
- `.cursor/rules/four-surface-review.mdc` for the four-interface architecture review.
- `.github/ISSUE_TEMPLATE/project_issue.md` for issue fields that prepare work for spec-kit.
- `docs/development-workflow.md` for the day-to-day develop, test, commit, and release loop.

