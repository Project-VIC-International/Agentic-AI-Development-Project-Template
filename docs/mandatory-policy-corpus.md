# Mandatory Development Policy Corpus

v0.2.0 pinned the Project VIC mandatory policy corpus in this repository. As of v0.2.1, agents follow the public-safe policies in `policies/`. The files under `.project-vic/` stay as the upstream pin. Do not load them as a second live rule set.

## Pinned source

| Record | Value |
| --- | --- |
| Corpus repository | [Project-VIC-International/Mandatory-Development-Policy-Corpus](https://github.com/Project-VIC-International/Mandatory-Development-Policy-Corpus) |
| Corpus version | `0.1.0` |
| Corpus commit | `57bfea65f7f97769446d62a3b7cc07ead09d2649` |
| Upstream policy commit | `dcb94f517e4a31fbb9e1a9b43f5fa0347eb114d7` |
| Manifest SHA-256 | `92cc25b23b92b88cd449e06e711a566a3c1d1fd2fdb1e9d9db255ca5865b1dba` |
| Policy count | 25 |
| Installed on | 2026-10-19 |

There is no GitHub release tag for this corpus yet. This repository pins the commit above. Do not update the pin by cloning the moving `main` branch.

The manifest copied into this repository is `.project-vic/manifest.json`.

## What agents follow

Edit `policies/`, then run:

```bash
python3 scripts/sync_agent_rules.py
```

That refreshes `.cursor/rules/*.mdc` and the policy sections in `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, and `.github/copilot-instructions.md`. OpenCode loads `policies/*.md` through `opencode.json`. Codex still uses `AGENTS.md` with `.codex/config.toml`.

`.hermes.md`, `.rules`, and `.github/instructions/` were removed in v0.2.1 so Hermes, Zed, and Copilot do not also load the full upstream corpus.

## Check

On 2026-10-19, `python3 scripts/corpus.py check` passed for the pinned corpus checkout, and the v0.2.0 install matched that checkout. v0.2.1 then adopted the public policy set from pull request 9. Confirm the live set with:

```bash
python3 scripts/sync_agent_rules.py --check
```
