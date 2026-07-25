# Changelog

## foundry--v1.0.1

### Added

- This changelog, kept beside the plugin's manifest from now on.

## foundry--v1.0.0

The product factory becomes its own plugin in the smithy monorepo.

### Added

- Per-plugin manifest with `"dependencies": ["forge"]`, so installing
  foundry pulls forge in automatically.
- `scaffold` splits its project-type catalog into an on-demand
  `project-types.md`.

### Changed

- scaffold and deploy move to the `/foundry:` namespace as skills
  with `disable-model-invocation: true`.
- Scaffolded projects include the dependency-rule fitness test from
  `forge:clean-architecture`. CI and task-runner choices are stated
  defaults with overrides, never unconditional requirements.
- deploy counts untracked files as a dirty tree.
- `infrastructure-as-code` trimmed, safety discipline intact:
  plan-before-apply, no destroy in deploys, no auto-approve.
