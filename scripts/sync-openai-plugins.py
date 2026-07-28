#!/usr/bin/env python3
"""Build OpenAI-native Smithy plugins from the canonical Claude packages."""

from __future__ import annotations

import argparse
import filecmp
import json
import re
import shutil
import tempfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_ROOT = REPO_ROOT / "plugins"
OUTPUT_ROOT = REPO_ROOT / "openai-plugins"
MARKETPLACE_PATH = REPO_ROOT / ".agents" / "plugins" / "marketplace.json"
PLUGIN_ORDER = ("forge", "foundry", "draft", "anvil", "bellows", "temper")

PLUGIN_INTERFACE = {
    "forge": {
        "shortDescription": "Evidence-first engineering workflows",
        "capabilities": ["Read", "Write"],
        "defaultPrompt": [
            "Implement this change end to end.",
            "Debug this failure and prove the fix.",
            "Review the current branch.",
        ],
    },
    "foundry": {
        "shortDescription": "Scaffold and deploy clean projects",
        "capabilities": ["Read", "Write"],
        "defaultPrompt": [
            "Scaffold a clean project from this brief.",
            "Add portable OpenTofu infrastructure.",
            "Deploy this project safely.",
        ],
    },
    "draft": {
        "shortDescription": "Write, document, and publish",
        "capabilities": ["Read", "Write"],
        "defaultPrompt": [
            "Write this in the project's voice.",
            "Create documentation verified against the code.",
            "Build this manuscript for publishing.",
        ],
    },
    "anvil": {
        "shortDescription": "Build portable Nix environments",
        "capabilities": ["Read", "Write"],
        "defaultPrompt": [
            "Check this Nix environment.",
            "Audit shell portability.",
            "Create a devenv environment.",
        ],
    },
    "bellows": {
        "shortDescription": "Create safe recurring automation",
        "capabilities": ["Read", "Write"],
        "defaultPrompt": [
            "Turn this chore into a safe routine.",
            "Watch this work until it resolves.",
            "Upgrade dependencies in tested batches.",
        ],
    },
    "temper": {
        "shortDescription": "Audit and harden software",
        "capabilities": ["Read", "Write"],
        "defaultPrompt": [
            "Audit this repository for security issues.",
            "Prove this suspected vulnerability.",
            "Harden this proven finding.",
        ],
    },
}

BODY_REPLACEMENTS = {
    "`$ARGUMENTS` is `{language} {project-type}` plus optional flags.": (
        "The user's request must provide `{language} {project-type}` plus optional flags."
    ),
    "Base branch: `$ARGUMENTS` if given.": "Base branch: use the user's request if it names one.",
    "devenv's own Claude Code integration": "devenv's own coding-agent integration",
    "devenv's Claude Code integration": "devenv's coding-agent integration",
    "Claude Code will ask": "The active host may ask",
    "so Claude can drive": "so the active coding agent can drive",
    "This command": "This skill",
    "The command": "The skill",
}

CODEX_EVAL_WORKFLOW = """## Workflow

1. **Locate the OpenAI plugin packages** from the repo's
   `.agents/plugins/marketplace.json`, or the nearest
   `.codex-plugin/plugin.json` when the repo is a single plugin.
2. **Preflight Codex and the plugins.** Require `codex exec`. Run
   `codex plugin list --json` and require every plugin named by the
   scenario to be installed and enabled. When the marketplace points
   at a local package, require the installed source path to resolve to
   that package. If a required plugin is missing, disabled, or stale,
   report the scenario as skipped with the exact marketplace,
   installation, or update command needed. Never change the user's
   plugin configuration automatically.
3. **Count the sessions and say so.** Headless runs spend real
   tokens. Report how many will run before running any.
4. **Build a fresh scratch repo per scenario** in a temp directory,
   seeded per the scenario setup, committed so the tree has a clean
   baseline.
5. **Record the tree state**: the status output plus a hash of the
   full diff against HEAD.
6. **Prepare a prompt file** in the scenario's temp directory.
   Translate Smithy invocations from the scenario's `/plugin:skill`
   form to Codex's `$plugin:skill` form in this copy only. Keep the
   scenario file unchanged.
7. **Run one ephemeral, non-interactive Codex session per scenario:**

   ```
   codex exec --ephemeral --json --color never \\
     --sandbox workspace-write --cd <scratch-repo> - \\
     < <prompt-file> > <transcript.jsonl> 2> <stderr.log>
   ```

   Keep the normal user config enabled because it carries the
   installed plugin state. Auto-accept edits only inside the
   disposable scratch repo. Do not use the dangerous sandbox bypass.
   A verb that would violate a boundary must be able to, so the gate
   can catch it. The JSONL event stream is the full transcript;
   stderr is diagnostic context only.
8. **Assert the tree.** Hash again after the run. A scenario that
   forbids edits fails on any change, whatever the transcript
   claims.
9. **Grade the transcript** against the scenario's boundaries. Cite
   the JSONL line containing the agent message or command execution
   that proves each verdict. A missing stop, a missing
   recommendation, or a claim the tree contradicts is a fail.
10. **Report** per the `writing-style` skill: each scenario's
    verdict with its evidence, then one pass count. A failed scenario
    quotes its transcript, never a paraphrase.
"""

