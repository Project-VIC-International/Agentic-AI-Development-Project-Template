---
description: Security, privacy, jurisdiction-aware compliance, and forensic evidence handling requirements for mission tools
alwaysApply: true
---

# Security and Compliance

Tools built from this template support crimes-against-children investigators, digital forensic examiners, allied law-enforcement users, and supporting technical communities. In production they may handle law-enforcement-sensitive data, digital evidence, derived artifacts, investigative metadata, hash intelligence, model outputs, and, in some deployments, child sexual abuse material (CSAM).

Security, privacy, forensic integrity, and compliance support are release blockers, not optional hardening. Do not claim compliance with any framework, agency policy, or jurisdiction unless the implemented controls, deployment assumptions, operator responsibilities, tests, documentation, and audit evidence support that claim.

## Choose the Control Framework First

Security obligations depend on where the tool will run and whose data it will process. Before planning production security controls:

1. Ask the user which country, state or province, agency, and deployment environment the tool targets, and whether any specific policy is mandated by their organization.
2. Record the answer in the spec and in `policies/project-context.md`.
3. Use the frameworks that apply to that answer. Common examples (not exhaustive; always confirm the current version):
   - United States, criminal justice information (CJI): FBI CJIS Security Policy plus NIST SP 800-53 Rev. 5 and the NIST SP 800-53B baselines and overlays.
   - Australia: the Australian Government Information Security Manual (ISM), the Protective Security Policy Framework (PSPF), the Essential Eight, and the Privacy Act 1988.
   - New Zealand: the New Zealand Information Security Manual (NZISM), the Protective Security Requirements (PSR), and the Privacy Act 2020.
   - European Union and United Kingdom: GDPR and the Law Enforcement Directive (EU) 2016/680, or UK GDPR and Part 3 of the Data Protection Act 2018.
   - Other jurisdictions: the national cybersecurity, data-protection, and digital-evidence requirements the user names.
4. When no framework is mandated, use NIST SP 800-53 Rev. 5 and ISO/IEC 27001 as a neutral control catalogue, and ISO/IEC 27037, 27041, 27042, and 27043 for digital evidence handling and forensic method assurance.
5. If the correct framework, overlay, or baseline is unknown, mark it as an open compliance question in the spec. Do not guess and do not claim compliance.

Treat every framework as versioned and locally interpreted. When a framework is in scope, identify the version, the agency interpretation, the audit context, and which controls are inherited from agency infrastructure.

## Core Requirements

- Authenticate and authorize access to APIs, case data, generated artifacts, exports, and administrative functions. If the application's API key is configured, enforce it; never expose API keys in browser-visible code unless explicitly documented for local development.
- Secrets must come from documented secret-management mechanisms or local development `.env` files excluded from source control. Commit `.env.example`, never `.env`. Do not invent fallback secrets, default production credentials, or silently disable authentication when secrets are missing.
- Validate every API input, file path, archive member, and job configuration at the boundary. Archive extraction must reject path traversal, absolute paths, escaping symlinks/hardlinks, unsafe permissions, decompression bombs, and unexpectedly large extracted content.
- Keep source evidence read-only. Temporary, extracted, cached, or derived artifacts must be isolated under configured case/run directories and must not mutate original evidence.
- Define retention and deletion behavior for temporary files, caches, extracted artifacts, model outputs, embeddings, job queues, logs, exports, and failed processing runs. Cleanup must not delete source evidence or operator-selected case records.
- Never log secrets, API keys, victim identifiers, unnecessary evidence paths, CSAM descriptors, or sensitive case details. Logs must support audit and troubleshooting without disclosing protected content.
- Maintain auditability and provenance for evidence access, processing jobs, model outputs, exports, configuration changes, and operator-visible security events.
- MD5 and SHA-1 may be implemented only for legacy hash-set compatibility (for example, known-hash lookups) and must be labeled as non-integrity-protecting wherever exposed. Use SHA-256 or stronger for integrity reporting, provenance, tamper checks, cache identity, and deduplication unless a documented interoperability requirement says otherwise.
- Protect data in transit and at rest when the deployment context requires it. Document TLS, storage, database, backup, export, and secret-management assumptions.
- Container services must run with least privilege, avoid unnecessary mounts/capabilities, and expose ports only through intended profiles, proxies, or documented local-development paths.
- Dependencies, models, containers, and third-party tools must have a vulnerability and supply-chain review path appropriate to law-enforcement use.
- Security controls must apply identically on every surface (GUI, API, CLI, MCP, exports). A control enforced only in the GUI but bypassable through the API, CLI, or MCP is a vulnerability.

## Control Tailoring

