---
name: docs
description: Write or update repo documentation. READMEs, ADRs, API references, and guides, verified against the code they describe.
---

# draft:docs

Write repo documentation that stays true to the code: READMEs,
ADRs, API references, setup and contributing guides. The work
context of `forge:writing-style` governs throughout. This plugin
requires forge.

The task is: the user's request

If the user's request is empty, ask what documentation is needed.

## The verification rule

Documentation states what the code does today. Read the code before
writing about it. Run every command you document when running it is
safe, and mark the ones you could not run. A doc the code
contradicts is worse than no doc, because it gets believed.

## Orientation

- Match the repo's existing documentation: structure, heading
  style, spelling, and tone. Never introduce a clashing format.
- Code samples are real code, quoted verbatim, per the quoting
  exemption in `forge:writing-style`. Never a sketch of code that
  might work.
- ADRs follow the repo's own template when one exists. Otherwise:
  context, decision, consequences, status.
- API references follow the ecosystem's native documentation
  convention, detected from the repo, never imposed.

## Workflow

1. **Restate the task** and where the doc lives.
2. **Branch** as `docs/{short-kebab-description}`, with types per
   `forge:conventional-commits`.
3. **Write**, verifying as you go per the rule above.
4. **Commit** per `forge:conventional-commits`, one document or
   section at a time.
5. **Report** per `forge:writing-style`: what was written, what was
   verified by running it, and what remains unverified.

## Boundaries

No push or PR (that is `forge:ship`). The changelog belongs to
`forge:version`. Style rules never rewrite quoted tool output.
