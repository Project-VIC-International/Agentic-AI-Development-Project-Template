# Project VIC Mandatory Development Policy — codex

This is a generated adapter. Do not edit it directly. The Project VIC policies below are mandatory and may not be weakened by repository-local or agent-generated guidance. If instructions conflict and the policy precedence does not resolve the conflict, stop and request human clarification. Instruction files guide models; they are not a security boundary. CI, least privilege, approval gates, hooks, and human review remain required.

Corpus version: 0.1.0
Pinned upstream commit: `dcb94f517e4a31fbb9e1a9b43f5fa0347eb114d7`
Policy count: 25


<!-- POLICY-BEGIN PVIC-ARCHITECTURE-BOUNDARIES 372bf64f6909b888743d813b419ce7c8eab39ce024f2df44fb05cc2f1cb51cbd -->

# Architecture Boundaries

Project VIC applications must keep core behavior in shared, testable service/application layers. GUI, API, CLI/pipeline, and MCP surfaces are adapters over the same capability, not separate implementations.

Architecture changes must preserve security, evidence integrity, ontology alignment, surface equivalence, and no-stubs behavior.

## Layering Requirements

- Business logic belongs in shared service/application layers.
- GUI/API/CLI/MCP adapters should parse inputs, call shared services, translate outputs, and handle surface-specific presentation only.
- Do not process evidence directly inside React components, FastAPI route handlers, MCP tool functions, or CLI argument parsing.
- Keep domain models, DTOs/contracts, persistence, ontology mapping, external-tool invocation, and UI state separate.
- Surface adapters may vary interaction style, but must not change validation, authorization, provenance, audit, ontology, or error semantics.

## Boundary Rules

- Domain/service code must not import GUI components, route handlers, MCP server code, or CLI parser internals.
- UI and API code must not bypass shared validation, authorization, audit, provenance, or export services.
- Persistence code must not mutate source evidence or embed presentation-specific assumptions.
- External tools such as `ffmpeg`, mounting tools, OCR engines, model runtimes, and validators should be invoked through bounded service wrappers.
- Ontology mapping and serialization should be centralized enough that GUI/API/CLI/MCP outputs do not drift.

## Architecture Changes

- Do not introduce new architectural patterns, frameworks, queues, databases, service meshes, plugin systems, or deployment topologies without an explicit Spec Kit requirement and plan.
- Prefer small extensions to existing local patterns over new abstractions.
- Add abstractions only when they reduce real duplication, isolate risky behavior, or support four-surface equivalence.
- Document trust boundaries, data flow, source evidence handling, and dependency changes when architecture shifts.

## Spec Kit Requirements

For architecture-relevant work:

- `/speckit.specify`: identify affected capabilities, surfaces, trust boundaries, data flows, and architectural constraints.
- `/speckit.plan`: describe shared services, adapters, contracts, persistence boundaries, external-tool wrappers, ontology mapping, and test strategy.
- `/speckit.tasks`: create concrete tasks for shared logic, each affected adapter, tests, docs, and migration notes.
- `/speckit.implement`: update shared services first where practical, then adapters, without duplicating business logic.
- `/speckit.analyze`: verify no surface drift, no bypassed controls, no hidden stubs, and no unintended architecture dependency.

## Required Agent Output

For architecture-relevant changes, the final agent response must summarize shared service changes, affected adapters, boundaries preserved or changed, new dependencies or patterns, tests added, and any surfaces intentionally left unchanged.
<!-- POLICY-END PVIC-ARCHITECTURE-BOUNDARIES -->

<!-- POLICY-BEGIN PVIC-AUTO-RESEARCH bf9074c5e5db7139c2f7e7d1177a9116814c2353ef3c20abf4a8cb3ad6d471e2 -->

# Autoresearch: Experiment-Driven Performance Improvement

Project VIC tools must not be optimized by intuition alone when performance is part of the requirement.

After a feature meets its functional spec, use experiment-driven autoresearch for performance-critical improvements. This means forming one measurable hypothesis, changing one variable, benchmarking the result, and keeping only verified improvements.

Correctness, forensic integrity, security, privacy, provenance, ontology alignment, and operator trust take priority over speed.

## When This Rule Applies

Use this loop when:

- A spec defines a performance threshold.
- A user or maintainer requests performance improvement.
- A feature processes large media collections, hash sets, archives, reports, exports, model inference, or GUI result sets.
- A bottleneck affects investigator usability, batch throughput, offline operation, or deployment feasibility.
- Release notes or changelog entries will claim a measurable performance improvement.

Do not run autoresearch for ordinary feature work, typo fixes, small correctness bugs, documentation-only edits, or security fixes unless performance is part of the acceptance criteria.

## Loop

1. Read the spec threshold, acceptance criteria, and current benchmark baseline.
2. Identify the bottleneck with measurement before changing code.
3. Hypothesize one measurable change.
4. Implement the change in an isolated branch, worktree, or subagent attempt.
5. Measure with the same dataset, hardware profile, configuration, command, and version baseline.
6. Compare before/after results.
7. Keep only verified improvements that preserve correctness and required behavior.
8. Add or update regression protection.
9. Ratchet the spec floor only when the improvement is merged and realistic for the intended deployment tier.

## Project VIC Performance Targets

Use this loop for performance-sensitive areas such as media discovery, hashing, Project VIC lookup matching, archive preprocessing, forensic image handling, video frame sampling, object detection or model inference throughput, OCR or transcription pipelines, artifact generation, JSON/CSV/XLSX/JSON-LD/Turtle/RDF/report export speed, CASE/UCO/CAC validation speed, API job throughput, CLI batch processing, MCP tool latency, GUI result rendering at scale, Docker startup and deployment performance, CPU-only fallback performance, and GPU utilization or memory behavior.

## Safety and Correctness Requirements

Never keep a performance improvement that changes investigative meaning, mutates source evidence, skips required validation, weakens authentication or authorization, drops audit or provenance events, removes ontology-aligned output, changes report/export semantics without a spec update, hides errors, creates fake success paths, breaks CPU-only operation unless explicitly approved, increases minimum hardware requirements without documentation and approval, requires internet access in offline or air-gapped workflows, leaks sensitive data in benchmark logs, or reduces accessibility or operator clarity.

Performance improvements must preserve the no-stubs, security, ontology-alignment, cross-platform, four-surface, and release-management rules.

## Benchmark Data

- Use benign synthetic or approved non-sensitive datasets.
- Never use real CSAM, real victim data, real agency data, real case identifiers, or sensitive investigative material in benchmark fixtures, logs, screenshots, or reports.
- Record dataset size, file counts, media types, archive types, hash counts, model names, and relevant configuration.
- If synthetic data is used, describe how it approximates the operational workload.
- If the benchmark does not represent real-world investigator use, state that limitation.

## Hardware and Deployment Profiles

Record the hardware and deployment profile for each experiment, including CPU model, RAM, GPU model and VRAM, driver/runtime version, operating system, WSL/Linux/Docker profile, storage type, container image or environment, CPU-only versus GPU mode, model precision or quantization, offline/air-gapped profile, and relevant environment variables where applicable.

Do not optimize only for high-end GPUs if intended users include low-resource investigators. Maintain realistic baselines for CPU-only and modest workstation deployments where applicable.

## Experiment Rules

- One experiment changes one variable.
- Measure before changing code.
- Use the same command, dataset, configuration, and hardware profile for before/after comparisons.
- Run enough repetitions to avoid obvious noise when the benchmark is short or variable.
- Record wall-clock time, throughput, memory use, error rate, and output equivalence where applicable.
- Validate that output artifacts remain equivalent unless the spec intentionally changes them.
- Stop after at least three consecutive low-value experiments or when the bottleneck is outside the module.
- Do not keep code that adds complexity without measurable benefit.
- Do not merge experimental branches that lack tests, documentation, or reproducible results.

## Output Equivalence

For performance work that changes processing, exports, or rendering:

- Verify source evidence remains read-only.
- Verify derived artifacts stay in approved output locations.
- Verify hashes, classifications, detections, reports, and exports remain semantically consistent.
- Verify CASE/UCO/CAC/SOLVE-IT output still validates where applicable.
- Verify GUI, API, CLI, and MCP surfaces still expose equivalent behavior where applicable.
- Verify errors remain actionable and safe.

## Research Logs

Store experiment records in the feature `research.md`, `tools/autoresearch/results/`, the relevant Spec Kit research document, or another documented repository location.

Each experiment record must include hypothesis, changed variable, commit or branch, benchmark command, dataset description, hardware profile, software/container version, before metrics, after metrics, output equivalence result, decision to keep/reject/retry/defer, and reason for the decision.

## Regression Protection

When a performance improvement merges:

- Add or update a benchmark, regression test, CI check, or documented manual verification step.
- Update spec thresholds when the new floor is realistic for the intended deployment tier.
- Update documentation if hardware, configuration, or operator guidance changes.
- Update `CHANGELOG.md` and release notes when the improvement is user-visible or operationally relevant.
- Include before/after measurements and test conditions in performance-related release notes.

## Spec Kit Requirements

For performance-relevant work:

- `/speckit.specify`: define the performance target, affected users, workload, dataset assumptions, hardware/deployment tier, correctness requirements, and success threshold.
- `/speckit.plan`: define the benchmark method, baseline command, metrics, profiling approach, safety checks, and regression protection.
- `/speckit.tasks`: create concrete tasks for profiling, experiments, implementation, validation, documentation, changelog, and release notes.
- `/speckit.implement`: run measured experiments and keep only verified improvements.
- `/speckit.analyze`: verify the improvement is real, reproducible, safe, documented, tested, and aligned with the spec.

## Required Agent Output

For performance-relevant changes, the final agent response must summarize baseline measured, bottleneck identified, experiment attempted, variable changed, dataset used, hardware/deployment profile, before/after metrics, correctness and output-equivalence checks, whether the change was kept or rejected, regression protection added, and spec threshold/changelog/docs/release notes updated.
<!-- POLICY-END PVIC-AUTO-RESEARCH -->

<!-- POLICY-BEGIN PVIC-BRAND-DESIGN-SYSTEM 3291afe0504e24f1c58da4cabdc47ae1e2fc6a0b30a9f031e53331b6d1377717 -->

# Project VIC Brand and Design System

Project VIC International tools, documentation, reports, demos, websites, APIs, CLIs, MCP servers, and communications must present a unified, professional, accessible, and victim-centered identity.

Visible surfaces must use Project VIC terminology, operator-first language, accessible UI patterns, and approved design-system guidance.

This rule applies to user-facing and operator-visible surfaces, including GUI/UI, API docs, CLI help text, MCP tool names and descriptions, generated reports, exports, screenshots, README files, release notes, websites, training material, and demo content.

## Source of Truth

Use the Project VIC International Brand & Design System when styling, naming, or writing user-facing copy:

<https://github.com/Project-VIC-International/project-vic-brand-design-system>

Until a vendored design-system snapshot exists in the repository:

- Prefer existing project theme tokens and shared UI components.
- Avoid introducing hardcoded colors, fonts, shadows, border radii, spacing systems, icon styles, or new visual language.
- Do not invent new Project VIC logos, colors, fonts, taglines, product names, mascots, or visual systems.
- If a needed design token, component, icon, layout, or brand asset is missing, document the gap instead of creating an inconsistent local standard.

## Terminology

Use exact capitalization and approved names:

- **Project VIC**
- **Project VIC International**
- **VICSafer**
- **VICPoint**
- **ICAC investigator**
- **digital forensics examiner**
- **child sexual abuse material (CSAM)**

Use **Project VIC International** for the nonprofit organization when formality or legal identity matters. Use **Project VIC** when referring to the broader ecosystem, tooling, community, or mission in less formal product contexts.

Define acronyms on first use in documentation and operator-facing text when the audience may include new users.

Avoid inconsistent or informal variants such as `Project Vic`, `PVIC` unless explicitly defined for internal technical use, `VIC Safer`, `VicSafer`, `CSAMs`, `child porn`, or `kiddie porn`.

## Operator-First Language

Operator-facing text should be direct, precise, calm, and useful.

- Avoid marketing-heavy phrases such as "revolutionary", "game-changing", "next-generation", "AI-powered magic", "one-click rescue", or "fully automated investigation".
- Prefer investigator-facing terms over ML jargon: "classification result", "known hash match", "unknown media", "review queue", "case artifact", "source media", "derived artifact", "model confidence", "processing job", "export", "provenance", and "validation result".
- Use technical terms where they are necessary, but explain them clearly.

## Verdict, Confidence, and Analytic-Result Language

When a tool presents analytic verdicts, classifications, detections, or confidence values to operators (investigators, examiners, prosecutors), the language must be standardized, honest, and identical across surfaces:

- Define one repository-level verbal confidence vocabulary (fixed bands such as "strong indication", "moderate indication", "no clear indication", "analysis incomplete") in the shared service layer, version it, and use it identically in GUI, reports, exports, CLI, API descriptions, and MCP outputs. Do not improvise per-surface phrasings.
- State findings as indications and analytic results, never as facts or legal conclusions. Banned formulations include "this image is fake", "this file is authentic for prosecution", "proven AI-generated", and any phrasing implying guilt, victim status, or legal classification.
- Label every displayed score as calibrated or uncalibrated. Do not present an uncalibrated score using probability language.
- Incomplete analysis must read as incomplete ("analysis incomplete — required detector unavailable"), never as a weak finding.
- Plain-language summaries generated for non-technical operators must be deterministic (template-generated from structured results, traceable to the underlying assertion or result IDs). Do not put free-form LLM-generated narrative in evidentiary output paths.
- Limitations and known error modes must accompany the verdict at the same visual weight, not behind a secondary link only.

## Victim-Centered and Trauma-Aware Content

- Use victim-centered, investigator-supportive, and professionally restrained language.
- Do not use sensational, graphic, exploitative, joking, gamified, or emotionally manipulative language.
- Do not use real or recognizable case imagery in screenshots, docs, fixtures, seed data, examples, reports, demos, or tests.
- Do not include realistic CSAM descriptions, victim identifiers, offender names, agency case numbers, or sensitive investigative facts in sample content.
- Use benign synthetic data for examples, demos, screenshots, reports, and test fixtures.
- Prefer language that centers the mission and investigators, not the tool as the hero.
- Avoid implying that software alone safeguards children. Project VIC tools support trained investigators and allied professionals.

## Accessibility

