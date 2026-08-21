# anvil

The fixed reference surface of the smithy family. Everything else in
the shop moves. The anvil is what metal gets shaped against, and a
Nix-defined environment plays the same role. The distro families move
underneath it, and the definition is the unmoving target they all
converge to.

anvil covers two repo shapes, recognized by files and never by
location: machine definitions (a `flake.nix` declaring
`homeConfigurations` or `nixosConfigurations`, or a
`configuration.nix`) and devenv development environments
(a `devenv.nix`). A `scripts/` tree of shell files also brings a repo
in scope for the checking verbs.

**Requires the forge plugin.** anvil borrows `forge:web-browsing`
(distro package databases, devenv documentation),
`forge:writing-style`, and `forge:conventional-commits` by name. The
browsing dependency is hard. Without it anvil has no sanctioned way
to read the references its rules forbid recalling from memory.

- `/anvil:check` runs per-dialect shell gates plus flake evaluation.
  Read-only.
- `/anvil:portability` audits shell and package selection across
  distro families, with file, line, family, and loud-or-silent
  verdicts. Read-only.
- `/anvil:env` creates or updates a devenv environment. It reads the
  devenv docs before writing, every time.
- `/anvil:switch` builds a machine definition, shows the closure
  diff, and activates only on confirmation.

anvil never runs `sudo`, installs a package, or changes system state
outside a Nix activation the user confirms. Bootstrap stays a script
the repo owns and a human runs. Cloud infrastructure stays foundry's.

Enable per repo, in machine definitions and devenv projects. Nine
skills is a real listing cost, which is the argument for never
enabling it globally.

## Open questions carried from the design

- Whether `switch` grows `nixos-rebuild` support, or stays
  home-manager first.
- Whether `env` should also run `devenv test`, or the cleaner split
  stays: env writes, check evaluates.
- Whether the portability trap list eventually earns a real linter.
  Today it is judgment applied by a model, and the list is too small
  and situational to justify a machine-applied rule.
- Whether formatting belongs to anvil at all. The current answer is
  to run a formatter the repo configures, and otherwise say nothing.
