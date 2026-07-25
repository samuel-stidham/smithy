# smithy

smithy is a marketplace of lean, repo-agnostic plugins for
[Claude Code](https://claude.com/claude-code): six plugins, one set
of shared rules. It makes no assumptions about
language, framework, or tooling. Every verb detects what it needs from
the repo itself: manifest files, lockfiles, existing patterns, and the
repo's own agent instructions. It never requires per-repo
configuration.

## The family

| Plugin | What it does | Where it runs |
| --- | --- | --- |
| **forge** | Core engineering workflow: execute tasks, debug, refactor, evaluate options, review diffs, ship draft PRs, cut releases, generate test harnesses. | Enabled globally. |
| **foundry** | Product factory: scaffold complete Clean Architecture project templates, deploy them with OpenTofu. | Enabled per repo. |
| **draft** | Writing studio: books, poetry, technical articles, and repo documentation, with ebook compilation. | Enabled per repo. |
| **anvil** | Nix environments: shell gates, distro-family portability audits, devenv environments, confirmed activation. | Enabled per repo. |
| **bellows** | Recurring automation: scheduled routines, watches over long-running work, CI pipelines, dependency upgrades. | Enabled per repo. |
| **temper** | Security: repo-wide audits across secrets, dependencies, code, and configuration, then hardening in exploitability order. | Enabled per repo. |

foundry, draft, anvil, bellows, and temper require forge. They borrow its shared
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
/plugin install bellows@smithy
/plugin install temper@smithy
```

Install forge at user scope so it is available everywhere. Keep the
leaves disabled globally and enable them per repo: draft in writing
projects, foundry where products get built or deployed, anvil in
machine definitions and devenv projects. bellows goes wherever
unattended jobs run, and temper wherever the code faces users or
handles secrets. One line in that repo's
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
- **debug** takes a symptom to a proven fix. It reproduces first,
  isolates by shrinking and bisecting, and names the root cause
  apart from the trigger that revealed it. The regression test runs
  both ways before it counts.
- **refactor** restructures code without changing behavior. It
  builds the safety net first, writing characterization tests where
  coverage is thin. Then it moves in small commits that each pass
  the full suite. A bug found mid-refactor gets reported, never
  silently fixed.
- **evaluate** answers one engineering decision with evidence: cited
  research per `citations`, an optional throwaway spike, and exactly
  one recommendation. Runners-up get the reason they lost.
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
- **docs** writes repo documentation verified against the code it
  describes: READMEs, ADRs, API references, and guides. Commands
  shown in a doc get run when safe, and unrun ones are marked.

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

## bellows

- **routine** turns a recurring chore into a scheduled job with a
  full definition: purpose, cadence, boundaries, report destination,
  stop procedure. It dry-runs the job attended before registering it
  on whatever scheduler the environment offers.
- **watch** babysits long-running external work until it resolves: a
  PR moving through CI and review, a deploy, a migration. It reports
  transitions, stays quiet on green, and never makes the decision
  the human is watching for.
- **ci** authors or updates the repo's CI pipeline on the provider
  the repo already uses, mirroring the gates developers run locally.
  Secrets stay in the provider's secret store.
- **upgrade** moves dependencies in risk-ordered batches, testing
  after each. Majors get their changelogs read through
  `forge:web-browsing` first, and deliberate pins stay pinned.

Every unattended job is judged against the `automation-boundaries`
skill: no default-branch pushes, no merges, no publishing, loud
failure, idempotent runs.

## temper

- **audit** reads the repo's security posture without changing it.
  It covers secrets in tree and history, dependencies through the
  ecosystem's own audit tool, code at trust boundaries, and
  configuration. Findings rank by exploitability, and everything the
  audit skipped gets named.
- **harden** fixes the findings in exploitability order, one commit
  per fix, tests after each. Changes to authentication,
  authorization, crypto, and session handling get confirmed before
  they land. A leaked credential gets reported for human rotation,
  never rotated by the plugin.

Both verbs share the `security-baseline` skill: exploitability
ranking, the secrets bar, validated trust boundaries, fail-closed
defaults, and audit honesty.

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
