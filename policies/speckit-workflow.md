---
description: Mandatory Spec Kit workflow for feature development, non-trivial fixes, and release-relevant changes
alwaysApply: true
---

# Spec Kit Driven Development

[GitHub Spec Kit](https://github.com/github/spec-kit) is the required planning and verification workflow for this project. Spec Kit works with many AI agents. Commands are written here in Spec Kit's reference form (`/speckit.specify`); use the form your agent exposes, for example `/speckit-specify` (Copilot and other skills-based agents) or `$speckit-specify` (Codex). Install Spec Kit with `specify init --here --integration <your-agent>` only after the intake is complete.

Agents must not jump directly from a non-trivial request to implementation. Requirements, design, tasks, implementation, tests, documentation, and release impact must remain traceable. The spec is how a non-programmer stays in control of an agent that writes code faster than any human can read it.

Use `policies/rule-index.md` for policy precedence, the shared data taxonomy, and output discipline. Spec Kit should evaluate the applicable policies, not force every specialized checklist into every task.

## Before the First Spec

1. The user completes the first version of `intake/problem-intake.md`.
2. The agent reviews the intake and asks clarifying questions.
3. The user approves a milestone plan (`planning/`).
4. Run `/speckit.constitution` to create `.specify/memory/constitution.md`. The constitution must not weaken any policy in `policies/`.

## Required Pipeline

All features, enhancements, and non-trivial bug fixes must follow the Spec Kit pipeline before implementation:

1. `/speckit.specify`: define requirements, users, acceptance criteria, risks, constraints, success metrics, affected surfaces, protected data, ontology impact, and release expectations.
2. `/speckit.clarify`: resolve ambiguity before planning; do not guess during implementation.
3. `/speckit.plan`: design the implementation, shared service-layer changes, data model, contracts, migrations, validation approach, testing strategy, deployment impact, and rollback considerations.
4. `/speckit.checklist` (when the feature has security, compliance, user-experience, ontology, release, or cross-platform implications): generate requirements-quality checklists. The user, not the agent, marks custom checklist items as satisfied.
5. `/speckit.tasks`: break work into dependency-ordered tasks with concrete file paths, affected surfaces, tests, docs, changelog, and validation work.
6. `/speckit.analyze`: read-only consistency check across spec, plan, and tasks before implementation. Fix problems at the step that owns them and re-run until clean.
7. `/speckit.implement`: execute tasks in order with real code, real validation, real tests, and no production stubs. For larger features, implement one phase at a time and verify each phase.
8. `/speckit.converge`: check the implementation against spec, plan, and tasks; it appends any missed work to `tasks.md`. Repeat implement and converge until it reports converged.

After converging, run `/speckit.analyze` again as a final review of code, tests, docs, changelog, release notes, and all affected surfaces. If your Spec Kit version does not have `/speckit.converge`, use the final `/speckit.analyze` for that check.

A Spec Kit workflow is not complete until the implementation has converged and the final review confirms that no required surface, test, documentation, security, ontology, release, or visible-surface work was silently skipped. Then the user tests the result and gives feedback.

## Applies To

Spec Kit is required for changes that affect:

- GUI workflows, API endpoints/schemas/auth/status behavior, CLI commands, pipeline behavior, container entry points, or MCP tools/resources/prompts.
- Reports, exports, artifacts, generated files, machine-readable output, data models, persistence, migrations, database behavior, or artifact shapes.
- Evidence handling, source media access, derived artifacts, provenance, audit logging, forensic integrity, security, privacy, compliance, dependencies, or supply-chain posture.
- CASE/UCO/CAC/SOLVE-IT ontology mappings or validation.
- Docker, deployment, offline/air-gapped, GPU, CPU-only, platform, configuration, or release behavior.
- Terminology, accessibility, operator-facing copy, screenshots, documentation, changelog, GitHub Actions, GitHub Issues, GitHub Projects, labels, or milestones.
- Performance work, benchmarking, autoresearch loops, or refactors that change behavior, public surfaces, data flow, dependency structure, or operational assumptions.

## Non-Trivial Change Criteria

Treat a change as non-trivial when any of the following are true:

- It touches more than one surface.
- It changes behavior visible to an investigator, operator, developer, integrator, or agent.
- It changes data that may appear in reports, exports, audit logs, provenance records, or ontology-aligned output.
- It changes security, evidence integrity, deployment, configuration, or release behavior.
- It requires new tests, documentation, migration notes, or changelog entries.
- It introduces, removes, or changes a dependency.
- It could affect trust in the correctness, safety, or completeness of the tool.

When in doubt, use Spec Kit. A ten-minute spec is cheap insurance against a ten-hour rebuild.

## May Be Skipped

Spec Kit may be skipped only for small, obvious, low-risk changes such as:

- Typo fixes.
- Formatting-only changes.
- Documentation-only edits with no behavior, command, configuration, schema, or release impact.
- Comment-only changes that do not alter claims about implemented behavior.
- Dependency bumps with no API, artifact, security, runtime, deployment, or behavior change.
- Small obvious bug fixes that do not change public surfaces, data models, outputs, security posture, deployment behavior, or release notes.

When Spec Kit is skipped, the agent must briefly state why the change is safe to handle without the full pipeline.

## Required Cross-Policy Checks

Every Spec Kit workflow must consider the applicable policies. Read the policy file before marking it. Mark a policy "not applicable" only when the spec or plan explains why it is not materially triggered.

- Security and compliance (`security-compliance.md`): jurisdiction and framework, protected data, authentication, authorization, audit, provenance, secrets, evidence handling, dependency risk.
- Privacy and test data (`privacy-redaction-and-synthetic-data.md`): data tier, channels, redaction.
- Ontology alignment (`ontology-alignment.md`): CASE/UCO/CAC/SOLVE-IT concepts, serialization, SHACL validation, fixtures, unmapped gaps.
- Four-surface parity (`four-surface-review.md`): GUI, API, CLI/pipeline, and MCP equivalence, plus interoperable exports.
- Cross-platform compatibility (`cross-platform.md`): Windows, macOS, Linux, WSL, Docker, CPU-only, GPU-accelerated, offline, and air-gapped behavior.
- No stubs (`no-stubs.md`): real implementation, real errors, real tests.
- Versioning and release management (`versioning-release-management.md`): issues, milestones, labels, changelog, docs, GitHub Actions, release notes, migration guidance.
- Visible surfaces (`brand-design-system.md`, `documentation-standards.md`): terminology, accessibility, trauma-aware language, synthetic-only examples.
- Conditional policies when their subject area is touched: architecture, data contracts, persistence, dependencies, human review, MCP safety, model governance, observability, testing, and autoresearch.

## Spec Locations and Authority

Specs live under `specs/`.

The constitution at `.specify/memory/constitution.md` is the highest project-local authority after explicit user instructions, and it must stay consistent with `policies/`.

If a spec, plan, task, implementation, or generated output conflicts with the constitution or the policies, the agent must identify the conflict and resolve it with the user before treating the work as complete.

## Phase Requirements

`/speckit.specify` must identify user need, mission context, primary users, affected surfaces, functional and non-functional requirements, acceptance criteria, protected data categories, evidence-handling requirements, security/compliance assumptions, ontology concepts, cross-platform/offline assumptions, failure modes, success metrics, open questions, and intentionally out-of-scope work.

`/speckit.plan` must identify architecture and shared service-layer changes, data model/schema changes, GUI/API/CLI/MCP contracts, validation and error strategies, audit/provenance behavior, ontology mapping, security controls, configuration, dependencies, deployment impact, testing strategy, docs/changelog impact, migration, rollback, and compatibility concerns.

`/speckit.tasks` must be concrete, dependency-ordered, and tied to files or surfaces. Include shared service-layer implementation, GUI/API/CLI/MCP updates, tests, fixtures, ontology validation, security validation, documentation, changelog, release notes, GitHub issue/milestone updates, and migration guidance where applicable. Do not create vague tasks such as "wire up later", "finish integration", "add tests eventually", or "update docs if needed".

`/speckit.implement` must follow tasks in order unless a justified change is documented, implement real behavior, use shared service layers where practical, update all affected surfaces, preserve security/evidence/ontology/platform requirements, add or update tests/docs/changelog, and fail honestly with actionable errors when prerequisites are missing.

`/speckit.converge` and the final `/speckit.analyze` must verify spec, plan, tasks, implementation, and tests remain consistent; affected surfaces were updated or explicitly ruled out; no production stubs or fake success paths remain; security and evidence handling are implemented and tested; ontology mappings remain valid; platform/deployment assumptions remain valid; docs/changelog match behavior; release/issue/milestone/label/GitHub Actions expectations are satisfied; and deferred work is documented without being exposed as complete.

## Required Agent Output

For Spec Kit-driven work, the final agent response must summarize whether Spec Kit was required, the spec path used or created, affected surfaces, key requirements, key implementation tasks, tests or validation performed, documentation and changelog impact, materially triggered policy impacts, skipped surfaces and why, deferred work and why it is not exposed as complete, and how the user can test the result.
