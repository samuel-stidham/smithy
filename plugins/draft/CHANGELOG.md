# Changelog

## draft--v1.2.1

### Changed

- creative cites the writing-style mechanical rules without a count,
  so the block can grow without breaking the reference. forge moved
  its watermark ban into that block.
- Poetry holds every other mechanical ban instead of naming the
  dash and semicolon pair, so the watermark ban reaches verse.
- review names its persona in a full sentence instead of through a
  connector colon.
- creative's voice rule names typography among what the project
  owns, taking over from the sentence forge removed. The mechanical
  bans still apply.
- Skill headings move to sentence case per the writing-style rule.

## draft--v1.2.0

### Added

- `/draft:review`: adversarial review of prose files through
  `forge:adversarial-review` with the prose lens pack. The lenses:
  factual accuracy, citation integrity, steelman integrity, writing
  style, and continuity. Takes a file path or glob, reports numbered
  severity findings and one verdict, never edits, and never chains
  into write.

## draft--v1.1.0

### Added

- `/draft:docs`: repo documentation. READMEs, ADRs, API references,
  and guides, verified against the code they describe. Commands
  shown in a doc get run when safe, and unrun ones are marked.

## draft--v1.0.1

### Added

- This changelog, kept beside the plugin's manifest from now on.

## draft--v1.0.0

The writing studio becomes its own plugin in the smithy monorepo.

### Added

- Per-plugin manifest with `"dependencies": ["forge"]`.
- `creative` skill: voice, continuity, pacing, and poetry rules
  extending `forge:writing-style`, plus the context flags including
  `--type-article`.
- `technical-writing` skill: article structure, verbatim code,
  research through `forge:web-browsing`, claims per
  `forge:citations`.
- write follows any publication target spec the project defines
  (fields, format, storage path).

### Changed

- write and publish move to the `/draft:` namespace as skills with
  `disable-model-invocation: true`.
- publish adds the dist ignore entry when the `.gitignore` lacks it.
