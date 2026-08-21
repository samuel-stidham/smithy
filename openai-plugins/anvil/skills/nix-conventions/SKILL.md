---
name: nix-conventions
description: Module layout rules for Nix machine definitions. Platform guards, store-resident scripts, home paths. Use when writing or reviewing Nix modules.
---

# Nix conventions

Module layout rules for machine definitions.

- **Platform guards.** `lib.optionals pkgs.stdenv.isLinux` for
  package lists. `lib.mkIf pkgs.stdenv.isLinux` for file and service
  blocks.
- **Scripts live in the store.** `writeShellApplication` plus
  `readFile`, never a checkout path inside a systemd unit. A unit
  pointing into a checkout breaks the moment the checkout moves or
  the machine bootstraps fresh.
- **Home paths are bound once.** `config.home.homeDirectory` through
  one named binding, never a literal.
