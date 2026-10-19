
# Project VIC Brand and Design System

Project VIC International tools, documentation, reports, demos, websites, APIs, CLIs, MCP servers, and communications must present a unified, professional, accessible, and victim-centered identity.

Visible surfaces must use Project VIC terminology, operator-first language, accessible UI patterns, and approved design-system guidance.

This rule applies to user-facing and operator-visible surfaces, including GUI/UI, API docs, CLI help text, MCP tool names and descriptions, generated reports, exports, screenshots, README files, release notes, websites, training material, and demo content.

## Source of Truth

Use the Project VIC International Brand & Design System when styling, naming, or writing user-facing copy:

<https://github.com/Project-VIC-International/project-vic-brand-design-system>

Until a vendored design-system snapshot exists in the repository:

- Prefer existing project theme tokens and shared UI components.
- Avoid introducing hardcoded colors, fonts, shadows, border radii, spacing systems, icon styles, or new visual language.
- Do not invent new Project VIC logos, colors, fonts, taglines, product names, mascots, or visual systems.
- If a needed design token, component, icon, layout, or brand asset is missing, document the gap instead of creating an inconsistent local standard.

## Terminology

Use exact capitalization and approved names:

- **Project VIC**
- **Project VIC International**
- **VICSafer**
- **VICPoint**
- **ICAC investigator**
- **digital forensics examiner**
- **child sexual abuse material (CSAM)**

Use **Project VIC International** for the nonprofit organization when formality or legal identity matters. Use **Project VIC** when referring to the broader ecosystem, tooling, community, or mission in less formal product contexts.

Define acronyms on first use in documentation and operator-facing text when the audience may include new users.

Avoid inconsistent or informal variants such as `Project Vic`, `PVIC` unless explicitly defined for internal technical use, `VIC Safer`, `VicSafer`, `CSAMs`, `child porn`, or `kiddie porn`.

## Operator-First Language

Operator-facing text should be direct, precise, calm, and useful.

- Avoid marketing-heavy phrases such as "revolutionary", "game-changing", "next-generation", "AI-powered magic", "one-click rescue", or "fully automated investigation".
- Prefer investigator-facing terms over ML jargon: "classification result", "known hash match", "unknown media", "review queue", "case artifact", "source media", "derived artifact", "model confidence", "processing job", "export", "provenance", and "validation result".
- Use technical terms where they are necessary, but explain them clearly.

## Verdict, Confidence, and Analytic-Result Language

When a tool presents analytic verdicts, classifications, detections, or confidence values to operators (investigators, examiners, prosecutors), the language must be standardized, honest, and identical across surfaces:

- Define one repository-level verbal confidence vocabulary (fixed bands such as "strong indication", "moderate indication", "no clear indication", "analysis incomplete") in the shared service layer, version it, and use it identically in GUI, reports, exports, CLI, API descriptions, and MCP outputs. Do not improvise per-surface phrasings.
- State findings as indications and analytic results, never as facts or legal conclusions. Banned formulations include "this image is fake", "this file is authentic for prosecution", "proven AI-generated", and any phrasing implying guilt, victim status, or legal classification.
- Label every displayed score as calibrated or uncalibrated. Do not present an uncalibrated score using probability language.
- Incomplete analysis must read as incomplete ("analysis incomplete — required detector unavailable"), never as a weak finding.
- Plain-language summaries generated for non-technical operators must be deterministic (template-generated from structured results, traceable to the underlying assertion or result IDs). Do not put free-form LLM-generated narrative in evidentiary output paths.
- Limitations and known error modes must accompany the verdict at the same visual weight, not behind a secondary link only.

## Victim-Centered and Trauma-Aware Content

- Use victim-centered, investigator-supportive, and professionally restrained language.
- Do not use sensational, graphic, exploitative, joking, gamified, or emotionally manipulative language.
- Do not use real or recognizable case imagery in screenshots, docs, fixtures, seed data, examples, reports, demos, or tests.
- Do not include realistic CSAM descriptions, victim identifiers, offender names, agency case numbers, or sensitive investigative facts in sample content.
- Use benign synthetic data for examples, demos, screenshots, reports, and test fixtures.
- Prefer language that centers the mission and investigators, not the tool as the hero.
- Avoid implying that software alone safeguards children. Project VIC tools support trained investigators and allied professionals.

## Accessibility

