---
name: prove
description: Prove or reject exactly one finding or suspected defect. Never modifies production code. Ends at a verdict, never a fix.
---

# forge:prove

Take one finding to a verdict. The `change-control` skill governs
the proof bar, the claim grades, and the classifications.

The finding is: the user's request

If the user's request is empty, ask for one. If it holds more than one
independent finding, ask which single one to prove.

## Workflow

1. **State the claim.** Its current classification, the rule it
   would violate, and what the proof bar still requires.
2. **Choose the strongest available proof.** In order of preference:
   a deterministic reproduction, a failing regression test, an
   execution trace, an authoritative static proof.
3. **Build the proof.** Test-only edits are allowed when a durable
   regression proof requires them. Any test written must fail for
   the intended reason. Confirm its failure message matches the
   claimed mechanism. Use synthetic fixtures and obviously fake
   secrets.
4. **Judge honestly.** If the proof fails, reject or downgrade the
   finding per `change-control`, say why, and stop.
5. **Report success** with the expected behavior, the actual
   behavior, the execution path, the triggering preconditions, the
   violated rule, and the evidence.

## Boundaries

Never modify production code. Stop after the proof and never fix
the issue. Recommend exactly one next command, normally
`forge:debug` or `forge:do-work` carrying the proven evidence.