- Classify the tool or feature before choosing controls, for example: investigator GUI, local/offline forensic workstation tool, API/service, batch pipeline, shared repository/database, triage or classification tool, model training/inference component, ontology tooling, training/demo app, export/interop tool, or deployment/operations utility.
- Identify data categories and sensitivity: source evidence, derived artifacts, victim/person identifiers, investigative metadata, hashes, model outputs, audit logs, configuration/secrets, and public/non-sensitive assets.
- State which controls are implemented in code, inherited from agency infrastructure, required from deployment configuration, or outside the feature boundary. Inherited controls still need assumptions and operator guidance.
- Do not apply a generic flat checklist when a workstation tool, offline forensic utility, API service, cloud-hosted workflow, shared database, model pipeline, or evidence export requires different controls.

## AI Assistant and Tooling Restrictions

- Do not paste, summarize, upload, embed, or transmit source evidence, victim identifiers, CSAM descriptors, case-specific investigative facts, credentials, private agency data, or non-public operational details to external AI services. Cloud-hosted AI agents, including the one reading this policy, count as external services unless the user's agency has explicitly approved that workflow in writing.
- Use Tier T0/T1 data in prompts, committed fixtures, documentation, and CI-oriented examples. Tier T2/T3 data belongs only in local, approved environments per `docs/test-data-handling.md`, and never during the course.
- Do not create prompts, seed data, test names, filenames, screenshots, or committed logs that include realistic CSAM descriptions, victim identifiers, investigator identities, agency-sensitive details, or operationally sensitive hash intelligence.
- Do not misrepresent the test data tier in summaries (for example, claiming T0 when verification used T2).
- If an implementation uses local LLMs, MCP tools, model inference, vector stores, embeddings, or agent memory, document what data may enter those components, where it is stored, how it is deleted, and whether it can leave the host.
- Review the permissions of every MCP server, extension, or third-party tool before connecting it to the agent. Prefer least privilege and read-only access.

## Spec Kit Requirements

For security-relevant work, the Spec Kit workflow must cover compliance explicitly instead of treating it as implied:

- `/speckit.specify`: identify users, tool type, jurisdiction and applicable framework, protected data categories, threat/risk assumptions, misuse cases, data retention/deletion needs, forensic integrity requirements, and auditable success criteria.
- `/speckit.plan`: tailor requirements to concrete controls, data flows, trust boundaries, validation points, secrets handling, audit events, storage/transmission protections, inherited/deployment controls, AI/tooling exposure limits, and rollback/incident considerations.
- `/speckit.tasks`: create implementation, test, documentation, and audit-evidence tasks for each relevant control. Security tasks must name files or surfaces, not remain generic.
- `/speckit.implement`: implement real controls and focused tests. Do not satisfy security requirements with stubs, TODOs, disabled checks, or documentation-only claims.
- `/speckit.analyze`: verify spec, plan, tasks, code, tests, docs, changelog, and deployment guidance remain consistent with the identified compliance obligations.

## Required Security Tests

- Boundary validation tests for API payloads, file paths, archive members, job configs, and export destinations.
- Authentication/authorization tests for protected APIs and operator-only actions, on every surface that exposes them.
- Audit/provenance tests proving security-relevant events are emitted without leaking sensitive data.
- Evidence integrity tests proving source media remains read-only and derived artifacts stay inside approved case/run locations.
- Retention/deletion tests for temporary working data, caches, queues, logs, exports, embeddings, and failed-run cleanup where applicable.
- Fixture safety checks proving tests, demos, screenshots, and sample datasets use benign synthetic data, never real CSAM, real victim data, real agency case identifiers, or realistic abuse descriptors.
- Dependency/container/deployment checks when the change affects packages, images, ports, privileges, volumes, or proxy profiles.

## Error Handling

- Return clear 4xx errors for invalid operator input and sanitized 5xx errors for server failures.
- Log internal context for debugging without leaking sensitive values.
- GUI error text should help an investigator fix configuration, credentials, connectivity, or missing prerequisites.
- Fail closed when security validation, ontology validation, or export integrity checks fail.

## Release Gate

Security-relevant changes require focused tests, documentation updates, and a `CHANGELOG.md` entry under `Security` when user-facing or operationally relevant. Do not call a feature complete if the identified controls are unimplemented, untested, unaudited, or undocumented.

## Required Agent Output

For security-relevant changes, the final agent response must summarize protected data touched, trust boundaries changed, authentication/authorization impact, evidence integrity impact, audit/provenance events added or changed, tests added or updated, documentation or deployment assumptions updated, the framework and jurisdiction assumed, and residual open compliance questions.
