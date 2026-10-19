# Note: this file must be adapted to the specific development project after the first version of `intake/problem-intake.md` is complete. Ask the agent to propose updates and have a human developer review them.

# Project VIC Internal Development Template Guidelines

This repository is a Project VIC International internal software development template. It helps a human developer start a new private Project VIC ecosystem capability with Cursor, Spec Kit, GitHub planning, synthetic test data, CASE/UCO/CAC awareness, and safety guardrails.

This file provides repository-local development context for Spec Kit and Cursor. It supplements, but does not replace, the Project VIC rules for security, ontology alignment, cross-platform compatibility, four-surface parity, no-stubs implementation, release management, and brand/design consistency.

This file may be updated by Spec Kit after the project is initialized. Preserve generated sections unless intentionally regenerating them. Maintainer-authored guidance should be added outside generated blocks.

## Template Status

- Do not assume an application stack until `intake/problem-intake.md`, the project constitution, and the first Spec Kit plan identify one.
- Do not initialize Spec Kit before the first version of `intake/problem-intake.md` is filled out.
- Once the project is understood, replace this template guidance with project-specific technologies, commands, surfaces, data flows, and validation steps.
- Keep the Project VIC safety, privacy, ontology, testing, no-stubs, release, cross-platform, and human-review rules active unless a maintainer explicitly changes them.

Do not introduce frameworks, databases, queues, package managers, build systems, deployment services, model pipelines, or major architectural dependencies without an explicit intake, spec, or plan requirement.

## Repository Surfaces To Establish

New Project VIC software projects should decide which surfaces are required during intake and planning:

- GUI or other human-facing interface.
- API or integration surface.
- CLI, pipeline, batch, or offline workflow.
- MCP server, prompts, tools, or resources for agent use.
- Container, deployment, setup, or operations surface.
- Reports, exports, generated artifacts, schemas, ontology output, or audit/provenance records.
- Documentation, planning, Spec Kit, GitHub issues, milestones, and release materials.

When one surface changes, check whether other planned surfaces need equivalent updates or a documented exception.

## Common Commands To Establish

Before implementation starts, define project-specific commands for:

- setup and dependency installation
- linting and formatting
- unit, integration, contract, and end-to-end tests (canonical T0 command per `testing-program.mdc`)
- API, GUI, CLI, MCP, report/export, ontology, and container validation where applicable
- GitHub Actions workflows per `testing-program.mdc` and `.github/workflows/README.md`
- human verification: `docs/manual-test-checklist.md` and per-release annex from `docs/templates/manual-test-release-annex.md`
- release versioning: plan through `v1.0.0` MVP per `docs/release-versioning.md` and `planning/release-roadmap-template.md`
- release and changelog validation

Do not treat a compile-only check as a substitute for real tests when behavior changes.

## Style and Implementation Guidance

- Follow existing local patterns before adding abstractions.
- Keep business logic in shared service/application layers where possible.
- Avoid duplicating behavior independently across GUI, API, CLI/pipeline, and MCP surfaces.
- Keep source evidence paths read-only and validate input roots when evidence handling is in scope.
- Reject path traversal and outputs outside approved case/run/output directories.
- Prefer structured parsers and serializers over ad-hoc string manipulation.
- Prefer explicit typed errors over silent failures.
- Do not add stubs, fake success responses, or TODO-only implementation paths.
- Keep docs, changelog, environment templates, API schemas, GUI types, pipeline artifacts, and release notes aligned.
- Default Tier T0/T1 for committed fixtures and docs. Tier T2 agency-approved samples: local/gitignored paths only, handling plan required, prohibited channels per `docs/test-data-handling.md`. Agents may assist configured local testing without hiding the tier used.
- Do not use real CSAM, victim data, agency-sensitive data, or sensitive investigative material in public examples, screenshots, demos, or documentation.

## Documentation and Release Hygiene

Update documentation when behavior changes for:

- installation
- deployment or container profiles
- configuration
- GUI usage
- API usage
- CLI/pipeline usage
- Project VIC lookup behavior
- evidence input and artifact output
- CASE/UCO/CAC exports
- ontology validation
- offline or air-gapped operation
- GPU/CPU behavior
- known limitations

User-visible or operator-visible changes should include a `CHANGELOG.md` entry.

## Manual Additions

Project-specific guidance should be added below this section by maintainers after intake and Spec Kit planning identify the actual product scope.

<!-- SPECKIT START -->
For additional context about technologies to be used, project structure,
shell commands, and other important information, read the current plan.
<!-- SPECKIT END -->
