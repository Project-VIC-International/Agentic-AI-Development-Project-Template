# Manual Test Release Annex (Layer B)

Copy this file into the active release spec folder, for example:

`specs/003-Spec-v0.3.0/manual-test-release.md`

Fill it in during `/speckit.plan` and complete it before the release. Use it with `docs/manual-test-checklist.md` (Layer A).

## Release Metadata

| Field | Value |
|-------|-------|
| Target release | v0.0.0 |
| GitHub milestone | |
| Primary objective | |
| Spec folder | |
| Tester(s) | |
| Test dates | |

## Deployment Under Test

- **Compose profile(s):** (for example `backend`, `api`, `cpu`)
- **Offline bundle:** yes / no / N/A
- **GPU required:** yes / no
- **Platforms:** (for example Ubuntu 24.04, Windows 11 with WSL, macOS)

## Features and Acceptance Criteria (this release)

Map each criterion in `spec.md` to test steps.

| ID / criterion | Layer A sections | Pass | Notes / issue |
|----------------|------------------|------|---------------|
| | 2, 5 | | |

## Breaking Changes and Migration

- [ ] Migration steps from the previous version verified
- [ ] Deprecated paths fail or warn as documented

## Surfaces in Scope

Check surfaces **changed or declared** in this release and run the matching Layer A sections. For the **v1.0.0 MVP**, include every surface required by the MVP exit criteria.

| Surface | In scope | Layer A sections | Pass |
|---------|----------|------------------|------|
| GUI | | 2, 8 | |
| API | | 2, 4, 5 | |
| CLI | | 2, 4, 5 | |
| MCP | | 2, 4, 5 | |
| Containers | | 7 | |
| Ontology / exports | | 5 | |

## Test Data for This Release

| Field | Value |
|-------|-------|
| Data tier (max) | T0 \| T1 \| T2 (T0/T1 during the course) |
| Handling plan link | (required for T2) |
| CI and commits | T0/T1 only |

## Main Investigator Journeys

Describe scenarios for the tier above. For T0/T1, link `examples/synthetic-data/` or project fixtures. For T2, give only the local path under `demo-data/local/` (never in git).

1. **Journey:**
   - Steps:
   - Expected result:

2. **Journey:**
   - Steps:
   - Expected result:

## Exploratory Charter (section 9)

| Field | Value |
|-------|-------|
| Mission | |
| Time box | minutes |
| Findings | issue # |

## Out of Scope (do not test as working)

-

## Test Execution Record

Paste the record from the appendix of `docs/manual-test-checklist.md` when complete.