- New GUI and web-visible work must target WCAG 2.2 AA unless the repository explicitly documents a different accessibility baseline.
- **Light and dark modes are mandatory for Project VIC GUIs** (ADR 0009 in the Brand & Design System). Follow OS/`prefers-color-scheme` by default and provide an explicit user override (`data-theme="light|dark"` or platform equivalent). Both modes must meet WCAG AA for text, cards, actions, and status/severity banners.
- **Excluded from the GUI theme-toggle mandate:** public marketing websites **projectvic.org** and **gpusforgood.org**. Those sites may ship a single curated marketing theme; they are not required to offer a product light/dark toggle.
- Consumer contract: <https://github.com/Project-VIC-International/project-vic-brand-design-system/blob/main/docs/gui-theming.md>
- Preserve keyboard navigation, visible focus indicators, readable typography, sufficient contrast, accessible forms, semantic headings, labels, alt text, and screen-reader-friendly status updates.
- Do not rely on color alone to communicate severity, category, confidence, status, or error conditions.
- Error messages must be clear, actionable, and accessible.
- Loading states, progress indicators, notifications, and validation messages must be perceivable and understandable.
- Touch targets, drag interactions, authentication flows, and repeated-entry workflows must account for accessibility requirements.

## GUI and UI

- Reuse existing theme patterns and components in the project.
- Prefer shared design-system tokens and components over local styling.
- Avoid hardcoded colors, one-off typography, custom spacing systems, and inconsistent icon styles.
- **Do not mode-mix.** Never put light-only fills (`background: white`, pastel `color-mix(..., white)`, or light-only hex) under a dark shell, and never put `--pv-color-text-primary` (or equivalent body text) on a pastel status fill. Use mode-aware pairs: `--pv-color-bg-surface` with `--pv-color-text-primary`; `--pv-color-role-*-tint` with the matching `--pv-color-role-*-text`.
- Severity / status banners must use design-system role tint + on-tint text tokens so they remain readable in both light and dark modes.
- Maintain consistent placement of primary actions, destructive actions, filters, status indicators, and help text.
- Use clear confirmations for destructive or irreversible actions.
- Do not make sensitive case details, evidence paths, victim identifiers, or CSAM-related descriptors more visible than necessary.
- UI text should help investigators understand what happened, what they can do next, and whether action is required.

## Reports, Exports, and Generated Artifacts

Reports and exports should explain what was found, how it was produced, what source media or records it came from, what tool/model/action produced it, what confidence, validation, or provenance is available, and what limitations apply.

- Human-readable reports and machine-readable outputs must use terminology consistent with the ontology-alignment rule.
- Reports must not include unnecessary sensitive details, real case imagery, or graphic descriptors.

## API, CLI, and MCP Surfaces

Visible text in API docs, CLI help, CLI errors, MCP tool names, MCP tool descriptions, and MCP structured outputs must follow Project VIC terminology and tone.

- API descriptions must use consistent field names and terminology.
- CLI commands must provide clear, operator-friendly help text and actionable errors.
- MCP tools must use safe, bounded descriptions that explain what the tool does without exaggerating capability.
- MCP, API, CLI, and GUI terminology must remain consistent unless a difference is intentional and documented.
- Do not expose internal implementation jargon to operators unless it is necessary for troubleshooting.

## Documentation and Communications

Documentation, release notes, websites, training materials, and public-facing copy must follow Project VIC terminology, avoid unsupported claims, avoid overpromising AI or automation, identify limitations honestly, use benign synthetic examples, avoid real case details, distinguish nonprofit mission language from product capability language, and keep screenshots and diagrams accessible and professional.

## Specs and Releases

Release notes must call out operator-visible copy, layout, report, export, terminology, accessibility, or workflow changes.

## Spec Kit Requirements

For visible-surface changes:

- `/speckit.specify`: identify affected user-visible surfaces, terminology, accessibility, brand, report, export, and documentation impact.
- `/speckit.plan`: define design-system tokens/components, copy changes, accessibility checks, screenshots/docs updates, and terminology alignment.
- `/speckit.tasks`: create explicit tasks for GUI/API/CLI/MCP/docs/report copy and accessibility updates.
- `/speckit.implement`: use approved components, terminology, and accessible patterns.
- `/speckit.analyze`: verify visible surfaces remain consistent with brand, terminology, accessibility, ontology alignment, and release documentation.

## Required Agent Output

For brand-relevant or visible-surface changes, the final agent response must summarize visible surfaces affected, brand/design-system elements used, new or changed terminology, accessibility checks performed, screenshots/docs/reports/release notes updated, design-system gaps found, and intentionally deferred brand or accessibility work.
<!-- POLICY-END PVIC-BRAND-DESIGN-SYSTEM -->

<!-- POLICY-BEGIN PVIC-CROSS-PLATFORM 8a3b5ae0ce536b4f87b1edeb660d96d8208e8611e33e69dba22f2d4c5e8e4693 -->

# Cross-Platform and Deployment Compatibility

Project VIC tools are built for investigators, digital forensics examiners, task forces, nonprofits, and agencies with widely varying technical resources. Tools must support users on Windows workstations, Linux hosts, WSL, Docker-compatible systems, GPU servers, offline systems, and air-gapped environments.

Cross-platform does not mean every component must run natively on every operating system. It means Project VIC tools must provide a supported path for common platforms, with Ubuntu/Linux containers as the default free-first baseline.

Project VIC tools must not require paid operating systems, paid cloud services, paid databases, paid queues, paid identity providers, or proprietary commercial infrastructure unless explicitly documented as optional.

## Free-First and Dependency Isolation

- Prefer free and open-source operating systems, runtimes, databases, queues, containers, and development tools.
- Ubuntu/Linux container support is the default deployment baseline unless the repository explicitly documents another baseline.
- Do not require global installation of language runtimes, Python packages, Node packages, system libraries, model weights, or forensic tools when a containerized, virtualenv, venv, uv, pipx, Conda, or documented isolated environment is feasible.
- Local development setup must avoid polluting the user's workstation.
- Runtime artifacts, caches, logs, temporary files, extracted content, generated files, and model downloads must stay under documented project, case, cache, or run directories.
- Do not assume internet access during install, startup, inference, validation, or normal operation unless the feature explicitly requires it.

## Path Handling

- Use `pathlib.Path` in Python and platform-safe path handling in API, GUI, and frontend code.
- Never concatenate filesystem paths with raw `/` or `\\` strings.
- Normalize and validate evidence paths before use; reject traversal and paths outside allowed roots.
- Preserve source evidence read-only. Do not write to mounted evidence, forensic images, original media, or operator-selected source directories unless explicitly documented and confirmed.
- Handle Windows, WSL, Linux, and container path differences explicitly.
- Do not assume case-insensitive filesystems.
- Do not assume Unix permissions are preserved on Windows-mounted paths.
- Handle spaces, Unicode, long paths, reserved Windows filenames, and path separators safely.
- Avoid hardcoded `/tmp`, `/home`, drive letters, user profile paths, or shell-specific behavior.
- Normalize timestamps and time zones in logs, exports, audit records, reports, and generated artifacts.

## Process and External Tools

- Invoke external tools with argument arrays, not shell strings.
- Do not use `shell=True` or shell pipelines unless there is a documented reason and inputs are strictly controlled.
- Detect `ffmpeg`, EWF/mount tooling, archive tools, OCR engines, GPU availability, Docker, model weights, ontology files, and other optional dependencies before use.
- Surface actionable errors when optional dependencies are absent.
- Do not silently skip required processing steps because a dependency is missing.
- External tool versions that affect output, provenance, or reproducibility must be logged or recorded in job metadata.
- Commands that touch evidence, derived artifacts, exports, or mounted filesystems must preserve provenance and avoid mutating source evidence.

## Containers and Deployment

- Project VIC services should be container-first unless the repository documents why native deployment is required.
- Docker Compose profiles such as `backend`, `api`, `gui`, `worker`, `edge`, `gpu`, and `dev` must remain independently usable when provided.
- Container services must support documented environment-variable configuration and must not require source-code edits for normal deployment.
- Container-created files must not become unusable by the host user. Document UID/GID behavior and support configurable user IDs where needed.
- Do not assume root access inside or outside containers unless explicitly required and documented.
- Avoid writing generated files as root into bind-mounted host directories.
- Exposed ports, volumes, mounts, profiles, and network assumptions must be documented.
- Production deployment paths must not depend on development-only bind mounts, debug servers, auto-reload behavior, or permissive CORS settings.
- Windows clients and WSL/Linux paths must be documented where behavior differs.

## CPU, GPU, and Model Runtime Compatibility

- CPU-only mode must remain valid unless the feature is explicitly documented as GPU-only.
- GPU support is an acceleration path, not a hard requirement.
- GPU availability must be detected at runtime.
- NVIDIA CUDA, ROCm, DirectML, Metal, or other GPU-specific paths must not break CPU-only operation.
- Model inference code must document hardware assumptions, memory requirements, fallback behavior, and expected degradation when GPU acceleration is unavailable.
- GPU-specific containers or profiles must fail cleanly when required drivers, runtimes, or devices are unavailable.

## Offline and Air-Gapped Operation

- Air-gapped deployments must not download packages, containers, models, fonts, JavaScript assets, telemetry libraries, external schemas, or validation assets at runtime.
- Provide documented ways to prefetch, mirror, vendor, or bundle required images, packages, model weights, ontology files, schemas, and validation assets.
- Features requiring internet access must be optional or fail closed with clear operator guidance.
- Do not add telemetry, analytics, crash reporting, auto-update checks, or external callbacks unless explicitly documented, disabled by default, and appropriate for law-enforcement deployment.
- Offline mode must preserve authentication, authorization, audit logging, evidence integrity, validation, and export behavior.

## Configuration

- Configuration must be explicit, documented, and environment-driven where practical.
- Do not hardcode hostnames, ports, credentials, model paths, evidence paths, user directories, or agency-specific assumptions.
- Provide safe defaults for local development, but do not silently disable authentication, authorization, audit logging, or evidence protections in production-like profiles.
- Missing or invalid configuration must produce actionable errors.

## Testing

- CI should validate Linux container builds and frontend/API tests.
- Where practical, CI should include platform-relevant checks for Linux and Windows path behavior.
- Any platform-specific behavior needs explicit tests or documented manual verification.
- Integration tests that require GPU, Docker, ffmpeg, EWF tooling, mounted forensic images, model weights, or other heavy prerequisites must skip cleanly when prerequisites are unavailable.
- Tests must verify that source evidence remains read-only and that derived artifacts stay inside approved case/run/output directories.
- Tests must use benign synthetic data and must not require real CSAM, real victim data, real case identifiers, or agency-sensitive evidence.

## Required Agent Output

For platform-relevant changes, the final agent response must summarize supported execution paths affected, host platforms considered, container profiles affected, new runtime dependencies, CPU/GPU behavior, offline or air-gapped impact, path/permission/mount behavior, tests added or skipped, documentation updated, and known platform limitations.
<!-- POLICY-END PVIC-CROSS-PLATFORM -->

<!-- POLICY-BEGIN PVIC-DATA-CONTRACTS-AND-SCHEMAS 626031c08bed04dddf1e90b6691c551871e64e17b0ae8062188da86419274d14 -->

# Data Contracts and Schemas

Project VIC data contracts must remain stable, documented, deterministic, and aligned across GUI, API, CLI/pipeline, MCP, reports, exports, persistence, and ontology outputs.

Do not rename, remove, reinterpret, or reshape fields casually. Contract drift can break investigator workflows, lab integrations, scripts, MCP agents, ontology validation, and release trust.

## Contract Surfaces

Keep these aligned when behavior or data shape changes:

- API request/response schemas, OpenAPI contracts, and error objects.
- Pydantic/SQLModel/domain models and DTOs.
- TypeScript types and GUI client models.
- CLI arguments, stdout/stderr conventions, exit codes, and JSON output.
- MCP tool schemas, resource shapes, prompts, and structured results.
- JSON, CSV, XLSX, JSON-LD, Turtle/RDF, reports, and generated artifacts.
- Database schema, migration scripts, and persisted artifact metadata.

## Schema Change Rules

- Schema changes require migration notes or explicit reset guidance.
- Breaking changes require SemVer major-version consideration and migration guidance.
- Additive backward-compatible fields should be preferred when practical.
- Machine-readable outputs must be deterministic and documented.
- Field names, enum values, IDs, timestamps, hashes, confidence values, and provenance links must keep the same meaning across surfaces.
- Nullable, optional, defaulted, deprecated, and removed fields must be intentional and documented.
- Do not expose sensitive evidence paths, victim identifiers, or protected case details unless required and approved.

## Ontology and Export Requirements

- CASE/UCO/CAC/SOLVE-IT exports must use verified ontology terms and include validation examples where applicable.
- JSON-LD/RDF outputs need stable prefixes, IRIs, contexts, and SHACL validation where applicable.
- Reports and exports must point back to source media/records and the action or process that produced them when used for investigative, evidentiary, audit, or interoperability purposes.
- Human-readable reports must not make claims that differ materially from machine-readable outputs.

## Tests and Fixtures

- Add or update fixtures for every exported artifact shape and public contract change.
- Tests must cover success, invalid input, missing field, unknown field, backwards-compatibility, and error behavior where applicable.
- Committed contract fixtures must use Tier T0/T1 per `docs/test-data-handling.md`.
- Golden files are acceptable when deterministic and reviewed; update them only when the schema change is intentional.

## Spec Kit Requirements

For contract-relevant work:

- `/speckit.specify`: identify affected schemas, consumers, compatibility expectations, sensitive fields, and ontology/export impact.
- `/speckit.plan`: define contract changes, versioning, migration notes, validation commands, fixture updates, and deprecation strategy.
- `/speckit.tasks`: create tasks for each affected surface, schema, fixture, validation, docs, changelog, and migration guidance.
- `/speckit.implement`: update contracts and tests together; do not leave generated types, docs, or examples stale.
- `/speckit.analyze`: verify all contract surfaces remain aligned and breaking changes are documented.

## Required Agent Output

For contract-relevant changes, the final agent response must summarize changed schemas, affected surfaces, compatibility impact, fixtures/tests updated, ontology validation impact, migration notes, and whether a version bump or changelog entry is needed.
<!-- POLICY-END PVIC-DATA-CONTRACTS-AND-SCHEMAS -->

<!-- POLICY-BEGIN PVIC-DATABASE-PERSISTENCE-MIGRATIONS b4a665993459d484b43ea05d693fae34c9abd6dfb20f40bbd405269780b54a23 -->

# Database, Persistence, and Migrations

Project VIC persistence changes must protect evidence integrity, operator trust, auditability, local-first deployments, and upgrade safety.

Do not change persistence behavior without migrations, rollback/reset guidance, data-integrity checks, and documentation.

## Persistence Principles

- Keep source evidence read-only. Store derived artifacts, extracted content, metadata, model outputs, audit events, and provenance separately from original evidence.
- Support SQLite/local-first deployments where appropriate.
- Optional MongoDB, Postgres, object stores, queues, or other services must remain optional unless explicitly approved in Spec Kit.
- Do not silently drop, rename, overwrite, or reinterpret persisted data.
- Persisted records should include enough provenance to explain what produced them, when, with which tool/model/configuration, and from which source.
- Audit/provenance records should be append-friendly and tamper-evident where practical.

