# Cursor Prompts

These prompts are examples. Edit them to match your project.

Start with `prompts/START-CURSOR-HERE.md` before using the prompts below.

## Understand the Template

```text
Read README.md, QUICKSTART.md, SECURITY.md, docs/, intake/problem-intake.md, planning/, examples/, prompts/, and .cursor/rules/. Explain how I should use this template and how the Cursor rules affect the workflow. Do not make changes yet.
```

## Review My Intake

```text
Review intake/problem-intake.md. Identify unclear requirements, security concerns, missing synthetic data details, likely CASE/UCO/CAC concepts, and questions I should answer before planning. Do not create files or GitHub issues yet.
```

## Create a Milestone Plan

```text
Using intake/problem-intake.md and planning/milestone-plan-template.md, draft a project-specific milestone plan from v0.1.0 through v1.0.0. Each milestone should produce something testable with synthetic data and should account for the Project VIC Cursor rules. Save the reviewed plan to a new file such as planning/my-milestone-plan.md only after I approve the draft. Do not create GitHub milestones or issues yet.
```

## Create GitHub Milestones and Issues

```text
I have reviewed and approved the project-specific milestone plan in planning/my-milestone-plan.md. Use GitHub CLI to create the milestones and issues in my private GitHub repository. Align each issue to .github/ISSUE_TEMPLATE/project_issue.md and show me the commands you plan to run before running them.
```

## Apply Spec-Kit

```text
Use the spec-kit flow for the approved issue: specify, plan, tasks, implement, analyze. Work on one issue only. Use synthetic data for testing. Explain how I should test the result and wait for feedback before moving to the next issue.
```

## Plan GitHub Actions

```text
Based on this project's actual requirements, recommend the smallest useful GitHub Actions workflow. Keep it appropriate for a free private GitHub repository. Avoid unnecessary scheduled jobs, large artifacts, long-running jobs, and paid add-ons.
```

## Check CASE/UCO/CAC Alignment

```text
Review the current data model and recommend where CASE, UCO, and CAC Ontology namespaces, classes, properties, and relationships should be reused. Do not force a graph database or RDF serialization unless it clearly helps the mission problem.
```

## Test With Synthetic Data

```text
Create or update synthetic test data for this feature. It must be representative of the workflow but must not include real case data, real people, real identifiers, CSAM, suspect material, credentials, agency-private information, or operational details.
```

