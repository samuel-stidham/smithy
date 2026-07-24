# foundry

The product factory of the forge family. Scaffolds complete Clean
Architecture project templates and deploys them with OpenTofu.

**Requires the forge plugin.** Foundry's skills borrow
`forge:clean-architecture`, `forge:clean-code`, and
`forge:writing-style` by name. Install and enable forge wherever
foundry runs.

- `/foundry:scaffold {language} {project-type}` generates a complete,
  working project, optionally with `--infra opentofu`.
- `/foundry:deploy [target]` applies a repo's own infrastructure
  safely.

Enable per repo where products get built or deployed.
