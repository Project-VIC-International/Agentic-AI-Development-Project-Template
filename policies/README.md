# Development Policies

This folder holds the development policies for projects built from this template. They are the single source of truth for every AI coding agent and every human contributor, whatever tool they use.

The policies are adapted from the development policy corpus that Project VIC International volunteers and their agents follow. They are written for digital forensics and investigation tools: evidence integrity, synthetic test data, honest results, interoperable exports, and human review.

## How Agents Find These Policies

| Agent or tool | What it reads | How the policies reach it |
|---------------|---------------|---------------------------|
| Cursor | `.cursor/rules/*.mdc` and `AGENTS.md` | Generated `.mdc` copy of every policy |
| Claude Code | `CLAUDE.md` | `@AGENTS.md` plus `@policies/...` imports of the core policies |
| Gemini CLI | `GEMINI.md` | Same imports as Claude Code |
| GitHub Copilot | `.github/copilot-instructions.md` and `AGENTS.md` | Pointer to the core policies and the index |
| Codex, OpenCode, Zed, Warp, and other `AGENTS.md` tools | `AGENTS.md` | Core rules plus the policy index |
| Any other agent | Nothing automatically | Paste `prompts/START-AGENT-HERE.md` at the start of a session |

See `docs/agent-setup.md` for setup steps for each agent.

## Core and Conditional Policies

Each policy starts with frontmatter:

```yaml
---
description: What the policy covers and when to read it
globs: ["docs/**", "README.md"]
alwaysApply: false
---
```

- **Core policies** (`alwaysApply: true`) apply to every task: the index, student mode, project context, security, privacy and test data, no stubs, the Spec Kit workflow, and human review.
- **Conditional policies** (`alwaysApply: false`) apply when a task touches their area. `globs` lists typical files for that area; agents that do not support globs use the description in the `AGENTS.md` index.

Precedence between policies is defined in `rule-index.md`.

## Changing a Policy

1. Edit the file in `policies/` (never the generated `.cursor/rules/*.mdc` copy).
2. Run `python3 scripts/sync_agent_rules.py`.
3. Review the diff, then commit the policy and the generated files together.

`python3 scripts/sync_agent_rules.py --check` reports anything out of date without changing files. See `rule-authoring.md` for writing guidance.

These policies are public. Do not add names, internal system names, private links, hostnames, or case details. Put project-specific facts in `project-context.md` in your own repository.

Following these policies does not by itself demonstrate compliance with any law, regulation, or security framework. Your agency remains responsible for its own legal, security, and evidence-handling requirements.
