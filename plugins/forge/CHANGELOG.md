# Changelog

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
