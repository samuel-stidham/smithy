---
name: deploy
description: Deploy the current project using its own infrastructure. Detects OpenTofu configs, Dockerfile, and release steps, then applies them safely.
argument-hint: "[optional target, e.g. staging|production]"
disable-model-invocation: true
---

# /foundry:deploy

Deploy the current project using infrastructure already in the repo.
This is the verb that follows `/foundry:scaffold --infra`. Scaffold
writes the infrastructure. Deploy applies it. Run only on explicit
user invocation, never as a side effect.

Target: $ARGUMENTS. Empty means detect the default environment. Ask
only when more than one exists and the choice is unclear.

Follow the `infrastructure-as-code` skill for every OpenTofu action.
This plugin requires forge.

## Detect, never assume

Read the repo for how it deploys: an `infra/` directory, a Dockerfile
and any registry named in CI or env, deploy stages in workflows,
deploy scripts or Makefile targets, notes in the repo's agent
instructions and README. Nothing to deploy means stop, say so, and
suggest `/foundry:scaffold --infra opentofu`.

## Pre-flight

Stop and report on any failure. Never force past one.

- Clean working tree, untracked files included. Deploy committed
  state only.
- Required CLIs installed, such as `tofu` and the container or cloud
  CLI the repo uses.
- Provider credentials present in the environment, never read from
  source.

## Workflow

1. **Image.** With a Dockerfile and a target registry, build and
   push, tagged with the commit SHA, never only `latest`. Skip when
   the project ships no container.
2. **Infrastructure.** Apply `infra/` with the plan-before-apply
   discipline the skill defines. Run `tofu init` first when the
   directory is uninitialized. Never print secret values from
   variables, outputs, or state.
3. **Release steps.** Run the app's own migrations, cache warms, or
   asset builds only when the project defines them. Never invent one.
4. **Verify.** Read the outputs, check the app responds, and report:
   what changed, the image tag, the outputs, any remaining manual
   step.

## Boundaries

No PRs (that is `/forge:ship`) and no release tags (that is
`/forge:version`).
