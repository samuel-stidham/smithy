# smithy

This repo is smithy, a Claude Code plugin marketplace holding four
plugins that share one set of rules. It is installed
across every machine and repo Samuel works in, Hudl and personal
alike, and must behave identically everywhere.

This file is the single source of truth for every AI agent working in
this repo. The root `CLAUDE.md` and `AGENTS.md`, plus the entries
under `.cursor/rules/`, `.github/copilot-instructions.md`, and
`.agents/rules/`, are thin pointers here. Change agent guidance in
this file only. Never restate it in a pointer file.

## The four plugins

- `plugins/forge/`: core engineering workflow. Verbs do-work, review,
  ship, version, and test-harness, the shared reference skills
  (writing-style, conventional-commits, clean-code,
  clean-architecture, web-browsing, citations), and the implementer
  agent. Enabled globally.
- `plugins/foundry/`: product factory. Verbs scaffold and deploy,
  plus infrastructure-as-code. Enabled per repo.
- `plugins/draft/`: writing studio. Verbs write and publish, plus
  creative and technical-writing. Enabled per repo.
- `plugins/anvil/`: Nix environments. Verbs check, portability, env,
  and switch, plus nix-conventions, shell-portability,
  shell-dialects, parity, and devenv. Enabled per repo, in machine
  definitions and devenv projects.

**Dependency rule:** leaf plugins (foundry, draft, anvil) borrow forge
skills by qualified name, such as `forge:clean-architecture`. forge
references nothing outside itself. Never point a forge file at a
leaf. A leaf verb appearing beside forge verbs is per-repo
enablement, never a file reference.

## Structure

There is no build step. Everything is prompt files. Each plugin has
`.claude-plugin/plugin.json` with its own version,
`skills/<name>/SKILL.md`, and optionally `agents/`. Verbs carry
`disable-model-invocation: true` and are invoked as
`/<plugin>:<name>`. Review additionally runs as a synchronous fork
(`context: fork`, `background: false`). Reference skills carry
`user-invocable: false` and load by name. The root
`.claude-plugin/marketplace.json` lists all four plugins, and the
leaf manifests declare `"dependencies": ["forge"]`. Each plugin
keeps its own `CHANGELOG.md` beside its manifest. The root changelog
holds pre-split history and repo-level changes only.

## Testing changes

Claude Code reads plugins from a per-version cache under
`~/.claude/plugins/cache/`, never this checkout. The plugins run only
in Claude Code, so test there even when editing from another agent.

1. For real installs: commit, bump the plugin's version in its
   `plugin.json`, push, then run
   `claude plugin update <plugin>@smithy` and restart the session.
   For fast iteration: install from a local path pointing at this
   checkout. A session restart then picks up each edit.
2. Invoke the changed verb in a real or scratch repo. Check the
   behavior matches the file.
3. Test a reference skill through the verbs that name it (grep for
   it), or by exercising the behavior its description covers.

There is no automated test suite. Testing means running the prompts
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
