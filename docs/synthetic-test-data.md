# Synthetic Test Data

Synthetic test data lets you build and test safely without exposing sensitive mission data.

## Requirements

Synthetic data should be:

- Generically representative of the mission workflow.
- Safe to place in prompts, repositories, logs, screenshots, and issues.
- Free of real case facts, people, identifiers, images, hashes, agency details, and operational leads.
- Structured enough to exercise the application realistically.
- Aligned to CASE/UCO/CAC concepts where practical, especially for data models, exports, and tests.

## Good Synthetic Data Examples

Good synthetic examples may include:

- Fake case identifiers such as `SYNTH-CASE-001`.
- Fictional names like `Alex Example` or `Jamie Sample`.
- Fake URLs under `example.org`.
- Small dummy files with harmless text.
- Made-up timestamps, tags, categories, and relationships.

## Bad Synthetic Data Examples

Do not use:

- Redacted real evidence.
- Real usernames, handles, URLs, hashes, or file names from a case.
- Real reports with names removed.
- Screenshots from investigative systems.
- Any contraband or suspected contraband.

## Prompt for Generating Synthetic Data

```text
Create a small synthetic dataset for testing this application. It must be generically representative of the mission workflow but must not include real case data, real people, real identifiers, CSAM, suspect material, operational details, credentials, or agency-private information. Align synthetic datasets to the CASE/UCO and CAC Ontologies and use the CASE/UCO SDK's MCP server to create serializers to convert other synthetic data sources into CASE/UCO/CAC format.
```

## See Also

- `examples/synthetic-data/README.md` for the example dataset folder.
- `examples/synthetic-data/sample-case-uco-cac.jsonc` for a commented CASE/UCO/CAC-style JSON-LD teaching example.
- `docs/case-uco-cac-guidance.md` for ontology guidance.

