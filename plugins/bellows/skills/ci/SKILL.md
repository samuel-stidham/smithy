---
name: ci
description: Author or update the repo's CI pipeline on its own provider, mirroring the gates the repo already runs locally.
argument-hint: "[pipeline goal, defaults to test and lint on every push]"
disable-model-invocation: true
---

# /bellows:ci

Author or update the repo's continuous integration pipeline. The
pipeline mirrors the gates the repo already runs locally, on the
provider the repo already uses.

The goal is: $ARGUMENTS. If empty, the goal is test and lint on
every push and pull request.

## Detect, never assume

- **Provider.** Read the existing config: `.github/workflows/`,
  `.gitlab-ci.yml`, `Jenkinsfile`, `.circleci/`, or whatever else is
  present. With none present, infer from the remote host and
  confirm before writing.
- **Gates.** The test, lint, and build commands come from the repo's
  own manifests and scripts. A gate developers cannot run locally is
  a gate they will not trust.
- **Versions.** Language and tool versions come from the repo's
  version files and lockfiles, never from memory.

## Opinions

- Fail loud and fast. Cheap gates run before expensive ones.
- Secrets come from the provider's secret store. Never inline,
  never echoed into logs.
- Cache deliberately: keyed on the lockfile, or not at all.
- A scheduled pipeline job is a routine. It carries the definition
  the `automation-boundaries` skill demands.
- Keep it boring. A clever pipeline is a second codebase to debug.

## Verify and report

Validate the config with the provider's own linter when one exists.
Commit per `forge:conventional-commits`. Report what runs, on which
triggers, and roughly how long the expected path takes. No push or
PR (that is `/forge:ship`).