## Migrations and Compatibility

- Schema changes require migrations or explicit reset guidance for pre-production/prototype data.
- Migrations must be deterministic, repeatable, and safe to run in documented deployment profiles.
- Include rollback guidance or explain why rollback is not supported.
- Breaking persistence changes require SemVer and release-management review.
- Data migrations must not delete source evidence or operator-selected case records.
- Migration docs must describe backup/restore expectations and known limitations.

## Indexes and Performance

- Add indexes intentionally and document the query/workflow they support.
- Consider write cost, storage impact, migration time, and low-resource deployments.
- Performance-related persistence changes need before/after evidence when claimed.
- Do not add a new database/cache/search service only to solve a local performance issue without Spec Kit approval.

## Security and Privacy

- Do not persist secrets, API keys, victim identifiers, sensitive case details, or unnecessary evidence paths unless explicitly required and protected.
- Define retention/deletion behavior for temporary records, queues, caches, failed jobs, embeddings, and derived artifacts.
- Logs and errors must not dump database rows containing protected data.
- Backups, exports, and debug dumps must follow security, privacy, and synthetic-data rules.

## Tests and Verification

- Test migrations from representative prior schema versions when feasible.
- Test fresh initialization, upgrade, missing/invalid config, permission-denied storage, and rollback/reset guidance.
- Test that source evidence remains read-only and derived data stays in approved storage locations.
- Use Tier T0/T1 in committed DB tests and migrations; Tier T2 only in local environments per `docs/test-data-handling.md`.

## Spec Kit Requirements

For persistence-relevant work:

- `/speckit.specify`: identify data to persist, protected fields, retention/deletion needs, deployment profiles, and compatibility expectations.
- `/speckit.plan`: define schema changes, migrations, indexes, backup/restore guidance, rollback/reset strategy, and tests.
- `/speckit.tasks`: create tasks for models, migrations, tests, docs, changelog, and release notes.
- `/speckit.implement`: update persistence and migration tests together; do not leave schema drift undocumented.
- `/speckit.analyze`: verify data integrity, migration safety, docs, release impact, and no source-evidence mutation.

## Required Agent Output

For persistence changes, the final agent response must summarize schema/data changes, migration or reset guidance, backup/restore impact, indexes added, retention/deletion behavior, tests run, and release/migration documentation updated.
<!-- POLICY-END PVIC-DATABASE-PERSISTENCE-MIGRATIONS -->

<!-- POLICY-BEGIN PVIC-DEPENDENCY-LICENSE-SUPPLY-CHAIN 871817015cff168cc2a449ccf7e372d301fb100b59ff18f8f88d95acb6a5ff84 -->

# Dependency, License, and Supply-Chain Governance

Project VIC dependencies must be legally compatible, secure, maintainable, reproducible, offline-capable where needed, and appropriate for law-enforcement deployment.

Agents must not add dependencies casually. Every new package, model, container base, dataset, service, SDK, or tool must have a documented reason.

## Dependency Selection

- Prefer free, open-source, actively maintained dependencies with permissive or compatible licenses.
- Do not add GPL, AGPL, commercially restricted, non-redistributable, proprietary, telemetry-heavy, or paid-service dependencies without maintainer approval.
- Do not add paid SaaS, cloud-only services, managed databases, hosted queues, analytics, crash reporting, telemetry packages, or proprietary SDKs unless explicitly approved and optional.
- Avoid dependency sprawl, abandoned packages, thin wrappers, and large frameworks for small needs.
- Prefer standard library and existing project dependencies when they are sufficient.

## Review Requirements

Before adding or upgrading a dependency, check license, maintenance status, security posture, transitive risk, platform support, offline/air-gapped behavior, package size, build requirements, and deployment impact.

Document model licenses, model weights, training/evaluation datasets, container bases, redistribution limits, export controls, and required attribution where applicable.

## Reproducibility and Pinning

- Pin versions where reproducibility, security, model behavior, or release artifacts depend on them.
- Use lockfiles when the ecosystem supports them.
- Container bases must be intentional, minimal enough for the use case, and compatible with CPU/GPU/offline profiles.
- Runtime downloads of packages, models, schemas, fonts, assets, or validators are not allowed in air-gapped deployments.
- Provide prefetch, mirror, vendor, or bundle guidance for offline dependencies.

## Security and SBOMs

- Dependency vulnerability findings must be fixed, pinned, replaced, or explicitly triaged.
- Do not suppress vulnerability checks without justification.
- Generate or update SBOMs where applicable for release-capable repositories.
- Secrets and credentials must not be embedded in dependency configuration, package registries, container images, model bundles, or examples.

## Spec Kit Requirements

For dependency-relevant work:

- `/speckit.specify`: identify why the dependency is needed, affected surfaces, deployment profiles, license constraints, and offline requirements.
- `/speckit.plan`: compare alternatives, document license/security/maintenance review, versioning/pinning, SBOM impact, and fallback behavior.
- `/speckit.tasks`: create tasks for dependency update, tests, docs, vulnerability checks, SBOM/release artifacts, and changelog.
- `/speckit.implement`: add only approved dependencies and update lockfiles/docs/tests together.
- `/speckit.analyze`: verify license compatibility, security posture, offline behavior, and release artifacts.

## Required Agent Output

For dependency changes, the final agent response must summarize dependencies added/updated/removed, why they are needed, license/security review, offline impact, lockfile/SBOM changes, tests run, and any maintainer approval needed.
<!-- POLICY-END PVIC-DEPENDENCY-LICENSE-SUPPLY-CHAIN -->

<!-- POLICY-BEGIN PVIC-DOCUMENTATION-STANDARDS c282c39d9e58ee60e4607d521d1f714afe89fa5b820be691e09fee7318585d91 -->

# Documentation Standards

Project VIC documentation must help police officer users succeed without assuming they are software developers, system administrators, or command-line users.

This rule complements `brand-design-system.mdc`. Use the brand/design rule for Project VIC terminology, tone, accessibility, and trauma-aware language. Use this rule for documentation structure, audience, readability, and practical operator guidance.

## Primary Audiences

Write documentation for these audiences, in this order:

- Police officer users: non-technical or semi-technical users who need to install, open, operate, and trust the tool.
- Local IT support staff: technical helpers who may install dependencies, configure systems, troubleshoot network or permission problems, and support police users.
- Technical contributors: developers, maintainers, integration partners, and agents who need architecture, testing, release, and contribution details.

Do not make police users read developer-focused material before they can understand what the tool does, when to use it, how to start, and where to get help.

## README Requirements

Each repository's `README.md` should be written primarily for the police officer user.

The README should answer:

- What is this tool?
- Who is it for?
- What problem does it help solve?
- What does it not do?
- What data is safe to use during setup, training, and testing?
- How does a user start the tool in the simplest supported way?
- When should the user ask local IT or Project VIC support for help?
- Where are the detailed user, IT support, and developer documents?

Keep command-line setup out of the main README unless it is the only supported path. If commands are unavoidable, explain what they do in plain language and link to the IT support documentation.

## Required Documentation Structure

Every Project VIC software repository should include a root `docs/` folder.

Use this structure unless the repository has a documented reason to choose another layout:

- `docs/user-guide.md`: step-by-step police user guide.
- `docs/it-support-guide.md`: installation, configuration, troubleshooting, updates, backups, permissions, and local environment support for IT staff.
- `docs/admin-guide.md`: administrative actions, roles, configuration, retention, audit, and security settings when applicable.
- `docs/troubleshooting.md`: common problems, symptoms, likely causes, and safe fixes.
- `docs/glossary.md`: project-specific terms, acronyms, and Project VIC terminology.
- `docs/developer-guide.md`: development setup, architecture, tests, release workflow, and contribution guidance.

Small repositories may combine files, but they must still clearly separate police user instructions from IT/developer instructions.

## Reading Level and Style

Write general user documentation at about a 10th grade reading level.

- Use short sentences and plain words.
- Prefer active voice.
- Define acronyms the first time they appear.
- Use consistent names for buttons, screens, files, and roles.
- Use numbered steps for procedures.
- Put warnings before the action that creates risk.
- Explain why a risky or confusing step matters.
- Avoid unexplained jargon, vendor buzzwords, and internal developer shorthand.

Technical documentation may include deeper details, but it should still include plain-language summaries and clear headings.

## Command-Line and Setup Guidance

Assume most police officer users do not know shells, terminals, paths, environment variables, package managers, containers, or Git.

When documentation includes commands:

- Say who should run the command: police user, local IT, developer, or maintainer.
- Say where to run it: Windows PowerShell, Command Prompt, macOS Terminal, Linux shell, WSL, container, or GitHub Codespaces.
- Provide copy-paste commands in fenced code blocks.
- Explain expected output or success signs.
- Explain what to do if the command fails.
- Avoid chained commands when a step-by-step sequence is safer for non-technical users.
- Do not ask police users to edit hidden files, environment variables, or system settings unless there is no safer setup path.

Prefer GUI-first or installer-style instructions for police users when the project supports them. Put advanced setup in the IT support guide.

## Screenshots, Examples, and Sample Data

Use benign synthetic examples only.

Documentation, screenshots, videos, examples, logs, issue templates, and sample outputs must not include real case data, real evidence paths, victim identifiers, investigator identifiers, credentials, agency-private facts, realistic abuse descriptions, or sensitive operational details.

Screenshots should show safe demo data and should not make sensitive fields more visible than necessary.

## Troubleshooting Standards

Troubleshooting sections should be organized by symptom, not by internal subsystem.

Use this pattern:

- What the user sees.
- What it usually means.
- What the user can safely try.
- When to ask local IT for help.
- What information is safe to share when asking for support.

Do not ask users to share logs or screenshots until the documentation explains how to check them for sensitive content.

## Accessibility and Format

Documentation should be easy to scan and accessible.

- Use clear headings.
- Keep paragraphs short.
- Use lists for steps and checklists.
- Avoid large walls of text.
- Add alt text for meaningful images.
- Do not rely on color alone in diagrams or screenshots.
- Keep links descriptive, not "click here."
- Provide printable or offline-friendly guidance when the deployment may be disconnected from the internet.

## Documentation and Release Hygiene

Documentation must match the implemented product.

Update docs and `CHANGELOG.md` when changes affect setup, installation, configuration, user workflows, roles, permissions, security behavior, evidence handling, exports, reports, supported platforms, troubleshooting, release steps, or known limitations.

Do not claim that a feature, platform, installer, workflow, or integration is supported unless it is implemented and tested or clearly marked as planned.

## Spec Kit Requirements

For documentation-relevant work:

- `/speckit.specify`: identify police user documentation, IT support documentation, developer documentation, readability, safety, and training needs.
- `/speckit.plan`: define the documentation files to update, audience split, screenshots/examples policy, support workflow, and validation approach.
- `/speckit.tasks`: create explicit tasks for README, user guide, IT support guide, troubleshooting, glossary, changelog, and release notes where applicable.
- `/speckit.implement`: update documentation with the behavior changes, using synthetic examples and clear audience labels.
- `/speckit.analyze`: verify documentation matches implemented behavior, avoids sensitive content, and separates police user guidance from IT/developer guidance.

## Required Agent Output

For documentation changes, the final agent response must summarize affected documentation files, intended audiences, readability and accessibility considerations, brand/design alignment, synthetic-data safeguards, docs/changelog updates, and any known documentation gaps.
<!-- POLICY-END PVIC-DOCUMENTATION-STANDARDS -->

<!-- POLICY-BEGIN PVIC-FOUR-SURFACE-REVIEW 616130da6eeef8a32baf7cc21f896946e1075145b3e8fd60b70ed27f305a9afe -->

# Four-Surface Capability Review

Project VIC applications should expose major capabilities through four user and automation surfaces:

1. GUI / UI
2. API
3. CLI / pipeline
4. MCP server

The four surfaces do not need identical interaction patterns, but they must provide equivalent access to the same core capability, validation rules, authorization model, ontology mappings, provenance behavior, audit events, outputs, and error semantics.

Silent surface drift is incomplete work.

**`1.0.0` MVP:** When intake, the release spec, and users require it, the MVP must provide applicable four-surface equivalence for declared MVP capabilities. Record required surfaces in MVP exit criteria and the release target section. If MVP intentionally omits a surface, document the gap, supported alternative, and operator impact.

**`2.0.0` platform / enterprise:** By default, Project VIC tools provide applicable four surfaces for declared production capabilities unless a maintainer designates a surface as unnecessary. This is the usual target for org-wide production-intent parity.

**Before `1.0.0`:** Missing surfaces are allowed when documented per milestone. **`1.x.x`** may add surfaces toward `2.0.0` without requiring all four at every patch.

This rule applies to Project VIC applications and services. Libraries, documentation-only repositories, ontology-only repositories, and internal build utilities may document why one or more surfaces are not applicable.

## Required Surfaces

| Surface | Primary users | Expected role |
|---|---|---|
| GUI / UI | ICAC investigators, forensic examiners, analysts, and operators | Human-facing workflows, visibility, review, configuration, reporting, and operational control |
| API | GUI clients, lab systems, integrations, scripts, and service-to-service workflows | Programmatic access, job control, schemas, status, artifacts, auth, and integration contracts |
| CLI / pipeline | Batch processing, offline operation, worker containers, direct operator runs, and automation scripts | Scriptable execution, local processing, container entry points, diagnostics, and reproducible workflows |
| MCP server | AI agents, investigator assistants, triage agents, and tool-using automation | Agent-safe tools, resources, prompts, structured outputs, and ontology-grounded automation |

## Shared Core Logic

- Business logic must live in shared application/service layers.
- GUI, API, CLI, and MCP surfaces should call the same underlying services rather than reimplementing feature logic independently.
- Validation, authorization, provenance creation, audit logging, ontology mapping, export generation, and error handling must be consistent across surfaces.
- Surface-specific adapters may translate inputs and outputs, but they must not change the meaning of the operation.
- If a capability is intentionally unavailable on a surface, document why, describe the supported alternative, identify whether the gap is temporary or permanent, and name the human decision or milestone that justifies it.
- Do not create placeholder GUI/API/CLI/MCP surfaces merely to satisfy this rule. Missing surfaces must fail honestly or remain undiscoverable until implemented.

## Surface Equivalence Requirements

When adding, changing, refactoring, or removing a capability, review all four surfaces.

### GUI / UI

- Does the operator need visibility, controls, filters, warnings, progress, review screens, or clearer terminology?
- Are errors actionable for investigators and forensic examiners?
- Are sensitive values redacted or minimized?
- Are outputs, reports, and status indicators consistent with API, CLI, and MCP behavior?
- Does the GUI use terminology aligned with CASE/UCO/CAC/SOLVE-IT concepts where applicable?

