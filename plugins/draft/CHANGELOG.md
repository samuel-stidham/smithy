# Changelog

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
