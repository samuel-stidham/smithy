---
name: clean-code
description: Code-level quality cues for any layer and language. Judgment over metrics. Use when implementing or reviewing code.
user-invocable: false
---

# Clean code

Judgment cues for code inside any layer. These record where this
codebase's owner differs from common defaults. Apply them over generic
best practice.

- **Optimize total reading cost, never function length.** Length is a
  weak signal. The real signals are deep nesting and long boolean
  chains. Extract a helper only when its name lets the caller be read
  without opening the body. A linear forty-line function often beats
  eight scattered helpers. Shattering one coherent operation across a
  file is the same complexity in a different outfit.
- **Keep related code close.** A helper used once, meaningful only
  beside its caller, belongs next to its caller. Every extraction adds
  a reader jump. Extract for clarity, never to relocate complexity
  somewhere less visible.
- **Temper DRY.** Unify duplication only when two sites express one
  rule that must stay in sync. A wrong abstraction costs more than a
  little repetition. Flags and branches accumulating in a shared
  function prove the abstraction was wrong. Prefer the duplication.
- **Name intent at call sites.** Raw literals and bare booleans hide
  meaning exactly where calls are read. Use named constants, enums, or
  named arguments whenever meaning is not obvious in place. The
  constant explains meaning, never restates the value: `MAX_RETRIES`,
  never `THREE`.
- **Guard early.** Handle edge cases and errors at the top and return.
  The happy path stays at the lowest indentation level.
- **Errors carry context.** Handle where you can act meaningfully.
  Propagate upward with context added otherwise. Never swallow, never
  return a silent default unless documented as intentional.
- **Comments explain why.** The code already says what. Unclear code
  gets rewritten, never narrated. No commented-out code. Version
  control remembers.
