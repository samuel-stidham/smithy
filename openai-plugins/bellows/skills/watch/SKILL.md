---
name: watch
description: Babysit long-running external work, such as a PR in CI, a deploy, or a migration, until it resolves.
---

# bellows:watch

Watch one piece of long-running external work until it resolves.
That means a PR moving through CI and review, a deploy, a
migration, a slow pipeline. Report on state changes. Stay quiet
between them.

The target is: the user's request

If the user's request is empty, ask what to watch and what resolved means.

## Workflow

1. **Define resolved.** The end state, the failure states, and what
   the watch may do about each. Settle anything ambiguous now.
   Nobody answers questions mid-watch.
2. **Match the cadence to the work.** Poll a ten-minute CI run every
   few minutes, a days-long review a few times a day. Prefer event
   notifications over polling wherever the environment offers them.
3. **Act inside the boundaries.** The `automation-boundaries` skill
   governs unattended action. Rerunning a flaky job and posting a
   status summary are in. Merging, force-pushing, and dismissing
   reviews are out.
4. **Report transitions.** Say what changed and what happens next.
   Green stays quiet. Failure is loud, with the evidence quoted
   verbatim in a fenced block.
5. **Close out.** When the work resolves, report the outcome and
   stop the watch. A watch that outlives its target is a leak.

## Boundaries

A watch observes and nudges. It never merges, and never makes the
decision the human is watching for.
