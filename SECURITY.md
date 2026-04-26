# Security and Sensitive Data

This template is for building mission-support tools in the crimes against children domain. Treat security and data handling as core requirements from the first session.

## Development Data Rules

Never place the following in prompts, repositories, issues, logs, screenshots, test files, or sample datasets:

- CSAM or suspected CSAM.
- Real case data.
- Victim, witness, suspect, or investigator identifiers.
- Credentials, API keys, tokens, passwords, or private certificates.
- Sensitive investigative techniques, leads, or operational details.
- Agency-private systems information.

Use synthetic data that is generically representative of your mission data. The synthetic data should preserve structure, fields, relationships, and workflow patterns without exposing real people, evidence, or investigations.

## Production Boundary

Build applications so they can later process and store real mission data, but only deploy them into approved production environments with the right legal, technical, and agency controls.

Development environments, personal GitHub accounts, test Cursor sessions, and public AI tools are not production investigative systems.

## Repository Defaults

- Use private repositories by default.
- Review permissions before connecting Cursor, GitHub CLI, MCP servers, or third-party tools.
- Keep GitHub Actions minimal to reduce cost and limit exposure.
- Do not upload large evidence-like files or use Git LFS unless your agency has approved the cost and data handling model.
- Remove secrets from commits immediately if they are accidentally added, and rotate the exposed secret.

## Synthetic Test Data

Good synthetic data should answer these questions:

- Does the application handle the same file types, fields, and relationships it will see in production?
- Can the user perform the same workflow they expect to perform with mission data?
- Can the test data be shared publicly without harm?
- Does the data avoid real names, locations, identifiers, hashes, case numbers, and operational details?

