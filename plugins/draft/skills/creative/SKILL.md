---
name: creative
description: Creative writing rules extending forge:writing-style. Voice, continuity, pacing, poetry, and the context flags. Use for manuscript content.
user-invocable: false
---

# Creative Writing

Extends the `forge:writing-style` skill for manuscript content:
chapters, scenes, essays, poems, worldbuilding. Load that skill
first. Its three mechanical rules never yield. Its habit rules yield
only where the project's existing prose establishes the pattern.
Development artifacts, such as reports, commit messages, and PR text,
stay in the work context even here.

## Flags

Commands whose main content goes beyond development artifacts accept
these. Strip them from arguments before interpreting the task.

- `--work`: force the work context. Wins over every other flag.
- `--creative`: force the creative context.
- `--type-{name}`: refine the form. `--type-prose` is the default.
  `--type-poetry` switches to the verse rules below. `--type-article`
  routes to the `technical-writing` skill and forces the work
  context. Every other type flag implies the creative context on its
  own. Any unknown type name is a question, never a guess.

## Voice

The repo owns the voice. Read the existing content first and match
its narrative distance, vocabulary register, rhythm, and spelling,
including British or other regional spelling. Never impose a house
style on a project that already has one. A project with no content
yet means asking for tone and audience before writing.

## Continuity

Check every new passage against what exists. Names, dates, places,
and established facts stay consistent. Track what each character
knows and when they learned it. Nobody reacts to what they have not
yet discovered. A forced contradiction gets flagged in the report,
never silently written into history.

## Pacing

Vary sentence length to control rhythm. Short carries tension. Long
carries reflection. Give the reader a beat between scenes instead of
jumping without transition.

## Poetry

`--type-poetry` adapts the mechanics to verse. Line and stanza
breaks outrank sentence structure. The twenty-two-word cap applies
per line instead of per sentence. The dash and semicolon bans hold.
Habits yield to the form. Match the form the project already uses,
such as free verse, meter, or rhyme, before choosing one.
