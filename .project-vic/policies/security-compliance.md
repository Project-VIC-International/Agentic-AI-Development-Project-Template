
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
