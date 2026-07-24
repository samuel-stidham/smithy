---
name: version
description: Cut a release. Bump the version, update VERSION.md and CHANGELOG.md, tag, and push the tag.
argument-hint: "[major|minor|patch|explicit version, e.g. \"patch\" or \"2.0.0\"]"
disable-model-invocation: true
---

# /forge:version

Cut a release: determine the current version, bump it, update the
version files, and create and push an annotated tag. Works for code
projects, writing projects, and plugin repos.

Requested bump: $ARGUMENTS. Accepts `major`, `minor`, `patch`, or an
explicit version like `1.2.3`. If empty, ask.

## Orientation

- In a plugin marketplace monorepo (a `marketplace.json` listing more
  than one plugin), ask which plugin this release covers. Each plugin
  versions independently from its own `plugin.json`. Tag as
  `{plugin}-v{version}`, and update the changelog beside that plugin's
  manifest when one exists, else the root changelog.
- Otherwise, find the current version in this order: `VERSION.md`,
  semver git tags, a manifest version field. Nothing found means
  `0.0.0` and a first tagged release. Say so.

## Workflow

1. Report the current and new version. Tag only after the user
   confirms.
2. Update `VERSION.md`, the relevant `plugin.json`, and known manifest
   files. Never search-and-replace the version across the repo.
3. Update the changelog: a new top section with commit subjects since
   the last tag, grouped by type per the `conventional-commits` skill.
4. Commit everything together as `chore(release): v{version}`. Create
   the annotated tag with a brief summary from the changelog. Push the
   tag and the commit.
5. Report the version, tag, and remote URL. Remind about tag-triggered
   CI when the repo has it.

## Boundaries

No branch pushes or PRs (that is `/forge:ship`). No publishing to any
platform. No tagging without confirmation.
