---
name: upgrade
description: Upgrade dependencies in risk-ordered batches, testing after each batch, with majors researched before they move.
argument-hint: "[scope: everything, one dependency, or security fixes only]"
disable-model-invocation: true
---

# /bellows:upgrade

Upgrade the repo's dependencies without breaking it. Batches ordered
by risk, the repo's own tests after every batch, and majors
researched before they move.

The scope is: $ARGUMENTS. If empty, the scope is every direct
dependency.

## Workflow

1. **Detect the ecosystem.** Manifests and lockfiles name the
   package manager and its upgrade tooling. Never assume them.
2. **Plan the batches.** Patch and minor updates batch together per
   manifest. Every major gets its own batch. Security fixes jump
   the queue.
3. **Research majors.** Read each major's changelog and migration
   notes through `forge:web-browsing` before touching it. Model
   memory of API changes is stale.
4. **Respect pins.** A version the repo pins deliberately, by
   constraint or comment, stays pinned. Surface it in the report
   instead of overriding it.
5. **Apply, test, commit.** One batch at a time: upgrade, run the
   repo's tests and lint, commit per `forge:conventional-commits`.
   A failing batch gets fixed or reverted before the next starts.
6. **Report** per `forge:writing-style`: what moved, what was held
   back and why, and what needs a human decision.

## Boundaries

Never pushes (that is `/forge:ship`). Never upgrades past a
deliberate pin. A lockfile-only refresh is still a commit, never a
silent side effect. Run as a routine, this verb obeys the
`automation-boundaries` skill.
