---
name: refactor
description: Behavior-preserving restructuring in small proven steps. Safety net first, and behavior changes never mix in.
argument-hint: "[target area and the debt to pay down]"
disable-model-invocation: true
---

# /forge:refactor

Restructure code without changing what it does. The whole verb
rests on one promise: behavior in equals behavior out, proven by
tests at every step.

The target is: $ARGUMENTS

If `$ARGUMENTS` is empty, ask what to refactor and why it hurts.

## Workflow

1. **Scope it.** Name the debt, the boundary of the change, and
   what better looks like. A refactor without a stated goal expands
   until something breaks.
2. **Build the safety net.** Find the tests covering current
   behavior. Where coverage is thin, write characterization tests
   that pin behavior as it is, bugs included, before touching
   anything.
3. **Move in small steps.** Each commit compiles, passes the full
   suite, and stands alone, per the `conventional-commits` skill.
   Layer moves follow the `clean-architecture` skill, code-level
   cleanups the `clean-code` skill.
4. **Never mix behavior changes.** A bug found mid-refactor gets
   reported and left in place. A silent fix breaks the promise the
   branch name makes and hides the fix from review.
5. **Report** per the `writing-style` skill: what moved, what got
   simpler, what debt remains. Fewer lines is never the goal and
   never claimed as one.

## Boundaries

Branch first as `refactor/{short-kebab-description}`, never push.
That is `/forge:ship`.
