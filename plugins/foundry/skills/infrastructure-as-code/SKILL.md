---
name: infrastructure-as-code
description: OpenTofu conventions. Module layout, provider abstraction, remote state, plan-before-apply, secrets. Use when scaffolding infra or deploying.
user-invocable: false
---

# Infrastructure as Code

The source of truth for how the foundry writes and applies OpenTofu,
used by `/foundry:scaffold --infra` and `/foundry:deploy`. Provider
aware, never provider locked.

OpenTofu only. The generated HCL works with both the `opentofu` and
`terraform` binaries. When a user asks for terraform, explain this
and continue with OpenTofu.

## Layout

Infrastructure lives in `infra/` at the repo root, separate from any
`infrastructure/` application layer. The root holds `main.tf`
(module wiring), `variables.tf` (typed, described inputs),
`outputs.tf` (what a deploy needs afterward), `providers.tf`, and
`terraform.tfvars.example` (placeholders only), plus `modules/`.

## Modules by role

Name modules for the role, never a brand: `networking/`,
`container/`, `database/`, `secrets/`. Optional and opt-in: `cache/`
(default Redis) and `search/` (default Meilisearch). Generate an
optional module only when the app declares the dependency. Read the
signals: services in `docker-compose.yml`, keys in `.env.example`,
framework config such as `CACHE_STORE`, `QUEUE_CONNECTION`, or
`SCOUT_DRIVER`. The infra mirrors the app, never a wishlist.

## Providers

`--provider` accepts `aws`, `gcp`, or `digitalocean`. Each role maps
to the provider's nearest managed service, falling back to a
self-hosted container where none exists. Managed Meilisearch does not
exist anywhere: self-host it with a persistent volume and say so in
the generated README. Provider specifics stay inside modules.
`main.tf` reads the same shape everywhere.

## State, discipline, and secrets

- Remote backend for state, always. State can hold secrets in plain
  text. The `.gitignore` excludes `*.tfstate`, `*.tfstate.*`, and
  `.terraform/`.
- Every apply runs `tofu fmt`, `tofu validate`, and `tofu plan`, then
  applies only after a human reads the plan and confirms. Never
  `tofu destroy` in a deploy. Never auto-approve an apply that
  creates or replaces resources.
- Secrets never live in HCL or committed files. The real
  `terraform.tfvars` is gitignored. Runtime secrets live in the
  provider's secret manager through the `secrets/` module. The app
  reads them from the environment, never from infra source.