### API

- Does the capability require a new or changed endpoint, request schema, response schema, auth requirement, job status, artifact reference, or error response?
- Are OpenAPI or other API contracts updated?
- Are API errors consistent with GUI, CLI, and MCP behavior?
- Are authorization, audit, provenance, and validation enforced at the service boundary?
- Are ontology-aligned fields, identifiers, and serialized outputs documented?

### CLI / Pipeline

- Does the capability require a new or changed command, flag, config value, environment variable, container entry point, or batch workflow?
- Does direct CLI use still work outside the GUI?
- Does containerized execution still work?
- Does CPU-only and offline execution still work where applicable?
- Are stdout, stderr, exit codes, logs, and output files suitable for scripts and forensic workflows?
- Are generated artifacts consistent with API, GUI, and MCP outputs?

### MCP Server

- Does the capability require a new or changed MCP tool, resource, prompt, schema, or structured output?
- Is the MCP surface safe for agent use, with bounded inputs, clear descriptions, and predictable outputs?
- Are tool names, descriptions, arguments, and return objects aligned with Project VIC terminology and ontology mappings?
- Does the MCP server avoid exposing sensitive evidence, secrets, victim identifiers, or unnecessary case details?
- Are MCP errors actionable to the agent without leaking protected data?
- Can an agent discover and use the capability without relying on hidden assumptions?

## Reports, Exports, and Artifacts

For changes affecting reports, exports, generated artifacts, or machine-readable output:

- Keep JSON, CSV, XLSX, JSON-LD, Turtle/RDF, human-readable reports, API responses, CLI outputs, and MCP outputs semantically consistent.
- Outputs must point back to source media, source records, and the action or process that produced them when used for investigative, evidentiary, audit, or interoperability purposes.
- Terminology and identifiers must remain aligned with the ontology-alignment rule.
- Do not allow the GUI report, API response, CLI output, and MCP result to describe materially different facts.

## Spec Kit Requirements

For any feature, fix, refactor, schema change, export change, workflow change, or operator-visible behavior change:

- `/speckit.specify`: identify affected GUI, API, CLI, and MCP surfaces. If a surface is missing, unaffected, or intentionally unnecessary, explain why and whether MVP (`1.0.0`) or `2.0.0` parity is expected.
- `/speckit.plan`: describe shared service-layer changes, surface adapters, contracts, ontology mappings, validation, authorization, audit, provenance, output consistency, and staged surface rollout.
- `/speckit.tasks`: create explicit tasks for each affected or required surface. Do not leave surface updates as generic follow-up work.
- `/speckit.implement`: update all affected surfaces and tests. Do not complete one surface while silently leaving the others stale.
- `/speckit.analyze`: verify surface parity across code, contracts, schemas, docs, examples, tests, changelog, and deployment guidance, or verify that missing surfaces have documented human-approved exceptions.

## Required Tests

Surface-relevant changes must include focused tests or documented manual verification for:

- Shared service-layer behavior.
- GUI-visible behavior where practical.
- API endpoint/schema behavior.
- CLI command/config/output behavior.
- MCP tool/resource/schema behavior.
- Authorization and validation consistency.
- Audit and provenance consistency.
- Export/report consistency.
- Ontology-aligned output consistency.
- Error behavior across surfaces.

Tests may skip cleanly when platform-specific prerequisites are unavailable, but skipped tests must not hide missing implementation.

## Required Agent Output

For every surface-relevant change, the final agent response must summarize the capability changed, GUI impact, API impact, CLI/pipeline impact, MCP impact, shared service-layer changes, reports/exports/artifacts affected, ontology mappings affected, tests added or updated, documentation updated, and any surfaces intentionally left unchanged, missing until a milestone, or human-designated unnecessary.
<!-- POLICY-END PVIC-FOUR-SURFACE-REVIEW -->

<!-- POLICY-BEGIN PVIC-HUMAN-REVIEW-AND-RISK-GATES 2691a4aefd5260d06167c66246b47f2015abbba970320ef40d31e56fdce17711 -->

# Human Review and Risk Gates

High-risk Project VIC changes require explicit human review before merge or release. Agent productivity must not bypass human accountability for evidence, security, privacy, compliance, ontology, model, deployment, or release risk.

Agents must identify high-risk work, state why it is high risk, and summarize residual concerns.

## High-Risk Changes

Human review is required for changes involving:

- Authentication, authorization, secrets, access control, or security boundaries.
- Evidence handling, source media access, deletion, cleanup, archive extraction, mounted forensic images, or artifact export.
- Audit logs, provenance records, report/export semantics, or ontology mappings.
- Database persistence, migrations, retention/deletion, backups, or data recovery.
- Model/AI inference, confidence thresholds, model updates, model downloads, or benchmark claims.
- Dependency, license, container base, supply-chain, SBOM, or vulnerability changes.
- GitHub Actions, release automation, versioning, changelog, release artifacts, or deployment profiles.
- MCP tools that expose data, perform writes, trigger processing, or affect operator workflows.
- Destructive operations, bulk changes, irreversible migrations, or broad refactors.

## Review Gates

- No auto-merge for high-risk work.
- Destructive or irreversible operations require extra review and clear operator confirmation patterns.
- Security-relevant releases must not proceed with unresolved critical/high risks unless explicitly accepted by maintainers.
- Deferred work must not be described as complete.
- CI failures, missing tests, skipped required surfaces, or undocumented migrations block release-bound work.

## Reviewer Checklist

Reviewers and agents must consider:

- Security, privacy, and compliance impact.
- Evidence integrity and source read-only behavior.
- No-stubs behavior and honest failure modes.
- GUI/API/CLI/MCP surface parity.
- Ontology alignment and validation.
- Tests, fixtures, and test-data tier/channel compliance (`docs/test-data-handling.md`).
- Documentation, changelog, migration, and release impact.
- Dependency/license/supply-chain risk.
- Residual risks, limitations, and operator guidance.

## Spec Kit Requirements

For high-risk work:

- `/speckit.specify`: identify risk class, affected users, protected data, failure impact, and required human review.
- `/speckit.plan`: define risk controls, test evidence, rollback/mitigation, review gates, and approval points.
- `/speckit.tasks`: create tasks for tests, docs, release notes, review evidence, and risk summary.
- `/speckit.implement`: do not merge risky behavior without review-ready evidence.
- `/speckit.analyze`: verify risks were addressed, deferred risks are documented, and release gates are satisfied.

## Required Agent Output

For high-risk changes, the final agent response must summarize risk category, why human review is required, affected protected data/surfaces, destructive or irreversible behavior, tests and mitigations, docs/release impact, residual concerns, and approval still needed.

<!-- POLICY-END PVIC-HUMAN-REVIEW-AND-RISK-GATES -->

<!-- POLICY-BEGIN PVIC-MCP-AGENT-SAFETY 3c5bcc90760ff34a038b50890d3d0d8f2b0f80c1ecf4be47a2af7687caaa95f8 -->

# MCP and Agent Safety

Project VIC MCP servers, tools, resources, and prompts must be safe for agent use, bounded in scope, ontology-grounded where applicable, and discoverable without hidden assumptions.

MCP is a first-class surface, but it must not become a path for leaking evidence, secrets, victim identifiers, sensitive case details, or non-public operational information.

## Tool Design

- Tool names must be stable, action-oriented, specific, and consistent with Project VIC terminology.
- Tool descriptions must state what the tool does, required inputs, side effects, limits, and safe failure behavior without exaggerating capability.
- Inputs must be bounded with explicit schemas, types, size limits, path constraints, enum values, and validation.
- Outputs should be structured objects, not prose-only blobs.
- Return ontology-aligned identifiers, provenance references, validation status, and actionable errors where applicable.
- Do not expose raw sensitive evidence unless explicitly approved by repository documentation and deployment context.

## Safety Boundaries

- MCP tools must call shared service layers rather than reimplementing business logic.
- Tools must enforce the same validation, authorization, audit, provenance, and no-stubs behavior as GUI/API/CLI surfaces.
- Tools must not perform destructive actions without explicit confirmation patterns.
- Risky operations should support dry-run or preview mode where practical.
- Tools must not silently mutate source evidence, operator-selected source directories, or original media.
- MCP resources/prompts/tools must not leak secrets, case details, victim identifiers, unnecessary evidence paths, or sensitive hash intelligence.

## Agent-Usable Errors

- Errors must be structured, safe, and specific enough for an agent to recover or report the issue.
- Do not include protected data in error messages.
- Missing dependencies, invalid inputs, unsupported configurations, and permission failures must return honest actionable errors, not fake success.

## Prompts and Resources

- Prompts must use benign synthetic examples and trauma-aware language.
- Resources should expose documentation, schemas, capabilities, and safe metadata rather than sensitive case content.
- MCP schemas and examples must stay aligned with API, CLI, GUI terminology, ontology mappings, and data-contract rules.

## Spec Kit Requirements

For MCP-relevant work:

- `/speckit.specify`: identify agent users, tool/resource/prompt purpose, protected data, side effects, and affected surfaces.
- `/speckit.plan`: define schemas, validation, authorization, audit/provenance, ontology mapping, dry-run/confirmation behavior, and error structure.
- `/speckit.tasks`: create tasks for shared service logic, MCP adapter, tests, docs, schemas, and examples.
- `/speckit.implement`: implement real tool behavior through shared services with bounded inputs and structured outputs.
- `/speckit.analyze`: verify safety, discoverability, no sensitive leakage, and surface equivalence.

## Required Agent Output

For MCP changes, the final agent response must summarize tools/resources/prompts changed, inputs/outputs, side effects, protected data exposure, safety controls, ontology alignment, tests, docs, and any human-review requirements.
<!-- POLICY-END PVIC-MCP-AGENT-SAFETY -->

<!-- POLICY-BEGIN PVIC-MODEL-AI-PIPELINE-GOVERNANCE 00089778ffb0da65dc36e3e3891ccf2c6e7ad4891c290297bdea55d1ceaed1c9 -->

# Model and AI Pipeline Governance

Project VIC model and AI features must support investigators without overstating certainty. Model outputs are analytic assistance, not determinations of fact, guilt, victim status, or legal classification.

AI/ML changes must preserve forensic integrity, security, privacy, ontology alignment, surface equivalence, and human review expectations.

## Model Output Requirements

- Label model outputs as classifications, detections, predictions, scores, or analytic results, not facts.
- Store model name, version, weights/checksum, runtime, parameters, confidence/score, thresholds, input artifact references, and provenance.
- Distinguish model confidence from forensic certainty.
- Do not hide false positives, false negatives, uncertainty, threshold limitations, or unsupported classes.
- Operator-facing text must explain what the model did, what it did not do, and what human review is expected.

## Model Updates and Evaluation

- Model updates require benchmark/evaluation notes before merge or release.
- Evaluation must document dataset type, size, class coverage, metrics, hardware, runtime, and limitations.
- Use benign synthetic or approved non-sensitive evaluation data unless repository policy explicitly permits another safe dataset.
- Never use real CSAM, real victim data, real agency data, or sensitive investigative material in model tests, docs, screenshots, or benchmark logs.
- Performance claims require measured benchmarks and output-equivalence checks.

## Detection Quality Baselines and Regression Gates

Repositories that ship detectors, classifiers, or scoring models exposed to operators must protect detection quality the same way they protect code quality:

- Maintain a versioned evaluation corpus (or a committed public-safe slice of one) and a repeatable evaluation command that reports task-appropriate metrics such as ROC-AUC, PR-AUC, EER, false-positive rate at a fixed operating point, and calibration error.
- Add a CI regression gate on the committed evaluation slice with checked-in metric floors. A change to a model, weight file, threshold, fusion logic, or preprocessing step that degrades gated metrics must block merge unless a maintainer documents acceptance of the regression.
- Ratchet metric floors only through merged, verified improvements (see `auto-research.mdc` for the experiment loop; its measurement discipline applies to detection-quality metrics, not only speed).
- A detector whose required dependencies, weights, or runtime are unavailable must be reported as unavailable and must degrade the overall result honestly (capped, labeled, and surfaced to the operator). Passing process gates while the flagship detector silently does not run is a release-blocking defect, not a warning.
- Record the evaluation dataset version, hardware profile, and metric results in the spec's research notes or a documented results location so claims are reproducible.

## Research-to-Production Graduation

New model or detector candidates follow a staged path; do not skip stages:

1. **Candidate review:** record source, code/weights availability, license and redistribution rights, runtime fit (CPU/offline), and evidence quality in a candidate matrix before any code lands.
2. **Isolated prototype:** implement in a prototype namespace, branch, or worktree with no GUI/API/CLI/MCP, report, export, audit, or ontology exposure. Prototypes fail honestly and are labeled diagnostic-only.
3. **Recorded decision:** every prototype ends with an explicit **graduate**, **iterate** (with a revisit date or milestone), or **retire** decision recorded in the spec. Prototypes must not remain dark indefinitely without a recorded owner and revisit point.
4. **Implementation spec:** graduation to production requires a follow-up spec covering benchmark evidence, calibration or explicit uncalibrated labeling, four-surface contracts, provenance/ontology mapping, offline prestaging, and human review of operator-facing claims.

## Deployment and Runtime

- CPU/GPU behavior, memory assumptions, model precision/quantization, and fallback behavior must be documented.
- GPU acceleration must not break CPU-only operation unless the feature is explicitly GPU-only.
- Model downloads must support offline/air-gapped workflows where applicable.
- Model weights, licenses, redistribution limits, checksums, and source URLs must be documented.
- Do not send evidence, derived artifacts, embeddings, thumbnails, prompts, or investigative metadata to external model APIs unless explicitly approved for the deployment context.

## Provenance and Ontology

- Model inference, preprocessing, postprocessing, thresholding, and export generation are provenance actions.
- CASE/UCO/CAC/SOLVE-IT outputs must represent model results with tool/model provenance, confidence, and validation status where applicable.
- Reports, API, CLI, GUI, and MCP outputs must describe model results consistently.

## Spec Kit Requirements

For model/AI-relevant work:

- `/speckit.specify`: identify model purpose, users, supported classes, inputs/outputs, thresholds, human-review expectations, protected data, and success metrics.
- `/speckit.plan`: define model versioning, provenance, evaluation method, benchmark data, deployment profile, CPU/GPU behavior, license, and offline handling.
- `/speckit.tasks`: create tasks for implementation, tests, evaluation evidence, docs, changelog, release notes, and model artifact metadata.
- `/speckit.implement`: implement real inference/evaluation behavior with documented thresholds and no fake detections.
- `/speckit.analyze`: verify model claims, provenance, evaluation evidence, docs, and surfaces remain aligned.

