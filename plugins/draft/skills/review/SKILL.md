---
name: review
description: Adversarial review of prose files through the prose lens pack. Verdict is SHIP IT, NEEDS WORK, or RETHINK.
argument-hint: "[file path or glob of the prose under review]"
disable-model-invocation: true
context: fork
background: false
---

# /draft:review

Review prose the way a hostile expert reader would: articles,
chapters, essays, and any other manuscript file. This verb runs per
the `forge:adversarial-review` skill with the prose lens pack. It is
read-only. It never edits the files, and it never chains into
`/draft:write`. Reconciling the findings belongs to whoever invoked
it. This plugin requires forge.

The artifact is: $ARGUMENTS, a file path or glob. If it resolves to
no files, report that as the entire output and return no verdict.

## Setup

1. Resolve the path or glob to prose files and read each in full.
   Skip dotfiles, ignored paths, and vendor or build directories.
2. Read the repo's guidance files: publication spec, style guides,
   outlines, and any worldbuilding or character reference. The
   lenses judge the prose against them and against earlier
   installments.
3. The synchronous fork this verb runs in is the skill's
   fresh-context dispatch, and this file is the brief. The persona:
   a hostile expert reader of the work's subject and genre.

## Review

Load the `forge:adversarial-review` skill and the prose lens pack
stored beside that skill's own file, at `lenses/prose.md`. Work
every matched file through each lens as its own pass.

## Findings

Return a numbered findings list ordered by severity. Each finding
carries the file, the passage, the lens it fails, the severity, and
what a correction requires. For a factual finding, state the
verifiable correction when one exists.

## Verdict

End with exactly one verdict, per the skill. Do not soften it to be
agreeable.

- **SHIP IT**: publishable as it stands. List optional nits
  separately.
- **NEEDS WORK**: fixable findings exist. The list above says what
  and where.
- **RETHINK**: the piece needs restructuring or a different
  approach. Explain the core concern.
