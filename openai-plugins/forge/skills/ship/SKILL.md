---
name: ship
description: Run pre-flight checks, push the branch, and open a draft PR with a structured body.
---

# forge:ship

Take the current branch's committed work to a draft PR. Run only on
explicit user invocation, never as a side effect of another command.

Extra context for the PR body, if any: the user's request

## Pre-flight

Stop and report on any failure. Never force past one.

1. Not on the repo's default branch (detect it, never assume) nor any
   branch the remote marks protected.
2. No uncommitted changes, untracked files included. Ask what to do
   with them before committing anything on the user's behalf.
3. The base branch has not moved ahead. Flag a needed rebase instead
   of rewriting history yourself.
4. The repo's own tests pass.

## Push and PR

Push with `git push -u origin <branch>`, skipping when already tracked
and current. With an authenticated `gh`, open a draft PR against the
repo's default branch. When the user supplies a prepared title and
body (do-work's report produces one), use them after verifying against
the actual commits. Otherwise build the body from the branch's real
commits and diff, structured as **What**, **Why**, **How**,
**Testing**. Title per the `conventional-commits` skill, prose per the
`writing-style` skill. Report the PR URL.

Without `gh`, still push once pre-flight passes. Print a copy-ready
title, body, and compare URL, and say plainly why you fell back.
