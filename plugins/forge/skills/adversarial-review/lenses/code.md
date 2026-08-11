# Code lens pack

The lens pack for diffs and code files. The `adversarial-review`
skill defines the dispatch, the findings format, and the verdict.

Work the diff through each lens as its own pass. Raise only real,
specific issues. Cite file and line. No generic advice.

- **Architecture.** Layer violations and dependency direction, per the
  `clean-architecture` skill. Missing abstraction where one is clearly
  needed, unnecessary abstraction where it is not.
- **Code quality.** Per the `clean-code` skill: naming, dead code,
  swallowed errors, duplication that should be shared.
- **Tests.** New behavior covered. Tests assert behavior, never
  implementation details. Obvious edge cases present.
- **Security.** Hardcoded secrets, injection risks, missing validation
  at trust boundaries, unsafe deserialization, authorization gaps.
- **Docs.** Public behavior or setup changed without the README or
  docs following.
- **Scope.** The diff matches the intent its branch name and commit
  subjects state, no more and no less. Flag unrequested changes and
  quiet scope creep.
