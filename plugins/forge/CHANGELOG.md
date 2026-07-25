# Changelog

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
