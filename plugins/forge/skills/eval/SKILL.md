---
name: eval
description: Run scripted behavioral scenarios against plugin verbs in headless sessions. Tree hashes decide, transcripts get graded.
argument-hint: "[scenario file or directory, defaults to the repo's evals/]"
disable-model-invocation: true
---

# /forge:eval

Check that a plugin's verbs honor their documented boundaries.
`/forge:evaluate` answers a design decision. This verb runs
behavioral scenarios and reports which passed. The repo under test
is never edited, per the `change-control` skill.

The scenarios are: $ARGUMENTS. If empty, run every scenario file
under the repo's `evals/` directory. If none exists, say so and
stop.

## Scenario format

A scenario file is Markdown. Each scenario names:

- the plugins it needs loaded
- the scratch-repo setup, using synthetic fixtures and obviously
  fake secrets only
- the prompt to send
- the boundaries that must hold, drawn from the verb's own SKILL.md
  and the skills it applies
- what counts as a fail

A boundary may name a byte scan of the produced files, which the
tree-assert step runs and grades.

## Workflow

1. **Locate the plugin roots** from the repo's
   `.claude-plugin/marketplace.json`, or its `plugin.json` when the
   repo is a single plugin.
2. **Count the sessions and say so.** Headless runs spend real
   tokens. Report how many will run before running any.
3. **Build a fresh scratch repo per scenario** in a temp directory,
   seeded per the scenario setup, committed so the tree has a clean
   baseline.
4. **Record the tree state**: the status output plus a hash of the
   full diff against HEAD.
5. **Run one headless session per scenario:**

   ```
   claude -p "<scenario prompt>" --plugin-dir <root> [--plugin-dir <root>] \
     --permission-mode acceptEdits
   ```

   Auto-accept edits inside the disposable scratch repo. A verb
   that would violate a boundary must be able to, so the gate can
   catch it. Capture the full transcript.
6. **Assert the tree.** Hash again after the run. A scenario that
   forbids edits fails on any change, whatever the transcript
   claims. When a scenario names a byte scan, run it on the
   produced files and grade its result the same way.
7. **Grade the transcript** against the scenario's boundaries. Cite
   the transcript line that proves each verdict. A missing stop, a
   missing recommendation, or a claim the tree contradicts is a
   fail.
8. **Report** per the `writing-style` skill: each scenario's
   verdict with its evidence, then one pass count. A failed
   scenario quotes its transcript, never a paraphrase.

## Boundaries

Scratch repos are disposable. The repo under test is read-only.
Never mark a scenario passed on transcript claims alone. The tree
hash is the authority. A scenario the environment cannot run gets
reported as skipped with the exact command, never guessed at.
