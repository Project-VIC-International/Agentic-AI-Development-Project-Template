---
description: Safe logging, operator status, audit events, provenance records, metrics, and long-running job states without leaking protected data
globs: ["**/*logging*", "**/*logger*", "**/*audit*", "**/*telemetry*", "**/*metrics*", "**/jobs/**", "**/workers/**"]
alwaysApply: false
---

# Observability, Audit Logging, and Operator Status

Tools must provide useful operational visibility without leaking protected data. Logging, operator status, audit events, provenance records, and debugging traces serve different purposes and must not be conflated.

## Observability Channels

- **Debug and application logs:** developer and operator troubleshooting.
- **Operator status:** GUI/API/CLI/MCP-facing progress, warnings, failures, and next steps.
- **Audit events:** who, what, when, action, and result for security-relevant and operator-relevant actions.
- **Provenance records:** what process, tool, and configuration produced an artifact or result.
- **Metrics and benchmarks:** performance, throughput, resource use, and health signals.

Each channel needs a clear audience, retention expectation, and sensitivity level.

## Safe Logging

- Logs should be structured where practical.
- Never log secrets, API keys, credentials, victim identifiers, sensitive case details, CSAM descriptors, raw evidence content, or unnecessary evidence paths.
- Use correlation IDs, job IDs, artifact IDs, or synthetic identifiers instead of sensitive values where possible.
- Errors should be correlation-friendly without leaking protected data.
- Do not enable verbose or debug logging by default in production-like profiles.
- Do not add third-party telemetry, analytics, or crash reporting that sends data off the machine without the user's approval (`policies/dependency-license-supply-chain.md`).
- Record timestamps in UTC (ISO 8601) so events from different machines and time zones can be correlated.

## Audit and Provenance

- Audit events should capture actor or service identity, action, target type, timestamp, result, and a safe correlation reference without exposing protected content.
- Record security-relevant events such as authentication failures, configuration changes, export creation, deletion or cleanup actions, administrative actions, and permission denials.
- Provenance records should capture source references, tool and model version, parameters, runtime, validation status, output artifact, and producing action.
- Audit and provenance records should be append-friendly and tamper-evident where practical.
- Retention periods follow the user's chosen control framework and agency rules (`policies/security-compliance.md`).

## Job Status and Long-Running Work

- Long-running jobs need progress, status, cancellation, retry or failure reason, and completion behavior.
- GUI, API, CLI, and MCP must expose consistent job states and error semantics where applicable.
- Do not mark jobs successful until all required processing, validation, and artifact writes have completed.
- Failure messages should help operators fix configuration, prerequisites, permissions, or inputs.

## Spec Kit Requirements

For observability-relevant work:

- `/speckit.specify`: identify operator status needs, audit/provenance events, sensitive fields, and failure modes.
- `/speckit.plan`: define log structure, correlation strategy, audit/provenance schema, retention assumptions, and surface behavior.
- `/speckit.tasks`: create tasks for instrumentation, redaction tests, status surfaces, docs, and changelog.
- `/speckit.implement`: add safe structured events and consistent status behavior.
- `/speckit.analyze`: verify observability is useful, safe, consistent, and aligned with security and privacy rules.

## Required Agent Output

For observability changes, the final agent response must summarize logs, status, audit, and provenance changes, sensitive-data redaction, correlation IDs, job-state behavior, tests added, and docs/operator guidance updated.