## Required Agent Output

For model/AI changes, the final agent response must summarize model/version/weights, thresholds, evaluation evidence, false-positive/false-negative considerations, provenance captured, CPU/GPU/offline behavior, sensitive-data controls, tests, and docs/release updates.
<!-- POLICY-END PVIC-MODEL-AI-PIPELINE-GOVERNANCE -->

<!-- POLICY-BEGIN PVIC-NO-STUBS 670b0799750d2d5a60dab71a5b88eb6c761879a1f58bb268fbeeb13442470068 -->

# No Stubs

Project VIC development must not leave fake, placeholder, or TODO-only behavior in production paths.

A feature is not complete because files, routes, buttons, commands, tools, or schemas exist. A feature is complete only when the documented behavior is implemented, connected to applicable surfaces, tested or manually verified, and able to fail honestly when prerequisites are unavailable.

Scaffolding is allowed only when it is not exposed as a working feature and is clearly marked as non-production. Production paths must either implement the documented behavior or fail with a typed, actionable error.

## Prohibited Production Behavior

Never add or leave the following in production paths:

- Placeholder implementations.
- Fake success responses.
- TODO-only endpoints.
- Hardcoded demo results.
- Mock returns presented as real output.
- Silent no-op behavior.
- Disabled checks that make tests pass.
- Fake Project VIC hash lookup results.
- Fake model detections or classifications.
- Fake provenance records.
- Fake audit events.
- Fake ontology mappings or validation results.
- Fake export files.
- Fake database writes.
- Fake authentication or authorization decisions.
- Catch-all exception handling that hides missing implementation.
- UI controls that appear functional but do not perform real work.
- MCP tools that return plausible-looking results without invoking real functionality.

## Required Behavior by Surface

### GUI / UI

- GUI controls must call real capabilities or be hidden/disabled until the capability exists.
- If a capability is unavailable, show clear operator-facing text explaining what is missing.
- Do not show fake counts, detections, statuses, reports, or progress.
- Do not mark jobs, exports, validations, or uploads successful unless the underlying operation actually succeeded.

### API

- API routes must perform the documented operation or return a typed, actionable error.
- API schemas must match real request and response behavior.
- Do not return placeholder JSON, fake IDs, fake job states, fake artifacts, or fake validation results.
- Missing dependencies must produce appropriate 4xx or 5xx errors without leaking sensitive details.

### CLI / Pipeline

- CLI and pipeline code must process real inputs, media, hashes, artifacts, and configuration.
- CLI commands must exit non-zero when required inputs, dependencies, configuration, or services are missing.
- Do not print fake success messages.
- Do not create fake output files to satisfy downstream steps.
- Batch workflows must fail clearly rather than silently skipping required processing.

### MCP Server

- MCP tools must invoke real underlying capabilities or return structured, actionable errors.
- Do not expose tools that only describe what they would do.
- Do not return fake investigation results, ontology mappings, job IDs, hash matches, or artifact references.
- MCP tool descriptions must not claim capabilities that are not implemented.
- Agent-facing errors must be safe, bounded, and specific enough for the agent to recover or report the issue.

## Dependencies and Prerequisites

If an external dependency is unavailable, detect it and fail honestly. Missing dependencies must never produce fake success paths.

Examples include GPU runtime, `ffmpeg`, EWF or forensic image mounting tools, Docker or container runtime, database services, Project VIC lookup data, model weights, ontology files, SHACL validators, API keys, mounted evidence, writable output directories, network access when required, and offline bundle assets.

## Tests and Fixtures

- Tests may use mocks, fixtures, synthetic data, monkeypatching, and fake services only when the test clearly verifies the behavior under test.
- Tests must not encode fake success paths that hide missing implementation.
- Use benign synthetic fixtures. Never require real CSAM, real victim data, real agency data, or sensitive investigative material.
- When a production dependency is mocked in a test, include at least one test or documented verification path proving the real integration works or fails honestly.
- Tests should verify both success and failure behavior.
- Tests should confirm that incomplete configuration, unavailable dependencies, invalid inputs, and unsupported platforms produce actionable failures.

## Spec Kit Requirements

For all Spec Kit-driven work:

- `/speckit.specify`: define observable behavior, required inputs, expected outputs, failure modes, and applicable surfaces.
- `/speckit.plan`: identify real implementation paths, dependencies, validation points, tests, and any intentionally deferred work.
- `/speckit.tasks`: create implementation and test tasks for each required behavior. Do not use generic "wire up later" tasks.
- `/speckit.implement`: implement real behavior. Do not satisfy requirements with stubs, TODOs, fake returns, disabled checks, or documentation-only claims.
- `/speckit.analyze`: verify that code, tests, docs, GUI, API, CLI, MCP, reports, exports, and changelog do not claim functionality that is incomplete.

A Spec Kit task is not complete until the planned behavior is implemented, connected to applicable surfaces, tested or manually verified, and documented where appropriate.

## Acceptable Deferred Work

Deferred work is allowed only when it is explicit and safe:

- The incomplete capability must not be exposed as working.
- The limitation must be documented in the spec, plan, task list, README, or issue tracker.
- The GUI/API/CLI/MCP surface must hide, disable, or clearly reject the unavailable capability.
- The code must fail with an actionable error if an operator or agent tries to use the unavailable path.
- The changelog or release notes must not describe deferred work as complete.

## Required Agent Output

For every implementation task, the final agent response must summarize what real behavior was implemented, which surfaces were connected, which dependencies are required, what happens when dependencies are missing, what tests or manual verification were added, whether any work remains deferred, and why deferred work is not exposed as a working feature.
<!-- POLICY-END PVIC-NO-STUBS -->

<!-- POLICY-BEGIN PVIC-OBSERVABILITY-AUDIT-LOGGING 54e4db2a35c73b380c67a630b1e10a91616852940a7f70c7024f919f8251e9e4 -->

# Observability, Audit Logging, and Operator Status

Project VIC tools must provide useful operational visibility without leaking protected data. Logging, operator status, audit events, provenance records, and debugging traces serve different purposes and must not be conflated.

## Observability Channels

- Debug/application logs: developer and operator troubleshooting.
- Operator status: GUI/API/CLI/MCP-facing progress, warnings, failures, and next steps.
- Audit events: who/what/when/action/result for security-relevant and operator-relevant actions.
- Provenance records: what process/tool/configuration produced an artifact or result.
- Metrics/benchmarks: performance, throughput, resource use, and health signals.

Each channel should have a clear audience, retention expectation, and sensitivity level.

## Safe Logging

- Logs should be structured where practical.
- Never log secrets, API keys, credentials, victim identifiers, sensitive case details, CSAM descriptors, raw evidence content, or unnecessary evidence paths.
- Use correlation IDs, job IDs, artifact IDs, or synthetic identifiers instead of sensitive values where possible.
- Errors should be correlation-friendly without leaking protected data.
- Do not enable verbose/debug logging by default in production-like profiles.

## Audit and Provenance

- Audit events should capture actor or service identity, action, target type, timestamp, result, and safe correlation reference without exposing protected content.
- Record security-relevant events such as auth failures, config changes, export creation, deletion/cleanup actions, administrative actions, and permission denials.
- Provenance records should capture source references, tool/model version, parameters, runtime, validation status, output artifact, and producing action.
- Audit/provenance records should be append-friendly and tamper-evident where practical.

## Job Status and Long-Running Work

- Long-running jobs need progress, status, cancellation, retry/failure reason, and completion behavior.
- GUI/API/CLI/MCP must expose consistent job states and error semantics where applicable.
- Do not mark jobs successful until all required processing, validation, and artifact writes have completed.
- Failure messages should help operators fix configuration, prerequisites, permissions, or inputs.

## Spec Kit Requirements

For observability-relevant work:

- `/speckit.specify`: identify operator status needs, audit/provenance events, sensitive fields, and failure modes.
- `/speckit.plan`: define log structure, correlation strategy, audit/provenance schema, retention assumptions, and surface behavior.
- `/speckit.tasks`: create tasks for instrumentation, redaction tests, status surfaces, docs, and changelog.
- `/speckit.implement`: add safe structured events and consistent status behavior.
- `/speckit.analyze`: verify observability is useful, safe, consistent, and aligned with security/privacy rules.

## Required Agent Output

For observability changes, the final agent response must summarize logs/status/audit/provenance changed, sensitive-data redaction, correlation IDs, job-state behavior, tests added, and docs/operator guidance updated.
<!-- POLICY-END PVIC-OBSERVABILITY-AUDIT-LOGGING -->

<!-- POLICY-BEGIN PVIC-ONTOLOGY-ALIGNMENT e95e798c8ce20cf629239545538c7f33747ebc402eec82eef1cdb3bf392223fe -->

# Ontology Alignment

Project VIC software outputs, APIs, reports, exports, generated artifacts, model outputs, and provenance records must remain defensible, explainable, and interoperable with Project VIC and digital investigation ecosystems.

Project VIC tools may use internal application schemas when appropriate, but externally meaningful data must have documented mappings to CASE/UCO/CAC/SOLVE-IT concepts where suitable.

## Required Ontology Grounding

- Use Cyber-investigation Analysis Standard Expression (CASE) and Unified Cyber Ontology (UCO), commonly referenced together as CASE/UCO.
- Use CASE for cyber-investigation concepts, investigative actions, provenance, roles, and investigation-oriented exchange.
- Use UCO for cyber observables, actions, analysis, configuration, core cyber-domain concepts, identity, location, markings, patterns, roles, time, tools, data types, and shared cyber-domain vocabulary.
- Use the Crimes Against Children (CAC) Ontology for crimes-against-children investigations, operations, grooming, sextortion, victim advocacy, offender tradecraft, ICAC/task-force concepts, cross-jurisdictional concepts, legislative-process concepts, and other CAC-specific topics.
- Use SOLVE-IT concepts for digital forensic techniques, weaknesses, mitigations, objectives, performed techniques, tool capabilities, and tool-profile descriptions when documenting analysis methods.
- Do not invent ad-hoc field names in CASE/UCO/CAC/SOLVE-IT exports when a canonical class or property exists.
- Do not invent ontology classes, properties, prefixes, IRIs, or namespaces. Verify terms against ontology source, generated docs, SDK bindings, or checked-in ontology artifacts before using them.
- If a needed concept is absent from CASE/UCO/CAC/SOLVE-IT, document the gap and prefer upstream extension over local vocabulary drift.

## Source of Truth

When mapping concepts, prefer sources in this order:

1. Checked-in ontology/version artifacts pinned by the repository.
2. Generated language bindings or mapping helpers from the CASE/UCO SDK.
3. Official ontology documentation and source repositories.
4. Existing Project VIC mappings in the repository.
5. New extension proposal or documented gap.

Official sources:

- CASE Ontology: https://github.com/casework/CASE.git
- Unified Cyber Ontology: https://github.com/ucoProject/UCO.git
- Crimes Against Children Ontology: https://github.com/Project-VIC-International/CAC-Ontology
- CASE/UCO SDK: https://github.com/vulnmaster/CASE-UCO-SDK.git

Use the CASE/UCO SDK and its MCP server (`case-uco`) to help automate class, property, relationship mapping, data serialization, and SHACL validation where available.

Use the CASE/UCO SDK to get or update ontology bindings for Python, Java, C#, and Rust projects.

Reference the CASE/UCO SDK docs folder and `ECOSYSTEM.md` to understand available CASE/UCO open-source capabilities for developers.

When CASE/UCO/CAC/SOLVE-IT do not provide adequate concept coverage, develop extension ontologies instead of creating isolated local vocabularies. Follow the Community Playground Guidelines.

## Project VIC Mapping Requirements

- Model analytic detections, classifier results, object detections, media classifications, model outputs, and confidence values as analytic results with model/tool provenance.
- Hashing and Project VIC lookup features must distinguish legacy lookup hashes such as MD5 from forensic integrity hashes such as SHA-256.
- Forensic image mounting, archive extraction, frame sampling, media preprocessing, OCR, transcription, object detection, hash lookup, deduplication, and export generation are provenance actions.
- Output artifacts (`JSON`, `CSV`, `XLSX`, `JSON-LD`, Turtle, RDF, reports, and API responses) must point back to source media, source records, and the action or process that produced them when those outputs are intended for investigative, evidentiary, audit, or interop use.
- Preserve identifiers needed to trace derived artifacts back to source evidence without exposing sensitive values unnecessarily.
- Keep human-readable reports and machine-readable exports aligned. Do not allow a report to say something materially different from the serialized data.

## Validation

- Keep SHACL validation available for CASE/UCO/CAC/SOLVE-IT output where applicable.
- Add or update fixtures when export shapes, report schemas, ontology mappings, or serialization formats change.
- Specs that alter artifact schemas must include ontology impact, validation commands, migration notes, and backward-compatibility considerations.
- Validation failures must be treated as implementation defects unless the spec documents a deliberate unsupported mapping or open ontology gap.
- Tests must use benign synthetic data. Do not use real CSAM, real victim data, real case identifiers, or sensitive investigative details in ontology fixtures, examples, screenshots, or docs.

## Spec Kit Requirements

For schema, export, report, API, model-output, or evidence-processing changes:

- `/speckit.specify`: identify domain concepts, data categories, intended consumers, required exports, and candidate CASE/UCO/CAC/SOLVE-IT mappings.
- `/speckit.plan`: define concrete mappings, prefixes, ontology versions, serialization formats, validation commands, migration concerns, and unmapped gaps.
- `/speckit.tasks`: create implementation and test tasks for mapping, serialization, validation, fixtures, docs, and migration notes.
- `/speckit.implement`: implement mappings and validation using real ontology terms, not placeholders.
- `/speckit.analyze`: verify code, schema, fixtures, docs, examples, and changelog remain aligned with the ontology mapping.

## Required Agent Output

For ontology-relevant changes, the final agent response must summarize new or changed data concepts, ontologies and versions consulted, classes and properties used, local fields that intentionally remain unmapped, validation commands run, fixtures and examples updated, migration or backward-compatibility concerns, and open ontology gaps or proposed extension work.
<!-- POLICY-END PVIC-ONTOLOGY-ALIGNMENT -->

<!-- POLICY-BEGIN PVIC-PRIVACY-REDACTION-AND-SYNTHETIC-DATA ff77e07cbd34da8d4051c9a8d28b7f7e1b11339f3af6b8bad8fd079b2933d061 -->

# Privacy, Redaction, and Test Data

Project VIC development protects sensitive data by **channel** and **tier**. Follow `docs/test-data-handling.md` as the source of truth.

**Default:** Tier **T0** (public-safe synthetic) for anything committed, in CI, in public issues, in docs/screenshots, and in external AI prompts.

