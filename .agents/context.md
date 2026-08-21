# smithy

This repo is smithy, a dual Claude Code and OpenAI plugin marketplace
holding six plugins that share one set of rules. It is installed
across every machine and repo Samuel works in, Hudl and personal
alike, and must behave identically everywhere.

This file is the single source of truth for every AI agent working in
this repo. The root `CLAUDE.md` and `AGENTS.md`, plus the entries
under `.cursor/rules/`, `.github/copilot-instructions.md`, and
`.agents/rules/`, are thin pointers here. Change agent guidance in
this file only. Never restate it in a pointer file.

## The six plugins

- `plugins/forge/`: core engineering workflow. Verbs do-work, debug,
  prove, verify, refactor, evaluate, review, ship, version,
  test-harness, and eval, the shared reference skills (writing-style,
  conventional-commits, clean-code, clean-architecture,
  change-control, adversarial-review, web-browsing, citations), and
  the implementer agent. Enabled globally.
- `plugins/foundry/`: product factory. Verbs scaffold and deploy,
  plus infrastructure-as-code. Enabled per repo.
- `plugins/draft/`: writing studio. Verbs write, publish, docs, and
  review, plus creative and technical-writing. Enabled per repo.
- `plugins/anvil/`: Nix environments. Verbs check, portability, env,
  and switch, plus nix-conventions, shell-portability,
  shell-dialects, parity, and devenv. Enabled per repo, in machine
  definitions and devenv projects.
- `plugins/bellows/`: recurring automation. Verbs routine, watch,
  ci, and upgrade, plus automation-boundaries. Enabled per repo,
  wherever unattended jobs run.
- `plugins/temper/`: security. Verbs audit and harden, plus
  security-baseline. Enabled per repo, wherever code faces users or
  handles secrets.

Plugin names are thematic to the smithy. Verb names are plain and
functional, named for the action they perform, never the metaphor.

**Dependency rule:** leaf plugins (foundry, draft, anvil, bellows,
temper) borrow forge skills by qualified name, such as
`forge:clean-architecture`. forge references nothing outside itself.
Never point a forge file at a leaf. A leaf verb appearing beside
forge verbs is per-repo enablement, never a file reference.

## Structure

The canonical packages live under `plugins/`. Each has a Claude
manifest at `.claude-plugin/plugin.json`, its
`skills/<name>/SKILL.md` files, and optionally `agents/`. Verbs carry
`disable-model-invocation: true` and are invoked as
`/<plugin>:<name>`. The review verbs additionally run as synchronous
forks (`context: fork`, `background: false`). Reference skills carry
`user-invocable: false` and load by name. The Claude marketplace is
`.claude-plugin/marketplace.json`. Each leaf plugin's own manifest
declares `"dependencies": ["forge"]`.

`scripts/sync-openai-plugins.py` generates the OpenAI packages under
`openai-plugins/` and the repo marketplace at
`.agents/plugins/marketplace.json`. Generated skills remove
Claude-only frontmatter, replace argument placeholders with the user
request, and use `agents/openai.yaml` to keep verbs explicit-only.
Never edit `openai-plugins/` or the OpenAI marketplace by hand. Run
the sync script after changing a canonical skill or manifest, then
run it with `--check`.

Each plugin keeps its own `CHANGELOG.md` beside its canonical
manifest. The root changelog holds pre-split history and repo-level
changes only.

## Testing changes

Claude Code reads plugins from a per-version cache under
`~/.claude/plugins/cache/`, never this checkout. Codex also installs
marketplace plugins into its cache, so neither host should be tested
by assuming it reads the canonical source files live.

1. For real installs: commit, bump the plugin's version in its
   `plugin.json`, push, then run
   `claude plugin update <plugin>@smithy` and restart the session.
   For fast iteration: install from a local path pointing at this
   checkout. A session restart then picks up each edit.
2. Invoke the changed verb in a real or scratch repo. Check the
   behavior matches the file.
3. Test a reference skill through the verbs that name it (grep for
   it), or by exercising the behavior its description covers.
4. Run `python3 scripts/sync-openai-plugins.py`, validate all six
   generated plugins, and run the script again with `--check`.
5. Add this checkout as a local Codex marketplace, install forge
   before any leaf plugin, start a new thread, and exercise the
   changed skill. OpenAI manifests do not declare Smithy's
   plugin-to-plugin dependencies.

Behavioral scenarios live in `evals/`, one file per protocol, and
run as a repeatable gate through `/forge:eval` in Claude Code or
`$forge:eval` in Codex. Everything else means running the prompts
against real scenarios and judging the output.

## Repo-agnostic by design

Every verb works the same in a Go monorepo, a TypeScript side
project, or a Python script.

- Never hardcode a language, framework, package manager, or test
  runner. Detect them from the target repo's manifests, lockfiles,
  and scripts.
- Never hardcode a base branch. Detect the repo's default branch.
- Never assume a CI provider, hosting platform, or cloud vendor.
- Repo-specific information comes from the target repo's `CLAUDE.md`,
  `AGENTS.md`, README, manifests, and code. forge ships with zero
  repo-specific configuration.

An instruction that only makes sense for one ecosystem gets rewritten
to detect and adapt.

## Editing the skills

Each skill is the single source of truth for its topic. Verbs
reference skills by name and never restate their rules. Cross-plugin
borrows always use the qualified name. Prose in every skill follows
the `forge:writing-style` skill. Each plugin releases independently,
tagged `{plugin}--v{version}` through `/forge:version` (the
double-hyphen form `claude plugin tag` produces).
