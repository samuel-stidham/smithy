---
name: debug
description: Start from a symptom, reproduce it, isolate the cause, fix it, and prove the fix with a regression test.
argument-hint: "[failing test, stack trace, bug report, or symptom]"
disable-model-invocation: true
---

# /forge:debug

Take a symptom to a proven fix. `/forge:do-work` executes a defined
task. This verb starts earlier, where all you have is something
wrong.

The symptom is: $ARGUMENTS

If `$ARGUMENTS` is empty, ask what is broken.

The `change-control` skill governs evidence and scope. Explicit
invocation authorizes prove, then fix, then verify, for one symptom
only. Unrelated findings get reported, never touched.

## Workflow

1. **Reproduce first.** No hypothesis and no fix before the failure
   happens in front of you. If reproduction and every other valid
   proof fail, stop with zero production changes. Say why. Never
   continue into a hypothetical repair.
2. **Orient.** The repo's agent instructions, the failing area's
   code, and its recent history. Regressions live in diffs, so find
   when it last worked.
3. **Isolate.** Shrink the reproduction until the failure is small.
   Bisect history when a known-good point exists. Change one
   variable per step.
4. **Name the cause.** The mechanism, stated plainly: this code, on
   this input, does this wrong thing. Distinguish the root cause
   from the trigger that revealed it. A fix aimed at the trigger is
   a recurrence scheduled.
5. **Fix small.** The smallest change that removes the cause, per
   the `clean-code` skill and within the `change-control` default
   repair budget. Fix causes, not tests.
6. **Prove it.** A regression test that fails before the fix and
   passes after. Run it both ways and say you did. Only then run
   the repo's full test suite.
7. **Report** per the `writing-style` skill: the cause chain, the
   fix, the proof, and anything suspicious found along the way.

## Boundaries

Branch first, commit per the `conventional-commits` skill, never
push. That is `/forge:ship`.
