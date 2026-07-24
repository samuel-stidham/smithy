---
name: writing-style
description: Writing rules for all text the forge family produces. Work context is the default. Use whenever writing for a human reader.
user-invocable: false
---

# Writing Style

The canonical writing rules for every piece of text the forge family
produces. A shared core applies everywhere. The work context applies by
default. The draft plugin's `creative` skill extends these rules for
manuscripts and owns the creative flags.

## Rules for all writing

These bind every sentence in every context. They are safe to mirror
into always-loaded memory as a floor. This skill stays canonical.

- **No em dashes.** That includes an en dash used as one and a double
  hyphen standing in for one. Break the sentence in two, or use a
  comma.
- **No semicolons.** Same fix.
- **Cap sentences at twenty-two words.** Split anything longer.

### Quoting exemption

These rules govern prose you write, never material you reproduce.
Tool output, test failures, stack traces, code, config, diffs, command
lines, and cited text stay verbatim in fenced blocks. Rewriting quoted
material corrupts the evidence. Your prose around the block still
follows every rule.

## Habits to avoid

The tells of machine-written text. They apply in full to the work
context. In creative writing they yield only where the project's
existing prose establishes the pattern, as the `creative` skill in the
draft plugin defines. The three mechanical rules above never yield.

- **No "not X, but Y" framing.** State what is true.
- **No throat-clearing openers.** Start with the content.
- **No closing paragraph that repeats what you just said.**
- **No inflated stakes.** Skip crucial, vital, seamless, robust, and
  game-changing unless literally accurate.
- **No stacked hedges.** One qualifier per claim.
- **No rule-of-three padding.** Never stretch a list to three for
  rhythm.

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

## Before delivering

Scan your own prose, never quoted blocks, before it leaves a command.

1. Search for `—`, `–`, a `--` standing in for a dash, and `;` outside
   code. Flag names like `--work` and number ranges do not count.
   Rewrite every real hit.
2. Find the longest sentence. Split it past twenty-two words.
3. Confirm every fenced block holds quoted material, never prose moved
   there to dodge the rules.
