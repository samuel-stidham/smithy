---
name: env
description: Create or update a devenv development environment for the current repo. Reads the devenv docs before writing, every time.
---

# anvil:env

Create or update a [devenv](https://devenv.sh/) environment for this
repo: `devenv.nix`, `devenv.yaml`, and the `.envrc` that activates it
through direnv. Evaluate the result before reporting success.

## Read before writing

Read the documentation first, every time, before writing a line.
This is not a fallback for feeling unsure. devenv's option surface
spans more than forty language modules plus processes, services,
scripts, tasks, git-hooks, and tests, and it moves. An environment
written from recalled option names evaluates to an error at best,
and at worst silently pins the wrong thing.

The reading list, through `forge:web-browsing`:

- `https://devenv.sh/reference/options/` for `devenv.nix`
- `https://devenv.sh/reference/yaml-options/` for `devenv.yaml`
- `https://devenv.sh/languages/<name>/` for every language the repo
  actually uses

## Workflow

1. Detect the repo's languages from its manifests. Never ask.
2. Read the pages above for exactly those languages.
3. Write `devenv.nix` and `devenv.yaml` per the `devenv` skill's
   conventions. Add the `.envrc` when it is missing.
4. Evaluate. Report success only after evaluation passes.

## Boundaries

No installs, no `sudo`, no system state. env writes and `check`
evaluates: this verb does not run `devenv test`. The `devenv` skill
records the file split, the pinning rules, the rule against baking
in devenv's own coding-agent integration, and the boundary against
`foundry:scaffold`.
