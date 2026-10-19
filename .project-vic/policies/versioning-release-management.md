
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