**Not a blanket ban** on realistic or agency-approved data for private manual testing and v0.5.x+ demos when a **test data handling plan** exists and the test record states the tier honestly.

## Non-negotiable prohibitions (all tiers, all channels)

Do not use or distribute:

- CSAM or suspected CSAM content or descriptions
- Real victim or offender identifiers in **public/shared** artifacts
- Credentials, API keys, or private certificates in repositories or issues
- Operationally sensitive hash intelligence or non-public Project VIC data in public examples

## Channel rules (what must stay synthetic or redacted)

These channels are **T0/T1 only** unless an approved plan explicitly allows a specific exception:

- Git commits, PR diffs, and CI logs/artifacts
- Public or shared GitHub Issues and release notes
- README, changelog, and committed documentation screenshots
- External cloud AI prompts and uploads (T2 requires explicit written approval for that workflow)
- Committed test fixtures and golden files

Use obviously synthetic identifiers in T0/T1 examples (filenames, hashes, people, agencies, case metadata, paths).

## Approved local and demo inputs (T1–T2)

- **T1 realistic synthetic:** structurally faithful data with fake identifiers; may be committed when safe to redistribute.
- **T2 agency-approved sample:** real or sanitized operational samples for controlled manual testing and law-enforcement demos (~v0.5.x+ typical). Store only under gitignored paths (e.g. `demo-data/local/`). Document via `docs/templates/test-data-handling-plan.md`.
- Agents must **not** refuse legitimate local testing with T2 when a plan exists; must **not** encourage committing T2 data or pasting it into prohibited channels.
- Record the tier in manual test execution records; do not mislabel T2 sessions as T0.

## Redaction requirements (product behavior)

When the application processes sensitive data:

- Logs, reports, exports, UI screenshots for **public** docs, and error messages must redact sensitive identifiers by default
- Prefer correlation IDs, artifact IDs, job IDs, or synthetic references over raw sensitive values where possible
- Redaction must not destroy required audit/provenance meaning; preserve safe traceability
- Add tests for redaction behavior; redaction tests may run in T1/T2 private environments while committed fixtures stay T0

## Prohibited content in artifacts

Do not create or commit:

- Real or realistic CSAM descriptions
- Real victim or offender names, agency case numbers, warrants, or investigative facts in **repo/docs/issues**
- Real evidence media, thumbnails, or paths in **committed** fixtures
- Graphic, sensational, exploitative, joking, or gamified sample content

## Tests and review

- **Automated/CI tests:** committed fixtures T0 (T1 only if redistribution-safe and identifier-safe)
- **Manual/demo:** T0–T2 per `docs/test-data-handling.md` and milestone maturity
- Review screenshots and fixtures before commit; use T0 for anything landing in git
- Do not use production logs or evidence-derived artifacts as **committed** test fixtures

## Spec Kit Requirements

For privacy-relevant work:

- `/speckit.specify`: protected data categories, test data tier targets by milestone, redaction needs, channel constraints
- `/speckit.plan`: T0 fixture strategy; T2 demo plan if v0.5.x+; redaction and audit tests
- `/speckit.tasks`: fixtures, gitignore paths, handling plan, redaction tests, docs
- `/speckit.implement`: T0 in repo/CI; never commit T2; implement redaction at boundaries
- `/speckit.analyze`: verify no prohibited content in committed artifacts; handling plan present if T2 claimed

## Required Agent Output

For privacy-relevant changes, summarize protected data, **test data tier** used or planned, channels affected, redaction behavior, committed vs local-only data, handling plan link if T2+, and limitations.
<!-- POLICY-END PVIC-PRIVACY-REDACTION-AND-SYNTHETIC-DATA -->

<!-- POLICY-BEGIN PVIC-PROJECT-VIC-RULE-INDEX a52f045770c114dcdad7b5ac9d9dc86154252d12557c830194f344cf053d1027 -->

# Project VIC Rule Index

Project VIC Cursor rules work together as a governance system. Apply the rules that are materially triggered by the task; do not dump every checklist into every response.

## Rule Precedence

When guidance appears to conflict, resolve it in this order:

1. Explicit user instruction.
2. Spec Kit constitution at `.specify/memory/constitution.md`.
3. Security, privacy, compliance, and evidence-integrity rules.
4. No-stubs, testing quality, and human-review rules.
5. Ontology, data-contract, persistence, and provenance rules.
6. Architecture, four-surface, MCP, and cross-platform rules.
7. Testing program (automation tiers, CI, scanners, human verification), release, dependency, observability, model, performance, and brand rules.
8. Repository-local context such as `specify-rules.mdc`.

If a conflict remains, stop and ask for human clarification rather than silently choosing the easier path.

## Rule Types

- Project VIC-wide standards define mission, safety, release, and interoperability expectations across repositories.
- Repository-local rules describe stack, commands, paths, and local conventions for the current repo.
- Conditional rules apply only when their subject area is materially touched, such as models, MCP, persistence, dependencies, performance, UI copy, or release automation.

## Shared Data Taxonomy

Use consistent language across rules, specs, docs, and agent summaries:

- Source evidence: original media, forensic images, mounted evidence, or operator-selected source records. Must remain read-only.
- Derived artifacts: extracted files, sampled frames, thumbnails, OCR/transcripts, model outputs, reports, exports, caches, and temporary working data.
- Investigative metadata: case labels, review status, hash lookup results, tags, notes, job metadata, and triage context.
- Protected identifiers: victim/person identifiers, agency case numbers, investigator identities, sensitive evidence paths, credentials, API keys, and non-public operational details.
- Provenance and audit data: who/what/when/action/result, tool/model versions, parameters, hashes, source references, and validation status.
- Public or synthetic data (Tier T0/T1): benign or realistic-synthetic fixtures safe for committed/shared channels.
- Controlled test/demo data (Tier T2/T3): agency-approved or operational samples allowed only in documented local or production environments; never mislabeled as T0 in records. See `docs/test-data-handling.md`.

## Agent Output Discipline

Final responses should summarize only the rule impacts that were materially triggered. For Spec Kit-driven work, use the Spec Kit output summary as the umbrella and include specialized checklist items only for affected areas.
<!-- POLICY-END PVIC-PROJECT-VIC-RULE-INDEX -->

<!-- POLICY-BEGIN PVIC-RELEASE-MANAGEMENT 616817f3442a235f645955f8dc05ed8f0b6b74f841c4abe4ba7fb7d13994e403 -->

# Release Management Redirect

Use `versioning-release-management.mdc` as the authoritative Project VIC standard for semantic versioning, changelog entries, GitHub Issues, milestones, labels, GitHub Actions, release notes, and release artifacts.

Do not create a second release-management checklist here. If release policy changes, update `versioning-release-management.mdc`.
<!-- POLICY-END PVIC-RELEASE-MANAGEMENT -->

<!-- POLICY-BEGIN PVIC-RULE-AUTHORING d2d4b2d3b4a63d8fc29391773b797519bbb373b520950b66d973962cd5ba2a97 -->

# Rule Authoring

Project VIC Cursor rules are governance artifacts. They should help agents make safe, consistent engineering decisions without creating contradictions, excessive noise, or false authority.

Use this rule when creating, reviewing, splitting, or maintaining `.cursor/rules/*.mdc` files.

## Rule Scope

- Prefer project-wide rules for mission standards: security, evidence integrity, ontology alignment, no-stubs behavior, release discipline, synthetic data, and human review.
- Prefer scoped or nested rules for stack-specific guidance, repository-local commands, framework conventions, or narrow file patterns.
- Do not make every rule `alwaysApply: true` if it only applies to a narrow area.
- Repository-local context rules should supplement, not override, Project VIC-wide standards.
- If a rule is only for docs, GUI, API, MCP, model, database, or release files, use `globs` where practical.
- Reusable Project VIC standard rules should avoid repo-specific product names unless the rule is intentionally product-specific.
- Repository-local rules should name the repository, stack, commands, and local paths clearly.

## Rule Precedence

Rules should align with `project-vic-rule-index.mdc`. If adding new precedence guidance, update the index instead of creating conflicting local hierarchies.

When rules overlap, prefer the stricter safety/evidence/security requirement and the more specific implementation rule for the touched surface.

## Rule Quality

- Keep rules focused and actionable.
- State what agents must do, what they must not do, and what final output is required when the rule is materially triggered.
- Include Spec Kit hooks when the rule affects non-trivial development.
- Prefer clear operational requirements over broad values statements.
- Avoid duplicating long sections from other rules; reference the other rule by name when possible.
- Avoid conflicting rules. If rules appear to conflict, identify precedence and update the rules.

## Frontmatter

Each rule must include valid `.mdc` frontmatter:

- `description`: concise, specific summary.
- `alwaysApply`: true only for broad standards.
- `globs`: include when rule applies to specific paths or file types.

Descriptions should be Project VIC-wide only when the rule is intended for reuse across Project VIC repositories.

## Maintenance

- Update rules when repeated agent failures occur.
- Update rules when Project VIC standards, Spec Kit workflow, compliance expectations, or architecture practices change.
- Keep rule language aligned with the Spec Kit constitution where appropriate.
- Do not edit generated sections casually; preserve generated blocks unless intentionally regenerating them.
- When rules change operational behavior, consider documentation, changelog, and release impact.

## Required Agent Output

For rule-authoring changes, the final agent response must summarize rules created or changed, scope/alwaysApply/glob decisions, conflicts considered, Spec Kit/constitution links, and any follow-up rules that should be split or consolidated.
<!-- POLICY-END PVIC-RULE-AUTHORING -->

<!-- POLICY-BEGIN PVIC-SECURITY-COMPLIANCE 3e3713c5373375dbef91a53409deb27d4bae1830a46a1a5a3ea98a2546ca5797 -->

# Security and Compliance

Project VIC International software is built for crimes-against-children investigators, digital forensics examiners, allied law-enforcement users, and supporting technical communities. Project VIC tools may handle law-enforcement-sensitive data, digital evidence, derived artifacts, investigative metadata, hash intelligence, model outputs, and, in some deployments, CSAM-related media.

Security, privacy, forensic integrity, and compliance support are release blockers, not optional hardening. Project VIC software may be designed to support NIST/CJIS-aligned and international law-enforcement deployments, but do not claim CJIS, NIST, agency, or jurisdictional compliance unless the implemented controls, deployment assumptions, operator responsibilities, tests, documentation, and audit evidence support that claim.

This comprehensive rule is intended for law-enforcement, evidence-capable, or security-relevant Project VIC repositories. Public websites, docs-only repos, template repos, conference demos, and low-risk utilities may need a smaller security-minimums rule or narrower file globs instead of this full rule.

## Core Requirements

- Authenticate and authorize access to APIs, case data, generated artifacts, exports, and administrative functions. If the application's API key is configured, enforce it; never expose API keys in browser-visible code unless explicitly documented for local development.
- Secrets must come from documented secret-management mechanisms or local development `.env` files excluded from source control. Do not invent fallback secrets, default production credentials, or silently disable authentication when secrets are missing.
- Validate every API input, file path, archive member, and job configuration at the boundary. Archive extraction must reject path traversal, absolute paths, escaping symlinks/hardlinks, unsafe permissions, decompression bombs, and unexpectedly large extracted content.
- Keep source evidence read-only. Temporary, extracted, cached, or derived artifacts must be isolated under configured case/run directories and must not mutate original evidence.
- Define retention and deletion behavior for temporary files, caches, extracted artifacts, model outputs, embeddings, job queues, logs, exports, and failed processing runs. Cleanup must not delete source evidence or operator-selected case records.
- Never log secrets, API keys, victim identifiers, unnecessary evidence paths, CSAM descriptors, or sensitive case details. Logs must support audit and troubleshooting without disclosing protected content.
- Maintain auditability and provenance for evidence access, processing jobs, model outputs, exports, configuration changes, and operator-visible security events.
- MD5 may be implemented only for legacy hash-set compatibility such as Project VIC lookups and must be labeled as non-cryptographic/non-integrity-protecting wherever exposed. Use SHA-256 or stronger for integrity reporting, provenance, tamper checks, cache identity, and deduplication unless a documented interoperability requirement says otherwise.
- Protect data in transit and at rest when the deployment context requires it. Document TLS, storage, database, backup, export, and secret-management assumptions.
- Container services must run with least privilege, avoid unnecessary mounts/capabilities, and expose ports only through intended profiles, proxies, or documented local-development paths.
- Dependencies, models, containers, and third-party tools must have a vulnerability and supply-chain review path appropriate to law-enforcement use.

## Compliance Baselines

When a change affects authentication, authorization, auditing, evidence handling, storage, networking, deployment, exports, dependencies, or operator workflows, address applicable controls from:

- NIST SP 800-53 Rev. 5 control families, especially Access Control, Audit and Accountability, Identification and Authentication, System and Communications Protection, System and Information Integrity, Configuration Management, Risk Assessment, Incident Response, Contingency Planning, Media Protection, Supply Chain Risk Management, and privacy-related controls.
- NIST SP 800-53B baselines, overlays, and tailoring guidance appropriate to the tool type, data sensitivity, operating environment, and threat model. Do not apply a generic flat checklist when a workstation tool, offline forensic utility, API service, cloud-hosted workflow, shared database, model pipeline, or evidence export requires different controls.
- FBI/DoJ CJIS Security Policy areas, especially access control, audit logging, identification/authentication, encryption, media protection, physical/logical protection assumptions, incident response, personnel/agency responsibility, and policy-area-specific data handling.
- Treat CJIS as versioned and jurisdictionally interpreted. When CJIS is in scope, identify the policy version, agency/state interpretation, audit context, and inherited agency controls. Do not claim CJIS compliance merely because code aligns with selected CJIS-style safeguards.
- Applicable non-U.S. law-enforcement, digital-evidence, privacy, cybersecurity, and data-sovereignty obligations when international deployment or users are in scope.

## Control Tailoring

- Classify each Project VIC tool or feature before choosing controls: VICSafer, VICPoint, CAC Ontology tooling, investigator GUI, local/offline forensic workstation, API/service, batch pipeline, shared repository/database, model training/inference component, training/demo app, export/interop tool, or deployment/operations utility.
- Identify data categories and sensitivity: source evidence, derived artifacts, victim/person identifiers, investigative metadata, hashes, model outputs, audit logs, configuration/secrets, and public/non-sensitive assets.
- State which controls are implemented in code, inherited from agency infrastructure, required from deployment configuration, or outside the feature boundary. Inherited controls still need assumptions and operator guidance.
- If the correct overlay or jurisdictional baseline is unknown, mark it as an open compliance question in the spec and avoid claiming compliance beyond implemented and tested controls.

## AI Assistant and Tooling Restrictions

