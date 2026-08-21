# bellows

The bellows keeps the fire hot when nobody is pumping. That is the
plugin's whole domain: work that runs while the smith is away.
Scheduled routines, long watches over slow external work, the CI
pipeline, and the dependency upgrades that rot when neglected.

**Requires the forge plugin.** bellows borrows `forge:writing-style`,
`forge:conventional-commits`, and `forge:web-browsing` by name.

- `/bellows:routine`: define a recurring job with explicit
  boundaries, dry-run it once attended, then register it on the
  scheduler the environment offers.
- `/bellows:watch`: babysit a PR, deploy, or pipeline run until it
  resolves. Reports transitions, stays quiet on green.
- `/bellows:ci`: author or update the repo's CI pipeline on its own
  provider, mirroring the gates the repo already runs locally.
- `/bellows:upgrade`: dependency upgrades in risk-ordered batches,
  tested per batch, with majors researched before they move.

The `automation-boundaries` reference skill is the standard every
unattended job is judged against. It holds the five definition
fields, the never-do list, loud failure, and idempotent runs.

bellows never merges, never pushes to a default branch, and never
publishes. A human makes every irreversible call. Enable per repo,
wherever unattended jobs run.
