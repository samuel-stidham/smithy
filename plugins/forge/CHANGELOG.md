# Changelog

## forge--v1.6.1

### Added

- Both lens packs raise each issue once, under the most specific
  lens.

### Changed

- The dash ban names the spaced hyphen as a banned substitute.
- The watermark ban moved into the mechanical block, retitled
  "Mechanical rules for all writing", so it binds every context.
  Citations of the block drop their count.
- The plain ASCII rule narrows to prose and exempts tokens a host
  mandates, such as a required PR trailer. Filed under changed
  because 1.6.0 called it additive while it tightened article quote
  style.
- The portable-sentence rule targets docs that describe one repo
  and exempts instructions written to run in any repo.
- The inline-header ban becomes a ban on bold labels that repeat
  their line, which the corpus's lead-ins already meet.
- The pre-delivery scan covers invisible marks, exempts
  double-hyphen identifiers, and keeps every sentence under the cap
  it checks.
- After a colon the sentence cap counts the stem and each item
  separately, which the corpus's step-and-report style relies on.
- The watermark ban names a host-mandated disclosure, such as a PR
  trailer, as no watermark.
- The ASCII rule's manuscript-typography sentence is gone.
  Work-context scoping already keeps the rule off manuscripts.
- The proof bar's fourth condition stays a property of the claim,
  in the active voice.
- eval grades a scenario's named byte scan beside tree hashes and
  transcript grading.
- verify reports per the writing-style skill, matching the other
  verbs.
- A prose sweep across the verbs, reference skills, and lens packs
  drops connector colons, named-actor passives, and propping
  adverbs. Each file drops what it held.
- version's release-commit template names the plugin as
  `{plugin} v{version}` in a marketplace monorepo.
- version routes a repo-level change riding along to the root
  changelog.
- Skill headings move to sentence case per the writing-style rule.

## forge--v1.6.0

### Added

- Six generation rules in writing-style. Habits to avoid adds active
  voice, a ban on adverbs propping weak verbs, and a ban on connector
  colons. The work context adds cut the portable sentence, no
  inline-header lists, and plain ASCII output. The ASCII rule carries
  a watermark ban that never yields. The pre-delivery scan now covers
  connector colons and non-ASCII punctuation in work-context output.
- A vague-attribution lens in the prose lens pack, directly after
  citation integrity. It flags any claim resting on "experts
  believe", "studies show", or "industry reports suggest" with no
  named source.

## forge--v1.5.0

### Changed

- The code lens pack narrows its security lens to repo-specific
  judgment: weakened auth, secrets in code or logs or output,
  widened IAM scope, deleted or skipped security tests, and the
  repo's own declared security rules. Generic vulnerability-class
  hunting defers to Anthropic's official `security-guidance` plugin,
  which reviews continuously.
- review detects whether `security-guidance` is active, opens its
  report with the coverage case, and recommends installing the
  plugin in one line when it is absent. Never blocking, never an
  install.
- version recommends an on-demand `claude-security` scan in the
  pre-tag confirmation when the repo holds deployable or sellable
  code. Recommendation only: the scan is never run and never blocks
  the tag.

## forge--v1.4.0

### Added

- `adversarial-review` reference skill: the shared review mechanism
  any verb can dispatch through. A hostile fresh-context reviewer
  with a written brief, numbered severity findings, one verdict, and
  a hard no-edit rule. Lens packs live in on-demand files under
  `lenses/`, code and prose to start. Detection selects the pack,
  with the calling verb as the tiebreak.

### Changed

- review dispatches through `adversarial-review` with the code lens
  pack. The six lenses moved into the pack verbatim. The interface,
  the diff-only reading scope, and the verdict behavior are
  unchanged. Each finding now carries an explicit severity label
  through the shared output contract.

## forge--v1.3.1

### Fixed

- `change-control` no longer reads as one pull request per fix. A new
  batching section lets a branch, pull request, or release carry many
  fixes. Each fix keeps its own scope, budget, evidence, and commit.
  The repair budget and the multi-issue stopping condition now bound
  one fix instead of the whole branch.

## forge--v1.3.0

### Added

- `/forge:eval`: scripted behavioral scenarios against plugin verbs
  in headless `claude -p` sessions with `--plugin-dir`, or
  `$forge:eval` in ephemeral `codex exec --json` sessions against
  verified installed plugins. One fresh scratch repo per scenario,
  edits auto-accepted so violations can actually happen, tree hashes
  as the authority, and transcripts graded against the verbs'
  documented boundaries. Scenario files live in the target repo's
  `evals/` directory.

## forge--v1.2.0

### Added

- `change-control` reference skill: evidence grades for claims, the
  proof bar for suspected bugs, six finding classifications, separate
  operating modes, a pre-edit report, a default repair budget, and
  stopping conditions. Verification never mutates.
- `/forge:prove`: one finding to a verdict. Test-only edits allowed
  for a durable regression proof, never a production change, and a
  hard stop after the proof.
- `/forge:verify`: the repo's own QA checks, narrowest to broadest,
  in check-only modes. Tree state recorded before and after, and any
  mutation reported instead of reverted.

### Changed

- do-work applies `change-control`: one vertical slice per feature,
  proven defects only, and unproven findings routed to
  `/forge:prove` or `/forge:debug`.
- debug is authorized as prove, then fix, then verify for one
  symptom. A failed proof stops it with zero production changes.
- review is explicitly read-only, returns at most five classified
  findings with evidence fields, and precedes its verdict with one
  `Recommended next proof`.

## forge--v1.1.0

### Added

- `/forge:debug`: symptom to proven fix. Reproduce first, isolate,
  name the cause apart from the trigger, fix small, and prove the
  fix with a regression test run both ways.
- `/forge:refactor`: behavior-preserving restructuring. Safety net
  first, characterization tests where coverage is thin, small
  passing commits, and no behavior change ever mixed in.
- `/forge:evaluate`: evidence-backed decision on a library, tool,
  or approach. Cited research per `citations`, an optional
  throwaway spike, and exactly one recommendation.

## forge--v1.0.1

### Added

- This changelog, kept beside the plugin's manifest from now on.

## forge--v1.0.0

The core engineering workflow becomes its own plugin in the smithy
monorepo.

### Added

- `citations` skill: verified, reader-accessible sources in APA
  style, a four-tier source ladder, and reference-ledger support.
- `agents/implementer.md`: an opus-pinned implementation subagent.
  do-work orchestrates at most two in flight, on disjoint files, and
  owns every commit itself.
- `web-browsing`: a Browserbase remote-session budget with usage
  checks, pace warnings, and leaked-session hygiene.

### Changed

- Commands collapsed into skills. Verbs carry
  `disable-model-invocation: true`; references carry
  `user-invocable: false`. review runs as a synchronous fork with six
  lenses, scope judged from branch name and commit subjects.
- `clean-architecture` reduced to the owner's positions plus a
  dependency-rule fitness test. `clean-code` reduced to
  counter-default judgment cues.
- version understands marketplace monorepos: per-plugin manifests,
  per-plugin changelogs, and `{plugin}--v{version}` tags matching
  `claude plugin tag`. Pushing the release commit and tag is its job.
- ship detects the repo's default branch, counts untracked files as
  dirty, and uses a prepared PR body when do-work supplies one.
- test-harness registers its generated MCP server in `.mcp.json`.
- writing-style is self-contained, with the per-line verse cap
  stated in the rule it modifies.

### Removed

- `token-budget`. Its surviving rules fold into do-work.