- Do not paste, summarize, upload, embed, or transmit source evidence, victim identifiers, CSAM descriptors, case-specific investigative facts, credentials, private agency data, or non-public Project VIC operational details to **external** AI services unless repository documentation and the test data handling plan explicitly authorize that workflow for the deployment context.
- Use Tier T0/T1 data in prompts, committed fixtures, documentation, and CI-oriented examples by default. Tier T2 agency-approved samples belong in **local, approved** environments per `docs/test-data-handling.md`; agents may help configure and test there without committing data or sending it to prohibited channels.
- Do not create prompts, seed data, test names, filenames, screenshots, or **committed** logs that include realistic CSAM descriptions, victim identifiers, investigator identities, agency-sensitive details, or operationally sensitive hash intelligence.
- Do not misrepresent test data tier in summaries (for example claiming T0 when verification used T2).
- If an implementation uses local LLMs, MCP tools, model inference, vector stores, embeddings, or agent memory, document what data may enter those components, where it is stored, how it is deleted, and whether it can leave the host.

## Spec Kit Requirements

For security-relevant work, the Spec Kit workflow must explicitly cover compliance instead of treating it as implied:

- `/speckit.specify`: identify law-enforcement users, tool type, protected data categories, threat/risk assumptions, applicable NIST/CJIS/international baselines or overlays, misuse cases, data retention/deletion needs, forensic integrity requirements, and auditable success criteria.
- `/speckit.plan`: tailor requirements to concrete controls, data flows, trust boundaries, validation points, secrets handling, audit events, storage/transmission protections, inherited/deployment controls, AI/tooling exposure limits, and rollback/incident considerations.
- `/speckit.tasks`: create implementation, test, documentation, and audit-evidence tasks for each relevant control. Security tasks must name files or surfaces, not remain generic.
- `/speckit.implement`: implement real controls and focused tests. Do not satisfy security requirements with stubs, TODOs, disabled checks, or documentation-only claims.
- `/speckit.analyze`: verify spec, plan, tasks, code, tests, docs, changelog, and deployment guidance remain consistent with the identified compliance obligations.

## Required Security Tests

- Boundary validation tests for API payloads, file paths, archive members, job configs, and export destinations.
- Authentication/authorization tests for protected APIs and operator-only actions.
- Audit/provenance tests proving security-relevant events are emitted without leaking sensitive data.
- Evidence integrity tests proving source media remains read-only and derived artifacts stay inside approved case/run locations.
- Retention/deletion tests for temporary working data, caches, queues, logs, exports, embeddings, and failed-run cleanup where applicable.
- Fixture safety checks proving tests, demos, screenshots, and sample datasets use benign synthetic data, never real CSAM, real victim data, real agency case identifiers, or realistic abuse descriptors.
- Dependency/container/deployment checks when the change affects packages, images, ports, privileges, volumes, or proxy profiles.

## Error Handling

- Return clear 4xx errors for invalid operator input and sanitized 5xx errors for server failures.
- Log internal context for debugging without leaking sensitive values.
- GUI error text should help an investigator fix configuration, credentials, connectivity, or missing prerequisites.

## Release Gate

Security-relevant changes require focused tests, documentation updates, and a `CHANGELOG.md` entry under `Security` when user-facing or operationally relevant. Do not call a feature complete if identified NIST/CJIS/international controls are unimplemented, untested, unaudited, or undocumented.

## Required Agent Output

For security-relevant changes, the final agent response must summarize protected data touched, trust boundaries changed, authentication/authorization impact, evidence integrity impact, audit/provenance events added or changed, tests added or updated, documentation or deployment assumptions updated, and residual open compliance questions.
<!-- POLICY-END PVIC-SECURITY-COMPLIANCE -->

<!-- POLICY-BEGIN PVIC-SPECIFY-RULES b617e3b01ff595ce4e2bdf97b6b95609fd7e5875759cd67626f04cbca1722235 -->
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
<!-- POLICY-END PVIC-SPECIFY-RULES -->

<!-- POLICY-BEGIN PVIC-SPECKIT-WORKFLOW aff1e72d4b7ec0d1c55cf745d836c6667a0a94e972e631ab4209db1238437b48 -->

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
<!-- POLICY-END PVIC-SPECKIT-WORKFLOW -->

<!-- POLICY-BEGIN PVIC-TESTING-PROGRAM 2a30b441e16ebfe4d85722aeb64533e0bdb90395f17b948111d9a60778101abc -->

# Testing Program

Project VIC repositories use a shared **testing program** that combines automated checks (local and GitHub Actions) with structured **human verification**. This rule defines how to run quality work; `testing-quality.mdc` defines what automated tests must prove.

Human testers follow `docs/manual-test-checklist.md`. Release-specific scenarios belong in `docs/templates/manual-test-release-annex.md` (copied per release spec).

## Standards Basis

The program aligns with risk-based acceptance practices from ISO/IEC/IEEE 29119 (documentation and traceability), ISTQB test levels and types, OWASP verification guidance for security spot-checks, WCAG 2.2 for accessibility spot-checks, and session-based exploratory testing for workflow discovery. Automated CI implements regression and contract tests; human checklists implement system and acceptance verification automation cannot fully replace.

Do not claim CJIS, NIST, or jurisdictional compliance solely because this program was followed.

## Testing Tiers

| Tier | When | Purpose |
|------|------|---------|
| **T0 Local** | Every change | Fast feedback via one documented developer command |
| **T1 PR CI** | Every pull request | Merge gate: lint, types, unit, contract tests, container build where applicable |
| **T2 Main / scheduled** | Default branch; optional cron | Integration drift: compose smoke, heavier integration, docs build, image scan on built artifacts |
| **T3 Release** | Tag or milestone closure | Ship confidence: release checklist, SBOM, full human checklist + release annex, manual/GPU/offline matrix when documented |
| **T4 Post-release** | Optional schedule | Rescan dependencies and published images; no substitute for T3 |

**CI parity:** T1 jobs must invoke the same scripts as T0 where possible. Behavior that only passes in CI is a defect.

**Skips:** Heavy prerequisites (GPU, EWF, large models, offline bundles) may skip in CI with explicit markers and summary counts. Skips must not be the only verification for a capability declared production-ready in the active release spec. See `cross-platform.mdc` and `testing-quality.mdc`.

## Maturity Minimums

Align with `versioning-release-management.mdc`:

| Target | T0 | T1 | T2 | T3 human verification |
|--------|----|----|----|------------------------|
| **0.x pre-MVP** | Documented `test` / `lint` | Lint + unit; grows by milestone | Optional integration / compose | Layer C; demo phases may use T2 |
| **1.0.0 MVP** | Same | Contract tests for **MVP-required** surfaces (GUI/API/CLI/MCP per spec) | Compose smoke when applicable | Full checklist + annex + record; **T3** production validation |
| **1.x maintenance** | Same | Regression on declared surfaces | As needed | Per release scope |
| **2.0.0 platform** | Same | Automation for declared production surfaces | Image scan on release artifacts | Full checklist + record |

Repositories below their target bar must state gaps in README and milestone notes. Do not describe deferred CI or manual coverage as complete.

## Local Execution Standard

Every application repository must document in `README.md` or `docs/developer-guide.md`:

- setup / install
- **test** (fast, default for T0)
- **test-all** or **integration** (optional, heavy)
- **lint** / format check
- **container-build** or **compose-smoke** when Docker is in scope

Use **one canonical entry point** per repo: either a thin `Makefile` / `justfile` wrapper or a single documented native command (`uv run pytest`, `npm test`). After intake and Spec Kit planning, replace template placeholders with project-specific commands.

## GitHub Actions Program

This template does not ship active workflows until the project stack is known (see `.github/workflows/README.md`). When adding workflows, use these conventions:

| Workflow file | Trigger | Role |
|---------------|---------|------|
| `ci.yml` | PR and push to default branch | T1 required checks |
| `security.yml` | PR, default branch, optional schedule | Dependency and image vulnerability scanning |
| `release.yml` | Tags or manual dispatch | T3 packaging, SBOM, release scans |
| `docs.yml` | PR when a docs site exists | Documentation build |

**Branch protection:** Required status check names must match real job names. Release-bound work must not merge on failed required checks.

**Constraints:** No scheduled model downloads, large artifacts, or secrets in logs unless the release plan requires them. CI and committed fixtures use Tier T0 per `docs/test-data-handling.md`. Manual verification may use T1–T2 with a documented handling plan.

**Org reuse:** Prefer `workflow_call` from a Project VIC organization `.github` repository when available. Copy examples from `docs/org-ci-reusable-workflows.md` and `docs/org-ci-reusable-workflows/examples/`; document the contract in `docs/developer-guide.md`.

**Templates:** Copy `docs/ci-workflow-templates/` into `.github/workflows/` when not using org reusables yet.

Affected surfaces (GUI, API, CLI, MCP, containers, ontology validation) must appear in T1 or T2 when declared for the product. See `four-surface-review.mdc`.

## Security Scanning Layers

Dependency and image scanners are **complementary**, not interchangeable.

| Layer | Typical tool | Sees | Misses |
|-------|----------------|------|--------|
| Application dependencies | Dependabot, ecosystem alerts | Manifests and lockfiles | OS packages only in images |
| Source patterns | CodeQL (when enabled) | Code vulnerabilities | Image-only packages |
| Container images | Docker Scout, Trivy, Grype | Base OS, image layers | Dev-only deps not in image |

**Rules:**

1. **Containerized services:** run application dependency scanning **and** image scanning on built or published images.
2. **Non-container libraries:** dependency scanning + tests; document image scan as N/A.
3. **Triage:** fix, pin, replace, or waive with linked issue (`type:security`), expiry, and operator impact in `CHANGELOG.md` **Security** when release-relevant. Do not suppress findings without justification (`dependency-license-supply-chain.mdc`).
4. **Release:** disposition of critical/high findings is recorded before tag; SBOM attached when release policy requires it.

## Test Types and Surfaces

| Type | Typical tier | Notes |
|------|----------------|-------|
| Unit | T1 | Shared services (`architecture-boundaries.mdc`) |
| Contract / schema | T1 | API, MCP, export fixtures |
| CLI | T1 | Exit codes, stdout/stderr, output paths |
| Integration | T2 | Services, DB, queues |
| Compose e2e | T2 | Documented profiles (`backend`, `api`, `cpu`, etc.) |
| GUI | T2 or T3 manual | Automated when feasible; otherwise manual checklist |
| Ontology / SHACL | T1 or T2 | Per `ontology-alignment.mdc` |
| Security | T1 + `security.yml` | Auth, path traversal, upload abuse |
| Performance | T3 or `auto-research.mdc` | Claims require measured evidence |

## Human Verification Program

Automated tiers do not replace hands-on acceptance testing.

**Layers:**

- **Layer A — Master:** `docs/manual-test-checklist.md` (stable, all apps).
- **Layer B — Release annex:** copy `docs/templates/manual-test-release-annex.md` into the release spec folder (e.g. `specs/003-Spec-v0.3.0/manual-test-release.md`) with milestone-specific scenarios.
- **Layer C — Change subset:** PR template lists items re-run from Layer A for the touched surfaces.

**Risk order when time is limited:** evidence integrity and honest failures → auth/export leakage → release acceptance criteria → four-surface parity → deployment/offline smoke → ontology/exports → accessibility → exploratory charter.

**Test execution record:** Before closing a release milestone, attach or link a record (see manual checklist appendix) with version, environment, automation URLs, pass/fail summary, open issues, residual risks, and sign-off.

**Distinction:** `human-review-and-risk-gates.mdc` covers code and design review before merge. This program covers product verification using the test data tier declared for the session (`docs/test-data-handling.md`).

## GitHub Hygiene

- Use `type:test` for test gaps and `type:security` for scanner triage.
- PRs reference resolved issues; include manual test subset when behavior is user-visible.
- Milestone closure requires tests, documented manual verification, or an explicit deferral with release-note limitation (`versioning-release-management.mdc`).

## Spec Kit Requirements

For test-program-relevant work:

- `/speckit.specify`: acceptance criteria, tiers affected, surfaces, scanner impact, human verification scope.
- `/speckit.plan`: T0 commands, workflows to add or change, skip matrix, Layer B annex outline, branch protection checks.
- `/speckit.tasks`: tasks for local docs, workflows, fixtures, manual annex, PR template, changelog.
- `/speckit.implement`: implement automation and docs together; no fake green CI.
- `/speckit.analyze`: T0/T1 parity, scanner coverage, skip inventory vs release scope, human record for releases.

## Required Agent Output

When this rule is materially triggered, the final response must summarize tiers implemented or changed, canonical local commands, workflows and required checks, security scanning layers, human verification layer (A/B/C) and record status, skips and why, tests or validation run, documentation updated, maturity gaps vs target version, and deferred work not presented as complete.
<!-- POLICY-END PVIC-TESTING-PROGRAM -->

<!-- POLICY-BEGIN PVIC-TESTING-QUALITY 36f8fe9d68755446efd451f1b211ccd5c3dc7a00a806c4b1c33ad008dc62f01f -->

# Testing and Quality

Project VIC tests must prove meaningful behavior, failure modes, surface consistency, and regression protection. Compile/build checks are useful, but they are not substitutes for behavioral tests when behavior changes.

For local commands, CI tiers (T0–T3), GitHub Actions conventions, security scanning layers, and human verification checklists, use `testing-program.mdc` and `docs/manual-test-checklist.md`.

For test **data** tiers (T0–T3) and demo/pilot policy, use `docs/test-data-handling.md`.

## Testing Principles

- Test behavior, not implementation details.
- Cover success, failure, invalid input, missing dependency, permission-denied, unsupported platform, and malformed data paths where applicable.
- Add regression tests for every fixed bug.
- **Committed and CI tests** must use Tier T0 public-safe synthetic fixtures (Tier T1 only when redistribution-safe with obviously fake identifiers).
- **Manual and demo verification** may use T1–T2 per `docs/test-data-handling.md`; record tier honestly; never commit Tier T2+ sample data.
- Do not encode fake success paths that hide missing implementation.
- Tests should verify honest actionable failure when prerequisites are unavailable.

## Required Coverage Areas

Surface-changing work should test GUI/API/CLI/MCP behavior where practical.

- GUI: user-visible state, errors, accessibility-relevant behavior, and terminology where practical.
- API: endpoint behavior, schemas, auth, validation, errors, and OpenAPI/contract expectations.
- CLI/pipeline: commands, flags, exit codes, stdout/stderr, output files, and batch behavior.
- MCP: tool schemas, structured outputs, bounded errors, and sensitive-data safety.
- Reports/exports: deterministic output, schema fixtures, and human/machine-readable consistency.

## Evidence, Security, and Ontology Tests

