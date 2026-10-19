# Mandatory Development Policy Corpus

Project VIC development agents in this repository follow the mandatory policy corpus. Do not edit the generated policy files by hand. A change to policy has to come from a new reviewed corpus version.

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

There is no GitHub release tag for this corpus yet. This repository pins the commit above. Do not update policy by cloning the moving `main` branch.

The manifest copied into this repository is `.project-vic/manifest.json`.

## Installed adapters

The official installer was `python3 scripts/corpus.py install` from the pinned corpus checkout. Cursor was installed with `--overwrite` because this repository already had different Cursor rules and those rules were replaced on purpose.

| Agent | Entry point |
| --- | --- |
| Cursor | `.cursor/rules/*.mdc` |
| Claude Code | `CLAUDE.md` |
| GitHub Copilot | `.github/copilot-instructions.md` and `.github/instructions/*.instructions.md` |
| Gemini CLI | `GEMINI.md` |
| Hermes Agent | `.hermes.md` |
| OpenCode | `opencode.json` |
| Zed | `.rules` |
| OpenAI Codex | `AGENTS.md` and `.codex/config.toml` |
| Warp | `AGENTS.md` |

Shared canonical policy text also lives in `.project-vic/policies/`. `.project-vic/PROJECT-VIC-POLICY.md` is the combined human-readable copy.

## Codex and Warp

Codex and Warp both use `AGENTS.md`, and the two generated copies are not byte-for-byte identical. Only the tool name on the first line differs. The policy text below that line is the same.

This repository keeps the Codex `AGENTS.md` together with `.codex/config.toml`. That config raises Codex's project-document limit to 262,144 bytes so the full corpus is not cut off at the 32 KiB default. Warp reads the same `AGENTS.md`. Its policy text matches the Warp adapter. The first-line label says Codex.

## Local rules that were not kept

The installer does not delete files. After installation, `.cursor/rules/student-mode.mdc` was still present. It is not part of the mandatory corpus, so it was removed. No local supplemental instruction is approved. Do not add a repository rule that weakens these policies.

## Check

On 2026-10-19, `python3 scripts/corpus.py check` passed in the pinned corpus checkout. Every installed adapter file was then compared with that checkout. All compared files matched. The Warp `AGENTS.md` was not copied, for the reason above.
