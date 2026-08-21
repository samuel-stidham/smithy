---
name: adversarial-review
description: The shared adversarial review mechanism. A hostile fresh-context reviewer, a lens pack matched to the artifact, severity findings, one verdict. Use whenever a verb runs a review.
user-invocable: false
---

# Adversarial review

The review mechanism every review verb dispatches through. This file
holds the invariants and stays short. The lenses live in packs under
`lenses/`, loaded on demand.

## The dispatch

The review runs in a dispatched subagent with a fresh context. The
subagent receives a written brief plus the paths of the artifact
under review. It never relies on conversational carryover from the
caller. A verb that itself runs as a synchronous fork with a fresh
context already satisfies the dispatch. Its own file is then the
brief.

## The persona

The reviewer is a hostile expert in the artifact's domain. The brief
names the persona.

## The output

The reviewer returns a numbered findings list, each finding with a
severity. The review ends with exactly one verdict: **SHIP IT**,
**NEEDS WORK**, or **RETHINK**. Nothing competes with the verdict,
and softening it to be agreeable is forbidden. A calling verb may
extend the findings format with its own fields and caps.

## The no-edit rule

The reviewer never edits the artifact. The caller reconciles every
finding itself. When a finding is factual and the caller cannot
verify the correction, the caller cuts the claim rather than
guessing.

## Lens packs

One pack per artifact class, each in its own file, loaded on demand:

- [lenses/code.md](lenses/code.md): diffs and code files.
- [lenses/prose.md](lenses/prose.md): articles and manuscripts.

Pack selection is detected, never configured, in this order:

1. Detect from the artifact. A git diff or code files select the
   code pack, and a diff selects it whatever file types it touches.
   Markdown articles or manuscripts reviewed as files select the
   prose pack.
2. When detection is ambiguous, use the pack the calling verb names.
