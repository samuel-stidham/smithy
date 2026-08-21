---
name: writing-style
description: Writing rules for all text the forge family produces. Work context is the default. Use whenever writing for a human reader.
---

# Writing style

The canonical writing rules for every piece of text the forge family
produces. A shared core applies everywhere. The work context applies by
default. The draft plugin's `creative` skill extends these rules for
manuscripts and owns the creative flags.

## Mechanical rules for all writing

These bind every sentence in every context. They are safe to mirror
into always-loaded memory as a floor. This skill stays canonical.

- **No em dashes.** That includes an en dash used as one and a double
  hyphen standing in for one. A spaced hyphen doing the same job
  counts too. Break the sentence in two, or use a comma.
- **No semicolons.** Same fix.
- **Cap sentences at twenty-two words.** In verse the cap applies per
  line. After a colon, the stem and each item count separately.
  Split anything longer.
- **No watermarks.** Never embed one, visible or hidden. Zero-width
  characters and other invisible marks count. A disclosure a host
  mandates, such as a PR trailer, is no watermark.

### Quoting exemption

These rules govern prose you write, never material you reproduce.
Tool output, test failures, stack traces, code, config, diffs, command
lines, and cited text stay verbatim in fenced blocks. Rewriting quoted
material corrupts the evidence. Your prose around the block still
follows every rule.

## Habits to avoid

The tells of machine-written text. They apply in full to the work
context. In creative writing they yield only where the project's
existing prose establishes the pattern. The mechanical rules above
never yield.

- **No "not X, but Y" framing.** State what is true.
- **No throat-clearing openers.** Start with the content.
- **No closing paragraph that repeats what you just said.** End on
  the last new fact.
- **No inflated stakes.** Skip crucial, vital, seamless, robust, and
  game-changing unless literally accurate.
- **No stacked hedges.** One qualifier per claim.
- **No rule-of-three padding.** Never stretch a list to three for
  rhythm.
- **Write in the active voice.** Scan for "is, are, was, were" plus
  a past participle. Name the actor instead. Passive is fine only
  when the actor is unknown or does not matter.
- **No adverb propping up a weak verb.** Replace it with a stronger
  verb, or with the number the adverb stands in for.
- **No colon as a mid-sentence connector.** A colon introduces a
  list or an example. Nothing else.

## The work context

The default. It covers reports, PR descriptions, commit messages,
README content, and inline documentation. Development artifacts stay
in the work context even inside creative commands.

- **Lead with the answer.** Open each section with its conclusion.
  When a command mandates its own order, such as a verdict that must
  come last, the command wins.
- **Use paragraph form.** Narrative explanation is prose. Numbered
  steps and checklists may stay lists.
- **Scale headings to the artifact.** A commit body needs none. A
  README does. Never add a heading to organize three sentences.
- **Keep vocabulary consistent.** One word per concept, reused.
- **Match the target repo's spelling.** Follow the convention already
  in its prose. Default to American English only when there is none.
- **Cut the portable sentence.** When a doc describes one repo, a
  sentence that would fit any other repo unchanged says nothing.
  Name the mechanism, the fact, or the number instead. Instructions
  written to run in any repo are exempt.
- **No restating bold labels.** A bold label and colon that repeat
  what the line says become prose. A lead-in that adds detail after
  its period stays.
- **Keep prose plain ASCII.** Straight quotes, sentence-case
  headings, no decorative emoji. A token a host mandates, such as a
  required PR trailer, is exempt.

## Before delivering

Scan your own prose, never quoted blocks, against the mechanical
rules. Check dashes and semicolons, the longest sentence, invisible
marks, and fenced blocks holding only quoted material. Identifiers
like `--work` or `plugin--v1.2.3` and number ranges do not count.
Also scan for connector colons, and for non-ASCII punctuation in
work-context prose.
