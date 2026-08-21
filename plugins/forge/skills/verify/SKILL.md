---
name: verify
description: Run the repo's own QA checks from narrowest to broadest without changing any file. Report every command and result.
argument-hint: "[optional focus: a test, module, or change to verify]"
disable-model-invocation: true
---

# /forge:verify

Run the repository's own quality checks and report what they say.
This verb introduces no production changes. The `change-control`
skill governs it. Verification never mutates.

The focus is: $ARGUMENTS. If empty, verify the current working tree.

## Workflow

1. **Detect the real QA commands** from the repo's agent
   instructions, manifests, scripts, and lockfiles. Never invent
   tooling the repo does not have. Never install dependencies just
   to verify.
2. **Record the working-tree state** before running anything, such
   as the status output and a diff summary.
3. **Run the applicable checks, narrowest to broadest:**
   1. the focused regression test
   2. the affected package or module tests
   3. the affected integration path
   4. the normal test suite
   5. type and static analysis
   6. format and lint in check-only mode
   7. security, vulnerability, or secret scans when relevant
   8. race, sanitizer, concurrency, build, or packaging checks when
      relevant

   Skip what does not apply and say so. Never run an auto-fix mode
   of any tool.
4. **Compare the working-tree state afterward.** If a check changed
   files, stop and report the mutation. Never silently revert it.
5. **Report** per the `writing-style` skill: every command run and
   its result, every skipped check with its reason, the diff size,
   and the remaining uncertainty.

## Boundaries

Never fix anything, including unrelated failures found along the
way. Report those and recommend `/forge:prove` or `/forge:debug`.
