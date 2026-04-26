# Problem Intake Example

## Mission Problem

Analysts need a safe way to track which synthetic files in a training dataset have been reviewed, hashed, and flagged for follow-up.

## Proposed User

Training participants learning how to move from file listings to small workflow tools.

## Proposed Solution

Create a small application that imports a CSV file inventory, lets the user mark review state, and produces a summary report.

## Constraints

- Use synthetic data only.
- Keep the first milestone small enough to build during a workshop.
- Prefer simple local storage and a simple interface.

## Synthetic Data Plan

Use fictional file names, fake identifiers, and harmless text files. Do not use real case names, real hashes, real paths from agency systems, or evidence-derived content.

## CASE/UCO/CAC Considerations

- Reuse CASE/UCO naming where file objects, hashes, and actions map cleanly.
- Keep the first milestone lightweight and avoid forcing full RDF serialization too early.
