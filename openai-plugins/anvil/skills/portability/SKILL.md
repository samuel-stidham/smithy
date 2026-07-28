---
name: portability
description: Distro-family audit of shell and package selection in a Nix repo. Every finding carries file, line, family, and a loud-or-silent verdict.
---

# anvil:portability

Audit the repo's shell and package choices against the distro
families it claims to support. This is the check shellcheck cannot
perform: shellcheck reads one script against one shell and has no
opinion about whether `/usr/bin/btrfs` exists on Fedora.

## Scope

Same test as `anvil:check`: a machine definition, a devenv
environment, or a `scripts/` tree. Otherwise say so and stop.

## Audit

Read the tree against the `shell-portability` skill's trap list.
That list is the plugin's real payload: every entry came from a
failure observed on a real machine. Package names are never recalled
from memory. Read each distro's package database through
`forge:web-browsing`, per the `parity` skill.

## Report

Every finding carries a file, a line, the exact string, the family
it breaks on, and a loud-or-silent verdict. A finding without a line
number is not a finding. This machine runs one family: mark every
finding about a family it did not run as unverified, in the report
and in any commit body drafted from it, per the `parity` skill's
honesty rule.
