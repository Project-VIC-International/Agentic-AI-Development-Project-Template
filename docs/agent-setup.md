# Agent Setup

This template works with any AI coding agent. The development policies live in one place, `policies/`, and small adapter files deliver them to each tool. You do not need to copy or edit rules for your agent.

The course instructor uses Cursor in the workshop. You can follow along with a different agent; the workflow is the same.

## Which File Each Agent Reads

| Agent | Loads automatically | Spec Kit integration key | Spec Kit command style |
|-------|---------------------|--------------------------|------------------------|
| Cursor | `.cursor/rules/*.mdc` (generated from `policies/`) and `AGENTS.md` | `cursor-agent` | type `/speckit` in chat and pick from the menu |
| Claude Code | `CLAUDE.md`, which imports `AGENTS.md` and the core policies | `claude` | `/speckit-specify` |
| OpenAI Codex | `AGENTS.md` | `codex` | `$speckit-specify` |
| GitHub Copilot (VS Code, CLI, coding agent) | `.github/copilot-instructions.md`; current versions also read `AGENTS.md` | `copilot` | `/speckit-specify` |
| Gemini CLI | `GEMINI.md`, which imports `AGENTS.md` and the core policies | `gemini` | as listed by `/help` |
| OpenCode | `AGENTS.md` | `opencode` | as listed in the command menu |
| Zed | The first instruction file it finds (for example `.github/copilot-instructions.md` or `AGENTS.md`), which points to the policies | `zed` | `/speckit-specify` |
| Warp | `AGENTS.md` | `generic` | depends on the commands folder you choose |
| Any other agent | Possibly nothing | `generic` | depends on the commands folder you choose |

Agent features change often. If your agent does not seem to follow the rules, use the start prompt below. It works with every agent.

## Start Prompt (works with any agent)

At the start of a new chat or session, paste the prompt from `prompts/START-AGENT-HERE.md`. It tells the agent to read `AGENTS.md` and the core policies before doing anything else.

To check that your agent has loaded the rules, ask:

```text
Before we start: which data am I allowed to use in this project, and what must you ask me before doing? Answer from the policies in this repository and name the files you read.
```

A correct answer mentions Tier T0/T1 synthetic data only, and asking before installs, pushes, repository changes, deletions, and spending money. If the answer is vague, paste the start prompt.

## Setting Up Spec Kit for Your Agent

Do this **after** your first intake is complete (see `START-HERE.md`).

1. Install the Spec Kit command-line tool. The setup scripts in `scripts/` can do this for you, or see the [Spec Kit installation guide](https://github.github.io/spec-kit/installation.html).
2. In the project folder, run the command for your agent, for example:

   ```bash
   specify init --here --integration cursor-agent
   ```

   Replace `cursor-agent` with the key from the table above. If you leave out `--integration`, Spec Kit asks you to choose.
3. Restart or reload your agent so it sees the new Spec Kit commands.
4. Ask your agent to run the constitution step, using the policies in `policies/` as the starting principles.

Spec Kit adds its own files (for example `.specify/` and an agent commands or skills folder). It does not change `AGENTS.md`, `CLAUDE.md`, or the other instruction files unless you install its optional `agent-context` extension. That extension writes only inside its own `SPECKIT START` / `SPECKIT END` markers.

## Safety Settings Worth Checking

Most agents can run terminal commands, edit files, and call external tools. During the course:

- **Keep command approval on.** Do not enable "auto-run", "YOLO", "full auto", or "skip permissions" modes. You should see and approve each terminal command, at least until you understand what the agent is doing.
- **Review MCP servers and extensions before adding them.** Each one can read data and take actions. See `policies/mcp-agent-safety.md`.
- **Know where your prompts go.** Cloud agents send your prompts and the files they read to the provider. Use only T0/T1 synthetic data (`docs/test-data-handling.md`). Check whether your agency allows the tool before using it for real work later.
- **Use privacy settings.** Many tools offer a privacy or "no training" mode. Turn it on if your agency requires it.

## If You Switch Agents

You can change agents at any time. The policies stay the same. Run `specify init --here --integration <new-key>` to add Spec Kit commands for the new agent, then paste the start prompt in the first session.

## Changing the Policies

Edit the files in `policies/`, then run:

```bash
python3 scripts/sync_agent_rules.py
```

This regenerates `.cursor/rules/`, the policy index in `AGENTS.md`, the imports in `CLAUDE.md` and `GEMINI.md`, and `.github/copilot-instructions.md`. Run it with `--check` to confirm nothing is out of date. See `policies/rule-authoring.md`.
