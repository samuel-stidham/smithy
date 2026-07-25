---
name: harden
description: Fix audit findings in exploitability order, one commit per fix, tests after each. Credential rotation stays human.
argument-hint: "[findings to fix, defaults to the latest audit]"
disable-model-invocation: true
---

# /temper:harden

Fix security findings, most exploitable first. Input is
`/temper:audit` output, a pasted report, or a fresh quick pass when
neither exists.

The findings are: $ARGUMENTS. If empty, use the latest audit in the
conversation, or run a quick audit pass first.

## Workflow

1. **Order by exploitability** per the `security-baseline` skill.
2. **Branch** as `fix/{short-kebab-description}`, with types per
   `forge:conventional-commits`.
3. **Fix one finding per commit.** Run the repo's tests after each.
   A fix that breaks behavior is not done.
4. **Confirm the risky ones first.** Changes to authentication,
   authorization, crypto, and session handling get shown to the
   user before they land.
5. **Report** per `forge:writing-style`: fixed, deferred, and
   rejected findings, each with its reason.

## The rotation rule

A leaked credential is dead the moment it leaks. Removing it from
the code is necessary and nowhere near sufficient. The human
rotates it at the source, since rotation touches systems this
plugin must never drive. Report the leak loudly, fix the code path,
and say rotation is still owed.

## Boundaries

Never pushes (that is `/forge:ship`). Never rotates credentials.
Never trades a real mitigation for a cosmetic one, such as hiding
an endpoint instead of authenticating it.
