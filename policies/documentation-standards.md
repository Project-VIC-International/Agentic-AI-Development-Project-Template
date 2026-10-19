---
description: Documentation structure, audiences, reading level, command-line guidance, troubleshooting, and safe examples for investigator, IT support, and developer docs
globs: ["README.md", "QUICKSTART.md", "CHANGELOG.md", "docs/**"]
alwaysApply: false
---

# Documentation Standards

Documentation must help investigator and examiner users succeed without assuming they are software developers, system administrators, or command-line users.

This policy complements `policies/brand-design-system.md`. Use that policy for terminology, tone, accessibility, and trauma-aware language. Use this policy for documentation structure, audience, readability, and practical operator guidance.

## Primary Audiences

Write documentation for these audiences, in this order:

- **Investigator and examiner users:** non-technical or semi-technical users who need to install, open, operate, and trust the tool.
- **Local IT support staff:** technical helpers who install dependencies, configure systems, troubleshoot network or permission problems, and support users.
- **Technical contributors:** developers, maintainers, integration partners, and agents who need architecture, testing, release, and contribution details.

Do not make users read developer-focused material before they can understand what the tool does, when to use it, how to start, and where to get help.

Readers may work in English as a second or third language. Plain words and short sentences help them as much as they help non-technical readers.

## README Requirements

Each repository's `README.md` should be written primarily for the investigator or examiner user. It should answer:

- What is this tool?
- Who is it for?
- What problem does it help solve?
- What does it not do?
- What data is safe to use during setup, training, and testing?
- How does a user start the tool in the simplest supported way?
- When should the user ask local IT or the project maintainers for help?
- Where are the detailed user, IT support, and developer documents?

Keep command-line setup out of the main README unless it is the only supported path. If commands are unavoidable, explain what they do in plain language and link to the IT support documentation.

## Required Documentation Structure

Every software repository should include a root `docs/` folder. Use this structure unless the repository documents a reason to choose another layout:

- `docs/user-guide.md`: step-by-step user guide.
- `docs/it-support-guide.md`: installation, configuration, troubleshooting, updates, backups, permissions, and local environment support for IT staff.
- `docs/admin-guide.md`: administrative actions, roles, configuration, retention, audit, and security settings when applicable.
- `docs/troubleshooting.md`: common problems, symptoms, likely causes, and safe fixes.
- `docs/glossary.md`: project-specific terms and acronyms.
- `docs/developer-guide.md`: development setup, architecture, tests, release workflow, and contribution guidance.

Small repositories may combine files, but they must still clearly separate user instructions from IT and developer instructions. Create these files when the project has behavior to document; do not fill them with placeholder text.

## Reading Level and Style

Write general user documentation at about a 10th grade (age 15–16) reading level.

- Use short sentences and plain words.
- Prefer active voice.
- Define acronyms the first time they appear.
- Use consistent names for buttons, screens, files, and roles.
- Use numbered steps for procedures.
- Put warnings before the action that creates risk.
- Explain why a risky or confusing step matters.
- Avoid unexplained jargon, vendor buzzwords, idioms, and internal developer shorthand.

Technical documentation may include deeper details, but it should still include plain-language summaries and clear headings.

## Command-Line and Setup Guidance

Assume most investigator users do not know shells, terminals, paths, environment variables, package managers, containers, or Git.

When documentation includes commands:

- Say who should run the command: user, local IT, developer, or maintainer.
- Say where to run it: Windows PowerShell, Command Prompt, macOS Terminal, Linux shell, WSL, container, or GitHub Codespaces.
- Provide copy-paste commands in fenced code blocks.
- Explain expected output or success signs.
- Explain what to do if the command fails.
- Avoid chained commands when a step-by-step sequence is safer for non-technical users.
- Do not ask users to edit hidden files, environment variables, or system settings unless there is no safer setup path.

Prefer GUI-first or installer-style instructions for users when the project supports them. Put advanced setup in the IT support guide.

## Screenshots, Examples, and Sample Data

Use benign synthetic examples only.

Documentation, screenshots, videos, examples, logs, issue templates, and sample outputs must not include real case data, real evidence paths, victim identifiers, investigator identifiers, credentials, agency-private facts, realistic abuse descriptions, or sensitive operational details.

Screenshots should show safe demo data and should not make sensitive fields more visible than necessary.

## Troubleshooting Standards

Organize troubleshooting by symptom, not by internal subsystem. Use this pattern:

- What the user sees.
- What it usually means.
- What the user can safely try.
- When to ask local IT for help.
- What information is safe to share when asking for support.

Do not ask users to share logs or screenshots until the documentation explains how to check them for sensitive content.

## Accessibility and Format

- Use clear headings and short paragraphs.
- Use lists for steps and checklists; avoid large walls of text.
- Add alt text for meaningful images.
- Do not rely on color alone in diagrams or screenshots.
- Keep links descriptive, not "click here."
- Provide printable or offline-friendly guidance when the deployment may be disconnected from the internet.

## Documentation and Release Hygiene

Documentation must match the implemented product.

Update docs and `CHANGELOG.md` when changes affect setup, installation, configuration, user workflows, roles, permissions, security behavior, evidence handling, exports, reports, supported platforms, troubleshooting, release steps, or known limitations.

Do not claim that a feature, platform, installer, workflow, or integration is supported unless it is implemented and tested or clearly marked as planned.

## Spec Kit Requirements

For documentation-relevant work:

- `/speckit.specify`: identify user documentation, IT support documentation, developer documentation, readability, safety, and training needs.
- `/speckit.plan`: define the documentation files to update, audience split, screenshots/examples policy, support workflow, and validation approach.
- `/speckit.tasks`: create explicit tasks for README, user guide, IT support guide, troubleshooting, glossary, changelog, and release notes where applicable.
- `/speckit.implement`: update documentation with the behavior changes, using synthetic examples and clear audience labels.
- `/speckit.analyze`: verify documentation matches implemented behavior, avoids sensitive content, and separates user guidance from IT and developer guidance.

## Required Agent Output

For documentation changes, the final agent response must summarize affected documentation files, intended audiences, readability and accessibility considerations, terminology alignment, synthetic-data safeguards, docs/changelog updates, and known documentation gaps.
