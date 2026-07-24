---
name: review
description: Audit the current branch's diff against its base. Verdict is SHIP IT, NEEDS WORK, or RETHINK.
argument-hint: "[optional base branch, defaults to the repo's default branch]"
disable-model-invocation: true
context: fork
---

# /forge:review

Audit the changes on the current branch against its base branch. This is
a diff review, scoped to what changed, with enough surrounding context
to judge whether it fits.

## Setup

1. Base branch: `$ARGUMENTS` if given. Otherwise detect the repo's
   default branch. Do not assume `main`.
2. Diff the merge base against HEAD. Read changed files beyond the
   hunks wherever the diff alone is unclear.
3. Read the repo's agent instructions (`CLAUDE.md`, `AGENTS.md`) and
   README for conventions before judging the diff against them.

## Lenses

Work the diff through each lens as its own pass. Raise only real,
specific issues. Cite file and line. No generic advice.

- **Architecture.** Layer violations and dependency direction, per the
  `clean-architecture` skill. Missing abstraction where one is clearly
  needed, unnecessary abstraction where it is not.
- **Code quality.** Per the `clean-code` skill: naming, dead code,
  swallowed errors, duplication that should be shared.
- **Tests.** New behavior covered. Tests assert behavior, never
  implementation details. Obvious edge cases present.
- **Security.** Hardcoded secrets, injection risks, missing validation
  at trust boundaries, unsafe deserialization, authorization gaps.
- **Docs.** Public behavior or setup changed without the README or
  docs following.
- **Scope.** The diff matches what was asked, no more and no less.
  Flag unrequested changes and quiet scope creep.

## Verdict

End with exactly one verdict. Nothing competes with it.

- **SHIP IT**: no blocking issues. List optional nits separately.
- **NEEDS WORK**: fixable issues exist. Order by severity. For each,
  give the file, the line, what is wrong, and what to do.
- **RETHINK**: the approach itself is wrong. Explain the core concern
  and sketch what a better approach looks like.

Do not soften the verdict to be agreeable.
