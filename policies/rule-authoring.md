---
description: How to create, change, and maintain the policies in policies/ and the generated agent instruction files (AGENTS.md, CLAUDE.md, GEMINI.md, Copilot, Cursor rules)
globs: ["policies/**", "AGENTS.md", "CLAUDE.md", "GEMINI.md", ".github/copilot-instructions.md", ".cursor/rules/**", "scripts/sync_agent_rules.py"]
alwaysApply: false
---

# Rule Authoring

Policies are governance artifacts. They should help any coding agent make safe, consistent engineering decisions without creating contradictions, excessive noise, or false authority.

Use this policy when creating, reviewing, splitting, or maintaining files in `policies/` or the agent instruction files generated from them.

## Layout

- `policies/*.md` is the **single source of truth**. Each file has YAML frontmatter (`description`, `alwaysApply`, optional `globs`) and a Markdown body that any agent can read.
- `scripts/sync_agent_rules.py` generates the agent-specific files from `policies/`:
  - `.cursor/rules/<name>.mdc` for Cursor, each marked as generated.
  - The policy index inside `AGENTS.md` (read by Codex, Cursor, Copilot coding agent, OpenCode, Zed, Warp, and others).
  - The `@policies/...` import list inside `CLAUDE.md` (Claude Code) and `GEMINI.md` (Gemini CLI).
  - The policy pointer inside `.github/copilot-instructions.md` (GitHub Copilot).
- Generated regions are bounded by `PROJECT-VIC-POLICY:START` / `PROJECT-VIC-POLICY:END` comments. Text outside those markers belongs to people or to Spec Kit and is never overwritten.

**Workflow:** edit `policies/<name>.md`, run `python3 scripts/sync_agent_rules.py`, review the diff, and commit the policy and generated files together. `python3 scripts/sync_agent_rules.py --check` reports drift without writing anything.

Never edit a generated `.cursor/rules/*.mdc` file directly; the next sync overwrites it. Hand-written Cursor rules without the generated marker are left alone.

## Public-Safe Content

This template and its policies are public. Policies may be copied into other public repositories. They must never contain:

- people's names, usernames, email addresses, or phone numbers;
- names of internal or non-public tools, systems, or projects;
- private repository URLs, internal hostnames, IP addresses, or network details;
- case details, agency-private facts, credentials, or tokens.

Keep agency- or project-specific facts in `policies/project-context.md` in the student's own repository, and keep that repository private if those facts are sensitive.

## Rule Scope

- Use `alwaysApply: true` only for broad standards that every task needs: safety, data handling, honesty, the workflow, and human review. Always-on text costs context on every request.
- Use `globs` and a specific `description` for policies that apply to narrow areas (docs, GUI, API, MCP, models, databases, releases). Agents that do not support globs still see the description in the `AGENTS.md` index and read the file when relevant.
- Project context supplements, but never overrides, the shared standards.
- Reusable policies should not name a specific product unless intentionally product-specific.

## Rule Precedence

Precedence lives in `policies/rule-index.md`. Update the index instead of creating competing local hierarchies. When policies overlap, prefer the stricter safety, evidence, or security requirement and the more specific implementation guidance for the touched surface.

## Rule Quality

- Keep policies focused and actionable: what agents must do, what they must not do, and the final output required when the policy is triggered.
- Include Spec Kit hooks when the policy affects non-trivial development.
- Prefer clear operational requirements over broad value statements.
- Reference other policies by path instead of duplicating long sections.
- Write for readers whose first language may not be English: short sentences, defined acronyms, no idioms.
- If policies conflict, identify the precedence and fix the policies.

## Frontmatter

```yaml
---
description: Concise, specific summary an agent can use to decide relevance
globs: ["docs/**", "README.md"]
alwaysApply: false
---
```

- `description` is required.
- `alwaysApply` is required (`true` or `false`).
- `globs` is optional and written as a JSON-style list on one line.

## Maintenance

- Update policies when repeated agent failures occur, and when standards, the Spec Kit workflow, compliance expectations, or architecture practices change.
- Keep policy language aligned with the Spec Kit constitution.
- Changing policies or agent instruction files is a high-risk change (`policies/human-review-and-risk-gates.md`): explain the change and get the user's approval.
- Do not edit generated sections by hand; regenerate them.
- When policies change operational behavior, consider documentation, changelog, and release impact.

## Required Agent Output

For rule-authoring changes, the final agent response must summarize policies created or changed, scope/alwaysApply/glob decisions, conflicts considered, constitution links, whether the sync script was run and `--check` passes, and any follow-up policies that should be split or consolidated.
