# smithy

smithy is a marketplace of lean, repo-agnostic plugins for
[Claude Code](https://claude.com/claude-code): four plugins, one set
of shared rules. It makes no assumptions about
language, framework, or tooling. Every verb detects what it needs from
the repo itself: manifest files, lockfiles, existing patterns, and the
repo's own agent instructions. It never requires per-repo
configuration.

## The family

| Plugin | What it does | Where it runs |
| --- | --- | --- |
| **forge** | Core engineering workflow: execute tasks, review diffs, ship draft PRs, cut releases, generate test harnesses. | Enabled globally. |
| **foundry** | Product factory: scaffold complete Clean Architecture project templates, deploy them with OpenTofu. | Enabled per repo. |
| **draft** | Writing studio: books, poetry, and technical articles, compiled into publishable ebooks. | Enabled per repo. |
| **anvil** | Nix environments: shell gates, distro-family portability audits, devenv environments, confirmed activation. | Enabled per repo. |

foundry, draft, and anvil require forge. They borrow its shared
skills by name (`forge:clean-architecture`, `forge:writing-style`,
`forge:citations`, `forge:web-browsing`) and declare the dependency
in their manifests, so installing any of them pulls forge in
automatically. forge depends on nothing.

## Installation

```text
/plugin marketplace add samuel-stidham/smithy
/plugin install forge@smithy
/plugin install foundry@smithy
/plugin install draft@smithy
/plugin install anvil@smithy
```

Install forge at user scope so it is available everywhere. Keep the
leaves disabled globally and enable them per repo: draft in writing
projects, foundry where products get built or deployed, anvil in
machine definitions and devenv projects. One line in that repo's
`.claude/settings.local.json` does it, or use the `/plugin` menu.

## Updating

```text
/plugin marketplace update smithy
```

Then update the plugin from the `/plugin` menu and restart Claude
Code. Each plugin versions independently, tagged
`{plugin}--v{version}`.

## forge

The verbs, invoked as `/forge:<name>`:

- **do-work** executes a development task end to end. It orients in
  the repo, shows a short plan, branches, implements through capped
  implementer subagents, tests with the repo's own tooling, and
  reports with a suggested PR title and body. It stops before
  pushing.
- **review** audits the current branch's diff against its base
  through six lenses: architecture, code quality, tests, security,
  docs, and scope. It runs in an isolated subagent that reads only
  the diff and the repo, and it ends with exactly one verdict:
  **SHIP IT**, **NEEDS WORK**, or **RETHINK**.
- **ship** runs pre-flight checks, pushes the branch, and opens a
  draft PR with a What/Why/How/Testing body built from your actual
  commits. Without `gh` it still pushes and prints a copy-ready body.
- **version** cuts a release: bump, changelog, annotated tag, push
  the tag. In a plugin marketplace monorepo it asks which plugin and
  tags that plugin's release in the format documented under
  Updating. It always confirms before tagging.
- **test-harness** generates an MCP server exposing the project's
  domain and application layers as tools, so Claude can drive the app
  headlessly for QA. It builds the harness only.

The shared reference skills, loaded by name: `clean-architecture`
(the owner's positions plus test-based enforcement of the dependency
rule), `clean-code` (judgment cues over metrics), `citations`
(verified, reader-accessible sources in APA style, with
reference-ledger support), `conventional-commits` (commit and PR
title format), `writing-style` (the rules that keep prose human),
and `web-browsing` (the browse CLI, with a Browserbase remote-session
budget).

## foundry

- **scaffold** generates a complete, working Clean Architecture
  project: layered structure with a dependency-rule fitness test, a
  multi-stage Dockerfile, compose, Makefile, CI, `.env.example`,
  README, per-layer example tests, and an MIT license. Types:
  `rest-api`, `cli-tool`, `background-worker`, `webhook-gateway`,
  `task-runner`, and `web-app` (which follows its framework's own
  conventions). Any language, using its real idioms.

  ```text
  /foundry:scaffold go rest-api
  /foundry:scaffold php web-app --infra opentofu --provider digitalocean
  ```

  `--infra opentofu` adds an `infra/` directory built to the
  `infrastructure-as-code` skill: modules named by role, provider
  abstraction across `aws`, `gcp`, and `digitalocean`, remote state,
  and secrets handling.
- **deploy** applies a repo's existing infrastructure: image build
  and push when a Dockerfile exists, plan-before-apply OpenTofu, the
  app's own release steps, then verification. It never destroys
  infrastructure and never prints secrets.

## draft

- **write** produces long-form prose in the project's own voice:
  fiction, nonfiction, poetry, or technical articles. It orients in
  the repo first and follows any publication target spec the project
  defines (fields, format, storage). Manuscripts follow the
  `creative` skill. Articles follow `technical-writing`, with
  research through `forge:web-browsing` and claims cited per
  `forge:citations`.

  ```text
  /draft:write chapter 3: the city falls and the survivors regroup
  /draft:write the elegy for the fallen city --type-poetry
  /draft:write article: what self-hosting CI taught me --type-article
  ```

- **publish** compiles a writing project into publishable EPUBs for
  Amazon KDP and Barnes and Noble Nook, validated against KDP's
  expectations. It builds local files only and never uploads. Needs
  [Pandoc](https://pandoc.org/installing.html) or an equivalent EPUB
  tool.

## anvil

- **check** runs the static gate over a Nix repo: every shell file
  checked with the right parser for its dialect (shellcheck cannot
  parse fish, so fish gets `fish -n`), then the flake or
  configuration evaluated. Builds nothing, changes nothing.
- **portability** audits shell and package selection against the
  distro families the repo claims. Every finding carries a file, a
  line, the family it breaks on, and a loud-or-silent verdict.
  Findings from families the machine did not run are marked
  unverified.
- **env** creates or updates a [devenv](https://devenv.sh/)
  development environment, reading the devenv option docs before
  writing a line, every time. Detects languages from manifests,
  writes `devenv.nix`, `devenv.yaml`, and the direnv `.envrc`, and
  evaluates before reporting success.
- **switch** builds a machine definition, shows the closure diff
  against the current generation, and activates only after
  confirmation. Prints the rollback command on failure. Never runs
  `sudo`, never bootstraps.

## Why this exists

forge exists to run multiple independent ventures off one consistent
workflow instead of rebuilding process for each new project. The core
verbs are how work gets planned, built, and shipped, whatever the
project. foundry is the engineering backbone behind a template
business. draft carries the books and the blog. Each new venture
starts from a working process instead of from zero, and every one of
them writes, commits, and ships by the same rules.

## Scope

forge is built for professional and personal development work, not
for academic use. Do not use it to complete coursework, assignments,
or exams. If you are unsure whether AI-assisted tools are allowed,
check your institution's academic integrity policy.

## License

MIT. See [LICENSE](LICENSE) for the full text.

## Inspiration

forge took inspiration from
[Shipyard](https://github.com/mattsears18/shipyard), an autonomous
engineering loop plugin for Claude Code. Shipyard is a far more
ambitious project: parallel worker pools in isolated worktrees,
autonomous triage, audit pipelines, and auto-merging PRs. forge stays
deliberately leaner. If our needs grow into parallel agents and
automated backlogs, we will adopt Shipyard rather than rebuild it.
Different tools fit different stages.
