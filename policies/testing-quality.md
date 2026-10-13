---
description: Require meaningful tests for behavior, failure modes, surfaces, and regression protection; read when writing or changing code or tests
globs: ["tests/**", "test/**", "**/*test*", "**/*spec*.ts", "**/fixtures/**", "**/conftest.py"]
alwaysApply: false
---

# Testing and Quality

Tests must prove meaningful behavior, failure modes, surface consistency, and regression protection. Compile/build checks are useful, but they are not substitutes for behavioral tests when behavior changes. An agent can produce plausible code that does not solve the problem; tests and human feedback are how the project finds out.

For local commands, CI automation levels (L0–L4), GitHub Actions conventions, security scanning layers, and human verification checklists, use `policies/testing-program.md` and `docs/manual-test-checklist.md`.

For test **data** tiers (T0–T3), use `docs/test-data-handling.md`.

## Testing Principles

- Test behavior, not implementation details.
- Cover success, failure, invalid input, missing dependency, permission-denied, unsupported platform, and malformed data paths where applicable.
- Add regression tests for every fixed bug.
- Committed and CI tests use Tier T0 public-safe synthetic fixtures (Tier T1 only when redistribution-safe with obviously fake identifiers).
- Manual and demo verification uses T0–T1 during the course; T2 only afterwards per `docs/test-data-handling.md`. Record the tier honestly; never commit Tier T2+ data.
- Do not encode fake success paths that hide missing implementation.
- Tests should verify honest, actionable failure when prerequisites are unavailable.
- Run the tests before saying they pass. Report the command and the result.

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

For behavior changes, the final agent response must summarize tests added or updated, failure modes covered, fixtures used, validation commands run and their results, skipped tests and why, manual verification if any, and remaining test gaps.
