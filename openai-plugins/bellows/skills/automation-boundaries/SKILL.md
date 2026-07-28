---
name: automation-boundaries
description: What unattended automation may and may not do. Every routine, watch, and scheduled job is judged against it.
---

# Automation Boundaries

The standard every unattended job is judged against. Attended work
has a human noticing when something goes sideways. Unattended work
has only these rules.

## The definition rule

Every routine carries five fields: purpose, cadence, boundaries,
report destination, and stop procedure. A job missing any of them
is not a routine yet.

## What unattended work may never do

- Push to the default branch, merge, or publish a release.
- Close an issue or PR, or dismiss a review.
- Spend outside a budget its definition states: API calls, cloud
  resources, browser sessions.
- Read or write a secret outside the environment's secret
  mechanism, or let one reach a log or report.

## The loudness rule

A routine that cannot do its job says so at its report destination.
A silent skip gets trusted for a year, so it is worse than a crash.
Green runs stay quiet. Failures are loud.

## The idempotence rule

Every run assumes the last run may have half-finished. Re-running
is always safe, and a run that cannot make that true says so in its
definition.
