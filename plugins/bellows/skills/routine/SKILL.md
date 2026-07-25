---
name: routine
description: Define a recurring job with explicit boundaries, dry-run it, then register it on the scheduler the environment offers.
argument-hint: "[job to automate and its cadence]"
disable-model-invocation: true
---

# /bellows:routine

Turn a recurring chore into a scheduled routine: a defined job that
runs unattended on a cadence. The definition is the deliverable. A
routine nobody can read, audit, or stop does not ship.

The job is: $ARGUMENTS

If `$ARGUMENTS` is empty, ask what to automate and how often.

## Workflow

1. **Understand the job.** What runs, on what cadence, and what done
   looks like. Confirm the job is genuinely recurring. A one-off
   task belongs to `/forge:do-work`.
2. **Pick the surface.** Detect what the environment offers and
   match the job to it. Agent work fits Claude Code's own scheduled
   agents. Repo work that CI should own fits the provider's
   scheduler. Machine work fits the machine's scheduler. Never
   assume a provider or platform.
3. **Write the definition.** The five fields the
   `automation-boundaries` skill demands: purpose, cadence,
   boundaries, report destination, stop procedure.
4. **Dry-run once.** Execute the job attended and watch it finish
   before scheduling it. A job that never ran attended never runs
   unattended.
5. **Register and report.** Schedule it, then report the definition,
   the first scheduled run, and the stop procedure per
   `forge:writing-style`.

## Boundaries

The routine itself obeys the `automation-boundaries` skill. This
verb never schedules a job whose dry run failed, and never registers
a routine missing its stop procedure.
