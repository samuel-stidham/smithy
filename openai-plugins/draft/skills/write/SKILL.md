---
name: write
description: Write long-form prose for a writing project. Fiction, nonfiction, poetry, or technical articles, in the project's own voice.
---

# draft:write

Write long-form prose for a writing project in this repo: fiction,
nonfiction, essays, worldbuilding, fanfiction, technical books, and
blog articles alike. The repo is the workspace, never the publishing
destination. This plugin requires forge.

The task is: the user's request

Strip context flags before reading the task (the `creative` skill
defines them). If nothing remains, ask what to write next.

## Orientation

- Read the repo's guidance files for subject, tone, audience,
  structure, and conventions. Treat them as editorial guidelines.
- Read the existing content. Match the established voice, pacing,
  and terminology. Never introduce a clashing style.
- Find the outline or table of contents and place the task in it.
- Load any project-specific skill file the repo carries, such as a
  worldbuilding bible, character reference, or style guide.
- If the project defines a publication target spec (fields, format,
  storage path), fill every field it names, in its format, and store
  output where it says. The spec wins over guesses about structure.

## Workflow

1. **Restate the task.** What you are writing, where it fits, and
   your assumptions. Briefly.
2. **Branch** as `{type}/{short-kebab-description}`: `feat` for new
   content, `fix` for corrections, `refactor` for restructuring,
   `docs` for metadata, with types per the
   `forge:conventional-commits` skill.
3. **Write.** Manuscript content follows the `creative` skill.
   Articles follow the `technical-writing` skill. Both extend
   `forge:writing-style`, whose work context still governs reports
   and commit messages. Produce complete prose. No placeholder
   paragraphs.
4. **Commit** per `forge:conventional-commits`, one section or scene
   at a time.
5. **Self-review.** Continuity with existing content, tone
   consistency, fit with the outline. Flag anything uncertain.
6. **Report** per `forge:writing-style`: what was written, where it
   fits, decisions made, continuity concerns, and a note that the
   diff deserves reading before shipping. Stopping early leaves a
   resume path.

## Boundaries

No push or PR (that is `forge:ship`). No outlines unless the outline
is the task. The repo defines voice, genre, and subject, never this
command.