- Evidence-handling tests must prove source evidence remains read-only.
- Path/archive tests must reject traversal, absolute paths, escaping links, unsafe permissions, and oversized/decompression-bomb inputs where applicable.
- Security tests must cover authentication, authorization, secrets handling, redaction, audit events, and permission failures where applicable.
- Ontology/export tests must validate generated CASE/UCO/CAC/SOLVE-IT output where applicable.
- Privacy tests must confirm fixtures, logs, screenshots, and outputs use synthetic or redacted data.

## Regression and Quality Gates

- Add tests before or with fixes for user-visible, security, evidence, export, or persistence bugs.
- Use golden files only for deterministic output and review changes carefully.
- Integration tests may skip cleanly when GPU, Docker, mounted forensic images, model weights, or other heavy prerequisites are unavailable, but skips must not hide missing implementation.
- Performance improvements need benchmark/regression protection when claimed.
- Do not claim completion if required tests are absent without documented manual verification.

## Spec Kit Requirements

For test-relevant work:

- `/speckit.specify`: identify acceptance criteria, failure modes, affected surfaces, data fixtures, and validation needs.
- `/speckit.plan`: define unit/integration/contract/e2e/manual verification strategy and skip conditions.
- `/speckit.tasks`: create explicit test tasks tied to files, surfaces, fixtures, docs, and validation commands.
- `/speckit.implement`: add or update tests alongside behavior.
- `/speckit.analyze`: verify tests cover requirements, failure modes, contracts, surfaces, and regression risk.

## Required Agent Output

For behavior changes, the final agent response must summarize tests added or updated, failure modes covered, fixtures used, validation commands run, skipped tests and why, manual verification if any, and remaining test gaps.
<!-- POLICY-END PVIC-TESTING-QUALITY -->

<!-- POLICY-BEGIN PVIC-VERSIONING-RELEASE-MANAGEMENT e38c4cabcb83755ffc78d7aee4c32549ca0b98405e1ceabf28b5f38269f8b4a4 -->

# Versioning and Release Management

Project VIC International development projects use Semantic Versioning and disciplined release management so users, contributors, investigators, agencies, and AI development agents can understand what changed, what is safe to use, and what remains incomplete.

A release is not complete until version metadata, changelog entries, documentation, tests, GitHub Issues, milestones, GitHub Projects, release notes, and release artifacts are aligned.

## Semantic Versioning

Project VIC projects follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html): `MAJOR.MINOR.PATCH`.

- Increment `MAJOR` for incompatible API, schema, artifact, CLI, MCP, data model, ontology mapping, deployment, or workflow changes.
- Increment `MINOR` for backward-compatible functionality.
- Increment `PATCH` for backward-compatible fixes, documentation corrections, test improvements, compatible security patches, and maintenance changes.
- Use pre-release identifiers for demos, pilots, alpha builds, beta builds, and release candidates, such as `1.0.0-alpha.1`, `1.0.0-beta.1`, or `1.0.0-rc.1`.
- Do not describe alpha, beta, pilot, or release-candidate builds as production-ready.

## Project VIC Maturity Convention

Project VIC uses this planning convention alongside SemVer. Human-readable summary: `docs/release-versioning.md`.

| Version | Planning meaning |
|---------|------------------|
| `0.x.y` | **Pre-MVP:** iterative, testable releases (skeleton, workflows, demos, hardening). Minor count is **project-specific** (`v0.12.0` is normal). Incomplete scope is allowed with documented limits. |
| `1.0.0` | **MVP:** a **single user** (or explicitly documented small deployment) can use the product **successfully in production** with **real operational data** (Tier T3 per `docs/test-data-handling.md`) in an approved environment. Satisfies the no-stubs rule for the **declared MVP scope**. |
| `1.x.y` | **MVP maintenance:** backward-compatible fixes and small enhancements on the MVP architecture (still single-user / small-scale unless the spec says otherwise). |
| `2.0.0` | **Platform / enterprise:** multi-user, larger-scale, or major feature depth; breaking changes allowed per SemVer. Default target for org-wide **production-intent** hardening (including four-surface parity for declared capabilities unless documented exceptions). |
| `3.0.0+` | **Ecosystem maturity (optional):** multi-agency, long-lived production; only when the product roadmap requires it. |

Do not use the maturity convention to override Semantic Versioning. If a breaking change occurs, increment the major version.

## Mandatory Release Planning Through v1.0.0

- Every application project must maintain an approved release roadmap through **`v1.0.0` MVP exit criteria** (for example `planning/my-release-plan.md` from `planning/release-roadmap-template.md`).
- Pre-MVP milestones are added as needed; the sample `v0.1.0`–`v0.9.0` themes in the roadmap template are **illustrative only**, not a required count or sequence.
- Each **release boundary** (typically each `0.x.0` minor and `1.0.0`) should have a GitHub milestone and, for non-trivial scope, one primary release-scoped Spec Kit folder.
- **`1.0.0`** always has a dedicated milestone, release spec, MVP exit criteria, and test execution record.
- After **`1.0.0`**, plan **`2.0.0`** when enterprise or multi-user scope is required; plan **`3.0.0`** only when documented.

## Four Surfaces and MVP

- **`1.0.0` MVP** may require GUI, API, CLI, and MCP **equivalence** for declared capabilities when intake, the release spec, and users require it. Record required surfaces in MVP exit criteria and `spec.md` release target.
- If MVP does not need all four surfaces, document gaps, supported alternatives, and milestone expectations per `four-surface-review.mdc`.
- **`2.0.0`** remains the default milestone for org-wide production-intent four-surface parity unless a maintainer documents a different target.

## Release-Scoped Spec Kit Specs

Spec Kit specs are release-scoped planning containers, not one-spec-per-small-feature tickets.

GitHub milestones and issues are the live source of truth for current minor and major release planning. Do not maintain a separate historical version roadmap as the active plan, and do not reverse-update old planning documents solely to mirror newly created GitHub activity.

When a GitHub milestone is ready for Spec Kit work, create or update one primary release spec under `specs/`. The spec describes the intended behavior for that milestone, while the GitHub release tag represents the implemented, tested, delivered artifact.

Use this naming pattern:

- `001-Spec-v0.1.0-initial-skeleton`
- `002-Spec-v0.2.0-import-workflow`
- `011-Spec-v0.11.0-demo-hardening`
- `012-Spec-v0.12.0-pilot-feedback`
- `013-Spec-v1.0.0-mvp`

The stable numeric prefix preserves chronological sorting (increment for each new release spec). The version in the folder name must match the GitHub milestone and Git tag. The slug should describe the primary release objective. Pre-MVP is not limited to nine minors.

A release spec may contain multiple features when those features are planned for the same release boundary. Do not create a new versioned spec for every tiny feature, defect, or maintenance task unless it represents a distinct release target.

Each release spec should use the standard Spec Kit structure:

- `spec.md`
- `plan.md`
- `tasks.md`
- `research.md`
- `data-model.md`
- `contracts/`
- `quickstart.md`

Each `spec.md` must include a release target section:

```md
## Release Target

Target release: v0.3.0
Release type: minor
Status: planned | in-progress | implemented | released
GitHub milestone: v0.3.0
Primary objective: Add Project VIC hash lookup and result review workflow.
MVP surfaces (v1.0.0 only): GUI, API, CLI, MCP | subset documented below
Surface gaps (if any): ...
```

The relationship is:

- `Spec-v0.3.0` is the contract for intended release behavior.
- `v0.3.0` is the implemented, tested, tagged release artifact.

Agents must reason within the active release boundary. For example, implement the remaining tasks for `Spec-v0.3.0`, but do not introduce behavior planned for `Spec-v0.4.0`.

Each active release milestone has one primary release spec unless the maintainer explicitly records a different structure. Each release spec may contain multiple features. Each feature must trace to requirements, tasks, tests, and release notes. The GitHub milestone, Git tag, changelog section, release notes, and spec folder must use the same version number.

## Version Sources

When changing the product version, update all relevant version surfaces. Examples include:

- `CHANGELOG.md`
- `README.md`
- Package metadata such as `pyproject.toml`, `package.json`, `.csproj`, `Cargo.toml`, or equivalent.
- API version endpoints or application metadata.
- GUI-visible version display.
- CLI `--version` output.
- MCP server metadata.
- Docker image tags and Docker Compose examples.
- GitHub Actions release workflows.
- Installation, upgrade, migration, generated documentation, and GitHub release notes.

Version metadata must remain consistent across GUI, API, CLI, MCP, container, documentation, changelog, and GitHub release surfaces.

## GitHub Issues, Projects, and Milestones

- Every planned feature, defect, security fix, documentation task, release task, and breaking change must have a GitHub Issue unless the repository documents a lighter-weight workflow.
- Every implementation issue must be assigned to a milestone before implementation begins.
- Every release must have a milestone.
- GitHub milestones/issues, not historical roadmap documents, define current release scope.
- GitHub Projects must be used for milestone planning when the repository has active multi-issue development.
- Pull requests must reference the issue or issues they resolve.
- Release notes must be traceable back to issues, pull requests, or documented release tasks.
- Issues that affect multiple Project VIC surfaces must identify GUI, API, CLI, MCP, docs, deployment, ontology, and security impact where applicable.
- Closing an issue requires implementation, tests or documented verification, documentation updates when needed, and changelog updates when user-facing or operationally relevant.

## Standard Issue Labels

Use project-specific labels where useful, but preserve these standard label categories when applicable.

- Type: `type:feature`, `type:bug`, `type:security`, `type:docs`, `type:test`, `type:release`, `type:refactor`, `type:maintenance`.
- Surface: `surface:gui`, `surface:api`, `surface:cli`, `surface:mcp`, `surface:docs`, `surface:deployment`, `surface:ontology`.
- Priority: `priority:critical`, `priority:high`, `priority:medium`, `priority:low`.
- Status: `status:needs-spec`, `status:planned`, `status:in-progress`, `status:blocked`, `status:needs-review`, `status:ready-for-release`.
- Release impact: `release:breaking`, `release:minor`, `release:patch`, `release:security`.

Project-specific labels may be added for tool names, partner programs, model pipelines, ontology modules, deployment profiles, or agency-specific workflows.

## GitHub Actions and Testing Program

Every release-capable repository must implement the Project VIC **testing program** in `testing-program.mdc`: documented T0 local commands, T1–T3 automation tiers, security scanning layers, and human verification per `docs/manual-test-checklist.md`.

- Pull requests must not be merged for release-bound work if required GitHub Actions checks fail.
- Release tags must be created only after required workflows pass.
- Workflows must test all affected surfaces declared for the product.
- Tests that require GPU, Docker, mounted forensic images, large model weights, offline bundles, or other heavy dependencies may skip cleanly when prerequisites are unavailable, but skipped tests must not hide missing implementation.

## Changelog

- Every user-visible, operator-visible, developer-visible, security-relevant, deployment-relevant, or release-relevant change must have a `CHANGELOG.md` entry.
- Use Keep a Changelog categories: `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, `Security`.
- Project VIC may also use `Performance`, `Documentation`, and `Migration`.
- Include affected surfaces where applicable: `GUI`, `API`, `CLI`, `MCP`, `Pipeline`, `Docs`, `Release`, `Security`, `Ontology`, or `Deployment`.
- Security entries should explain operator impact without exposing exploit details beyond what is appropriate.
- Performance entries must include before/after measurements, test conditions, and links or references to benchmark evidence when applicable.
- Breaking changes must include migration guidance.

## README and Docs

Update documentation when behavior changes for installation, deployment, configuration, authentication or authorization, evidence input, GUI usage, API usage, CLI usage, MCP server usage, Docker Compose profiles, offline or air-gapped operation, GPU or CPU behavior, model weights, CASE/UCO/CAC/SOLVE-IT output, Project VIC lookup behavior, reports and exports, release flow, migration or upgrade steps, or known limitations.

Documentation must not claim support for features, platforms, integrations, or workflows that are incomplete or untested.

## Release Checklist

- The release has a GitHub milestone.
- All release-bound issues are closed or explicitly deferred.
- Deferred issues are documented in release notes when relevant.
- Required GitHub Actions pass (T1/T2 per `testing-program.mdc`).
- Tests and builds pass for affected surfaces.
- Dependency and image vulnerability checks are clean or explicitly triaged (Dependabot plus image scan when containerized).
- **Test execution record** attached or linked for the release (see `docs/manual-test-checklist.md` appendix); Layer B release annex completed when human verification is required for the milestone.
- Security-relevant changes have appropriate tests and documentation.
- CASE/UCO/CAC/SOLVE-IT validation passes when exports or ontology mappings change.
- Docker Compose profiles still work for changed services.
- GUI, API, CLI, and MCP surfaces meet MVP or release-spec parity requirements; documented gaps only where allowed.
- CPU-only mode still works unless the release explicitly removes it.
- Offline or air-gapped behavior is preserved where applicable.
- The release-scoped Spec Kit folder, release target section, GitHub milestone, changelog section, and release notes use the same version number.
- Version metadata is consistent across files and surfaces.
- `CHANGELOG.md`, `README.md`, and docs are updated.
- Migration guidance exists for breaking API, schema, artifact, environment variable, ontology, deployment, CLI, or MCP changes.
- GitHub release notes mirror the changelog and identify known limitations.
- Release artifacts are attached, tagged, checksummed, or documented as appropriate.

## Release Artifacts

Release artifacts may include source archives, package artifacts, container image tags, Docker Compose examples, checksums, SBOMs, offline bundles, model weight instructions or bundles, ontology files or validation assets, generated documentation, migration guides, API schemas, MCP tool schemas, and example outputs using benign synthetic data.

Release artifacts must not include secrets, real evidence, real victim data, real agency data, or sensitive investigative material.

## Spec Kit Requirements

For release-relevant work:

- `/speckit.specify`: create or update the release-scoped spec folder, identify the intended version, release target section, milestone, release scope, affected surfaces, compatibility expectations, and documentation obligations.
- `/speckit.plan`: define required implementation, tests, GitHub Actions (per `testing-program.mdc`), manual test release annex, changelog entries, docs, migration notes, release artifacts, and issue/milestone links.
- `/speckit.tasks`: create explicit tasks for each release-scoped feature, version updates, tests, docs, changelog, release notes, artifacts, and GitHub issue hygiene.
- `/speckit.implement`: update the code, tests, docs, version metadata, changelog, and release automation.
- `/speckit.analyze`: verify release scope, issue status, milestone status, release spec folder, release target section, version metadata, changelog, docs, tests, workflows, and artifacts are consistent.

## Required Agent Output

For release-relevant changes, the final agent response must summarize version impact, milestone affected, issues linked or created, labels applied or recommended, GitHub Actions affected, surfaces affected, version files updated, changelog entries added, documentation updated, migration guidance added, release artifacts affected, and known limitations or deferred work.
<!-- POLICY-END PVIC-VERSIONING-RELEASE-MANAGEMENT -->
