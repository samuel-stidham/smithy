---
name: switch
description: Build a machine definition, show the closure diff, and activate only on confirmation. Prints the rollback on failure.
---

# anvil:switch

Build and activate a machine definition, with the diff shown in
between. Activation is the one hard-to-reverse thing anvil does.
Showing the closure diff before the confirmation is the whole design
of this verb, never a nicety.

## Scope

Machine definitions only: a `flake.nix` declaring
`homeConfigurations` or `nixosConfigurations`, or a
`configuration.nix`. A devenv-only repo is out of scope here, since
direnv owns its activation. Getting a machine definition wrong logs
you out, which is why every step below gates the next.

## Workflow

1. Evaluate. Stop on any evaluation error.
2. Build the activation package. A build failure ends the run.
3. Diff the built closure against the current generation and print
   what would change: packages added, removed, and version-changed,
   plus changed files and units.
4. Activate only after the user confirms. Never activate as a side
   effect of anything.
5. On failure, print the rollback command before any diagnosis.

## Boundaries

Home-manager first. No `sudo`, no package installs, no bootstrap:
anvil proposes those steps and a human runs them. Whether this verb
grows `nixos-rebuild` support is an open question recorded in the
plugin README.
