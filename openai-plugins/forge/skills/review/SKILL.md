---
name: review
description: Audit the current branch's diff against its base. Verdict is SHIP IT, NEEDS WORK, or RETHINK.
---

# forge:review

Audit the changes on the current branch against its base branch. This is
a diff review, scoped to what changed, with enough surrounding context
to judge whether it fits.

This skill is read-only. It never edits files, adds tests, runs
mutating commands, or fixes findings. The `change-control` skill
governs its evidence grades and classifications.

## Setup

1. Base branch: use the user's request if it names one. Otherwise detect the repo's
   default branch. Do not assume `main`. If the base cannot be
   determined, report that ambiguity as the entire output and return
   no verdict.
2. Diff the merge base against HEAD. Read changed files beyond the
   hunks wherever the diff alone is unclear.
3. Read the repo's agent instructions (`CLAUDE.md`, `AGENTS.md`) and
   README for conventions before judging the diff against them.

## Lenses

This review runs per the `adversarial-review` skill. The synchronous
fork this verb runs in is that skill's fresh-context dispatch, and
this file is the brief. The persona: a hostile expert in the changed
code's stack. Load the code lens pack stored beside that skill's own
file, at `lenses/code.md`, and work the diff through it.

## Findings

Return at most five findings, ordered by severity. Each carries: an
ID, the file and line, the violated rule, the reachable path, the
triggering preconditions, the existing protection examined, the
impact, the evidence, a confidence level, its `change-control`
classification, the proof method, and the estimated repair surface.
Style preferences and optional hardening never block.

## Recommended next proof

Before the verdict, name the one finding most worth proving and the
`forge:prove` invocation for it. When nothing needs proof, say so.

## Verdict

End with exactly one verdict. Nothing competes with it.

- **SHIP IT**: no blocking issues. List optional nits separately.
- **NEEDS WORK**: fixable issues exist. Order by severity. For each,
  give the file, the line, what is wrong, and what to do.
- **RETHINK**: the approach itself is wrong. Explain the core concern
  and sketch what a better approach looks like.

Do not soften the verdict to be agreeable.
