# Test Data Handling

Projects built from this template use **tiered test data**. The tiers tell you, and your AI agent, which data may go where.

**During the course and workshop: use Tier T0 or T1 only.** Tiers T2 and T3 are described so you know how to handle real-world testing later, inside your own agency and under its rules.

**Default:** Tier T0 (public-safe synthetic) for anything committed, shared, sent to an AI agent, or automated.

This document is the reference for agents and humans. The short version for beginners is [synthetic-test-data.md](synthetic-test-data.md).

## Data Tiers

| Tier | Name | Typical use | Commit to git? | CI / GitHub Actions? | Cloud AI agent prompts? |
|------|------|-------------|----------------|----------------------|--------------------------|
| **T0** | Public-safe synthetic | Unit tests, fixtures, docs, screenshots, pull requests, issues | Yes | Yes | Yes (still no CSAM or realistic abuse content) |
| **T1** | Realistic synthetic | UI testing, volume, file formats, demo realism without agency data | Yes, if identifiers are obviously fake | Yes | Yes, with the same content rules as T0 |
| **T2** | Agency-approved sample | Private manual testing and pilot demos **after the course**, with examiner feedback | **No.** Local or approved storage only | **No** | Only if your agency's written approval covers it; prefer local models |
| **T3** | Production operational | Live agency environment | No | No | Only as your agency's policy allows |

**Non-negotiable for every tier and channel:** no CSAM or suspected CSAM in repositories, issues, prompts, CI artifacts, or examples. No real victim identifiers, credentials, or agency-private operational details in public or shared channels.

"Agency approval" means approval from whoever is authorized under your organization's and jurisdiction's rules. An AI agent can never give or assume that approval.

## Maturity Guidance

Align with the [release roadmap template](../planning/release-roadmap-template.md) and `policies/versioning-release-management.md`.

| Phase | Versions (guide) | Default tier | Manual testing and demos |
|-------|------------------|--------------|--------------------------|
| Course and workshop | Any | T0 | T0 or T1 only |
| Pre-MVP build | v0.1–v0.4 (flexible) | T0 | T0 or T1 |
| Demo or pilot | about v0.5 and later (not fixed) | T0 in repo and CI | T1, or T2 with a documented plan |
| Pre-MVP hardening | later 0.x versions | T0 in repo and CI | T2 as needed |
| **v1.0.0 MVP** | MVP tag | T0 for automation | T3 validation in an approved environment |
| **v2.0.0+** | Platform | T0 for automation | T3 under agency controls |

Pilot demos often need realistic data when synthetic data cannot show whether examiners trust the labels and workflow. Using approved T2 data is not a policy violation when it is documented. It must never be hidden from the test record.

## Channel Matrix

"Do not use real data" means: **do not put protected data in the wrong channel.**

| Channel | Allowed tiers | Notes |
|---------|---------------|-------|
| Git commits, pull request diffs, Actions logs | T0, T1 | Use `testdata/` or `examples/synthetic-data/`; local tiers are gitignored |
| GitHub Issues and comments | T0, T1 | Describe scenarios; link to the handling plan, not raw fields |
| README, docs, changelog, screenshots | T0, T1 | Use obviously fake identifiers |
| AI agent prompts, chats, and attached files (cloud) | T0, T1 | T2 only with written agency approval for that exact tool and workflow |
| Remote MCP servers and agent plugins | T0, T1 | Same rule as cloud AI prompts |
| Local disk, air-gapped lab, agency VM | T0–T3 per plan | Strongest controls for T2 and T3 |
| In-person demo workstation | T1–T2 | Plan documents machine, audience, and retention |

Anything you type into a cloud AI agent, paste into its chat, or let it read from disk may leave your machine. Treat the agent as an external service.

## Test Data Handling Plan (required for T2 and T3)

Before the first use of T2 data, copy [templates/test-data-handling-plan.md](templates/test-data-handling-plan.md) into your repository (for example `docs/test-data-handling-plan.md` or the release spec folder) and fill it in. Minimum fields:

- approver role and date
- tier (T2 or T3)
- environment (hardware, network, offline status, who has access)
- data description (category only; no case narrative in shared copies)
- allowed uses (manual test, demo date, training)
- **prohibited channels** (issues, public repository, CI, cloud AI, chat tools, and so on)
- storage path (for example `demo-data/local/`, which is gitignored)
- retention and deletion

If your repository is public, keep the filled plan in a private location instead, because even the description of a dataset can be sensitive.

Agents and testers must **record the tier** in manual test execution records and release annexes. Never label a T2 session as T0.

## Local-Only Storage

Keep T2 and T3 data outside version control:

```text
demo-data/local/          # agency-approved samples (gitignored)
testdata/local/           # developer machine-only inputs (gitignored)
```

Both paths are in the root `.gitignore`. Never commit evidence, operational exports, or credentials. Do not let an agent index or read these folders unless your plan allows it.

## Automated and Manual Testing

| Activity | Data tier |
|----------|-----------|
| CI, pre-commit hooks, committed test fixtures | **T0** (T1 only with obviously fake identifiers that are safe to share) |
| Local test command in the developer workflow | T0/T1 from the repository |
| Manual checklist, demos, pilots with examiners | T0–T2 per plan (T0/T1 during the course) |
| Production | T3, agency environment only |

## Product Redaction and Test Inputs

If the product processes sensitive data, it must redact sensitive fields in logs, exports, and the UI. That is a separate question from which tier you test with. You can test redaction with T1 data, or later with T2 data in a private environment, while commits stay at T0.

## Agent Behavior

- Generate T0/T1 fixtures by default.
- During the course, refuse T2 or T3 data and explain why.
- After the course, help users configure approved T2 data only in approved environments, and suggest a handling plan when they need demo realism.
- Never encourage committing T2 paths, pasting T2 data into issues, or sending T2 data to cloud AI without approval.
- Never claim that testing used T0 when the record says T2.
- If protected data appears in a prompt, file, or log, stop, tell the user, and do not repeat the data back.

## Related

- [SECURITY.md](../SECURITY.md)
- [manual-test-checklist.md](manual-test-checklist.md)
- `policies/privacy-redaction-and-synthetic-data.md`
- `policies/testing-quality.md` and `policies/testing-program.md`
