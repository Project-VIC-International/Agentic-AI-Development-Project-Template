#!/usr/bin/env python3
"""Generate agent-specific instruction files from the canonical policies/ folder.

policies/*.md is the single source of truth. This script writes:

  .cursor/rules/<name>.mdc          one generated Cursor rule per policy
  AGENTS.md                         policy index between the PROJECT-VIC-POLICY markers
  CLAUDE.md, GEMINI.md              @policies/... imports between the markers
  .github/copilot-instructions.md   policy pointer between the markers

Only generated .mdc files (those containing GENERATED_TAG) and the text between
the markers are ever changed. Everything else belongs to people or to Spec Kit.

Usage:
  python3 scripts/sync_agent_rules.py           write generated files
  python3 scripts/sync_agent_rules.py --check   exit 1 if anything is out of date

Requires Python 3.10+ and the standard library only.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POLICY_DIR = ROOT / "policies"
CURSOR_RULES_DIR = ROOT / ".cursor" / "rules"

GENERATED_TAG = "by scripts/sync_agent_rules.py"
START_MARKER = "<!-- PROJECT-VIC-POLICY:START -->"
END_MARKER = "<!-- PROJECT-VIC-POLICY:END -->"
FIRST_POLICY = "rule-index"
EXCLUDED_FILES = {"README.md"}


class SyncError(Exception):
    """A problem the user must fix before the sync can run."""


@dataclass(frozen=True)
class Policy:
    name: str
    description: str
    always_apply: bool
    globs: tuple[str, ...]
    body: str

    @property
    def path(self) -> str:
        return f"policies/{self.name}.md"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def parse_scalar(raw: str) -> str:
    value = raw.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def parse_policy(path: Path) -> Policy:
    text = read_text(path)
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        raise SyncError(f"{path.relative_to(ROOT)}: missing frontmatter (first line must be ---)")
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        raise SyncError(f"{path.relative_to(ROOT)}: frontmatter is not closed with ---") from None

    fields: dict[str, str] = {}
    for number, line in enumerate(lines[1:end], start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, sep, value = line.partition(":")
        if not sep:
            raise SyncError(f"{path.relative_to(ROOT)}:{number}: expected 'key: value'")
        fields[key.strip()] = value.strip()

    unknown = set(fields) - {"description", "alwaysApply", "globs"}
    if unknown:
        raise SyncError(f"{path.relative_to(ROOT)}: unknown frontmatter keys: {', '.join(sorted(unknown))}")

    description = parse_scalar(fields.get("description", ""))
    if not description:
        raise SyncError(f"{path.relative_to(ROOT)}: description is required")

    always_raw = fields.get("alwaysApply", "").lower()
    if always_raw not in {"true", "false"}:
        raise SyncError(f"{path.relative_to(ROOT)}: alwaysApply must be true or false")

    globs: tuple[str, ...] = ()
    if fields.get("globs"):
        try:
            parsed = json.loads(fields["globs"])
        except json.JSONDecodeError as exc:
            raise SyncError(f"{path.relative_to(ROOT)}: globs must be a JSON list on one line ({exc})") from None
        if not isinstance(parsed, list) or not all(isinstance(g, str) and g for g in parsed):
            raise SyncError(f"{path.relative_to(ROOT)}: globs must be a list of non-empty strings")
        globs = tuple(parsed)

    body = "\n".join(lines[end + 1 :]).strip("\n") + "\n"
    return Policy(path.stem, description, always_raw == "true", globs, body)


def load_policies() -> list[Policy]:
    if not POLICY_DIR.is_dir():
        raise SyncError("policies/ folder not found")
    policies = [parse_policy(p) for p in POLICY_DIR.glob("*.md") if p.name not in EXCLUDED_FILES]
    if not policies:
        raise SyncError("no policies found in policies/")
    return sorted(policies, key=lambda p: (p.name != FIRST_POLICY, p.name))


def yaml_scalar(text: str) -> str:
    needs_quotes = (
        ": " in text
        or " #" in text
        or text != text.strip()
        or text.startswith(("[", "{", "&", "*", "!", "|", ">", "%", "@", "`", "'", '"', "-", "?", "#"))
        or text.lower() in {"true", "false", "null", "yes", "no", "on", "off", "~"}
    )
    return json.dumps(text, ensure_ascii=False) if needs_quotes else text


def render_mdc(policy: Policy) -> str:
    front = ["---", f"description: {yaml_scalar(policy.description)}"]
    if policy.globs:
        front.append(f"globs: {json.dumps(list(policy.globs))}")
    front.append(f"alwaysApply: {'true' if policy.always_apply else 'false'}")
    front.append("---")
    notice = (
        f"<!-- Generated from {policy.path} {GENERATED_TAG}. "
        "Edit the source policy, then re-run the script. -->"
    )
    return "\n".join(front) + "\n" + notice + "\n\n" + policy.body


def render_agents_index(policies: list[Policy]) -> str:
    always = [p for p in policies if p.always_apply]
    conditional = [p for p in policies if not p.always_apply]
    out = [
        "<!-- Generated by scripts/sync_agent_rules.py from policies/. Do not edit between these markers. -->",
        "",
        "### Core policies (read before every task)",
        "",
        "| Policy | Summary |",
        "|--------|---------|",
    ]
    out += [f"| `{p.path}` | {escape_cell(p.description)} |" for p in always]
    out += [
        "",
        "### Conditional policies (read when the task touches the area)",
        "",
        "| Policy | Read when | Typical files |",
        "|--------|-----------|---------------|",
    ]
    for p in conditional:
        files = ", ".join(f"`{g}`" for g in p.globs) if p.globs else "Any, by topic"
        out.append(f"| `{p.path}` | {escape_cell(p.description)} | {escape_cell(files)} |")
    return "\n".join(out)


def render_imports(policies: list[Policy]) -> str:
    lines = [
        "<!-- Generated by scripts/sync_agent_rules.py from policies/. Do not edit between these markers. -->",
        "",
        "Core policies (always loaded):",
        "",
    ]
    lines += [f"@{p.path}" for p in policies if p.always_apply]
    lines += [
        "",
        "Conditional policies are listed in AGENTS.md. Read the matching file in policies/ "
        "before working in that area.",
    ]
    return "\n".join(lines)


def render_copilot(policies: list[Policy]) -> str:
    lines = [
        "<!-- Generated by scripts/sync_agent_rules.py from policies/. Do not edit between these markers. -->",
        "",
        "Before every task, read these core policies:",
        "",
    ]
    lines += [f"- `{p.path}`: {p.description}" for p in policies if p.always_apply]
    lines += [
        "",
        "Read the matching conditional policy listed in `AGENTS.md` before working in its area.",
    ]
    return "\n".join(lines)


def escape_cell(text: str) -> str:
    return text.replace("|", "\\|")


def replace_region(path: Path, content: str) -> str:
    rel = path.relative_to(ROOT)
    if not path.exists():
        raise SyncError(f"{rel} not found. Restore it from the template, keeping the policy markers.")
    text = read_text(path)
    if text.count(START_MARKER) != 1 or text.count(END_MARKER) != 1:
        raise SyncError(
            f"{rel} must contain exactly one {START_MARKER} and one {END_MARKER} line. "
            "Add them back where the generated policy list belongs."
        )
    head, rest = text.split(START_MARKER)
    _, tail = rest.split(END_MARKER)
    return f"{head}{START_MARKER}\n{content}\n{END_MARKER}{tail}"


def is_generated(path: Path) -> bool:
    try:
        head = read_text(path)[:2000]
    except OSError:
        return False
    return GENERATED_TAG in head


def plan(policies: list[Policy]) -> tuple[dict[Path, str], list[Path], list[str]]:
    """Return (files to write, generated files to delete, warnings)."""
    writes: dict[Path, str] = {}
    warnings: list[str] = []

    wanted = set()
    for policy in policies:
        target = CURSOR_RULES_DIR / f"{policy.name}.mdc"
        wanted.add(target)
        if target.exists() and not is_generated(target):
            warnings.append(
                f"{target.relative_to(ROOT)} is hand-written, so it was not overwritten. "
                f"Rename it or delete it to use {policy.path}."
            )
            continue
        writes[target] = render_mdc(policy)

    deletes = []
    if CURSOR_RULES_DIR.is_dir():
        for existing in sorted(CURSOR_RULES_DIR.glob("*.mdc")):
            if existing not in wanted and is_generated(existing):
                deletes.append(existing)

    writes[ROOT / "AGENTS.md"] = replace_region(ROOT / "AGENTS.md", render_agents_index(policies))
    imports = render_imports(policies)
    writes[ROOT / "CLAUDE.md"] = replace_region(ROOT / "CLAUDE.md", imports)
    writes[ROOT / "GEMINI.md"] = replace_region(ROOT / "GEMINI.md", imports)
    copilot = ROOT / ".github" / "copilot-instructions.md"
    writes[copilot] = replace_region(copilot, render_copilot(policies))
    return writes, deletes, warnings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--check", action="store_true", help="report drift without writing; exit 1 if out of date")
    args = parser.parse_args(argv)

    try:
        policies = load_policies()
        writes, deletes, warnings = plan(policies)
    except SyncError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    changed = [p for p, text in writes.items() if not p.exists() or read_text(p) != text]

    for warning in warnings:
        print(f"warning: {warning}", file=sys.stderr)

    if args.check:
        for path in changed:
            print(f"out of date: {path.relative_to(ROOT)}")
        for path in deletes:
            print(f"stale: {path.relative_to(ROOT)}")
        if changed or deletes:
            print("Run: python3 scripts/sync_agent_rules.py", file=sys.stderr)
            return 1
        if warnings:
            return 1
        print(f"All agent files are in sync with {len(policies)} policies.")
        return 0

    for path in changed:
        write_text(path, writes[path])
        print(f"updated: {path.relative_to(ROOT)}")
    for path in deletes:
        path.unlink()
        print(f"removed: {path.relative_to(ROOT)}")
    print(f"Synced {len(policies)} policies ({len(changed)} updated, {len(deletes)} removed).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
