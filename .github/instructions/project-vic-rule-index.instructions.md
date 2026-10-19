---
applyTo: "**"
---


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
