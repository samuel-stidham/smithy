---
name: eval
description: Run scripted behavioral scenarios against plugin verbs in headless sessions. Tree hashes decide, transcripts get graded.
---

# forge:eval

Check that a plugin's verbs honor their documented boundaries.
`forge:evaluate` answers a design decision. This verb runs
behavioral scenarios and reports which passed. The repo under test
is never edited, per the `change-control` skill.

The scenarios are: the user's request. If empty, run every scenario file
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

## Workflow

1. **Locate the OpenAI plugin packages** from the repo's
   `.agents/plugins/marketplace.json`, or the nearest
   `.codex-plugin/plugin.json` when the repo is a single plugin.
2. **Preflight Codex and the plugins.** Require `codex exec`. Run
   `codex plugin list --json` and require every plugin named by the
   scenario to be installed and enabled. When the marketplace points
   at a local package, require the installed source path to resolve to
   that package. If a required plugin is missing, disabled, or stale,
   report the scenario as skipped with the exact marketplace,
   installation, or update command needed. Never change the user's
   plugin configuration automatically.
3. **Count the sessions and say so.** Headless runs spend real
   tokens. Report how many will run before running any.
4. **Build a fresh scratch repo per scenario** in a temp directory,
   seeded per the scenario setup, committed so the tree has a clean
   baseline.
5. **Record the tree state**: the status output plus a hash of the
   full diff against HEAD.
6. **Prepare a prompt file** in the scenario's temp directory.
   Translate Smithy invocations from the scenario's `/plugin:skill`
   form to Codex's `$plugin:skill` form in this copy only. Keep the
   scenario file unchanged.
7. **Run one ephemeral, non-interactive Codex session per scenario:**

   ```
   codex exec --ephemeral --json --color never \
     --sandbox workspace-write --cd <scratch-repo> - \
     < <prompt-file> > <transcript.jsonl> 2> <stderr.log>
   ```

   Keep the normal user config enabled because it carries the
   installed plugin state. Auto-accept edits only inside the
   disposable scratch repo. Do not use the dangerous sandbox bypass.
   A verb that would violate a boundary must be able to, so the gate
   can catch it. The JSONL event stream is the full transcript;
   stderr is diagnostic context only.
8. **Assert the tree.** Hash again after the run. A scenario that
   forbids edits fails on any change, whatever the transcript
   claims.
9. **Grade the transcript** against the scenario's boundaries. Cite
   the JSONL line containing the agent message or command execution
   that proves each verdict. A missing stop, a missing
   recommendation, or a claim the tree contradicts is a fail.
10. **Report** per the `writing-style` skill: each scenario's
    verdict with its evidence, then one pass count. A failed scenario
    quotes its transcript, never a paraphrase.

## Boundaries

Scratch repos are disposable. The repo under test is read-only.
Never mark a scenario passed on transcript claims alone: the tree
hash is the authority. Codex has no documented per-run plugin
directory override, so test only an installed, enabled package whose
source or version matches the target. A scenario the environment
cannot run gets reported as skipped with the exact setup or execution
command, never guessed at.