- New GUI and web-visible work must target WCAG 2.2 AA unless the repository explicitly documents a different accessibility baseline.
- **Light and dark modes are mandatory for Project VIC GUIs** (ADR 0009 in the Brand & Design System). Follow OS/`prefers-color-scheme` by default and provide an explicit user override (`data-theme="light|dark"` or platform equivalent). Both modes must meet WCAG AA for text, cards, actions, and status/severity banners.
- **Excluded from the GUI theme-toggle mandate:** public marketing websites **projectvic.org** and **gpusforgood.org**. Those sites may ship a single curated marketing theme; they are not required to offer a product light/dark toggle.
- Consumer contract: <https://github.com/Project-VIC-International/project-vic-brand-design-system/blob/main/docs/gui-theming.md>
- Preserve keyboard navigation, visible focus indicators, readable typography, sufficient contrast, accessible forms, semantic headings, labels, alt text, and screen-reader-friendly status updates.
- Do not rely on color alone to communicate severity, category, confidence, status, or error conditions.
- Error messages must be clear, actionable, and accessible.
- Loading states, progress indicators, notifications, and validation messages must be perceivable and understandable.
- Touch targets, drag interactions, authentication flows, and repeated-entry workflows must account for accessibility requirements.

## GUI and UI

- Reuse existing theme patterns and components in the project.
- Prefer shared design-system tokens and components over local styling.
- Avoid hardcoded colors, one-off typography, custom spacing systems, and inconsistent icon styles.
- **Do not mode-mix.** Never put light-only fills (`background: white`, pastel `color-mix(..., white)`, or light-only hex) under a dark shell, and never put `--pv-color-text-primary` (or equivalent body text) on a pastel status fill. Use mode-aware pairs: `--pv-color-bg-surface` with `--pv-color-text-primary`; `--pv-color-role-*-tint` with the matching `--pv-color-role-*-text`.
- Severity / status banners must use design-system role tint + on-tint text tokens so they remain readable in both light and dark modes.
- Maintain consistent placement of primary actions, destructive actions, filters, status indicators, and help text.
- Use clear confirmations for destructive or irreversible actions.
- Do not make sensitive case details, evidence paths, victim identifiers, or CSAM-related descriptors more visible than necessary.
- UI text should help investigators understand what happened, what they can do next, and whether action is required.

## Reports, Exports, and Generated Artifacts

Reports and exports should explain what was found, how it was produced, what source media or records it came from, what tool/model/action produced it, what confidence, validation, or provenance is available, and what limitations apply.

- Human-readable reports and machine-readable outputs must use terminology consistent with the ontology-alignment rule.
- Reports must not include unnecessary sensitive details, real case imagery, or graphic descriptors.

## API, CLI, and MCP Surfaces

Visible text in API docs, CLI help, CLI errors, MCP tool names, MCP tool descriptions, and MCP structured outputs must follow Project VIC terminology and tone.

- API descriptions must use consistent field names and terminology.
- CLI commands must provide clear, operator-friendly help text and actionable errors.
- MCP tools must use safe, bounded descriptions that explain what the tool does without exaggerating capability.
- MCP, API, CLI, and GUI terminology must remain consistent unless a difference is intentional and documented.
- Do not expose internal implementation jargon to operators unless it is necessary for troubleshooting.

## Documentation and Communications

Documentation, release notes, websites, training materials, and public-facing copy must follow Project VIC terminology, avoid unsupported claims, avoid overpromising AI or automation, identify limitations honestly, use benign synthetic examples, avoid real case details, distinguish nonprofit mission language from product capability language, and keep screenshots and diagrams accessible and professional.

## Specs and Releases

Release notes must call out operator-visible copy, layout, report, export, terminology, accessibility, or workflow changes.

## Spec Kit Requirements

For visible-surface changes:

- `/speckit.specify`: identify affected user-visible surfaces, terminology, accessibility, brand, report, export, and documentation impact.
- `/speckit.plan`: define design-system tokens/components, copy changes, accessibility checks, screenshots/docs updates, and terminology alignment.
- `/speckit.tasks`: create explicit tasks for GUI/API/CLI/MCP/docs/report copy and accessibility updates.
- `/speckit.implement`: use approved components, terminology, and accessible patterns.
- `/speckit.analyze`: verify visible surfaces remain consistent with brand, terminology, accessibility, ontology alignment, and release documentation.

## Required Agent Output

For brand-relevant or visible-surface changes, the final agent response must summarize visible surfaces affected, brand/design-system elements used, new or changed terminology, accessibility checks performed, screenshots/docs/reports/release notes updated, design-system gaps found, and intentionally deferred brand or accessibility work.