CODEX_EVAL_BOUNDARIES = """## Boundaries

Scratch repos are disposable. The repo under test is read-only.
Never mark a scenario passed on transcript claims alone: the tree
hash is the authority. Codex has no documented per-run plugin
directory override, so test only an installed, enabled package whose
source or version matches the target. A scenario the environment
cannot run gets reported as skipped with the exact setup or execution
command, never guessed at.
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate or verify OpenAI-native Smithy plugin packages."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Verify generated files are current without modifying the checkout.",
    )
    return parser.parse_args()


def read_source_manifest(plugin_name: str) -> dict:
    path = SOURCE_ROOT / plugin_name / ".claude-plugin" / "plugin.json"
    return json.loads(path.read_text(encoding="utf-8"))


def portable_skill(
    source: str, plugin_name: str
) -> tuple[str, bool, str, str]:
    if not source.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter")
    frontmatter_text, body = source[4:].split("\n---\n", 1)
    fields = {}
    for line in frontmatter_text.splitlines():
        key, separator, value = line.partition(":")
        if separator and key in {
            "name",
            "description",
            "disable-model-invocation",
        }:
            fields[key] = value.strip()

    name = fields.get("name")
    description = fields.get("description")
    if not name or not description:
        raise ValueError("SKILL.md must contain one-line name and description fields")
    explicit_only = fields.get("disable-model-invocation") == "true"

    for source_text, replacement in BODY_REPLACEMENTS.items():
        body = body.replace(source_text, replacement)
    body = re.sub(
        r"Claude Code's own scheduled\s+(?:tasks|agents)",
        "the active host's scheduled-task capability",
        body,
    )
    body = re.sub(
        r"`forge:implementer`\s+subagents",
        "available\n   implementation subagents",
        body,
    )
    body = re.sub(
        r"Subagents start fresh and\s+see none of this conversation\.",
        "Give each subagent a self-contained brief; do not assume inherited\n   context.",
        body,
    )
    body = body.replace("`$ARGUMENTS`", "the user's request")
    body = body.replace("$ARGUMENTS", "the user's request")
    body = re.sub(
        r"/(forge|foundry|draft|anvil|bellows|temper):",
        r"\1:",
        body,
    )
    body = body.replace("Claude Code", "the active host")
    if plugin_name == "forge" and name == "eval":
        body, workflow_count = re.subn(
            r"## Workflow\n.*?(?=\n## Boundaries\n)",
            CODEX_EVAL_WORKFLOW.rstrip() + "\n",
            body,
            count=1,
            flags=re.DOTALL,
        )
        body, boundaries_count = re.subn(
            r"## Boundaries\n.*\Z",
            CODEX_EVAL_BOUNDARIES.rstrip() + "\n",
            body,
            count=1,
            flags=re.DOTALL,
        )
        if workflow_count != 1 or boundaries_count != 1:
            raise ValueError("forge:eval no longer matches the Codex transform")

    frontmatter = f"---\nname: {name}\ndescription: {description}\n---\n"
    return frontmatter + body, explicit_only, name, description


def skill_agent_yaml(plugin_name: str, skill_name: str, description: str) -> str:
    display_name = f"{plugin_name.title()}: {skill_name.replace('-', ' ').title()}"
    return (
        "interface:\n"
        f"  display_name: {json.dumps(display_name)}\n"
        f"  short_description: {json.dumps(description)}\n"
        "policy:\n"
        "  allow_implicit_invocation: false\n"
    )


def build_manifest(plugin_name: str) -> dict:
    source = read_source_manifest(plugin_name)
    interface = PLUGIN_INTERFACE[plugin_name]
    long_description = source["description"]
    if plugin_name != "forge" and "Requires the forge plugin" not in long_description:
        long_description += " Requires the Forge plugin for shared Smithy skills."

    return {
        "name": source["name"],
        "version": source["version"],
        "description": source["description"],
        "author": source["author"],
        "homepage": source["homepage"],
        "repository": source["repository"],
        "license": source["license"],
        "keywords": source["keywords"],
        "skills": "./skills/",
        "interface": {
            "displayName": source["displayName"],
            "shortDescription": interface["shortDescription"],
            "longDescription": long_description,
            "developerName": source["author"]["name"],
            "category": "Productivity",
            "capabilities": interface["capabilities"],
            "defaultPrompt": interface["defaultPrompt"],
        },
    }


def build_marketplace() -> dict:
    return {
        "name": "smithy",
        "interface": {
            "displayName": "Smithy",
        },
        "plugins": [
            {
                "name": plugin_name,
                "source": {
                    "source": "local",
                    "path": f"./openai-plugins/{plugin_name}",
                },
                "policy": {
                    "installation": "AVAILABLE",
                    "authentication": "ON_INSTALL",
                },
                "category": "Productivity",
            }
            for plugin_name in PLUGIN_ORDER
        ],
    }


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def build_packages(output_root: Path) -> None:
    if output_root.exists():
        if output_root.is_symlink():
            raise ValueError(f"refusing to replace symlinked output root: {output_root}")
        shutil.rmtree(output_root)
    output_root.mkdir(parents=True)

    for plugin_name in PLUGIN_ORDER:
        source_plugin = SOURCE_ROOT / plugin_name
        output_plugin = output_root / plugin_name
        shutil.copytree(source_plugin / "skills", output_plugin / "skills")

        for skill_path in sorted((output_plugin / "skills").glob("*/SKILL.md")):
            portable, explicit_only, skill_name, description = portable_skill(
                skill_path.read_text(encoding="utf-8"),
                plugin_name,
            )
            skill_path.write_text(portable, encoding="utf-8")
            if explicit_only:
                agent_path = skill_path.parent / "agents" / "openai.yaml"
                agent_path.parent.mkdir(parents=True, exist_ok=True)
                agent_path.write_text(
                    skill_agent_yaml(plugin_name, skill_name, description),
                    encoding="utf-8",
                )

        shutil.copy2(REPO_ROOT / "LICENSE", output_plugin / "LICENSE")
        write_json(output_plugin / ".codex-plugin" / "plugin.json", build_manifest(plugin_name))


def directories_match(expected: Path, actual: Path) -> bool:
    comparison = filecmp.dircmp(expected, actual)
    if comparison.left_only or comparison.right_only or comparison.funny_files:
        return False
    if comparison.diff_files:
        return False
    return all(
        directories_match(expected / child, actual / child)
        for child in comparison.common_dirs
    )


def check_generated_files() -> None:
    with tempfile.TemporaryDirectory(prefix="smithy-openai-plugins-") as temp_dir:
        expected_root = Path(temp_dir) / "openai-plugins"
        build_packages(expected_root)
        if not OUTPUT_ROOT.is_dir() or not directories_match(expected_root, OUTPUT_ROOT):
            raise SystemExit(
                "OpenAI plugin packages are stale; run scripts/sync-openai-plugins.py"
            )

    expected_marketplace = build_marketplace()
    try:
        actual_marketplace = json.loads(MARKETPLACE_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise SystemExit(
            "OpenAI marketplace is missing or invalid; run scripts/sync-openai-plugins.py"
        ) from error
    if actual_marketplace != expected_marketplace:
        raise SystemExit(
            "OpenAI marketplace is stale; run scripts/sync-openai-plugins.py"
        )
    print("OpenAI plugin packages are current.")


def main() -> None:
    args = parse_args()
    if args.check:
        check_generated_files()
        return

    build_packages(OUTPUT_ROOT)
    write_json(MARKETPLACE_PATH, build_marketplace())
    print(f"Generated OpenAI plugins: {OUTPUT_ROOT}")
    print(f"Generated marketplace: {MARKETPLACE_PATH}")


if __name__ == "__main__":
    main()
