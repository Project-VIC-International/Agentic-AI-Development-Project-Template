---
description: No stubs - implement real functionality with tested behavior and actionable failures
alwaysApply: true
---

# No Stubs

Development must not leave fake, placeholder, or TODO-only behavior in production paths.

A feature is not complete because files, routes, buttons, commands, tools, or schemas exist. A feature is complete only when the documented behavior is implemented, connected to applicable surfaces, tested or manually verified, and able to fail honestly when prerequisites are unavailable.

Scaffolding is allowed only when it is not exposed as a working feature and is clearly marked as non-production. Production paths must either implement the documented behavior or fail with a typed, actionable error.

## Prohibited Production Behavior

Never add or leave the following in production paths, in any language:

- Placeholder implementations, or `pass`, `NotImplemented`, `return {}`, `return None`, empty handlers, or commented-out logic as shipped behavior.
- Fake success responses.
- TODO-only endpoints or functions.
- Hardcoded demo results.
- Mock returns presented as real output.
- Silent no-op behavior.
- Disabled checks that make tests pass.
- Fake hash lookup results.
- Fake model detections or classifications.
- Fake provenance records.
- Fake audit events.
- Fake ontology mappings or validation results.
- Fake export files.
- Fake database writes.
- Fake authentication or authorization decisions.
- Fake IDs, hashes, ontology terms, security checks, or performance numbers.
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

Examples include GPU runtime, `ffmpeg`, EWF or forensic image mounting tools, Docker or container runtime, database services, hash-set lookup data, model weights, ontology files, SHACL validators, API keys, mounted evidence, writable output directories, network access when required, and offline bundle assets.

## Tests and Fixtures

- Tests may use mocks, fixtures, synthetic data, monkeypatching, and fake services only when the test clearly verifies the behavior under test.
- Tests must not encode fake success paths that hide missing implementation.
- Use benign synthetic fixtures. Synthetic data is safe representative input, not permission to fake the implementation.
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

- The user explicitly chose to defer it, and a tracked GitHub issue exists.
- The incomplete capability is not exposed as working.
- The limitation is documented in the spec, plan, task list, README, or issue tracker.
- The GUI/API/CLI/MCP surface hides, disables, or clearly rejects the unavailable capability.
- The code fails with an actionable error if an operator or agent tries to use the unavailable path.
- The changelog and release notes do not describe deferred work as complete.

## Required Agent Output

For every implementation task, the final agent response must summarize what real behavior was implemented, which surfaces were connected, which dependencies are required, what happens when dependencies are missing, what tests or manual verification were added, whether any work remains deferred, and why deferred work is not exposed as a working feature.
