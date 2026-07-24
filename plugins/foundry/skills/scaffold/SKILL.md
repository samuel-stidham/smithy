---
name: scaffold
description: Generate a complete, working Clean Architecture project template for a language and project type. Optional OpenTofu infrastructure.
argument-hint: "{language} {project-type} [--infra opentofu --provider aws|gcp|digitalocean]"
disable-model-invocation: true
---

# /foundry:scaffold

Generate a complete, real, working Clean Architecture project in the
current directory, or a new subdirectory the user confirms when the
directory is non-empty. Every file must compile, run, and pass as
written. No placeholder comments standing in for logic.

Follow the `forge:clean-architecture` skill for layering, naming, and
the fitness test. Follow the `forge:clean-code` skill inside layers.
This plugin requires forge.

## Arguments

`$ARGUMENTS` is `{language} {project-type}` plus optional flags. Ask
when either is missing or ambiguous. Never guess.

Project types and their shapes live in
[project-types.md](project-types.md). Read it before generating.
Language is unrestricted: use the named language's real idioms,
package manager, test framework, and conventional layout.

## Infrastructure with --infra

Opt-in only. `--infra opentofu` follows the
`foundry:infrastructure-as-code` skill as the source of truth for the
`infra/` layout, modules, providers, state, and secrets. `--provider`
is then required: `aws`, `gcp`, or `digitalocean`. The only accepted
`--infra` value is `opentofu`. If the user passes `terraform`, explain
that the foundry uses OpenTofu and continue.

Generate the minimum the project needs. Wire `infra/` to the generated
Dockerfile. Add a deploy stage to the CI pipeline.

## Every project includes

1. Layered structure per `forge:clean-architecture`, in the
   language's idiomatic directory names. The `web-app` type follows
   its framework instead, keeping business logic out of controllers.
2. The dependency-rule fitness test that skill defines.
3. Multi-stage Dockerfile: non-root final stage, runtime artifact
   only.
4. `docker-compose.yml` with only the dependencies the type needs.
5. Makefile: `build`, `run`, `test`, `lint`, `docker-build`.
6. GitHub Actions CI at `.github/workflows/ci.yml`: deps, lint, test.
7. `.env.example` with placeholders and one-line comments. No real
   secrets.
8. README: what it is, the architecture and data flow, how to run
   locally and in Docker, how to test.
9. Example tests per layer, per the skill's testing strategy. They
   must actually pass.
10. `.editorconfig`, `.gitignore`, and an MIT `LICENSE` (ask when the
    copyright name is unclear).

## Process

1. State the language, type, flags, and file tree. Briefly.
2. Create real, working files.
3. Run the Makefile test and lint targets. With `--infra`, also run
   `tofu validate`. Fix failures before reporting success.
4. Report what was created, how to run it, and the decisions worth
   revisiting. Prose per the `forge:writing-style` skill.

No commit, push, or PR. Committing is `/forge:do-work` or
`/forge:ship` territory.
