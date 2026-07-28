---
name: harden
description: Fix exactly one proven security finding with the smallest correct mitigation. Credential rotation stays human.
---

# temper:harden

Fix exactly one proven security finding. Input is a single finding
with its proof, from `temper:audit`, `forge:prove`, or a pasted
report carrying equivalent evidence. The `forge:change-control` and
`security-baseline` skills govern the evidence bar and the standard.

The finding is: the user's request. If empty, stop and recommend
`temper:audit`. If it holds more than one finding, ask which single
one to fix. If it lacks proof per `forge:change-control`, stop and
recommend `forge:prove`.

## Workflow

1. **Branch** as `fix/{short-kebab-description}`, with types per
   `forge:conventional-commits`.
2. **Apply the smallest correct mitigation**, within the
   `forge:change-control` default repair budget.
3. **Use the existing proof as the acceptance test.** It must fail
   before the fix and pass after. Then run the repo's tests. A fix
   that breaks behavior is not done.
4. **Confirm the risky ones first.** Changes to authentication,
   authorization, crypto, and session handling get shown to the
   user before they land.
5. **Report** per `forge:writing-style`: the finding, the
   mitigation, the proof run both ways, and its reasoning.

Other audit findings stay untouched, however tempting. Each gets
its own proof and its own invocation.

## The rotation rule

A leaked credential is dead the moment it leaks. Removing it from
the code is necessary and nowhere near sufficient. The human
rotates it at the source, since rotation touches systems this
plugin must never drive. Report the leak loudly, fix the code path,
and say rotation is still owed.

## Boundaries

Never pushes (that is `forge:ship`). Never rotates credentials.
Never trades a real mitigation for a cosmetic one, such as hiding
an endpoint instead of authenticating it.
