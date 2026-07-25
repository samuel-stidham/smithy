---
name: check
description: Static gate for a Nix repo. Per-dialect shell checks plus flake evaluation, building nothing.
disable-model-invocation: true
---

# /anvil:check

Run the static gate over a Nix-defined environment: every shell file
checked with the right parser for its dialect, then the configuration
evaluated. Nothing is built and nothing changes state.

## Scope

The repo is in scope when it has a `flake.nix` declaring
`homeConfigurations` or `nixosConfigurations`, a `configuration.nix`,
a `devenv.nix`, or a `scripts/` tree of shell files. Absent all of
those, say the repo is out of scope and stop.

## Discover

Find every shell file the repo owns, including scripts embedded in
Nix through `writeShellApplication`. Detect each file's dialect from
its shebang, extension, and location (a `fish/` tree is fish). Detect
the interactive shell the configuration declares
(`programs.fish.enable`, `programs.zsh.enable`, a `fish/` or `zsh/`
tree, shebangs, `$SHELL` as a runtime fallback). Never ask the owner
and never run one tool over everything.

## Gates per dialect

Pick the gate by dialect. The `shell-dialects` skill holds the
differences and the reason this table exists: shellcheck cannot parse
fish, and trusting its false errors on correct fish breaks working
shell.

| Dialect | Gate |
| --- | --- |
| bash, sh | `shellcheck -x` plus `bash -n` |
| fish | `fish -n`, plus `fish_indent --check` when the repo uses it |
| zsh | `zsh -n` |

Then evaluate: `nix flake check` for a flake, an evaluation of the
configuration otherwise. Build nothing.

## Report

Rank findings by whether they fail loudly or silently. A crash gets
fixed. A quiet skip gets trusted for a year, so it outranks the
crash. Name every file you could not reach and say so plainly.
Silent partial coverage reads as a clean bill of health, which is
worse than no run at all. A fish tree excluded because the only
configured linter cannot read it is the exact shape of that failure.
