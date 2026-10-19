---
description: Privacy, redaction, and tiered test data; channel safety for anything that could carry sensitive data into prompts, commits, CI, issues, docs, screenshots, logs, or benchmarks
alwaysApply: true
---

# Privacy, Redaction, and Test Data

This project protects sensitive data by **channel** and **tier**. `docs/test-data-handling.md` is the source of truth for the tiers and the channel matrix.

**Default:** Tier **T0** (public-safe synthetic) for anything committed, in CI, in issues, in docs and screenshots, and in AI agent prompts.

**During the course or any workshop:** Tier **T0 or T1 only**, on every channel. No exceptions.

**After the course:** realistic or agency-approved data (Tier T2) may be used for private manual testing and pilot demos only inside the user's agency, in an approved local environment, with a written test data handling plan, and with the tier recorded honestly in the test record.

## Non-Negotiable Prohibitions (All Tiers, All Channels)

Do not use, create, or distribute:

- CSAM or suspected CSAM, or descriptions of it.
- Real victim or offender identifiers in public or shared artifacts.
- Credentials, API keys, tokens, or private certificates in repositories, prompts, or issues.
- Operationally sensitive hash intelligence or non-public agency data in examples.

## Channel Rules (What Must Stay Synthetic or Redacted)

These channels are **T0/T1 only** unless an approved plan explicitly allows a specific exception:

- Git commits, PR diffs, and CI logs/artifacts.
- Public or shared GitHub Issues and release notes.
- README, changelog, and committed documentation screenshots.
- Prompts and uploads to cloud-hosted AI agents and models (including the agent reading this policy).
- Committed test fixtures and golden files.

Use obviously synthetic identifiers in T0/T1 examples (filenames, hashes, people, agencies, case metadata, paths), such as `SYNTH-CASE-001`, `Alex Example`, or `example.org`.

## Approved Local and Demo Inputs (After the Course)

- **T1 realistic synthetic:** structurally faithful data with fake identifiers; may be committed when safe to redistribute.
- **T2 agency-approved sample:** real or sanitized operational samples for controlled manual testing and law-enforcement pilot demos. Store only under gitignored paths such as `demo-data/local/`. Document with `docs/templates/test-data-handling-plan.md` before first use.
- Agents must not encourage committing T2 data or pasting it into prohibited channels. When a user has an approved plan and a local or offline environment, agents may help configure and test there without seeing the data itself.
- Record the tier in manual test execution records; do not mislabel T2 sessions as T0.

## Redaction Requirements (Product Behavior)

When the application processes sensitive data:

- Logs, reports, exports, public-doc screenshots, and error messages must redact sensitive identifiers by default.
- Prefer correlation IDs, artifact IDs, job IDs, or synthetic references over raw sensitive values.
- Redaction must not destroy required audit/provenance meaning; preserve safe traceability.
- Add tests for redaction behavior. Committed redaction fixtures stay T0.

## Prohibited Content in Artifacts

Do not create or commit:

- Real or realistic CSAM descriptions.
- Real victim or offender names, agency case numbers, warrants, or investigative facts.
- Real evidence media, thumbnails, or paths.
- Graphic, sensational, exploitative, joking, or gamified sample content.

## Tests and Review

- Automated and CI tests: committed fixtures are T0 (T1 only if redistribution-safe and identifier-safe).
- Manual and demo testing: T0–T1 during the course; T2 only afterwards per `docs/test-data-handling.md`.
- Review screenshots and fixtures before commit.
- Do not use production logs or evidence-derived artifacts as committed test fixtures.

## Spec Kit Requirements

For privacy-relevant work:

- `/speckit.specify`: protected data categories, test data tier targets by milestone, redaction needs, channel constraints.
- `/speckit.plan`: T0 fixture strategy; T2 demo plan only if the project is past the course and approved; redaction and audit tests.
- `/speckit.tasks`: fixtures, gitignore paths, handling plan, redaction tests, docs.
- `/speckit.implement`: T0 in repo and CI; never commit T2; implement redaction at boundaries.
- `/speckit.analyze`: verify no prohibited content in committed artifacts; handling plan present if T2 is claimed.

## Required Agent Output

For privacy-relevant changes, summarize protected data, the test data tier used or planned, channels affected, redaction behavior, committed versus local-only data, the handling plan link if T2 or above, and limitations.
