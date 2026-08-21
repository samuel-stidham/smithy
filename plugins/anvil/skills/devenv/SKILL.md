---
name: devenv
description: devenv conventions. File split, interpreter pinning, direnv activation, and the boundary against foundry. Use when writing development environments.
user-invocable: false
---

# devenv

Conventions for [devenv](https://devenv.sh/) development
environments. The first rule is `/anvil:env`'s read-before-write
rule, and it binds here too. Anything whose vocabulary lives in
someone else's release notes gets read, never recalled.

- **File split.** `devenv.nix` is the environment. `devenv.yaml` is
  inputs. `devenv.lock` is the pin. `.envrc` runs
  `eval "$(devenv direnvrc)"` then `use devenv`, so direnv activates
  on `cd`.
- **Interpreter pinning.** An exact interpreter needs the
  `nixpkgs-python` input, never whatever CPython nixpkgs happens to
  ship.
- **Unfree toolchains.** `allowUnfree` is mandatory for CUDA.
  Neither this nor the pinning rule is guessable from option names.
- **devenv's Claude Code integration.** The owner configures it
  inside their environment (`claude.code.enable`), and it generates
  hooks, commands, and MCP config from there. Never bake it or its
  pieces into a generated environment.
- **The foundry boundary.** foundry scaffolds an application. anvil
  defines the environment the application is built in. A repo can
  want both. They write different files.
