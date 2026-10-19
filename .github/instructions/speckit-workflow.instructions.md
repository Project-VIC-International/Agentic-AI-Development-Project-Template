---
applyTo: "**"
---


# Spec Kit Driven Development

Spec Kit is the required planning and verification workflow for Project VIC development.

Agents must not jump directly from a non-trivial request to implementation. Requirements, design, tasks, implementation, tests, documentation, and release impact must remain traceable.

This rule applies to Project VIC applications and services. Repository-specific details may refine this workflow, but they must not bypass security, ontology alignment, cross-platform compatibility, four-surface parity, no-stubs implementation, release management, or brand/design requirements.

Use `project-vic-rule-index.mdc` for rule precedence, shared data taxonomy, and output discipline. Spec Kit should evaluate applicable rules, not force every specialized checklist into every task.

## Required Pipeline

All Project VIC features, enhancements, and non-trivial bug fixes must follow the Spec Kit pipeline before implementation:

1. `/speckit.specify` — define requirements, users, acceptance criteria, risks, constraints, success metrics, affected surfaces, protected data, ontology impact, and release expectations.
2. `/speckit.plan` — design the implementation, shared service-layer changes, data model, contracts, migrations, validation approach, testing strategy, deployment impact, and rollback considerations.
3. `/speckit.tasks` — break work into dependency-ordered tasks with concrete file paths, affected surfaces, tests, docs, changelog, and validation work.
4. `/speckit.implement` — execute tasks in order with real code, real validation, real tests, and no production stubs.
5. `/speckit.analyze` — verify consistency across spec, plan, tasks, code, tests, docs, changelog, release notes, and all affected surfaces.

A Spec Kit workflow is not complete until `/speckit.analyze` confirms that implemented behavior matches approved requirements and that no required surface, test, documentation, security, ontology, release, or brand work was silently skipped.

## Applies To

Spec Kit is required for changes that affect:

- GUI workflows, API endpoints/schemas/auth/status behavior, CLI commands, pipeline behavior, container entry points, or MCP tools/resources/prompts.
- Reports, exports, artifacts, generated files, machine-readable output, data models, persistence, migrations, database behavior, or artifact shapes.
- Evidence handling, source media access, derived artifacts, provenance, audit logging, forensic integrity, security, privacy, compliance, dependencies, or supply-chain posture.
- CASE/UCO/CAC/SOLVE-IT ontology mappings or validation.
- Docker, deployment, offline/air-gapped, GPU, CPU-only, platform, configuration, or release behavior.
- Brand, terminology, accessibility, operator-facing copy, screenshots, documentation, changelog, GitHub Actions, GitHub Issues, GitHub Projects, labels, or milestones.
- Performance work, benchmarking, `auto-research` loops, or refactors that change behavior, public surfaces, data flow, dependency structure, or operational assumptions.

## Non-Trivial Change Criteria

Treat a change as non-trivial when any of the following are true:

- It touches more than one surface.
- It changes behavior visible to an investigator, operator, developer, integrator, or agent.
- It changes data that may appear in reports, exports, audit logs, provenance records, or ontology-aligned output.
- It changes security, evidence integrity, deployment, configuration, or release behavior.
- It requires new tests, documentation, migration notes, or changelog entries.
- It introduces, removes, or changes a dependency.
- It could affect trust in the correctness, safety, or completeness of Project VIC software.

When in doubt, use Spec Kit.

## May Be Skipped

Spec Kit may be skipped only for small, obvious, low-risk changes such as:

- Typo fixes.
- Formatting-only changes.
- Documentation-only edits with no behavior, command, configuration, schema, or release impact.
- Comment-only changes that do not alter claims about implemented behavior.
- Dependency bumps with no API, artifact, security, runtime, deployment, or behavior change.
- Small obvious bug fixes that do not change public surfaces, data models, outputs, security posture, deployment behavior, or release notes.

When Spec Kit is skipped, the agent must briefly state why the change is safe to handle without the full pipeline.

## Required Cross-Rule Checks

Every Spec Kit workflow must consider applicable Project VIC rules. Mark a rule "not applicable" only when the spec or plan explains why it is not materially triggered.

- Security and compliance: protected data, authentication, authorization, audit, provenance, secrets, evidence handling, dependency risk, and compliance assumptions.
- Ontology alignment: CASE/UCO/CAC/SOLVE-IT concepts, serialization, SHACL validation, fixtures, and unmapped gaps.
- Cross-platform compatibility: Windows, WSL, Linux, Docker, CPU-only, GPU-accelerated, offline, and air-gapped behavior.
- Four-surface parity: GUI, API, CLI/pipeline, and MCP server equivalence.
- No stubs: real implementation, real errors, real tests, and no fake production behavior.
- Versioning and release management: issues, milestones, labels, changelog, docs, GitHub Actions, release notes, and migration guidance.
- Brand and design system: Project VIC terminology, accessibility, visible-surface consistency, trauma-aware language, and synthetic-only examples.
- Conditional rules: architecture, data contracts, persistence, dependencies, human review, MCP safety, model governance, observability, privacy/synthetic data, testing quality, and autoresearch when their subject area is touched.

## Spec Locations and Authority

Specs live under `specs/`.

The constitution at `.specify/memory/constitution.md` is the highest project-local authority after explicit user instructions.

If a spec, plan, task, implementation, or generated output conflicts with the constitution or Project VIC Cursor rules, the agent must identify the conflict and resolve it before treating the work as complete.

## Phase Requirements

`/speckit.specify` must identify user need, mission context, primary users, affected surfaces, functional and non-functional requirements, acceptance criteria, protected data categories, evidence-handling requirements, security/compliance assumptions, ontology concepts, cross-platform/offline assumptions, failure modes, success metrics, open questions, and intentionally out-of-scope work.

`/speckit.plan` must identify architecture and shared service-layer changes, data model/schema changes, GUI/API/CLI/MCP contracts, validation and error strategies, audit/provenance behavior, ontology mapping, security controls, configuration, dependencies, deployment impact, testing strategy, docs/changelog impact, migration, rollback, and compatibility concerns.

`/speckit.tasks` must be concrete, dependency-ordered, and tied to files or surfaces. Include shared service-layer implementation, GUI/API/CLI/MCP updates, tests, fixtures, ontology validation, security validation, documentation, changelog, release notes, GitHub issue/milestone updates, and migration guidance where applicable. Do not create vague tasks such as "wire up later", "finish integration", "add tests eventually", or "update docs if needed".

`/speckit.implement` must follow tasks in order unless a justified change is documented, implement real behavior, use shared service layers where practical, update all affected surfaces, preserve security/evidence/ontology/platform requirements, add or update tests/docs/changelog, and fail honestly with actionable errors when prerequisites are missing.

`/speckit.analyze` must verify spec, plan, tasks, implementation, and tests remain consistent; affected surfaces were updated or explicitly ruled out; no production stubs or fake success paths remain; security and evidence handling are implemented and tested; ontology mappings remain valid; platform/deployment assumptions remain valid; docs/changelog match behavior; release/issue/milestone/label/GitHub Actions expectations are satisfied; and deferred work is documented without being exposed as complete.

## Required Agent Output

For Spec Kit-driven work, the final agent response must summarize whether Spec Kit was required, spec path used or created, affected surfaces, key requirements, key implementation tasks, tests or validation performed, documentation and changelog impact, materially triggered rule impacts, skipped surfaces and why, and deferred work and why it is not exposed as complete.
